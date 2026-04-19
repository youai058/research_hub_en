#!/usr/bin/env python3
"""Harness structural validator.

Usage: validate.py <project_root>

Exit codes:
  0 = all OK
  1 = warnings only
  2 = fatal errors (settings JSON broken, hook path missing, etc.)
"""
from __future__ import annotations

import json
import os
import re
import shutil
import sys
from pathlib import Path

ERRORS: list[str] = []
WARNS: list[str] = []
OKS: list[str] = []

DEFAULT_MODES = {"plan", "default", "acceptEdits", "bypassPermissions"}
MCP_TYPES = {"stdio", "sse", "http"}


def err(msg: str) -> None:
    ERRORS.append(msg)


def warn(msg: str) -> None:
    WARNS.append(msg)


def ok(msg: str) -> None:
    OKS.append(msg)


def parse_frontmatter(text: str) -> tuple[dict, str] | tuple[None, str]:
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        return None, text
    raw = text[4:end]
    body = text[end + 4 :].lstrip("\n")
    meta: dict = {}
    for line in raw.splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*)\s*:\s*(.*)$", line)
        if m:
            k, v = m.group(1), m.group(2).strip()
            if v.startswith('"') and v.endswith('"'):
                v = v[1:-1]
            meta[k] = v
    return meta, body


def check_settings(path: Path) -> dict | None:
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text())
    except Exception as e:
        err(f"{path}: JSON parse failed — {e}")
        return None
    ok(f"{path.name}: JSON valid")

    perms = data.get("permissions", {})
    mode = perms.get("defaultMode")
    if mode and mode not in DEFAULT_MODES:
        err(f"{path}: permissions.defaultMode='{mode}' not in {DEFAULT_MODES}")

    for key in ("allow", "deny", "ask"):
        for entry in perms.get(key, []) or []:
            if not re.match(r"^[A-Za-z_]+\(.*\)$", entry):
                warn(f"{path}: permissions.{key} entry '{entry}' not ToolName(pattern) form")

    sl = data.get("statusLine")
    if isinstance(sl, dict) and sl.get("type") == "command":
        cmd = sl.get("command")
        if cmd:
            head = cmd.split()[0]
            # Accept either an absolute/relative path that exists on disk, or
            # a bare executable name resolvable via PATH (e.g. `python3`).
            if not (Path(head).exists() or shutil.which(head)):
                err(f"{path}: statusLine.command executable not found: {head}")

    hooks = data.get("hooks", {})
    for event, entries in hooks.items():
        if not isinstance(entries, list):
            err(f"{path}: hooks.{event} must be list")
            continue
        for i, entry in enumerate(entries):
            for hk in entry.get("hooks", []):
                if hk.get("type") != "command":
                    continue
                cmd = hk.get("command", "")
                head = cmd.split()[0] if cmd else ""
                if head and not Path(head).exists():
                    err(f"{path}: hooks.{event}[{i}] path missing: {head}")
                elif head and not os.access(head, os.X_OK):
                    warn(f"{path}: hooks.{event}[{i}] not executable: {head}")
    return data


def check_agents(agents_dir: Path) -> None:
    if not agents_dir.is_dir():
        return
    for f in sorted(agents_dir.glob("*.md")):
        text = f.read_text()
        meta, _ = parse_frontmatter(text)
        if meta is None:
            err(f"{f}: missing YAML frontmatter")
            continue
        for k in ("name", "description"):
            if k not in meta:
                err(f"{f}: frontmatter missing '{k}'")
        if meta.get("name") and meta["name"] != f.stem:
            err(f"{f}: frontmatter name '{meta['name']}' != filename '{f.stem}'")
        if meta.get("model") != "opus":
            warn(f"{f}: model is '{meta.get('model')}' (recommended: opus)")
    ok(f"agents/: {len(list(agents_dir.glob('*.md')))} files checked")


def check_skills(skills_dir: Path) -> list[tuple[str, str, Path]]:
    descs: list[tuple[str, str, Path]] = []
    if not skills_dir.is_dir():
        return descs
    for d in sorted(skills_dir.iterdir()):
        if not d.is_dir():
            continue
        sk = d / "SKILL.md"
        if not sk.exists():
            err(f"{d}: SKILL.md missing")
            continue
        text = sk.read_text()
        meta, body = parse_frontmatter(text)
        if meta is None:
            err(f"{sk}: missing YAML frontmatter")
            continue
        # Strict PyYAML parse — catches unquoted scalars that contain ": "
        # (e.g. description: ... Triggers: '...') which the hand-rolled parser
        # above silently drops. Added for Med-2 (3rd audit).
        try:
            import yaml  # type: ignore
        except ImportError:
            warn(f"{sk}: PyYAML unavailable, skipped strict YAML check")
        else:
            try:
                raw_fm = text.split("---", 2)[1] if text.startswith("---") else ""
                yaml.safe_load(raw_fm)
            except Exception as e:
                err(f"{sk}: frontmatter not strict-YAML parseable — {str(e)[:120]}")
        for k in ("name", "description"):
            if k not in meta:
                err(f"{sk}: frontmatter missing '{k}'")
        if meta.get("name") and meta["name"] != d.name and meta["name"] != f"lldm-{d.name}":
            warn(f"{sk}: name '{meta['name']}' differs from dir '{d.name}'")
        lines = body.count("\n") + 1
        if lines > 500:
            warn(f"{sk}: {lines} lines (>500, consider references/)")
        descs.append((meta.get("name", d.name), meta.get("description", ""), sk))
    ok(f"skills/: {len(descs)} files checked")
    return descs


def check_commands(cmds_dir: Path) -> None:
    if not cmds_dir.is_dir():
        return
    n = 0
    for f in cmds_dir.rglob("*.md"):
        n += 1
        text = f.read_text()
        meta, body = parse_frontmatter(text)
        if meta is not None:
            at = meta.get("allowed-tools")
            if at and not (at.startswith("[") or at.startswith("-")):
                warn(f"{f}: allowed-tools should be array")
        if re.search(r"\$ARGUMENTS|\$[1-9]", body) and meta and "argument-hint" not in meta:
            warn(f"{f}: uses $ARGUMENTS but no argument-hint")
    ok(f"commands/: {n} files checked")


def check_mcp(project: Path) -> None:
    mcp = project / ".mcp.json"
    if not mcp.exists():
        return
    try:
        data = json.loads(mcp.read_text())
    except Exception as e:
        err(f"{mcp}: JSON parse failed — {e}")
        return
    ok(".mcp.json: JSON valid")
    for name, cfg in data.get("mcpServers", {}).items():
        t = cfg.get("type")
        if t not in MCP_TYPES:
            err(f".mcp.json: server '{name}' type '{t}' not in {MCP_TYPES}")
        if t == "stdio":
            cmd = cfg.get("command", "")
            if cmd.startswith("/") and not Path(cmd).exists():
                warn(f".mcp.json: server '{name}' command path missing: {cmd}")


def check_trigger_overlap(descs: list[tuple[str, str, Path]]) -> None:
    tokens = []
    for name, desc, path in descs:
        toks = set(re.findall(r"[A-Za-z]{3,}", desc.lower()))
        tokens.append((name, toks, path))
    reported: set[tuple[str, str]] = set()
    for i in range(len(tokens)):
        for j in range(i + 1, len(tokens)):
            a_name, a_tok, _ = tokens[i]
            b_name, b_tok, _ = tokens[j]
            overlap = a_tok & b_tok
            if len(overlap) >= 8:
                key = tuple(sorted([a_name, b_name]))
                if key in reported:
                    continue
                reported.add(key)
                warn(f"trigger overlap: '{a_name}' ~ '{b_name}' ({len(overlap)} shared tokens)")


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: validate.py <project_root>", file=sys.stderr)
        return 2
    root = Path(sys.argv[1]).resolve()
    claude = root / ".claude"
    if not claude.is_dir():
        err(f"{claude}: not a directory")
    else:
        check_settings(claude / "settings.json")
        check_settings(claude / "settings.local.json")
        check_agents(claude / "agents")
        descs = check_skills(claude / "skills")
        check_commands(claude / "commands")
        check_trigger_overlap(descs)
        check_mcp(root)

    print("== Harness Validation Report ==")
    for m in OKS:
        print(f"[OK]    {m}")
    for m in WARNS:
        print(f"[WARN]  {m}")
    for m in ERRORS:
        print(f"[ERROR] {m}")
    print(f"-- summary: {len(OKS)} ok, {len(WARNS)} warn, {len(ERRORS)} error")

    if ERRORS:
        return 2
    if WARNS:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

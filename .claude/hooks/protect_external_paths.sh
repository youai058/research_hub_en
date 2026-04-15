#!/usr/bin/env bash
# PreToolUse hook — block writes outside research_hub and risky Bash behaviors.
#
# Scope:
#   - Write/Edit/MultiEdit: reject file_path outside /home[1]/irteam/sw/research_hub/**
#     Also reject ~/.claude/ (user global) unconditionally.
#   - Bash: reject shell-level paid API / HF download invocations.
#     These belong in explicit user-approved scripts.
#
# Contract: exit 2 aborts the tool. Message goes to stderr so Claude sees it;
# a user-facing hint is also echoed to stdout.
#
# These targets always require explicit user approval per CLAUDE.md §2
# (see lessons.md 2026-04-15). Stage commands do not bypass this guard.
set -euo pipefail

payload="$(cat)"

python3 - <<'PY' "$payload"
import json, os, re, sys

try:
    data = json.loads(sys.argv[1]) if sys.argv[1].strip() else {}
except Exception:
    sys.exit(0)

tool = data.get("tool_name") or data.get("tool") or ""
tin = data.get("tool_input") or data.get("input") or {}

RESEARCH_HUB_PREFIXES = (
    "/home/irteam/sw/research_hub",
    "/home1/irteam/sw/research_hub",
)

FORBIDDEN_PREFIXES = (
    "/home/irteam/sw/LLM",
    "/home1/irteam/sw/LLM",
    "/home/irteam/sw/LLDM",
    "/home1/irteam/sw/LLDM",
    "/home/irteam/.claude",
    "/home1/irteam/.claude",
    os.path.expanduser("~/.claude"),
)

SW_ROOTS = (
    "/home/irteam/sw",
    "/home1/irteam/sw",
)

def normalize(p: str) -> str:
    if not p:
        return ""
    p = os.path.expanduser(p)
    # Try realpath; if it fails (nonexistent file) fall back to abspath.
    try:
        rp = os.path.realpath(p)
    except Exception:
        rp = os.path.abspath(p)
    return rp

def block(reason: str) -> None:
    msg = (
        f"[protect_external_paths] blocked: {reason}\n"
        "stage 커맨드는 이 guardrail을 우회하지 않음 — 사용자 승인 필요 (lessons.md 2026-04-15)"
    )
    print(msg)
    print(msg, file=sys.stderr)
    sys.exit(2)

def path_is_forbidden(raw: str) -> tuple[bool, str]:
    if not raw:
        return False, ""
    norm = normalize(raw)
    # Absolute user-global claude dir is always forbidden.
    for fp in FORBIDDEN_PREFIXES:
        fp_n = normalize(fp)
        if not fp_n:
            continue
        if norm == fp_n or norm.startswith(fp_n.rstrip("/") + "/"):
            return True, f"path '{raw}' resolves under forbidden prefix '{fp}'"
    # Allow anything under research_hub after realpath.
    for rh in RESEARCH_HUB_PREFIXES:
        rh_n = normalize(rh)
        if norm == rh_n or norm.startswith(rh_n.rstrip("/") + "/"):
            return False, ""
    # Anything else under /home*/irteam/sw but NOT research_hub = LLDM project.
    for sw in SW_ROOTS:
        sw_n = normalize(sw)
        if norm == sw_n or norm.startswith(sw_n.rstrip("/") + "/"):
            return True, (
                f"path '{raw}' is under {sw} but outside research_hub/ "
                "(LLDM attack project is read-only from this harness)"
            )
    # Outside sw tree entirely — don't block (e.g. /tmp). Agents occasionally
    # need /tmp scratch files. Only LLDM + user-global are hard-forbidden.
    return False, ""

# ---- Write/Edit/MultiEdit path guard ----
if tool in ("Write", "Edit", "MultiEdit"):
    candidates = []
    fp = tin.get("file_path")
    if fp:
        candidates.append(fp)
    # MultiEdit uses file_path too; edits list doesn't carry separate paths.
    for c in candidates:
        bad, reason = path_is_forbidden(c)
        if bad:
            block(reason)
    sys.exit(0)

# ---- Bash guard ----
if tool != "Bash":
    sys.exit(0)

cmd = tin.get("command", "") or ""
if not cmd:
    sys.exit(0)

# 1. Paid API calls embedded in `python -c` / `python3 -c` / heredocs.
PAID_PATTERNS = [
    r"anthropic\.[A-Za-z_]*messages\.create",
    r"anthropic\.[A-Za-z_]*Anthropic\s*\(",
    r"openai\.ChatCompletion",
    r"openai\.chat\.completions",
    r"openai\.OpenAI\s*\(",
    r"google\.generativeai",
    r"genai\.GenerativeModel",
]
# Only flag when invoked via shell python -c / python3 -c (i.e. ad-hoc eval).
PYEVAL_RE = re.compile(r"\bpython3?\s+-c\b", re.IGNORECASE)
if PYEVAL_RE.search(cmd):
    for pat in PAID_PATTERNS:
        if re.search(pat, cmd):
            block(
                f"paid API call in shell python -c: matches /{pat}/. "
                "Put the call in a tracked script + explicit user approval."
            )

# 2. HF downloads / transformers.from_pretrained in shell eval.
HF_PATTERNS = [
    r"huggingface-cli\s+download",
    r"from_pretrained\s*\(",
    r"snapshot_download\s*\(",
]
if PYEVAL_RE.search(cmd):
    for pat in HF_PATTERNS:
        if re.search(pat, cmd):
            block(
                f"large model/data download in shell python -c: /{pat}/. "
                "Use a tracked script or ask user."
            )
# huggingface-cli is a shell-level binary, flag regardless of python -c
for pat in [r"huggingface-cli\s+download"]:
    if re.search(pat, cmd):
        block(f"huggingface-cli download needs explicit user approval: /{pat}/")

sys.exit(0)
PY

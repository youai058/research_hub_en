#!/usr/bin/env python3
"""Append a lesson entry to the appropriate docs/lessons*.md file.

Append-only — never deletes or rewrites previous entries. Updates the
frontmatter `updated:` field and bumps the session-reported count.

Subcommands
-----------
append    write a new dated entry
count     report entry counts per domain file

Domains map to files:
  global    docs/lessons.md
  paper     docs/lessons-paper.md
  research  docs/lessons-research.md
  impl      docs/lessons-impl.md
  analysis  docs/lessons-analysis.md
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any

KST = timezone(timedelta(hours=9))

DOMAIN_MAP = {
    "global": "lessons.md",
    "paper": "lessons-paper.md",
    "research": "lessons-research.md",
    "impl": "lessons-impl.md",
    "analysis": "lessons-analysis.md",
}


def _slugify(s: str, maxlen: int = 60) -> str:
    out = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return out[:maxlen] or "untitled"


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def find_root(explicit: str | None) -> Path:
    if explicit:
        return Path(explicit).resolve()
    here = Path(__file__).resolve()
    for p in [here.parent, *here.parents]:
        if (p / "docs").is_dir() and (p / "research").is_dir():
            return p
    fb = Path("/home/irteam/sw/research_hub")
    if fb.is_dir():
        return fb
    raise SystemExit("cannot locate research_hub root (use --root)")


def today_kst() -> str:
    return datetime.now(KST).strftime("%Y-%m-%d")


def count_entries(text: str) -> int:
    return len(re.findall(r"^## \d{4}-\d{2}-\d{2}", text, re.MULTILINE))


def bump_frontmatter_updated(text: str, today: str) -> str:
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 4)
    if end == -1:
        return text
    head = text[4:end]
    body = text[end + 5 :]
    if re.search(r"^updated:.*$", head, re.MULTILINE):
        head = re.sub(r"^updated:.*$", f"updated: {today}", head, count=1, flags=re.MULTILINE)
    else:
        head = head.rstrip("\n") + f"\nupdated: {today}"
    return "---\n" + head + "\n---\n" + body


def ensure_file(path: Path, domain: str) -> None:
    if path.is_file():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    today = today_kst()
    template = f"""---
domain: {domain}
updated: {today}
---

# Lessons — {domain.capitalize()}

append-only. 오래된 항목은 삭제하지 말고 `superseded` 표시.

---

<!-- append entries below this line -->
"""
    path.write_text(template, encoding="utf-8")


def cmd_append(args: argparse.Namespace) -> int:
    root = find_root(args.root)
    if args.domain not in DOMAIN_MAP:
        raise SystemExit(f"invalid domain: {args.domain!r} (valid: {list(DOMAIN_MAP)})")
    target = root / "docs" / DOMAIN_MAP[args.domain]
    ensure_file(target, args.domain)

    today = today_kst()
    title = args.title.strip()
    if not title:
        raise SystemExit("append: --title is required and must be non-empty")

    rule = (args.rule or "TODO").strip()
    why = (args.why or "TODO").strip()
    when = (args.when or "TODO").strip()

    block = (
        f"\n## {today} — {title}\n"
        f"- **Rule**: {rule}\n"
        f"- **Why**: {why}\n"
        f"- **When to apply**: {when}\n"
    )

    original = target.read_text(encoding="utf-8")
    new_text = original.rstrip() + "\n" + block
    new_text = bump_frontmatter_updated(new_text, today)
    target.write_text(new_text, encoding="utf-8")

    # Emit KG byproduct: Lesson node appended to docs/lessons-<domain>.kg.json
    kg_summary = _emit_lesson_kg(
        target_md=target,
        domain=args.domain,
        date=today,
        title=title,
        rule=rule,
        why=why,
        when=when,
    )

    result = {
        "status": "appended",
        "file": str(target.relative_to(root)),
        "domain": args.domain,
        "date": today,
        "title": title,
        "entry_count": count_entries(new_text),
        "has_placeholders": any(v == "TODO" for v in (rule, why, when)),
        "kg": kg_summary,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


def _emit_lesson_kg(
    *,
    target_md: Path,
    domain: str,
    date: str,
    title: str,
    rule: str,
    why: str,
    when: str,
) -> dict[str, Any]:
    """Append a Lesson node to the sibling .kg.json file.

    Schema-compatible with paper-kg/scripts/schema.py:KGFile. One file per
    lessons-<domain>.md, accumulating nodes across appends (nodes list only,
    no edges — Lesson is a leaf concept here).
    """
    kg_path = target_md.with_suffix(target_md.suffix + ".kg.json")
    if kg_path.suffix != ".kg.json":
        # e.g. lessons.md -> lessons.md.kg.json; we prefer lessons.kg.json
        kg_path = target_md.with_name(target_md.stem + ".kg.json")

    slug = _slugify(f"{date}-{title}")
    node_id = f"lesson:{domain}--{slug}"

    existing: dict[str, Any]
    if kg_path.is_file():
        try:
            existing = json.loads(kg_path.read_text(encoding="utf-8"))
        except Exception:
            existing = {}
    else:
        existing = {}

    nodes = existing.get("nodes") or []
    # idempotent: skip if id already present
    if any(n.get("id") == node_id for n in nodes):
        return {"kg_path": str(kg_path), "status": "duplicate", "id": node_id}

    nodes.append({
        "id": node_id,
        "type": "Lesson",
        "name": title,
        "meta": {
            "domain": domain,
            "date": date,
            "rule": rule,
            "why": why,
            "when": when,
        },
    })

    source_sha = _sha256_file(target_md) if target_md.is_file() else None
    payload = {
        "version": 1,
        "source_file": str(target_md.as_posix()),
        "source_sha": source_sha,
        "extracted_at": datetime.now(KST).isoformat(timespec="seconds"),
        "author_agent": "lesson.py",
        "nodes": nodes,
        "edges": existing.get("edges") or [],
    }

    kg_path.parent.mkdir(parents=True, exist_ok=True)
    tmp = kg_path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(kg_path)

    # Med-3 (3차 audit): direct .write_text bypasses PostToolUse(Write|Edit|
    # MultiEdit) hook. Touch the KG stale marker so kg-curator re-ingests the
    # new lesson node on next build. target_md is <root>/docs/lessons-*.md,
    # so parents[1] is the research_hub root.
    try:
        root = target_md.resolve().parents[1]
        stale = root / "papers" / "kg" / ".stale"
        stale.parent.mkdir(parents=True, exist_ok=True)
        stale.touch()
    except Exception:
        pass

    return {"kg_path": str(kg_path), "status": "appended", "id": node_id, "nodes": len(nodes)}


def cmd_count(args: argparse.Namespace) -> int:
    root = find_root(args.root)
    out: dict[str, Any] = {}
    for dom, name in DOMAIN_MAP.items():
        p = root / "docs" / name
        if p.is_file():
            out[dom] = count_entries(p.read_text(encoding="utf-8"))
        else:
            out[dom] = None
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=None)
    sub = ap.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("append", help="append a new dated lesson entry")
    a.add_argument("--domain", required=True, choices=list(DOMAIN_MAP.keys()))
    a.add_argument("--title", required=True)
    a.add_argument("--rule", default=None)
    a.add_argument("--why", default=None)
    a.add_argument("--when", default=None, dest="when")
    a.set_defaults(func=cmd_append)

    c = sub.add_parser("count", help="print entry counts per domain")
    c.set_defaults(func=cmd_count)

    return ap


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())

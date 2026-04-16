#!/usr/bin/env python3
"""Collect raw.md abstracts into a single JSON bundle for paper-triage.

Purpose: let the paper-triage agent score N abstracts with one Read instead of
N per-file Reads. Pure extraction, no scoring. Runtime-only — does not mutate
any raw.md.

Output: JSON array of {path, slug, title, abstract, venue, year, venue_class,
published, categories}. Path is relative to --root.
"""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("[collect_abstracts] PyYAML required (conda env LLDM)", file=sys.stderr)
    sys.exit(3)

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
ABSTRACT_RE = re.compile(
    r"##\s*Abstract\s*\n(.+?)(?=\n##\s|\Z)", re.DOTALL | re.IGNORECASE
)


def extract(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8", errors="replace")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        print(f"[collect_abstracts] YAML parse fail {path}: {e}", file=sys.stderr)
        return None
    abst = ""
    am = ABSTRACT_RE.search(text)
    if am:
        abst = am.group(1).strip()
    return {
        "slug": path.stem.replace(".raw", ""),
        "title": fm.get("title", ""),
        "abstract": abst,
        "venue": fm.get("venue", ""),
        "year": fm.get("year", ""),
        "venue_class": fm.get("venue_class", ""),
        "published": fm.get("published", ""),
        "categories": fm.get("categories", []) or [],
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", default="/home/irteam/sw/research_hub",
                    help="Project root (abs path)")
    ap.add_argument("--glob", default="papers/metadata/**/*.raw.md",
                    help="Glob pattern relative to --root")
    ap.add_argument("--chunk", type=int, default=0,
                    help="Emit one JSON array per N items (0=single array)")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    items = []
    skipped = 0
    for p in sorted(root.glob(args.glob)):
        if not p.is_file():
            continue
        rec = extract(p)
        if rec is None:
            skipped += 1
            continue
        rec["path"] = str(p.relative_to(root))
        items.append(rec)

    if args.chunk > 0:
        for i in range(0, len(items), args.chunk):
            print(json.dumps(items[i:i + args.chunk], ensure_ascii=False))
    else:
        print(json.dumps(items, ensure_ascii=False, indent=2))
    print(f"[collect_abstracts] emitted={len(items)} skipped={skipped}",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""verify_sub_phase.py — SSOT artifact verifier for research_hub Phase C sub-phases.

Role
----
Each sub-phase agent (A-1, A-1.5, A-2, A-3, A-4, B-1, B-2-critic, B-2-codex,
E-1, E-2, E-3, F-1, F-2) produces artifacts that the dispatch loop must verify
before proceeding to the next sub-phase.  This script is that single verification
point — every check lives here, not scattered across command prompts.

E-3 / F-2 reject contract
--------------------------
A codex-reviewer "reject" verdict is a *content* decision, not a process error.
When this script detects a reject, it exits 0 and writes the verdict to stdout so
the dispatch loop can read it and decide whether to retry.  Only missing or
malformed artifacts (process errors) produce a non-zero exit code.

Usage
-----
  python verify_sub_phase.py snapshot <sub_phase_id> --slug <slug> [--stage-version N] [--batch-i N]
  python verify_sub_phase.py verify   <sub_phase_id> --slug <slug> [--stage-version N] [--batch-i N]

RESEARCH_HUB_ROOT env var overrides the default repo-root detection (same
convention as .claude/hooks/inject_lessons.sh).
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path


def _root() -> Path:
    """Return repo root: RESEARCH_HUB_ROOT env override or two levels up from this file."""
    env_val = os.environ.get("RESEARCH_HUB_ROOT")
    if env_val:
        return Path(env_val)
    return Path(__file__).resolve().parents[2]


SUB_PHASES: dict[str, dict] = {
    "A-1":   {"glob": "papers/metadata/**/*.raw.md",
              "on_fail": ("paper-hunter did not collect any new raw.md", 6)},
    "A-1.5": {"glob": "papers/vector_db/abstracts_manifest.json",
              "mode": "mtime",
              "on_fail": ("abstract-indexer did not preserve/grow manifest", 10)},
    "A-2":   {"glob": "research/topics/{slug}.md",
              "on_fail": ("paper-triage did not append a log line", 5)},
    "A-3":   {"glob": "papers/marp-summary/**/*.md",
              "mode": "batch",
              "on_fail": ("paper-summarizer batch produced no summary", 9)},
    "A-4":   {"glob": "papers/vector_db/manifest.json",
              "mode": "mtime",
              "on_fail": ("rag-curator did not grow manifest", 7)},
    "B-1":   {"glob": "research/answers/*.md",
              "on_fail": ("answer-formulator did not emit an answer file", 9)},
    "B-2-critic": {"glob": "research/critiques/*.md",
                   "on_fail": ("critic did not emit a critique file", 10)},
    "B-2-codex":  {"glob": "research/reviews/qa_{slug}_codex_review.md",
                   "on_fail": ("codex-reviewer did not emit a review file", 11)},
    "E-1":   {"glob": "experiments/{slug}/code/**/*",
              "extra_required": ["experiments/{slug}/IMPL_MAP.md"],
              "on_fail": ("code-implementer did not add code or IMPL_MAP", 12)},
    "E-2":   {"glob": "experiments/{slug}/qa_fail_*.md",
              "expect": "no-new",
              "on_fail": ("implementation-verifier emitted qa_fail_*.md", 13)},
    "E-3":   {"glob": "research/reviews/experiments_{slug}_codex_review.md",
              "verdict_parse": True,
              "on_fail": ("codex-reviewer did not emit a review file (E-3)", 14)},
    "F-1":   {"glob": "research/diagnoses/{slug}.md",
              "extra_required": ["research/diagnoses/{slug}.html"],
              "on_fail": ("results-analyst did not emit diagnosis", 15)},
    "F-2":   {"glob": "research/reviews/analyze_{slug}_codex_review.md",
              "verdict_parse": True,
              "on_fail": ("codex-reviewer did not emit a review file (F-2)", 16)},
}


def _snapshot_path(sub_phase_id: str, slug: str, batch_i: int | None) -> Path:
    suffix = f"_b{batch_i}" if batch_i is not None else ""
    return Path(f"/tmp/.verify_{sub_phase_id}_{slug}{suffix}.json")


def _resolve_glob(pattern: str, slug: str, root: Path) -> list[Path]:
    resolved = pattern.format(slug=slug)
    if "**" in resolved or "*" in resolved or "?" in resolved:
        return sorted(root.glob(resolved))
    p = root / resolved
    return [p] if p.exists() else []


def _do_snapshot(args, spec: dict, root: Path) -> int:
    paths = _resolve_glob(spec["glob"], args.slug, root)
    data = {
        "sub_phase": args.sub_phase_id,
        "slug": args.slug,
        "glob": spec["glob"],
        "paths": [str(p) for p in paths],
        "count": len(paths),
        "mtimes": {str(p): p.stat().st_mtime for p in paths if p.exists()},
        "batch_i": args.batch_i,
        "ts": time.time(),
    }
    _snapshot_path(args.sub_phase_id, args.slug, args.batch_i).write_text(
        json.dumps(data)
    )
    return 0


def _fail(spec: dict, suffix: str = "") -> int:
    msg, code = spec["on_fail"]
    print(f"{msg}{suffix}", file=sys.stderr)
    return code


VALID_VERDICTS = {"approve", "approve_with_revisions", "reject"}


def _parse_verdict(review_path: Path) -> str | None:
    """Parse YAML frontmatter `verdict:` key. Returns the value if it is one
    of VALID_VERDICTS, else None (caller treats as failure).
    """
    if not review_path.exists():
        return None
    in_fm = False
    seen_open = False
    for raw in review_path.read_text().splitlines():
        line = raw.rstrip()
        if line == "---":
            if not seen_open:
                seen_open = True
                in_fm = True
                continue
            break
        if in_fm and line.startswith("verdict:"):
            val = line.split(":", 1)[1].strip()
            return val if val in VALID_VERDICTS else None
    return None


def _do_verify(args, spec: dict, root: Path) -> int:
    snap_p = _snapshot_path(args.sub_phase_id, args.slug, args.batch_i)
    if not snap_p.exists():
        print(f"missing snapshot — run `snapshot {args.sub_phase_id}` first",
              file=sys.stderr)
        return 2
    pre = json.loads(snap_p.read_text())
    post_paths = _resolve_glob(spec["glob"], args.slug, root)
    post_count = len(post_paths)
    mode = spec.get("mode", "default")
    if spec.get("verdict_parse"):
        if not post_paths:
            return _fail(spec)
        verdict = _parse_verdict(post_paths[0])
        if verdict is None:
            return _fail(spec, suffix=" — missing or invalid `verdict:` frontmatter")
        print(f"{args.sub_phase_id}: OK (verdict: {verdict})")
        return 0
    if mode == "mtime":
        if not post_paths:
            return _fail(spec, suffix=" (file missing)")
        pre_mtimes = pre.get("mtimes", {})
        post_max = max(p.stat().st_mtime for p in post_paths)
        pre_max = max(pre_mtimes.values()) if pre_mtimes else 0.0
        if post_max <= pre_max:
            return _fail(spec)
    elif spec.get("expect") == "no-new":
        if post_count > pre["count"]:
            return _fail(spec)
    elif post_count <= pre["count"]:
        return _fail(spec)
    for extra in spec.get("extra_required", []):
        rp = root / extra.format(slug=args.slug)
        if not rp.exists():
            return _fail(spec, suffix=f" (missing {extra.format(slug=args.slug)})")
    if mode == "mtime":
        marker = "touched"
    elif spec.get("expect") == "no-new":
        marker = "no new artifacts"
    elif mode == "batch":
        marker = f"batch {args.batch_i}: +{post_count - pre['count']} artifacts"
    else:
        marker = f"+{post_count - pre['count']} artifacts"
    print(f"{args.sub_phase_id}: OK ({marker})")
    return 0


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="verify_sub_phase",
        description="Snapshot or verify Phase C sub-phase artifacts.",
    )
    subparsers = parser.add_subparsers(dest="cmd", required=True)

    for cmd_name in ("snapshot", "verify"):
        sub = subparsers.add_parser(cmd_name, help=f"{cmd_name} artifacts for a sub-phase")
        sub.add_argument("sub_phase_id", help="Sub-phase ID (e.g. A-1, B-2-critic)")
        sub.add_argument("--slug", required=True, help="Topic/experiment slug")
        sub.add_argument("--stage-version", type=int, default=None, help="Stage version number")
        sub.add_argument("--batch-i", type=int, default=None, help="Batch index (0-based)")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.sub_phase_id not in SUB_PHASES:
        known = list(SUB_PHASES.keys())
        print(
            f"unknown sub_phase '{args.sub_phase_id}' (known: {known})",
            file=sys.stderr,
        )
        return 2

    spec = SUB_PHASES[args.sub_phase_id]
    root = _root()
    if args.cmd == "snapshot":
        return _do_snapshot(args, spec, root)
    if args.cmd == "verify":
        return _do_verify(args, spec, root)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

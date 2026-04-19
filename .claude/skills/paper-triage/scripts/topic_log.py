#!/usr/bin/env python3
"""Topic log manager for paper-triage.

Three subcommands used by the paper-triage agent:

    slug   --topic "..."           → print deterministic slug
    load   <slug>                  → print the topic text of an existing file
    append --slug --topic          → create/append research/topics/<slug>.md
           --stats-json '{...}'       with a new run entry (fcntl lock)

The topic file is a log of past triage runs, not canonical state. Canonical
topic for any run is always the --topic string on the CLI that run.
"""
from __future__ import annotations
import argparse
import fcntl
import hashlib
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

try:
    import yaml
except ImportError:
    print("[topic_log] PyYAML required (conda env LLDM)", file=sys.stderr)
    sys.exit(3)

UTC = timezone.utc
ROOT = Path("/home/irteam/sw/research_hub")
TOPICS_DIR = ROOT / "research" / "topics"
ASCII_TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9]*")
FM_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
TOPIC_SECTION_RE = re.compile(
    r"#\s*Topic\s*\n(.+?)(?=\n##\s|\Z)", re.DOTALL
)


def now_iso() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


def slugify(topic: str, override: str | None = None) -> str:
    """Deterministic slug: up to 4 ASCII tokens + 8-char sha256 suffix.

    Korean-only topics collapse to just the hash prefix `topic-<hash8>`, which
    is stable and language-independent. Users can pass --slug to override.
    """
    if override:
        cleaned = re.sub(r"[^A-Za-z0-9-]", "-", override.strip().lower())
        return re.sub(r"-+", "-", cleaned).strip("-") or "topic"
    tokens = [t.lower() for t in ASCII_TOKEN_RE.findall(topic)][:4]
    digest = hashlib.sha256(topic.encode("utf-8")).hexdigest()[:8]
    if tokens:
        return f"{'-'.join(tokens)}-{digest}"
    return f"topic-{digest}"


def _load_topic_text(path: Path) -> str | None:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return None
    m = TOPIC_SECTION_RE.search(text)
    return m.group(1).strip() if m else None


def resolve_unique_slug(base: str, topic: str) -> str:
    """Return base, or base-2/-3/... if an existing file has a different topic."""
    TOPICS_DIR.mkdir(parents=True, exist_ok=True)
    slug = base
    i = 2
    while True:
        path = TOPICS_DIR / f"{slug}.md"
        if not path.exists():
            return slug
        existing = _load_topic_text(path)
        if existing is not None and existing.strip() == topic.strip():
            return slug
        print(
            f"[topic_log] slug collision: '{slug}' used for different topic, "
            f"trying '{base}-{i}'",
            file=sys.stderr,
        )
        slug = f"{base}-{i}"
        i += 1


def load_by_slug(slug: str) -> str:
    path = TOPICS_DIR / f"{slug}.md"
    if not path.exists():
        print(f"[topic_log] no such topic file: {path}", file=sys.stderr)
        sys.exit(4)
    text = _load_topic_text(path)
    if not text:
        print(f"[topic_log] topic section missing in {path}", file=sys.stderr)
        sys.exit(4)
    return text


def _format_run_line(now: str, stats: dict) -> str:
    thr = stats.get("threshold")
    thr_desc = f"threshold {thr}" if thr is not None else "top-n"
    line = (
        f"- {now} — scanned {stats.get('scanned', 0)}, "
        f"accepted {stats.get('accepted', 0)} ({thr_desc})"
    )
    slugs = stats.get("accepted_slugs") or []
    if slugs:
        line += f" [{', '.join(slugs)}]"
    return line


def _new_file_body(slug: str, topic: str, now: str, stats: dict) -> str:
    fm = {
        "slug": slug,
        "created_at": now,
        "last_run_at": now,
        "run_count": 1,
    }
    fm_text = yaml.safe_dump(fm, allow_unicode=True, sort_keys=False).strip()
    run_line = _format_run_line(now, stats)
    return (
        f"---\n{fm_text}\n---\n\n"
        f"# Topic\n{topic.strip()}\n\n"
        f"## Runs\n{run_line}\n"
    )


def append_run(slug: str, topic: str, stats: dict) -> Path:
    TOPICS_DIR.mkdir(parents=True, exist_ok=True)
    path = TOPICS_DIR / f"{slug}.md"
    now = now_iso()
    with open(path, "a+", encoding="utf-8") as f:
        fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        try:
            f.seek(0)
            existing = f.read()
            if not existing:
                new_text = _new_file_body(slug, topic, now, stats)
            else:
                fm_match = FM_RE.match(existing)
                if not fm_match:
                    new_text = _new_file_body(slug, topic, now, stats)
                else:
                    fm_data = yaml.safe_load(fm_match.group(1)) or {}
                    fm_data["last_run_at"] = now
                    fm_data["run_count"] = int(fm_data.get("run_count", 0)) + 1
                    new_fm = yaml.safe_dump(
                        fm_data, allow_unicode=True, sort_keys=False
                    ).strip()
                    body = existing[fm_match.end():]
                    run_line = _format_run_line(now, stats)
                    if re.search(r"^##\s*Runs\s*$", body, re.MULTILINE):
                        body = body.rstrip() + f"\n{run_line}\n"
                    else:
                        body = body.rstrip() + f"\n\n## Runs\n{run_line}\n"
                    new_text = f"---\n{new_fm}\n---\n{body}"
            f.seek(0)
            f.truncate()
            f.write(new_text)
            f.flush()
        finally:
            fcntl.flock(f.fileno(), fcntl.LOCK_UN)
    return path


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="cmd", required=True)

    s_slug = sub.add_parser("slug", help="Compute slug for topic")
    s_slug.add_argument("--topic", required=True)
    s_slug.add_argument("--override", default=None, help="Manual slug override")

    s_load = sub.add_parser("load", help="Load topic text by slug")
    s_load.add_argument("slug")

    s_append = sub.add_parser(
        "append", help="Create or append topic file with run stats"
    )
    s_append.add_argument("--slug", required=True)
    s_append.add_argument("--topic", required=True)
    s_append.add_argument(
        "--stats-json", required=True,
        help='JSON: {"scanned":N,"accepted":N,"threshold":float|null,'
             '"accepted_slugs":[...]}',
    )

    args = ap.parse_args()

    if args.cmd == "slug":
        base = slugify(args.topic, args.override)
        print(resolve_unique_slug(base, args.topic))
    elif args.cmd == "load":
        print(load_by_slug(args.slug))
    elif args.cmd == "append":
        try:
            stats = json.loads(args.stats_json)
        except json.JSONDecodeError as e:
            print(f"[topic_log] --stats-json invalid: {e}", file=sys.stderr)
            return 2
        print(append_run(args.slug, args.topic, stats))
    return 0


if __name__ == "__main__":
    sys.exit(main())

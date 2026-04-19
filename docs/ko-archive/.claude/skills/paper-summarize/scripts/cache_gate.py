#!/usr/bin/env python3
"""cache_gate.py — classify accepted raw.md paths into {hits, stale, misses}.

Given a list of paper-hunter raw.md paths, determine for each whether its
corresponding Marp summary is:
  - hit:   summary exists AND summary.frontmatter.source_digest_sha256 ==
           sha256(<slug>.digest.md) AND prompt_version matches digest
  - stale: summary exists but the SHA mismatches (including missing field
           from pre-v7 summaries) OR the digest file is corrupt
  - miss:  digest or summary is absent

Output is emitted as JSON (written to --out) with three keys:
    {"hits": [...], "stale": [...], "misses": [...]}

Values are the input raw.md paths verbatim (absolute), so callers can chunk
and re-pass them to the paper-summarizer agent.

Usage:
    python3 cache_gate.py --paths <raw_md> [<raw_md> ...] --out <out.json>

Exit codes:
    0  classification written
    1  input/usage error (a raw.md path does not exist or has no metadata/ ancestor)
    2  output path unwritable
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


def _log(msg: str) -> None:
    print(f"[cache_gate] {msg}", file=sys.stderr, flush=True)


def _resolve_slug(raw_md: Path) -> str:
    """Best-effort slug from `<slug>.raw.md` filename, falling back to frontmatter."""
    name = raw_md.name
    if name.endswith(".raw.md"):
        base = name[: -len(".raw.md")]
        if base:
            return base
    # Fallback: parse frontmatter slug scalar.
    text = raw_md.read_text(encoding="utf-8", errors="replace")
    m = re.search(r'^\s*slug\s*:\s*"?([^"\n]+)"?\s*$', text, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return raw_md.stem


def _parse_raw_frontmatter(raw_md: Path) -> dict:
    text = raw_md.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end < 0:
        return {}
    fm = text[3:end]
    meta: dict = {}
    for line in fm.splitlines():
        m = re.match(r'^\s*([A-Za-z_][A-Za-z0-9_]*)\s*:\s*"?([^"\n]*)"?\s*$', line)
        if m:
            meta[m.group(1)] = m.group(2).strip()
    return meta


def _papers_root(raw_md: Path) -> Path | None:
    """Walk up until we find `.../papers/metadata/...` and return `.../papers`."""
    parts = raw_md.parts
    try:
        idx = parts.index("metadata")
    except ValueError:
        return None
    return Path(*parts[:idx])


def _venue_year_subpath(raw_md: Path) -> Path | None:
    parts = raw_md.parts
    try:
        idx = parts.index("metadata")
    except ValueError:
        return None
    return Path(*parts[idx + 1 : -1])


def _digest_path(raw_md: Path, slug: str) -> Path | None:
    root = _papers_root(raw_md)
    sub = _venue_year_subpath(raw_md)
    if root is None or sub is None:
        return None
    return root / "digest" / sub / f"{slug}.digest.md"


def _summary_path(raw_md: Path, slug: str) -> Path | None:
    """Route by venue_class: whitelist → <V>/<Y>/, etc → etc/<Y>/."""
    root = _papers_root(raw_md)
    sub = _venue_year_subpath(raw_md)
    if root is None or sub is None:
        return None
    meta = _parse_raw_frontmatter(raw_md)
    vc = meta.get("venue_class", "whitelist")
    if vc == "etc":
        # sub is <Venue>/<Year>; etc flattens to etc/<Year>
        year = Path(*sub.parts[1:]) if len(sub.parts) >= 2 else sub
        return root / "marp-summary" / "etc" / year / f"{slug}.md"
    return root / "marp-summary" / sub / f"{slug}.md"


def _parse_summary_cache_fields(summary: Path) -> tuple[str | None, str | None]:
    """Return (source_digest_sha256, prompt_version) from summary frontmatter."""
    try:
        text = summary.read_text(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        return None, None
    if not text.startswith("---"):
        return None, None
    end = text.find("\n---", 3)
    if end < 0:
        return None, None
    fm = text[3:end]
    sha = None
    pv = None
    for line in fm.splitlines():
        m = re.match(r'^\s*source_digest_sha256\s*:\s*"?([^"\n]+)"?\s*$', line)
        if m:
            sha = m.group(1).strip()
        m2 = re.match(r'^\s*prompt_version\s*:\s*"?([^"\n]+)"?\s*$', line)
        if m2:
            pv = m2.group(1).strip()
    return sha, pv


def _parse_digest_prompt_version(digest: Path) -> str | None:
    try:
        text = digest.read_text(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        return None
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end < 0:
        return None
    fm = text[3:end]
    for line in fm.splitlines():
        m = re.match(r'^\s*prompt_version\s*:\s*"?([^"\n]+)"?\s*$', line)
        if m:
            return m.group(1).strip()
    return None


def _classify_one(raw_md: Path) -> str:
    """Return one of 'hit' | 'stale' | 'miss'."""
    slug = _resolve_slug(raw_md)
    digest = _digest_path(raw_md, slug)
    summary = _summary_path(raw_md, slug)
    if digest is None or summary is None:
        return "miss"
    if not digest.exists():
        return "miss"
    if not summary.exists():
        return "miss"

    try:
        digest_sha = hashlib.sha256(digest.read_bytes()).hexdigest()
    except Exception as e:  # noqa: BLE001
        _log(f"digest sha calc failed for {digest}: {e} → stale")
        return "stale"

    cached_sha, cached_pv = _parse_summary_cache_fields(summary)
    if cached_sha is None:
        return "stale"
    if cached_sha != digest_sha:
        return "stale"

    digest_pv = _parse_digest_prompt_version(digest)
    if digest_pv is not None and cached_pv is not None and digest_pv != cached_pv:
        return "stale"
    return "hit"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--paths", nargs="+", required=True,
                    help="absolute paths to <slug>.raw.md files")
    ap.add_argument("--out", required=True, help="output JSON path")
    args = ap.parse_args()

    result: dict[str, list[str]] = {"hits": [], "stale": [], "misses": []}
    for p_str in args.paths:
        raw_md = Path(p_str).resolve()
        if not raw_md.exists():
            _log(f"raw.md missing: {raw_md} → treating as miss")
            result["misses"].append(str(raw_md))
            continue
        cls = _classify_one(raw_md)
        if cls == "hit":
            result["hits"].append(str(raw_md))
        elif cls == "stale":
            result["stale"].append(str(raw_md))
        else:
            result["misses"].append(str(raw_md))

    try:
        out_path = Path(args.out).resolve()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(
            json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    except Exception as e:  # noqa: BLE001
        _log(f"output write failed: {e}")
        return 2

    _log(
        f"classified: hits={len(result['hits'])} "
        f"stale={len(result['stale'])} misses={len(result['misses'])}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())

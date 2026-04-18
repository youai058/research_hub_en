#!/usr/bin/env python3
"""kg_skeleton.py — emit the deterministic portion of a paper's `.kg.json`.

Reads a digest.md's YAML frontmatter and emits a schema-valid KGFile JSON
containing Paper, Author, Venue, Method, Dataset, Model, Metric nodes plus
AUTHORED_BY, PUBLISHED_IN, USES_METHOD, USES_DATASET, USES_MODEL edges.

Deliberately does NOT emit Claim, Result, MAKES_CLAIM, REPORTS_RESULT,
EVIDENCED_BY — those require interpretation of the paper content and are
left for paper-summarizer (Claude) to author on top of this skeleton.

Usage:
    python3 kg_skeleton.py --digest <path> --slug <slug> --out <path>

Exit codes:
    0  skeleton written successfully
    1  input/usage error (digest missing, --slug missing, etc.)
    2  output path unwritable
    3  schema validation failed (no file written)
"""

from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import re
import sys
from pathlib import Path

KST = _dt.timezone(_dt.timedelta(hours=9))


def _log(msg: str) -> None:
    print(f"[kg_skeleton] {msg}", file=sys.stderr, flush=True)


def _now_kst_iso() -> str:
    return _dt.datetime.now(KST).strftime("%Y-%m-%dT%H:%M:%S%z")


def _slugify(name: str) -> str:
    """Collapse arbitrary entity name to a kg ID suffix: lowercase, alnum+hyphen."""
    s = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return s or "unnamed"


def _parse_frontmatter(digest_path: Path) -> tuple[dict, str]:
    """Parse YAML frontmatter. Returns (meta, body).

    Supports the subset produced by gemini_digest.py v7: scalar keys quoted,
    and list keys (authors, methods, datasets, models, metrics, figures)
    with `- "item"` entries OR inline `[]`.
    """
    text = digest_path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        raise ValueError(f"digest missing YAML frontmatter: {digest_path}")
    end = text.find("\n---", 3)
    if end < 0:
        raise ValueError(f"digest frontmatter not closed: {digest_path}")
    fm_block = text[3:end].strip("\n")
    body = text[end + 4 :].lstrip("\n")

    meta: dict = {}
    current_list_key: str | None = None
    for line in fm_block.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            current_list_key = None
            continue
        # List continuation: `  - "item"` or `  - item`
        m_list = re.match(r"^\s+-\s+(.*)$", line)
        if m_list and current_list_key is not None:
            val = m_list.group(1).strip()
            if len(val) >= 2 and val[0] == val[-1] and val[0] in ("'", '"'):
                val = val[1:-1]
            meta[current_list_key].append(val)
            continue
        # Scalar or list-start: `key: value` or `key:` (then list continues)
        m_kv = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.*)$", line)
        if not m_kv:
            current_list_key = None
            continue
        key = m_kv.group(1)
        val = m_kv.group(2).strip()
        if val == "":
            meta[key] = []
            current_list_key = key
            continue
        if val == "[]":
            meta[key] = []
            current_list_key = None
            continue
        # scalar
        if len(val) >= 2 and val[0] == val[-1] and val[0] in ("'", '"'):
            val = val[1:-1]
        meta[key] = val
        current_list_key = None
    return meta, body


def _build_skeleton(meta: dict, slug: str, digest_path: Path) -> dict:
    slug_id = _slugify(slug)
    nodes: list[dict] = []
    edges: list[dict] = []

    # --- Paper node ---
    paper_id = f"paper:{slug_id}"
    nodes.append({
        "id": paper_id,
        "type": "Paper",
        "name": meta.get("slug", slug),
        "meta": {
            "venue": meta.get("venue", ""),
            "year": meta.get("year", ""),
            "venue_class": meta.get("venue_class", ""),
            "source_digest": str(digest_path),
        },
    })

    # --- Venue node + PUBLISHED_IN edge ---
    venue = meta.get("venue", "").strip()
    year = meta.get("year", "").strip()
    if venue:
        venue_id = f"venue:{_slugify(venue)}-{_slugify(year)}" if year else f"venue:{_slugify(venue)}"
        nodes.append({
            "id": venue_id, "type": "Venue", "name": venue,
            "meta": {"year": year},
        })
        edges.append({
            "src": paper_id, "type": "PUBLISHED_IN", "dst": venue_id, "meta": {},
        })

    # --- Author nodes + AUTHORED_BY edges ---
    for author_name in meta.get("authors", []) or []:
        aid = f"author:{_slugify(author_name)}"
        nodes.append({
            "id": aid, "type": "Author", "name": author_name, "meta": {},
        })
        edges.append({
            "src": paper_id, "type": "AUTHORED_BY", "dst": aid, "meta": {},
        })

    # --- canonical entity nodes (Method/Dataset/Model/Metric) ---
    # These types are in ALIAS_REQUIRED_TYPES. We emit them with alias_check
    # queried_existing=False + rationale so they pass bootstrap softening
    # (kg-curator handles alias merges; skeleton makes a best-effort identity).
    def _alias_stub(rationale: str) -> dict:
        return {
            "queried_existing": False,
            "matched": None,
            "rationale": rationale,
        }

    entity_specs = [
        ("methods", "Method", "method", "USES_METHOD"),
        ("datasets", "Dataset", "dataset", "USES_DATASET"),
        ("models", "Model", "model", "USES_MODEL"),
        ("metrics", "Metric", "metric", "MEASURES_WITH"),
    ]
    for digest_key, type_name, id_prefix, edge_type in entity_specs:
        for name in meta.get(digest_key, []) or []:
            entity_id = f"{id_prefix}:{_slugify(name)}"
            nodes.append({
                "id": entity_id,
                "type": type_name,
                "name": name,
                "meta": {},
                "alias_check": _alias_stub(
                    f"emitted by kg_skeleton.py from digest frontmatter "
                    f"field `{digest_key}`; kg-curator should resolve aliases"
                ),
            })
            edges.append({
                "src": paper_id, "type": edge_type, "dst": entity_id, "meta": {},
            })

    # --- file envelope ---
    source_sha = hashlib.sha256(digest_path.read_bytes()).hexdigest()
    return {
        "version": 1,
        "source_file": str(digest_path),
        "source_sha": source_sha,
        "author_agent": "kg_skeleton.py",
        "extracted_at": _now_kst_iso(),
        "nodes": nodes,
        "edges": edges,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--digest", required=True, help="path to <slug>.digest.md")
    ap.add_argument("--slug", required=True, help="paper slug")
    ap.add_argument("--out", required=True, help="output .kg.skeleton.json path")
    args = ap.parse_args()

    digest_path = Path(args.digest).resolve()
    out_path = Path(args.out).resolve()

    if not digest_path.exists():
        _log(f"digest not found: {digest_path}")
        return 1

    try:
        meta, _body = _parse_frontmatter(digest_path)
    except Exception as e:  # noqa: BLE001
        _log(f"frontmatter parse failed: {e}")
        return 1

    skeleton = _build_skeleton(meta, args.slug, digest_path)

    # Schema validation (hard requirement — no file written on failure).
    try:
        sys.path.insert(
            0,
            str(Path(__file__).resolve().parent.parent.parent / "paper-kg" / "scripts"),
        )
        from schema import KGFile  # type: ignore
        KGFile.model_validate(skeleton)
    except Exception as e:  # noqa: BLE001
        _log(f"schema validation failed: {e}")
        return 3

    try:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(
            json.dumps(skeleton, ensure_ascii=False, indent=2, sort_keys=False) + "\n",
            encoding="utf-8",
        )
    except Exception as e:  # noqa: BLE001
        _log(f"output write failed: {e}")
        return 2

    _log(f"wrote skeleton: {out_path} (nodes={len(skeleton['nodes'])}, edges={len(skeleton['edges'])})")
    return 0


if __name__ == "__main__":
    sys.exit(main())

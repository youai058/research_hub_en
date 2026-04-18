#!/usr/bin/env python3
"""Dense-retrieval pre-filter for paper-triage.

Takes a topic (topic.json spec OR flat string) and returns the top-K raw.md
candidates from the `abstracts` ChromaDB collection, after applying an
`exclude` substring veto and a `signal_methods` +0.05 cosine boost.

Usage:
  python3 retrieve.py --topic-spec <path>        # structured topic
  python3 retrieve.py --topic "<string>"         # flat topic
  python3 retrieve.py --topic-from <slug>        # reuse previously logged topic
  [--k-cap 300] [--cosine-threshold 0.5] [--root <path>]

Output:
  stdout: JSON list [{path, slug, title, abstract, venue, year, venue_class,
          published, categories, cos_score, signal_hit}]
  stderr: single-line summary
Exit codes:
  0 normal
  2 argument error / topic missing or malformed
  3 missing sentence-transformers / chromadb
  5 abstracts collection missing or empty
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

COLLECTION = "abstracts"
EMBED_MODEL = "BAAI/bge-m3"


def find_root(explicit: str | None) -> Path:
    if explicit:
        return Path(explicit).resolve()
    here = Path(__file__).resolve()
    for p in [here.parent, *here.parents]:
        if (p / "papers").is_dir() and (p / "research").is_dir():
            return p
    cand = Path("/home/irteam/sw/research_hub")
    if cand.is_dir():
        return cand
    raise SystemExit("cannot locate research_hub root (use --root)")


def resolve_topic(args, root: Path) -> tuple[str, list[str], list[str]]:
    """Return (query_text, exclude_list, signal_methods).

    Priority: --topic-spec > --topic > --topic-from. Exactly one required.
    """
    modes = [bool(args.topic_spec), bool(args.topic), bool(args.topic_from)]
    if sum(modes) != 1:
        print("[retrieve] exactly one of --topic-spec / --topic / --topic-from required",
              file=sys.stderr)
        sys.exit(2)

    if args.topic_spec:
        spec_path = Path(args.topic_spec).resolve()
        if not spec_path.is_file():
            print(f"[retrieve] topic spec not found: {spec_path}", file=sys.stderr)
            sys.exit(2)
        validator = Path(__file__).resolve().parents[3] / "skills" / "topic-refine" / "scripts" / "topic_spec.py"
        r = subprocess.run(
            [sys.executable, str(validator), "validate", str(spec_path)],
            capture_output=True, text=True,
        )
        if r.returncode != 0:
            print(f"[retrieve] topic spec failed validation: {r.stderr.strip()}",
                  file=sys.stderr)
            sys.exit(2)
        spec = json.loads(spec_path.read_text(encoding="utf-8"))
        tc = spec.get("triage_context", {}) or {}
        refined = spec.get("refined_topic", "") or ""
        core_q = tc.get("core_question", "") or ""
        query_text = f"{refined}. {core_q}".strip(". ").strip()
        if not query_text:
            print("[retrieve] empty query text from topic spec", file=sys.stderr)
            sys.exit(2)
        exclude_list = [s for s in tc.get("exclude", []) or [] if s]
        signal_methods = [s for s in tc.get("signal_methods", []) or [] if s]
        return query_text, exclude_list, signal_methods

    if args.topic:
        return args.topic.strip(), [], []

    if args.topic_from:
        log_loader = root / ".claude" / "skills" / "paper-triage" / "scripts" / "topic_log.py"
        r = subprocess.run(
            [sys.executable, str(log_loader), "load", args.topic_from],
            capture_output=True, text=True,
        )
        if r.returncode != 0:
            print(f"[retrieve] topic_log load failed: {r.stderr.strip()}", file=sys.stderr)
            sys.exit(2)
        return r.stdout.strip(), [], []

    sys.exit(2)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    g = ap.add_mutually_exclusive_group(required=False)
    g.add_argument("--topic-spec", help="Path to topic.json (structured)")
    g.add_argument("--topic", help="Flat topic string")
    g.add_argument("--topic-from", help="Slug of an existing research/topics/<slug>.md")
    ap.add_argument("--root", default=None)
    ap.add_argument("--k-cap", type=int, default=300,
                    help="Upper bound on returned candidates (default 300)")
    ap.add_argument("--cosine-threshold", type=float, default=0.5,
                    help="Minimum cosine similarity (after signal boost) to keep")
    args = ap.parse_args()

    root = find_root(args.root)
    query_text, exclude_list, signal_methods = resolve_topic(args, root)

    try:
        import chromadb  # type: ignore
        from sentence_transformers import SentenceTransformer  # type: ignore
    except ImportError as e:
        print(f"[retrieve] missing dependency: {e}. Activate conda env LLDM.", file=sys.stderr)
        return 3

    chroma_dir = root / "papers" / "vector_db" / "chroma"
    if not chroma_dir.is_dir():
        print("[retrieve] ChromaDB directory missing. "
              "Run .claude/skills/abstract-index/scripts/index.py (A-1.5 abstract-indexer) first.",
              file=sys.stderr)
        return 5
    client = chromadb.PersistentClient(path=str(chroma_dir))
    try:
        col = client.get_collection(COLLECTION)
    except Exception:
        print("[retrieve] abstracts collection missing. "
              "Run .claude/skills/abstract-index/scripts/index.py (A-1.5 abstract-indexer) first.",
              file=sys.stderr)
        return 5
    if col.count() == 0:
        print("[retrieve] abstracts collection is empty. "
              "Run A-1.5 abstract-indexer first.", file=sys.stderr)
        return 5

    model = SentenceTransformer(EMBED_MODEL)
    q_vec = model.encode([query_text], normalize_embeddings=True)[0].tolist()

    # n_results=k_cap because the cosine-threshold cutoff is applied client-side
    # (Chroma has no native similarity floor).
    hits = col.query(
        query_embeddings=[q_vec],
        n_results=args.k_cap,
        include=["metadatas", "documents", "distances"],
    )

    metadatas = hits.get("metadatas", [[]])[0]
    distances = hits.get("distances", [[]])[0]
    documents = hits.get("documents", [[]])[0]
    ids = hits.get("ids", [[]])[0]

    exc_lower = [e.lower() for e in exclude_list]
    sm_lower = [s.lower() for s in signal_methods]

    out: list[dict] = []
    vetoed = 0
    boosted = 0
    for doc_id, meta, dist, doc in zip(ids, metadatas, distances, documents):
        cos_sim = 1.0 - float(dist)
        title = (meta.get("title") or "")
        abstract = (meta.get("abstract") or "")
        text_lower = f"{title}\n{abstract}".lower()

        if any(e in text_lower for e in exc_lower):
            vetoed += 1
            continue

        signal_hit = any(s in text_lower for s in sm_lower)
        if signal_hit:
            cos_sim += 0.05
            boosted += 1

        if cos_sim < args.cosine_threshold:
            continue

        # Re-derive the raw.md path from the slug + manifest so we emit the
        # exact path the triage agent expects. Look up in the manifest (cheap).
        path = _path_from_slug(root, meta.get("slug", doc_id))

        out.append({
            "path": path,
            "slug": meta.get("slug", doc_id),
            "title": title,
            "abstract": abstract,
            "venue": meta.get("venue", ""),
            "year": meta.get("year", ""),
            "venue_class": meta.get("venue_class", ""),
            "published": meta.get("published", ""),
            "categories": [],  # not indexed; triage agent does not use this
            "cos_score": round(cos_sim, 4),
            "signal_hit": signal_hit,
        })

    out.sort(key=lambda h: h["cos_score"], reverse=True)
    out = out[: args.k_cap]

    print(json.dumps(out, ensure_ascii=False, indent=2))
    cos_range = (
        f"[{out[-1]['cos_score']:.3f},{out[0]['cos_score']:.3f}]"
        if out else "[n/a,n/a]"
    )
    print(
        f"[retrieve] candidates={len(out)} cos_range={cos_range} "
        f"vetoed={vetoed} boosted={boosted} threshold={args.cosine_threshold} "
        f"k_cap={args.k_cap}",
        file=sys.stderr,
    )
    return 0


def _path_from_slug(root: Path, slug: str) -> str:
    """Find the raw.md path for a given slug via the indexer manifest.

    Falls back to empty string if not found — retrieve.py is not authoritative
    on path mapping; triage will re-check existence.
    """
    manifest_path = root / "papers" / "vector_db" / "abstracts_manifest.json"
    if not manifest_path.is_file():
        return ""
    try:
        m = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return ""
    for rel, entry in m.get("files", {}).items():
        if entry.get("slug") == slug:
            return rel
    return ""


if __name__ == "__main__":
    raise SystemExit(main())

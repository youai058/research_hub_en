#!/usr/bin/env python3
"""Top-k RAG query CLI.

Usage:
  python3 query.py "your question" --k 5
  python3 query.py "q" --k 10 --filter venue=ICLR year=2026
  python3 query.py "q" --root /home/irteam/sw/research_hub

Emits JSON list to stdout.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

COLLECTION = "papers"
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


def parse_filters(items: list[str]) -> dict:
    where: dict = {}
    for it in items:
        if "=" not in it:
            continue
        k, _, v = it.partition("=")
        where[k.strip()] = v.strip()
    if len(where) <= 1:
        return where
    return {"$and": [{k: v} for k, v in where.items()]}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("question", nargs="+")
    ap.add_argument("--k", type=int, default=5)
    ap.add_argument("--filter", nargs="*", default=[])
    ap.add_argument("--root", default=None)
    ap.add_argument("--preview-chars", type=int, default=400)
    args = ap.parse_args()

    root = find_root(args.root)
    chroma_dir = root / "papers" / "vector_db" / "chroma"
    if not chroma_dir.is_dir():
        print(json.dumps({"error": f"chroma dir not found: {chroma_dir}"}))
        return 1

    import chromadb  # type: ignore
    from sentence_transformers import SentenceTransformer  # type: ignore

    client = chromadb.PersistentClient(path=str(chroma_dir))
    try:
        col = client.get_collection(COLLECTION)
    except Exception as e:
        print(json.dumps({"error": f"collection '{COLLECTION}' missing: {e}"}))
        return 1

    q = " ".join(args.question)
    model = SentenceTransformer(EMBED_MODEL)
    qv = model.encode([q], normalize_embeddings=True, show_progress_bar=False)[0].tolist()

    where = parse_filters(args.filter) or None
    res = col.query(
        query_embeddings=[qv],
        n_results=args.k,
        where=where,
        include=["documents", "metadatas", "distances"],
    )

    out = []
    docs = res.get("documents", [[]])[0]
    metas = res.get("metadatas", [[]])[0]
    ids = res.get("ids", [[]])[0]
    dists = res.get("distances", [[]])[0]
    for i in range(len(ids)):
        text = docs[i] or ""
        preview = text[: args.preview_chars]
        if len(text) > args.preview_chars:
            preview += "…"
        out.append(
            {
                "id": ids[i],
                "score": round(1.0 - float(dists[i]), 4),
                "source": (metas[i] or {}).get("source", ""),
                "section": (metas[i] or {}).get("section_title", ""),
                "slug": (metas[i] or {}).get("slug", ""),
                "venue": (metas[i] or {}).get("venue", ""),
                "year": (metas[i] or {}).get("year", ""),
                "text": preview,
            }
        )
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

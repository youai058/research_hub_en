#!/usr/bin/env python3
"""Report RAG manifest and ChromaDB collection status.

Usage:
  python3 status.py
  python3 status.py --root /home/irteam/sw/research_hub
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

COLLECTION = "papers"


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


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=None)
    args = ap.parse_args()
    root = find_root(args.root)
    rag_dir = root / "papers" / "rag"
    manifest_path = rag_dir / "manifest.json"
    chroma_dir = rag_dir / "chroma"

    info: dict = {
        "root": str(root),
        "manifest_path": str(manifest_path),
        "chroma_dir": str(chroma_dir),
        "manifest_exists": manifest_path.is_file(),
        "chroma_exists": chroma_dir.is_dir(),
    }

    if manifest_path.is_file():
        try:
            m = json.loads(manifest_path.read_text(encoding="utf-8"))
            info["embed_model"] = m.get("embed_model")
            info["last_update"] = m.get("last_update")
            info["files_tracked"] = len(m.get("files", {}))
            info["chunks_tracked"] = sum(f.get("chunks", 0) for f in m.get("files", {}).values())
            info["cursors"] = list(m.get("cursors", {}).keys())
        except Exception as e:
            info["manifest_error"] = str(e)

    if chroma_dir.is_dir():
        try:
            import chromadb  # type: ignore

            client = chromadb.PersistentClient(path=str(chroma_dir))
            try:
                col = client.get_collection(COLLECTION)
                info["collection"] = COLLECTION
                info["collection_count"] = col.count()
            except Exception as e:
                info["collection_error"] = f"{COLLECTION} missing: {e}"
        except ImportError:
            info["chromadb_import_error"] = "chromadb not installed"

    print(json.dumps(info, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

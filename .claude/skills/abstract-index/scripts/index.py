#!/usr/bin/env python3
"""Incremental abstract indexer for paper-triage dense-retrieval pre-filter.

Scans `papers/metadata/**/*.raw.md`, extracts `title` + `## Abstract`,
embeds with bge-m3, and upserts into ChromaDB collection `abstracts`.

Usage:
  python3 index.py
  python3 index.py --root /path/to/research_hub
  python3 index.py --rebuild
  python3 index.py --rebuild-manifest
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone, timedelta
from pathlib import Path

KST = timezone(timedelta(hours=9))
COLLECTION = "abstracts"
EMBED_MODEL = "BAAI/bge-m3"
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
ABSTRACT_RE = re.compile(r"##\s*Abstract\s*\n(.+?)(?=\n##\s|\Z)", re.DOTALL | re.IGNORECASE)


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


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


@dataclass
class AbstractDoc:
    doc_id: str
    text: str
    metadata: dict


def _parse_yaml_lite(front: str) -> dict:
    """Minimal frontmatter parser: key: value lines only (no nested lists).

    Enough for raw.md headers (title/venue/year/venue_class/published).
    """
    meta: dict = {}
    for line in front.splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip().strip("'").strip('"')
    return meta


def extract_abstract(path: Path) -> AbstractDoc | None:
    """Parse a raw.md file. Return None if no `## Abstract` block or no frontmatter."""
    text = path.read_text(encoding="utf-8", errors="replace")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    meta = _parse_yaml_lite(m.group(1))
    am = ABSTRACT_RE.search(text)
    if not am:
        return None
    abstract = am.group(1).strip()
    if not abstract:
        return None
    title = meta.get("title", "") or path.stem.replace(".raw", "")
    slug = path.stem.replace(".raw", "")
    doc_text = f"{title}\n\n{abstract}"
    return AbstractDoc(
        doc_id=slug,
        text=doc_text,
        metadata={
            "slug": slug,
            "title": title,
            "abstract": abstract,
            "venue": meta.get("venue", ""),
            "year": str(meta.get("year", "")),
            "venue_class": meta.get("venue_class", ""),
            "published": meta.get("published", ""),
        },
    )


def iter_raw_md(papers_metadata_dir: Path):
    if not papers_metadata_dir.is_dir():
        return
    for p in sorted(papers_metadata_dir.rglob("*.raw.md")):
        if p.is_file():
            yield p


def load_manifest(path: Path) -> dict:
    if path.is_file():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print(f"[warn] corrupt manifest, starting fresh: {path}", file=sys.stderr)
    return {
        "version": 1,
        "embed_model": EMBED_MODEL,
        "last_update": None,
        "files": {},
    }


def save_manifest(path: Path, manifest: dict) -> None:
    manifest["last_update"] = datetime.now(KST).isoformat(timespec="seconds")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")


def get_collection(chroma_dir: Path, rebuild: bool):
    import chromadb  # type: ignore

    client = chromadb.PersistentClient(path=str(chroma_dir))
    if rebuild:
        try:
            client.delete_collection(COLLECTION)
        except Exception:
            pass
    return client.get_or_create_collection(
        name=COLLECTION, metadata={"hnsw:space": "cosine"}
    )


def load_embedder():
    from sentence_transformers import SentenceTransformer  # type: ignore

    return SentenceTransformer(EMBED_MODEL)


def embed(model, texts: list[str]) -> list[list[float]]:
    vecs = model.encode(texts, normalize_embeddings=True, show_progress_bar=False)
    return [v.tolist() for v in vecs]


def run(root: Path, rebuild: bool, rebuild_manifest: bool) -> dict:
    papers_meta = root / "papers" / "metadata"
    vdb = root / "papers" / "vector_db"
    chroma_dir = vdb / "chroma"
    manifest_path = vdb / "abstracts_manifest.json"
    vdb.mkdir(parents=True, exist_ok=True)

    manifest = load_manifest(manifest_path)
    if rebuild:
        manifest["files"] = {}

    current: dict[str, dict] = {}
    to_upsert: list[Path] = []
    for p in iter_raw_md(papers_meta):
        data = p.read_bytes()
        sha = sha256_bytes(data)
        try:
            rel = p.relative_to(root).as_posix()
        except ValueError:
            rel = str(p)
        current[rel] = {
            "sha256": sha,
            "mtime": int(p.stat().st_mtime),
            "slug": p.stem.replace(".raw", ""),
        }
        if rebuild_manifest:
            continue
        prior = manifest["files"].get(rel)
        if rebuild or not prior or prior.get("sha256") != sha:
            to_upsert.append(p)

    removed_rels = [rel for rel in manifest["files"] if rel not in current]

    if rebuild_manifest:
        manifest["files"] = current
        save_manifest(manifest_path, manifest)
        return {"rebuilt_manifest": True, "files": len(current),
                "added": 0, "updated": 0, "deleted": 0, "skipped": 0}

    if not to_upsert and not removed_rels and not rebuild:
        manifest["files"] = current
        save_manifest(manifest_path, manifest)
        return {"indexed": len(current), "added": 0, "updated": 0,
                "deleted": 0, "skipped": 0}

    collection = get_collection(chroma_dir, rebuild=rebuild)

    # Handle deletions
    deleted = 0
    if removed_rels:
        ids = [manifest["files"][rel]["slug"] for rel in removed_rels
               if "slug" in manifest["files"][rel]]
        if ids:
            try:
                collection.delete(ids=ids)
                deleted = len(ids)
            except Exception as e:
                print(f"[warn] delete failed: {e}", file=sys.stderr)

    # Handle upserts
    added = 0
    updated = 0
    skipped = 0
    if to_upsert:
        model = load_embedder()
        batch_size = 64
        batch_docs: list[AbstractDoc] = []
        batch_rels: list[str] = []

        def flush():
            nonlocal added, updated
            if not batch_docs:
                return
            ids = [d.doc_id for d in batch_docs]
            texts = [d.text for d in batch_docs]
            metas = [d.metadata for d in batch_docs]
            vecs = embed(model, texts)
            collection.upsert(ids=ids, embeddings=vecs, documents=texts, metadatas=metas)
            for rel, d in zip(batch_rels, batch_docs):
                if rel in manifest["files"]:
                    updated += 1
                else:
                    added += 1
            batch_docs.clear()
            batch_rels.clear()

        for p in to_upsert:
            doc = extract_abstract(p)
            try:
                rel = p.relative_to(root).as_posix()
            except ValueError:
                rel = str(p)
            if doc is None:
                skipped += 1
                print(f"[skip] no frontmatter or abstract: {rel}", file=sys.stderr)
                continue
            batch_docs.append(doc)
            batch_rels.append(rel)
            if len(batch_docs) >= batch_size:
                flush()
        flush()

    manifest["files"] = current
    save_manifest(manifest_path, manifest)
    return {
        "indexed": len(current),
        "added": added,
        "updated": updated,
        "deleted": deleted,
        "skipped": skipped,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", default=None)
    ap.add_argument("--rebuild", action="store_true")
    ap.add_argument("--rebuild-manifest", action="store_true")
    args = ap.parse_args()
    root = find_root(args.root)
    t0 = time.time()
    try:
        summary = run(root, rebuild=args.rebuild, rebuild_manifest=args.rebuild_manifest)
    except ImportError as e:
        print(f"[fatal] missing dependency: {e}. Activate conda env LLDM.", file=sys.stderr)
        return 3
    summary["elapsed_s"] = round(time.time() - t0, 2)
    # Emit summary JSON to stderr so stdout remains reserved (future: path list).
    print(json.dumps(summary, ensure_ascii=False, indent=2), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

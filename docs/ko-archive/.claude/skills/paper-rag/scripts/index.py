#!/usr/bin/env python3
"""Incremental RAG indexer for papers/marp-summary/**/*.md using ChromaDB + bge-m3.

Usage:
  python3 index.py                    # incremental (default)
  python3 index.py --rebuild          # drop collection and rebuild
  python3 index.py --rebuild-manifest # recompute hashes only
  python3 index.py --root /path       # override research_hub root

Run from any cwd; root auto-detected or passed via --root.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Iterable

KST = timezone(timedelta(hours=9))
CHUNK_TOKEN_LIMIT = 1200
COLLECTION = "papers"
EMBED_MODEL = "BAAI/bge-m3"
# Directories under papers/ that must NEVER be indexed. Any path whose
# parts include one of these (exact match) or whose component starts
# with underscore is skipped.
SKIP_DIRS = {"_fixture", "rag", "kg", "vector_db"}


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


def approx_tokens(text: str) -> int:
    return int(len(text.split()) * 1.3) + 1


@dataclass
class Chunk:
    chunk_id: str
    text: str
    metadata: dict = field(default_factory=dict)


def parse_frontmatter(md: str) -> tuple[dict, str]:
    if not md.startswith("---\n"):
        return {}, md
    end = md.find("\n---\n", 4)
    if end == -1:
        return {}, md
    front = md[4:end]
    body = md[end + 5 :]
    meta: dict = {}
    for line in front.splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            meta[k.strip()] = v.strip().strip("'").strip('"')
    return meta, body


def split_sections(body: str) -> list[tuple[str, str]]:
    """Return [(title, text)] by `##` headings. Leading text stored as 'Intro'."""
    lines = body.splitlines()
    sections: list[tuple[str, list[str]]] = [("Intro", [])]
    for line in lines:
        m = re.match(r"^#{2,3}\s+(.*)$", line)
        if m:
            sections.append((m.group(1).strip(), []))
        else:
            sections[-1][1].append(line)
    out = [(t, "\n".join(buf).strip()) for t, buf in sections if "\n".join(buf).strip()]
    return out


def _atomic_segments(section_text: str) -> list[str]:
    """Split a section into atoms, keeping $$...$$ and markdown tables intact.

    An atom is either:
      - a preserved block (math or table), or
      - a run of paragraph text between blocks.
    """
    segments: list[str] = []
    i = 0
    n = len(section_text)
    buf: list[str] = []

    def flush_buf():
        if buf:
            txt = "\n".join(buf).strip()
            if txt:
                segments.append(txt)
            buf.clear()

    lines = section_text.split("\n")
    idx = 0
    while idx < len(lines):
        line = lines[idx]
        if line.strip().startswith("$$"):
            flush_buf()
            block = [line]
            idx += 1
            while idx < len(lines):
                block.append(lines[idx])
                if lines[idx].strip().endswith("$$"):
                    idx += 1
                    break
                idx += 1
            segments.append("\n".join(block))
            continue
        if line.lstrip().startswith("|") and idx + 1 < len(lines) and re.match(r"^\s*\|[\s\-:|]+\|\s*$", lines[idx + 1]):
            flush_buf()
            block = [line, lines[idx + 1]]
            idx += 2
            while idx < len(lines) and lines[idx].lstrip().startswith("|"):
                block.append(lines[idx])
                idx += 1
            segments.append("\n".join(block))
            continue
        buf.append(line)
        idx += 1
    flush_buf()
    return segments


def _pack_segments(segments: list[str], limit: int) -> list[str]:
    """Greedy pack atoms into chunks under the token limit. Atoms larger than
    limit are emitted standalone (we never split math/table blocks)."""
    chunks: list[str] = []
    cur: list[str] = []
    cur_tok = 0
    for seg in segments:
        seg_tok = approx_tokens(seg)
        if seg_tok >= limit:
            if cur:
                chunks.append("\n\n".join(cur))
                cur, cur_tok = [], 0
            chunks.append(seg)
            continue
        if cur_tok + seg_tok > limit and cur:
            chunks.append("\n\n".join(cur))
            cur, cur_tok = [], 0
        cur.append(seg)
        cur_tok += seg_tok
    if cur:
        chunks.append("\n\n".join(cur))
    return chunks


def chunk_paper(path: Path, root: Path) -> tuple[dict, list[Chunk]]:
    md = path.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(md)
    slug = path.stem
    try:
        rel = path.relative_to(root).as_posix()
    except ValueError:
        rel = str(path)
    base_meta = {
        "slug": slug,
        "source": rel,
        "title": meta.get("title", slug),
        "venue": meta.get("venue", ""),
        "year": meta.get("year", ""),
        "authors": meta.get("authors", ""),
    }
    sections = split_sections(body)
    chunks: list[Chunk] = []
    for sec_idx, (title, text) in enumerate(sections):
        atoms = _atomic_segments(text)
        packed = _pack_segments(atoms, CHUNK_TOKEN_LIMIT)
        for c_idx, c_text in enumerate(packed):
            cid = f"{slug}_{sec_idx}_{c_idx}"
            cm = dict(base_meta)
            cm["section_title"] = title
            cm["section_idx"] = sec_idx
            cm["chunk_idx"] = c_idx
            chunks.append(Chunk(cid, c_text, cm))
    return base_meta, chunks


def iter_papers(papers_dir: Path) -> Iterable[Path]:
    marp_dir = papers_dir / "marp-summary"
    if not marp_dir.is_dir():
        return
    for p in sorted(marp_dir.rglob("*.md")):
        if p.name.endswith(".raw.md"):
            continue
        try:
            rel_parts = p.relative_to(marp_dir).parts
        except ValueError:
            rel_parts = p.parts
        skip = False
        for part in rel_parts[:-1]:  # exclude filename
            if part in SKIP_DIRS or part.startswith("_"):
                skip = True
                break
        if skip:
            continue
        yield p


def load_manifest(manifest_path: Path) -> dict:
    if manifest_path.is_file():
        try:
            return json.loads(manifest_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print(f"[warn] manifest corrupt, starting fresh: {manifest_path}", file=sys.stderr)
    return {
        "version": 1,
        "embed_model": EMBED_MODEL,
        "last_update": None,
        "files": {},
        "cursors": {},
    }


def save_manifest(manifest_path: Path, manifest: dict) -> None:
    manifest["last_update"] = datetime.now(KST).isoformat(timespec="seconds")
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")


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


def index(root: Path, rebuild: bool, rebuild_manifest: bool) -> dict:
    papers_dir = root / "papers"
    vdb_dir = papers_dir / "vector_db"
    chroma_dir = vdb_dir / "chroma"
    manifest_path = vdb_dir / "manifest.json"
    vdb_dir.mkdir(parents=True, exist_ok=True)

    manifest = load_manifest(manifest_path)
    if rebuild:
        manifest["files"] = {}

    paths = list(iter_papers(papers_dir))
    current: dict[str, dict] = {}
    to_reindex: list[Path] = []
    for p in paths:
        data = p.read_bytes()
        sha = sha256_bytes(data)
        try:
            rel = p.relative_to(root).as_posix()
        except ValueError:
            rel = str(p)
        prior = manifest["files"].get(rel)
        entry = {
            "sha256": sha,
            "mtime": int(p.stat().st_mtime),
            "chunks": prior.get("chunks", 0) if prior else 0,
            "chunk_ids": prior.get("chunk_ids", []) if prior else [],
        }
        current[rel] = entry
        if rebuild_manifest:
            continue
        if rebuild or not prior or prior.get("sha256") != sha:
            to_reindex.append(p)

    removed = [rel for rel in manifest["files"] if rel not in current]

    if rebuild_manifest:
        manifest["files"] = current
        save_manifest(manifest_path, manifest)
        return {"rebuilt_manifest": True, "files": len(current)}

    if not to_reindex and not removed and not rebuild:
        manifest["files"] = current
        save_manifest(manifest_path, manifest)
        return {"changed": 0, "removed": 0, "files": len(current)}

    collection = get_collection(chroma_dir, rebuild=rebuild)

    for rel in removed:
        ids = manifest["files"][rel].get("chunk_ids", [])
        if ids:
            try:
                collection.delete(ids=ids)
            except Exception as e:
                print(f"[warn] delete failed for {rel}: {e}", file=sys.stderr)

    total_chunks = 0
    if to_reindex:
        model = load_embedder()
        for p in to_reindex:
            try:
                rel = p.relative_to(root).as_posix()
            except ValueError:
                rel = str(p)
            prior = manifest["files"].get(rel, {})
            prior_ids = prior.get("chunk_ids", [])
            if prior_ids:
                try:
                    collection.delete(ids=prior_ids)
                except Exception as e:
                    print(f"[warn] delete prior chunks for {rel}: {e}", file=sys.stderr)
            _, chunks = chunk_paper(p, root)
            if not chunks:
                current[rel]["chunks"] = 0
                current[rel]["chunk_ids"] = []
                continue
            ids = [c.chunk_id for c in chunks]
            texts = [c.text for c in chunks]
            metas = [c.metadata for c in chunks]
            batch = 32
            for i in range(0, len(texts), batch):
                vecs = embed(model, texts[i : i + batch])
                collection.upsert(
                    ids=ids[i : i + batch],
                    embeddings=vecs,
                    documents=texts[i : i + batch],
                    metadatas=metas[i : i + batch],
                )
            current[rel]["chunks"] = len(chunks)
            current[rel]["chunk_ids"] = ids
            total_chunks += len(chunks)
            print(f"[idx] {rel} → {len(chunks)} chunks", file=sys.stderr)

    manifest["files"] = current
    save_manifest(manifest_path, manifest)
    return {
        "changed": len(to_reindex),
        "removed": len(removed),
        "files": len(current),
        "chunks_written": total_chunks,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=None)
    ap.add_argument("--rebuild", action="store_true")
    ap.add_argument("--rebuild-manifest", action="store_true")
    args = ap.parse_args()
    root = find_root(args.root)
    t0 = time.time()
    summary = index(root, rebuild=args.rebuild, rebuild_manifest=args.rebuild_manifest)
    summary["elapsed_s"] = round(time.time() - t0, 2)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Incremental KG ingest from `.kg.json` sibling files.

Collects `*.kg.json` under papers/, research/, experiments/, docs/,
validates with Pydantic, upserts into kg.sqlite with a 2-pass transaction
(nodes first, then edges), appends to extraction_log.jsonl, and writes
rejections to rejected.jsonl.

Usage:
    python3 index.py                        # incremental
    python3 index.py --rebuild              # drop DB and re-ingest everything
    python3 index.py --rebuild-manifest     # recompute manifest hashes only
    python3 index.py --dry-run              # validate only, no DB writes
    python3 index.py --file <path>          # ingest a single file
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

import db as kgdb  # noqa: E402
from schema import (  # noqa: E402
    ALIAS_BOOTSTRAP_THRESHOLD,
    ID_REGEX,
    KGFile,
    KGNode,
    SCHEMA_VERSION,
    enforce_alias_check,
    normalize_id,
)
from pydantic import ValidationError  # noqa: E402

KST = timezone(timedelta(hours=9))

REPO_ROOT = Path(__file__).resolve().parents[4]
VDB_DIR = REPO_ROOT / "papers" / "vector_db"
DB_PATH = VDB_DIR / "kg.sqlite"
MANIFEST_PATH = VDB_DIR / "kg-manifest.json"
LOG_PATH = VDB_DIR / "extraction_log.jsonl"
REJECTED_PATH = VDB_DIR / "rejected.jsonl"
STALE_PATH = VDB_DIR / "kg.stale"
KG_STAGING_DIR = VDB_DIR / "kg-staging"

# Directories scanned for `*.kg.json` files.
# Paper KG extractions now live in a flat staging dir; research/experiments/docs
# may still produce .kg.json sibling files for non-paper entities.
SCAN_ROOTS = (
    KG_STAGING_DIR,
    REPO_ROOT / "research",
    REPO_ROOT / "experiments",
    REPO_ROOT / "docs",
)


def now_kst() -> str:
    return datetime.now(KST).isoformat(timespec="seconds")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def load_manifest() -> dict:
    if MANIFEST_PATH.exists():
        return json.loads(MANIFEST_PATH.read_text())
    return {
        "version": 1,
        "embed_model": None,
        "last_update": None,
        "files": {},
        "schema_version": SCHEMA_VERSION,
    }


def save_manifest(manifest: dict) -> None:
    manifest["schema_version"] = SCHEMA_VERSION
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")


def collect_kg_files() -> list[Path]:
    out: list[Path] = []
    for root in SCAN_ROOTS:
        if not root.exists():
            continue
        for p in sorted(root.rglob("*.kg.json")):
            # Exclude anything under a `_fixture/` subtree. These are
            # intentional test samples (including the kg-reject invalid
            # fixture). Ingesting them would either append a rejection every
            # single run (invalid fixtures) or pollute the KG with synthetic
            # nodes (valid fixtures), drowning real extractions in noise.
            if "_fixture" in p.parts:
                continue
            out.append(p)
    return out


def append_jsonl(path: Path, record: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a") as fh:
        fh.write(json.dumps(record, ensure_ascii=False) + "\n")


def reject(path: Path, reason: str, detail: str | None = None) -> None:
    append_jsonl(
        REJECTED_PATH,
        {
            "rejected_at": now_kst(),
            "source_file": str(path.relative_to(REPO_ROOT)),
            "reason": reason,
            "detail": detail,
        },
    )


def validate_file(path: Path) -> tuple[KGFile | None, str | None]:
    try:
        raw = json.loads(path.read_text())
    except json.JSONDecodeError as e:
        return None, f"invalid JSON: {e}"
    try:
        kg = KGFile.model_validate(raw)
    except ValidationError as e:
        return None, f"pydantic: {e}"
    return kg, None


def upsert_file(
    conn,
    kg: KGFile,
    abs_path: Path,
    author_agent_override: str | None = None,
) -> tuple[int, int, str | None]:
    """Run the 2-pass upsert inside a single transaction.

    Returns (nodes_upserted, edges_inserted, error_or_None).
    """
    rel = str(abs_path.relative_to(REPO_ROOT))
    author = author_agent_override or kg.author_agent
    now = now_kst()

    cur_nodes = kgdb.node_count(conn)

    # Alias-check enforcement gate (per file, using pre-ingest count).
    for node in kg.nodes:
        ok, err = enforce_alias_check(node, cur_nodes)
        if not ok:
            return 0, 0, err

    try:
        conn.execute("BEGIN")
        # Remove prior records from this file (delete-then-insert keyed by source_file).
        conn.execute("DELETE FROM edges WHERE source_file = ?", (rel,))
        conn.execute("DELETE FROM aliases WHERE source_file = ?", (rel,))
        # Nodes belonging solely to this file can be overwritten; FK RESTRICT prevents
        # dropping nodes that other files reference. We therefore UPSERT instead of delete.

        # Pass 1: nodes
        local_ids: set[str] = set()
        for node in kg.nodes:
            nid = normalize_id(node.id)
            local_ids.add(nid)
            meta_json = json.dumps(node.meta, ensure_ascii=False)
            existing = conn.execute(
                "SELECT type, source_file, meta FROM nodes WHERE id = ?", (nid,)
            ).fetchone()
            if existing:
                # H5: preserve ownership (source_file/source_sha/author_agent/
                # created_at) of the original creator. Later files can only
                # enrich name/meta; type change is a hard error.
                if existing["type"] != node.type:
                    raise ValueError(
                        f"node {nid} type conflict: "
                        f"existing={existing['type']!r} new={node.type!r} from {rel}"
                    )
                try:
                    old_meta = json.loads(existing["meta"]) or {}
                except json.JSONDecodeError:
                    old_meta = {}
                merged = {**old_meta, **node.meta}
                merged_json = json.dumps(merged, ensure_ascii=False)
                conn.execute(
                    "UPDATE nodes SET name=?, meta=?, updated_at=? WHERE id=?",
                    (node.name, merged_json, now, nid),
                )
            else:
                conn.execute(
                    "INSERT INTO nodes (id, type, name, meta, source_file, "
                    "source_sha, author_agent, created_at, updated_at) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (
                        nid,
                        node.type,
                        node.name,
                        meta_json,
                        rel,
                        kg.source_sha,
                        author,
                        now,
                        now,
                    ),
                )
            # alias_merge helper: if alias_check stores aliases metadata we don't
            # auto-write to aliases table — only `alias_merge` edges do that.

        # Pass 2: edges — validate dangling first.
        for edge in kg.edges:
            src = normalize_id(edge.src)
            dst = normalize_id(edge.dst)
            for endpoint, label in ((src, "src"), (dst, "dst")):
                if endpoint in local_ids:
                    continue
                row = conn.execute(
                    "SELECT 1 FROM nodes WHERE id = ?", (endpoint,)
                ).fetchone()
                if row is None:
                    raise ValueError(
                        f"dangling edge {label}={endpoint!r} "
                        f"(type={edge.type}, not in file nor DB)"
                    )

            if edge.type == "alias_merge":
                # Route to aliases table: dst is canonical, src is alias id.
                alias_text = str(edge.meta.get("alias_text") or src)
                conn.execute(
                    "INSERT OR IGNORE INTO aliases "
                    "(alias, canonical_id, added_by, added_at, source_file) "
                    "VALUES (?, ?, ?, ?, ?)",
                    (alias_text, dst, author, now, rel),
                )
                continue

            conn.execute(
                "INSERT INTO edges (src, type, dst, meta, source_file, "
                "source_sha, author_agent, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    src,
                    edge.type,
                    dst,
                    json.dumps(edge.meta, ensure_ascii=False),
                    rel,
                    kg.source_sha,
                    author,
                    now,
                ),
            )

        conn.execute("COMMIT")
    except Exception as e:
        conn.execute("ROLLBACK")
        return 0, 0, str(e)

    return len(kg.nodes), len(kg.edges), None


def drop_file(conn, rel_path: str) -> tuple[int, int, int]:
    """Remove all rows originating from this source file.

    Returns (nodes_dropped, edges_dropped, aliases_dropped).

    H2 cascade: after deleting edges and aliases from this file, delete
    nodes that were owned by this file AND are no longer referenced by
    any remaining edge or alias. Nodes still referenced stay; FK RESTRICT
    would block their deletion anyway.
    """
    with conn:
        edges_n = conn.execute(
            "SELECT COUNT(*) FROM edges WHERE source_file = ?", (rel_path,)
        ).fetchone()[0]
        conn.execute("DELETE FROM edges WHERE source_file = ?", (rel_path,))

        aliases_n = conn.execute(
            "SELECT COUNT(*) FROM aliases WHERE source_file = ?", (rel_path,)
        ).fetchone()[0]
        conn.execute("DELETE FROM aliases WHERE source_file = ?", (rel_path,))

        # Orphan nodes: owned by this file AND unreferenced anywhere.
        orphan_ids = [
            row[0]
            for row in conn.execute(
                "SELECT id FROM nodes WHERE source_file = ? "
                "AND id NOT IN (SELECT src FROM edges) "
                "AND id NOT IN (SELECT dst FROM edges) "
                "AND id NOT IN (SELECT canonical_id FROM aliases)",
                (rel_path,),
            ).fetchall()
        ]
        nodes_n = 0
        for nid in orphan_ids:
            try:
                conn.execute("DELETE FROM nodes WHERE id = ?", (nid,))
                nodes_n += 1
            except Exception:
                # FK RESTRICT still fired — leave the node in place.
                pass

        return nodes_n, edges_n, aliases_n


def cmd_run(
    rebuild: bool = False,
    rebuild_manifest: bool = False,
    dry_run: bool = False,
    single_file: str | None = None,
) -> dict:
    VDB_DIR.mkdir(parents=True, exist_ok=True)
    KG_STAGING_DIR.mkdir(parents=True, exist_ok=True)
    manifest = load_manifest()

    if rebuild:
        if DB_PATH.exists():
            DB_PATH.unlink()
        manifest["files"] = {}

    conn = kgdb.open_and_migrate(DB_PATH)

    if single_file:
        files = [Path(single_file).resolve()]
    else:
        files = collect_kg_files()

    if rebuild_manifest:
        manifest["files"] = {}
        for p in files:
            rel = str(p.relative_to(REPO_ROOT))
            manifest["files"][rel] = {
                "sha256": sha256_file(p),
                "mtime": p.stat().st_mtime,
            }
        manifest["last_update"] = now_kst()
        save_manifest(manifest)
        # H4: --rebuild-manifest must clear the stale flag, otherwise the
        # SessionStart hook keeps reporting the KG as stale forever.
        if STALE_PATH.exists():
            STALE_PATH.unlink()
        return {"mode": "rebuild-manifest", "files": len(files)}

    changed = 0
    rejected = 0
    unchanged = 0
    total_nodes = 0
    total_edges = 0

    current_rels: set[str] = set()
    for p in files:
        rel = str(p.relative_to(REPO_ROOT))
        current_rels.add(rel)
        sha = sha256_file(p)
        prev = manifest["files"].get(rel)
        if prev and prev.get("sha256") == sha and not rebuild:
            unchanged += 1
            continue

        kg, err = validate_file(p)
        if kg is None:
            reject(p, "validation", err)
            rejected += 1
            continue

        # Verify envelope source_sha matches computed sha (provenance integrity).
        if kg.source_sha and kg.source_sha != sha:
            # Agents may populate source_sha of their source .md, not of the .kg.json.
            # We treat mismatch as informational, not fatal.
            pass

        if dry_run:
            changed += 1
            total_nodes += len(kg.nodes)
            total_edges += len(kg.edges)
            continue

        n, e, upsert_err = upsert_file(conn, kg, p)
        if upsert_err:
            reject(p, "upsert", upsert_err)
            rejected += 1
            continue
        changed += 1
        total_nodes += n
        total_edges += e
        manifest["files"][rel] = {"sha256": sha, "mtime": p.stat().st_mtime}
        append_jsonl(
            LOG_PATH,
            {
                "ts": now_kst(),
                "action": "upsert",
                "source_file": rel,
                "nodes": n,
                "edges": e,
                "author_agent": kg.author_agent,
            },
        )

    # Handle removals: files in manifest but no longer on disk.
    removed = 0
    if not single_file and not dry_run:
        stale = [rel for rel in list(manifest["files"].keys()) if rel not in current_rels]
        for rel in stale:
            nodes_d, edges_d, aliases_d = drop_file(conn, rel)
            manifest["files"].pop(rel, None)
            removed += 1
            append_jsonl(
                LOG_PATH,
                {
                    "ts": now_kst(),
                    "action": "drop",
                    "source_file": rel,
                    "nodes_dropped": nodes_d,
                    "edges_dropped": edges_d,
                    "aliases_dropped": aliases_d,
                },
            )

    if not dry_run:
        manifest["last_update"] = now_kst()
        save_manifest(manifest)
        # Clear stale flag only on *fully successful* ingest.
        # If any file was rejected, keep .stale so the next SessionStart still
        # nudges the user to re-run `/research-kg build` after fixing the
        # offending .kg.json. This prevents the hook from silently masking a
        # partial failure. (Med-A re-audit fix.)
        if STALE_PATH.exists() and rejected == 0:
            STALE_PATH.unlink()

    return {
        "mode": "rebuild" if rebuild else ("dry-run" if dry_run else "incremental"),
        "scanned": len(files),
        "changed": changed,
        "unchanged": unchanged,
        "removed": removed,
        "rejected": rejected,
        "total_nodes_seen": total_nodes,
        "total_edges_seen": total_edges,
        "bootstrap_threshold": ALIAS_BOOTSTRAP_THRESHOLD,
    }


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(prog="paper-kg index")
    p.add_argument("--rebuild", action="store_true")
    p.add_argument("--rebuild-manifest", action="store_true")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--file", default=None)
    args = p.parse_args(argv)

    summary = cmd_run(
        rebuild=args.rebuild,
        rebuild_manifest=args.rebuild_manifest,
        dry_run=args.dry_run,
        single_file=args.file,
    )
    print(json.dumps(summary, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

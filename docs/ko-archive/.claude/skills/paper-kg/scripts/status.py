"""Print KG status: counts, by_type breakdown, manifest summary, rejected count.

Output is a single JSON object on stdout so that callers (loop_state.py,
session_start.sh) can parse it deterministically.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

import db as kgdb  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[4]
VDB_DIR = REPO_ROOT / "papers" / "vector_db"
DB_PATH = VDB_DIR / "kg.sqlite"
MANIFEST_PATH = VDB_DIR / "kg-manifest.json"
REJECTED_PATH = VDB_DIR / "rejected.jsonl"
STALE_PATH = VDB_DIR / "kg.stale"
SCHEMA_VERSION_PATH = VDB_DIR / "schema.version"


def _count_lines(path: Path) -> int:
    if not path.exists():
        return 0
    with path.open() as fh:
        return sum(1 for _ in fh)


def gather_status() -> dict:
    out: dict = {
        "db_exists": DB_PATH.exists(),
        "stale": STALE_PATH.exists(),
        "schema_version": None,
        "db_schema_version": None,
        "manifest_schema_version": None,
        "nodes": 0,
        "edges": 0,
        "by_type": {},
        "last_upsert": None,
        "rejected_count": _count_lines(REJECTED_PATH),
        "files_tracked": 0,
    }

    if SCHEMA_VERSION_PATH.exists():
        out["schema_version"] = SCHEMA_VERSION_PATH.read_text().strip()

    if MANIFEST_PATH.exists():
        manifest = json.loads(MANIFEST_PATH.read_text())
        out["last_upsert"] = manifest.get("last_update")
        out["files_tracked"] = len(manifest.get("files", {}))
        out["manifest_schema_version"] = manifest.get("schema_version")

    if out["db_exists"]:
        conn = kgdb.open_and_migrate(DB_PATH)
        out["nodes"] = kgdb.node_count(conn)
        out["edges"] = kgdb.edge_count(conn)
        out["by_type"] = kgdb.by_type(conn)
        out["db_schema_version"] = kgdb.get_schema_version(conn)

    return out


def main(_argv: list[str]) -> int:
    print(json.dumps(gather_status(), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

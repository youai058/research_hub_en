"""SQLite triplestore for paper-kg.

Schema: nodes (PK id), edges (FK src/dst → nodes), aliases (FK canonical_id).
FK policy: ON DELETE RESTRICT — silent data loss is forbidden; deletions must
go through explicit incremental upsert (delete-then-insert keyed by source_file).
"""

from __future__ import annotations

import sqlite3
import sys
from pathlib import Path

# SCHEMA_VERSION is the single source of truth, owned by schema.py.
_SCRIPT_DIR = Path(__file__).resolve().parent
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))
from schema import SCHEMA_VERSION  # noqa: E402

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS nodes (
    id            TEXT PRIMARY KEY,
    type          TEXT NOT NULL,
    name          TEXT NOT NULL,
    meta          TEXT NOT NULL,
    source_file   TEXT NOT NULL,
    source_sha    TEXT NOT NULL,
    author_agent  TEXT NOT NULL,
    created_at    TEXT NOT NULL,
    updated_at    TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_nodes_type    ON nodes(type);
CREATE INDEX IF NOT EXISTS idx_nodes_name    ON nodes(name);
CREATE INDEX IF NOT EXISTS idx_nodes_source  ON nodes(source_file);

CREATE TABLE IF NOT EXISTS edges (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    src           TEXT NOT NULL,
    type          TEXT NOT NULL,
    dst           TEXT NOT NULL,
    meta          TEXT NOT NULL,
    source_file   TEXT NOT NULL,
    source_sha    TEXT NOT NULL,
    author_agent  TEXT NOT NULL,
    created_at    TEXT NOT NULL,
    FOREIGN KEY (src) REFERENCES nodes(id) ON DELETE RESTRICT,
    FOREIGN KEY (dst) REFERENCES nodes(id) ON DELETE RESTRICT
);

CREATE INDEX IF NOT EXISTS idx_edges_src    ON edges(src);
CREATE INDEX IF NOT EXISTS idx_edges_dst    ON edges(dst);
CREATE INDEX IF NOT EXISTS idx_edges_type   ON edges(type);
CREATE INDEX IF NOT EXISTS idx_edges_source ON edges(source_file);

CREATE TABLE IF NOT EXISTS aliases (
    alias         TEXT NOT NULL,
    canonical_id  TEXT NOT NULL,
    added_by      TEXT NOT NULL,
    added_at      TEXT NOT NULL,
    source_file   TEXT NOT NULL DEFAULT '',
    PRIMARY KEY (alias, canonical_id),
    FOREIGN KEY (canonical_id) REFERENCES nodes(id) ON DELETE RESTRICT
);

CREATE INDEX IF NOT EXISTS idx_aliases_canonical ON aliases(canonical_id);
CREATE INDEX IF NOT EXISTS idx_aliases_source    ON aliases(source_file);

CREATE TABLE IF NOT EXISTS schema_meta (
    key           TEXT PRIMARY KEY,
    value         TEXT NOT NULL,
    updated_at    TEXT NOT NULL DEFAULT ''
);
"""


def open_db(path: str | Path) -> sqlite3.Connection:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(p))
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA journal_mode = WAL")
    conn.row_factory = sqlite3.Row
    return conn


def migrate(conn: sqlite3.Connection) -> None:
    conn.executescript(SCHEMA_SQL)
    # Additive column migration for pre-H2 databases that lack aliases.source_file.
    alias_cols = {row[1] for row in conn.execute("PRAGMA table_info(aliases)").fetchall()}
    if "source_file" not in alias_cols:
        conn.execute(
            "ALTER TABLE aliases ADD COLUMN source_file TEXT NOT NULL DEFAULT ''"
        )
        conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_aliases_source ON aliases(source_file)"
        )
    # W2: persist schema version in the DB itself so there's no drift between
    # schema.py / manifest.json / kg.sqlite. schema_meta is authoritative for
    # any caller that only has the sqlite file.
    from datetime import datetime, timezone, timedelta
    kst_now = datetime.now(timezone(timedelta(hours=9))).isoformat(timespec="seconds")
    conn.execute(
        "INSERT INTO schema_meta (key, value, updated_at) VALUES (?, ?, ?) "
        "ON CONFLICT(key) DO UPDATE SET value=excluded.value, updated_at=excluded.updated_at",
        ("schema_version", SCHEMA_VERSION, kst_now),
    )
    conn.commit()


def get_schema_version(conn: sqlite3.Connection) -> str | None:
    """Return schema_version stored in the DB, or None if the meta table is
    missing (pre-W2 DB)."""
    try:
        row = conn.execute(
            "SELECT value FROM schema_meta WHERE key = ?", ("schema_version",)
        ).fetchone()
    except sqlite3.OperationalError:
        return None
    return row[0] if row else None


def open_and_migrate(path: str | Path) -> sqlite3.Connection:
    conn = open_db(path)
    migrate(conn)
    return conn


def node_count(conn: sqlite3.Connection) -> int:
    return conn.execute("SELECT COUNT(*) FROM nodes").fetchone()[0]


def edge_count(conn: sqlite3.Connection) -> int:
    return conn.execute("SELECT COUNT(*) FROM edges").fetchone()[0]


def by_type(conn: sqlite3.Connection) -> dict[str, int]:
    rows = conn.execute(
        "SELECT type, COUNT(*) FROM nodes GROUP BY type ORDER BY type"
    ).fetchall()
    return {r[0]: r[1] for r in rows}


if __name__ == "__main__":
    import sys

    db_path = sys.argv[1] if len(sys.argv) > 1 else "papers/vector_db/kg.sqlite"
    conn = open_and_migrate(db_path)
    print(f"db: {db_path}")
    print(f"nodes: {node_count(conn)}")
    print(f"edges: {edge_count(conn)}")
    print(f"by_type: {by_type(conn)}")

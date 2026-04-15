"""Query interface for paper-kg triplestore.

Subcommands:
    node <id>
    neighbors <id> [--hops N] [--edge-type T]
    lookup --type T (--exact-name NAME | --name-fuzzy STR) [--k K]
    sql "SELECT ..."
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

import db as kgdb  # noqa: E402
from schema import normalize_id  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[4]
DB_PATH = REPO_ROOT / "papers" / "kg" / "kg.sqlite"

try:
    from rapidfuzz import fuzz as _rf_fuzz

    def _fuzzy_score(query: str, target: str) -> float:
        return float(_rf_fuzz.WRatio(query, target))

    _FUZZY_BACKEND = "rapidfuzz.WRatio"
except ModuleNotFoundError:
    from difflib import SequenceMatcher

    def _fuzzy_score(query: str, target: str) -> float:
        # Fallback scorer when rapidfuzz is not installed. Keeps the ≥85 gate
        # conservative: naive token-overlap / |query_tokens| can score 100 for
        # "foo" against "bar bazz foo" (one-token query subset), which would
        # silently alias-merge unrelated canonical entities. Use Jaccard
        # (|∩|/|∪|) and require ≥2 matching tokens for multi-token targets;
        # for single-token queries, require substring containment.
        q = query.lower().strip()
        t = target.lower().strip()
        if not q or not t:
            return 0.0
        # Sequence ratio as baseline — cannot alone fabricate ≥85 for wildly
        # different strings, so leave it as-is.
        base = SequenceMatcher(None, q, t).ratio() * 100.0

        q_tokens = set(re.findall(r"[a-z0-9]+", q))
        t_tokens = set(re.findall(r"[a-z0-9]+", t))

        if len(q_tokens) <= 1:
            # Single-token query: substring boost only when the match is
            # a prefix or covers ≥50% of the target length. Suffix-only
            # matches (e.g. "foo" in "bar bazz foo") are too weak — they
            # would silently alias unrelated canonical entities.
            if q and q in t and (t.startswith(q) or len(q) * 2 >= len(t)):
                base = max(base, 90.0)
            elif t and t in q:
                base = max(base, 90.0)
            return base

        if q_tokens and t_tokens:
            inter = len(q_tokens & t_tokens)
            union = len(q_tokens | t_tokens)
            jaccard = inter / union if union else 0.0
            # Require ≥2 shared tokens before boosting. A single shared token
            # across multi-word phrases is too weak a signal.
            if inter >= 2:
                base = max(base, jaccard * 100.0)
            # Substring boost only when query is wholly contained.
            if q in t:
                base = max(base, 90.0)
        return base

    _FUZZY_BACKEND = "difflib.SequenceMatcher+jaccard"


def _row_to_node(row) -> dict:
    return {
        "id": row["id"],
        "type": row["type"],
        "name": row["name"],
        "meta": json.loads(row["meta"]),
        "source_file": row["source_file"],
        "author_agent": row["author_agent"],
        "updated_at": row["updated_at"],
    }


def _row_to_edge(row) -> dict:
    return {
        "id": row["id"],
        "src": row["src"],
        "type": row["type"],
        "dst": row["dst"],
        "meta": json.loads(row["meta"]),
        "source_file": row["source_file"],
    }


def cmd_node(conn, node_id: str) -> dict | None:
    nid = normalize_id(node_id)
    row = conn.execute("SELECT * FROM nodes WHERE id = ?", (nid,)).fetchone()
    return _row_to_node(row) if row else None


def cmd_neighbors(
    conn,
    node_id: str,
    hops: int,
    edge_type: str | None,
) -> dict:
    nid = normalize_id(node_id)
    visited: set[str] = {nid}
    frontier: set[str] = {nid}
    edges: list[dict] = []
    seen_edge_ids: set[int] = set()
    for _ in range(max(1, hops)):
        next_frontier: set[str] = set()
        if not frontier:
            break
        placeholders = ",".join("?" * len(frontier))
        type_clause = " AND type = ?" if edge_type else ""
        sql = (
            f"SELECT * FROM edges WHERE (src IN ({placeholders}) "
            f"OR dst IN ({placeholders})){type_clause}"
        )
        full_params = list(frontier) + list(frontier) + ([edge_type] if edge_type else [])
        for row in conn.execute(sql, full_params):
            if row["id"] in seen_edge_ids:
                continue
            seen_edge_ids.add(row["id"])
            edges.append(_row_to_edge(row))
            for endpoint in (row["src"], row["dst"]):
                if endpoint not in visited:
                    visited.add(endpoint)
                    next_frontier.add(endpoint)
        frontier = next_frontier

    nodes = []
    if visited:
        placeholders = ",".join("?" * len(visited))
        for row in conn.execute(
            f"SELECT * FROM nodes WHERE id IN ({placeholders})", list(visited)
        ):
            nodes.append(_row_to_node(row))
    return {"root": nid, "hops": hops, "nodes": nodes, "edges": edges}


def cmd_lookup(
    conn,
    type_filter: str | None,
    exact_name: str | None,
    name_fuzzy: str | None,
    k: int,
) -> list[dict]:
    params: list = []
    where = []
    if type_filter:
        where.append("type = ?")
        params.append(type_filter)
    if exact_name:
        where.append("name = ?")
        params.append(exact_name)
    sql = "SELECT * FROM nodes"
    if where:
        sql += " WHERE " + " AND ".join(where)
    sql += " ORDER BY updated_at DESC LIMIT 500"

    rows = conn.execute(sql, params).fetchall()
    candidates = [_row_to_node(r) for r in rows]

    if name_fuzzy:
        scored = []
        for node in candidates:
            hay = node["name"]
            aliases = node["meta"].get("aliases", []) if isinstance(node["meta"], dict) else []
            best = _fuzzy_score(name_fuzzy, hay)
            for a in aliases or []:
                best = max(best, _fuzzy_score(name_fuzzy, str(a)))
            if best >= 85.0:
                node["score"] = round(best, 2)
                scored.append(node)
        scored.sort(key=lambda x: x["score"], reverse=True)
        return scored[:k]

    return candidates[:k]


def cmd_sql(conn, query: str) -> list[dict]:
    cur = conn.execute(query)
    cols = [d[0] for d in cur.description] if cur.description else []
    return [dict(zip(cols, row)) for row in cur.fetchall()]


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(prog="paper-kg query")
    sub = p.add_subparsers(dest="cmd", required=True)

    pn = sub.add_parser("node")
    pn.add_argument("id")

    pne = sub.add_parser("neighbors")
    pne.add_argument("id")
    pne.add_argument("--hops", type=int, default=1)
    pne.add_argument("--edge-type", default=None)

    pl = sub.add_parser("lookup")
    pl.add_argument("--type", dest="type_filter", default=None)
    pl.add_argument("--exact-name", default=None)
    pl.add_argument("--name-fuzzy", default=None)
    pl.add_argument("--k", type=int, default=10)

    psql = sub.add_parser("sql")
    psql.add_argument("query")

    args = p.parse_args(argv)
    if not DB_PATH.exists():
        print(json.dumps({"error": "kg.sqlite missing", "path": str(DB_PATH)}))
        return 2
    conn = kgdb.open_and_migrate(DB_PATH)

    if args.cmd == "node":
        result = cmd_node(conn, args.id)
    elif args.cmd == "neighbors":
        result = cmd_neighbors(conn, args.id, args.hops, args.edge_type)
    elif args.cmd == "lookup":
        if not (args.exact_name or args.name_fuzzy):
            print(json.dumps({"error": "lookup requires --exact-name or --name-fuzzy"}))
            return 2
        result = cmd_lookup(
            conn, args.type_filter, args.exact_name, args.name_fuzzy, args.k
        )
        if args.name_fuzzy:
            result = {"backend": _FUZZY_BACKEND, "matches": result}
    elif args.cmd == "sql":
        result = cmd_sql(conn, args.query)
    else:
        print(json.dumps({"error": f"unknown subcommand {args.cmd}"}))
        return 2

    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

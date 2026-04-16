"""Hybrid retrieval: runs RAG and KG lookups in a single pass.

RAG is invoked by importing `paper-rag/scripts/query.py` as a Python module
(not subprocess) so that the bge-m3 model and ChromaDB client can be reused
when called repeatedly from the same interpreter.

Output JSON (stdout):
    {
      "query": "...",
      "rag": {"chunks": [...]},
      "kg":  {"matched_nodes": [...], "neighbors": [...]},
      "hybrid": {"joint_rank": [...], "rationale": "..."}
    }
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

import db as kgdb  # noqa: E402
import query as kgquery  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[4]
DB_PATH = REPO_ROOT / "papers" / "vector_db" / "kg.sqlite"
RAG_QUERY_PATH = REPO_ROOT / ".claude" / "skills" / "paper-rag" / "scripts" / "query.py"

_rag_module = None


def _load_rag_module():
    global _rag_module
    if _rag_module is not None:
        return _rag_module
    if not RAG_QUERY_PATH.exists():
        return None
    spec = importlib.util.spec_from_file_location("paper_rag_query", RAG_QUERY_PATH)
    if spec is None or spec.loader is None:
        return None
    mod = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(mod)  # type: ignore[arg-type]
    except Exception:
        return None
    _rag_module = mod
    return mod


def _run_rag(question: str, k: int) -> dict:
    mod = _load_rag_module()
    if mod is None:
        return {"error": "paper-rag query module not importable", "chunks": []}

    # H3: try every candidate entry point before falling back to main().
    # Previously a TypeError from a single candidate (e.g. signature mismatch)
    # caused the whole _run_rag to bail out, hiding workable alternatives.
    attempts: list[str] = []
    for fn_name in ("query", "search", "topk", "run_query"):
        fn = getattr(mod, fn_name, None)
        if not callable(fn):
            continue
        try:
            result = fn(question, k=k)
        except TypeError as e:
            # Signature mismatch — try calling with just the positional arg.
            attempts.append(f"{fn_name}(k=) TypeError: {e}")
            try:
                result = fn(question)
            except TypeError as e2:
                attempts.append(f"{fn_name}(question) TypeError: {e2}")
                continue
            except Exception as e2:
                attempts.append(f"{fn_name}(question) error: {e2}")
                continue
        except Exception as e:
            attempts.append(f"{fn_name} error: {e}")
            continue

        if isinstance(result, dict) and "chunks" in result:
            return result
        if isinstance(result, list):
            return {"chunks": result}
        attempts.append(f"{fn_name} returned unexpected type {type(result).__name__}")

    # Fallback: call main([...]) and capture its stdout via a proxy.
    import contextlib
    import io

    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            mod.main([question, "--k", str(k)])  # type: ignore[attr-defined]
    except SystemExit:
        pass
    except Exception as e:
        return {
            "error": f"rag main failed: {e}",
            "attempts": attempts,
            "chunks": [],
        }
    text = buf.getvalue().strip()
    if not text:
        return {"chunks": [], "attempts": attempts}
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return {"chunks": [], "raw": text, "attempts": attempts}
    if isinstance(data, list):
        return {"chunks": data, "attempts": attempts}
    if isinstance(data, dict):
        data.setdefault("attempts", attempts)
        return data
    return {"chunks": [], "attempts": attempts}


_ENTITY_RX = re.compile(r'"([^"]{3,})"|([A-Z][A-Za-z0-9\-]{2,})')


def _extract_entities(question: str) -> list[str]:
    out: list[str] = []
    for m in _ENTITY_RX.finditer(question):
        cand = m.group(1) or m.group(2)
        if cand and cand not in out:
            out.append(cand)
    return out


def _run_kg(conn, question: str, k: int) -> dict:
    entities = _extract_entities(question)
    matched: list[dict] = []
    seen_ids: set[str] = set()
    for ent in entities:
        res = kgquery.cmd_lookup(
            conn,
            type_filter=None,
            exact_name=None,
            name_fuzzy=ent,
            k=k,
        )
        for node in res:
            if node["id"] in seen_ids:
                continue
            seen_ids.add(node["id"])
            matched.append(node)

    neighbors: list[dict] = []
    for node in matched[:k]:
        nbrs = kgquery.cmd_neighbors(conn, node["id"], hops=1, edge_type=None)
        for edge in nbrs["edges"]:
            neighbors.append(
                {"from": edge["src"], "edge": edge["type"], "to": edge["dst"]}
            )
    return {"matched_nodes": matched[:k], "neighbors": neighbors, "entities": entities}


def _joint_rank(rag_result: dict, kg_result: dict) -> dict:
    chunks = rag_result.get("chunks", []) or []
    chunk_sources: list[str] = []
    for c in chunks:
        src = c.get("source") if isinstance(c, dict) else None
        if src and src not in chunk_sources:
            chunk_sources.append(src)

    kg_papers: list[str] = []
    for node in kg_result.get("matched_nodes", []):
        if node.get("type") == "Paper" and node["id"] not in kg_papers:
            kg_papers.append(node["id"])

    joint = []
    rationale_parts = []
    for src in chunk_sources:
        joint.append({"source": src, "origin": "rag"})
    for pid in kg_papers:
        joint.append({"id": pid, "origin": "kg"})
    if chunk_sources and kg_papers:
        rationale_parts.append("both RAG chunks and KG paper nodes found")
    elif chunk_sources:
        rationale_parts.append("RAG-only (no KG paper match)")
    elif kg_papers:
        rationale_parts.append("KG-only (RAG empty)")
    else:
        rationale_parts.append("no matches in either backend")
    return {"joint_rank": joint, "rationale": "; ".join(rationale_parts)}


def run_hybrid(question: str, k: int, rag_enabled: bool, kg_enabled: bool) -> dict:
    out: dict = {"query": question}
    out["rag"] = _run_rag(question, k) if rag_enabled else {"chunks": [], "skipped": True}

    if kg_enabled and DB_PATH.exists():
        conn = kgdb.open_and_migrate(DB_PATH)
        out["kg"] = _run_kg(conn, question, k)
    else:
        out["kg"] = {"matched_nodes": [], "neighbors": [], "skipped": not kg_enabled}

    out["hybrid"] = _joint_rank(out["rag"], out["kg"])
    return out


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(prog="paper-kg hybrid_query")
    p.add_argument("question")
    p.add_argument("--k", type=int, default=5)
    p.add_argument("--expand-chunks", type=int, default=0, help="reserved")
    p.add_argument("--no-rag", action="store_true")
    p.add_argument("--no-kg", action="store_true")
    args = p.parse_args(argv)

    result = run_hybrid(
        question=args.question,
        k=args.k,
        rag_enabled=not args.no_rag,
        kg_enabled=not args.no_kg,
    )
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

#!/usr/bin/env bash
# PostToolUse hook — mark RAG and/or KG as stale when their source files change.
# Two lanes:
#   RAG lane: papers/**/*.md (not *.raw.md, not papers/rag/**, not papers/kg/**)
#             → touch papers/rag/.stale
#   KG  lane: papers/**/*.kg.json, research/**/*.kg.json,
#             experiments/**/*.kg.json, docs/lessons*.kg.json
#             → touch papers/kg/.stale
set -euo pipefail

# ROOT is derived from this script's location so the hook works under both
# /home/irteam/sw/research_hub and /home1/irteam/sw/research_hub (symlink pair).
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
RAG_STALE="$ROOT/papers/rag/.stale"
KG_STALE="$ROOT/papers/kg/.stale"

payload="$(cat)"

python3 - <<'PY' "$payload" "$RAG_STALE" "$KG_STALE" "$ROOT"
import json, os, sys, time
payload, rag_stale, kg_stale, root = sys.argv[1:5]
try:
    data = json.loads(payload) if payload.strip() else {}
except Exception:
    sys.exit(0)
tool = data.get("tool_name") or data.get("tool") or ""
if tool not in ("Write", "Edit", "MultiEdit"):
    sys.exit(0)
params = data.get("tool_input") or data.get("input") or {}
path = params.get("file_path") or params.get("path") or ""
if not path:
    sys.exit(0)
# Normalize both sides via realpath so the /home/irteam <-> /home1/irteam
# symlink pair resolves to the same root.
try:
    path_real = os.path.realpath(path)
    root_real = os.path.realpath(root)
    rel = os.path.relpath(path_real, root_real)
except ValueError:
    sys.exit(0)

if rel.startswith(".."):
    sys.exit(0)

def touch(flag_path: str, rel_path: str, lane: str) -> None:
    os.makedirs(os.path.dirname(flag_path), exist_ok=True)
    with open(flag_path, "w") as f:
        f.write(f"{time.time()}\n{rel_path}\n")
    print(f"[{lane}-stale] marked due to {rel_path}", file=sys.stderr)

# KG lane: any .kg.json under the research directories (but not inside
# papers/kg/ and not under any `_fixture/` subtree — fixtures are intentional
# test samples that would otherwise flip the stale flag every edit and drown
# real extractions in noise; paper-kg/scripts/index.py also skips them).
kg_triggers = (
    rel.endswith(".kg.json")
    and not rel.startswith("papers/kg/")
    and "_fixture/" not in rel
    and (
        rel.startswith("papers/")
        or rel.startswith("research/")
        or rel.startswith("experiments/")
        or rel.startswith("docs/")
    )
)
if kg_triggers:
    touch(kg_stale, rel, "kg")
    sys.exit(0)

# RAG lane: markdown paper summaries under papers/ (excluding raw/rag/kg).
if (
    rel.startswith("papers/")
    and rel.endswith(".md")
    and not rel.endswith(".raw.md")
    and "/rag/" not in rel
    and "/kg/" not in rel
):
    touch(rag_stale, rel, "rag")
    sys.exit(0)
PY

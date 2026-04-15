#!/usr/bin/env bash
# SessionStart hook — summarize research_hub loop state for the agent.
# v3 schema: stage / inner_phase / sub_phase / slug / stage_version.
# Autonomous mode injection removed (v3 refactor).
# Stdout is injected into the session as additional context.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
LOOP="$ROOT/research/loop_state.json"
MANIFEST="$ROOT/papers/rag/manifest.json"
STALE_FLAG="$ROOT/papers/rag/.stale"
KG_DB="$ROOT/papers/kg/kg.sqlite"
KG_STALE="$ROOT/papers/kg/.stale"

echo "<research-hub-session>"

if [[ -f "$LOOP" ]]; then
  python3 -c "
import json, os
with open('$LOOP') as f:
    s = json.load(f)
stage = s.get('stage')
inner = s.get('inner_phase')
sub   = s.get('sub_phase')
slug  = s.get('slug')
ver   = s.get('stage_version')
schema_ver = s.get('version', 1)
print(f\"loop_schema_version: {schema_ver}\")
print(f\"stage: {stage or 'idle'}\")
print(f\"inner_phase: {inner or '(none)'}\")
print(f\"sub_phase: {sub or '(none)'}\")
print(f\"slug: {slug or '(none)'}\")
print(f\"stage_version: {ver if ver is not None else '(none)'}\")
hist = s.get('history') or []
if hist:
    last = hist[-1]
    print(f\"last_event: {last.get('event', '?')} @ {last.get('at', '?')}\")
# v1/v2 detection → advise migration
if schema_ver < 3:
    print(f\"advisory: loop_state.json is v{schema_ver}; next loop_state.py call will migrate to v3 and write a .bak.json backup.\")
" 2>/dev/null || echo "loop_state: unreadable"
else
  echo "loop_state: missing (no cycles yet)"
  echo "advisory: run /research-papers <topic> (or /research-qa/-experiments/-analyze) to enter a stage."
fi

if [[ -f "$MANIFEST" ]]; then
  python3 -c "
import json, os
with open('$MANIFEST') as f:
    m = json.load(f)
files = m.get('files', {})
chunks = sum(f.get('chunks', 0) for f in files.values())
print(f\"rag_indexed_papers: {len(files)}\")
print(f\"rag_chunks: {chunks}\")
print(f\"rag_last_update: {m.get('last_update') or 'never'}\")
if not files:
    print('⚠ empty RAG index detected — run /research-index to rebuild (guard_empty_rag hook is advisory-only in v3).')
" 2>/dev/null || echo "rag_manifest: unreadable"
else
  echo "rag_manifest: missing"
fi

if [[ -f "$STALE_FLAG" ]]; then
  echo "rag_state: STALE — rag-curator should reindex before next answer-formulate/critique"
fi

# KG block — run status.py and surface a few key counters.
if [[ -f "$KG_DB" ]]; then
  python3 "$ROOT/.claude/skills/paper-kg/scripts/status.py" 2>/dev/null | python3 -c "
import json, sys
try:
    s = json.load(sys.stdin)
except Exception:
    print('kg_db: unreadable')
    sys.exit(0)
print(f\"kg_nodes: {s.get('nodes', 0)}\")
print(f\"kg_edges: {s.get('edges', 0)}\")
print(f\"kg_files_tracked: {s.get('files_tracked', 0)}\")
print(f\"kg_last_update: {s.get('last_upsert') or 'never'}\")
if s.get('rejected_count'):
    print(f\"kg_rejected: {s['rejected_count']}\")
"
else
  echo "kg_db: missing"
fi
if [[ -f "$KG_STALE" ]]; then
  echo "kg_state: STALE — run /research-kg build to rebuild before next query"
fi

# Lessons summary — count active entries (## YYYY-MM-DD headings)
for name in lessons lessons-paper lessons-research lessons-impl lessons-analysis; do
  f="$ROOT/docs/${name}.md"
  if [[ -f "$f" ]]; then
    count=$(awk '/^## [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]/ {c++} END{print c+0}' "$f")
    printf "lessons/%s: %s entries\n" "$name" "$count"
  fi
done
echo "lessons_rule: agents must Read docs/lessons.md + their domain file before starting"

echo "</research-hub-session>"

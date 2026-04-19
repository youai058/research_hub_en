---
name: paper-kg
description: "SQLite knowledge graph. Incremental ingest of `.kg.json` byproducts → papers/vector_db/kg.sqlite triplestore, Pydantic validation + 2-pass upsert (no LLM calls), query node / neighbors / lookup / sql + hybrid_query (RAG+KG). kg-curator + all emitting agents. Triggers: 'KG indexing', 'knowledge graph query', 'triple upsert', 'hybrid query'."
---

# Paper KG Skill

Knowledge graph on an SQLite triplestore. Agents write a `.kg.json` byproduct next to each prose file; `kg-curator` validates and ingests these files without LLM calls.

## Core principles

1. **Extraction is a byproduct**: no separate LLM extraction pass. `.kg.json` is written by the emitting agent (paper-summarizer etc.) alongside the prose.
2. **1:1 sibling rule**: `<source>.md` ↔ `<source>.kg.json` in the same directory. Script emissions (lesson.py, loop_state.py) append per entry.
3. **Alias is the agent's call**: before creating a new canonical node (Method/Dataset/Model/Metric), call `lookup --name-fuzzy` and record the outcome in `alias_check`.
4. **No LLM in the curator**: only Pydantic validation, ID regex, type ↔ prefix consistency, FK existence, and mandatory `alias_check`.

## Stack

- **Store**: `sqlite3` — `papers/vector_db/kg.sqlite` (PRAGMA foreign_keys=ON, WAL mode)
- **Schema**: 3 tables — `nodes` (PK id) / `edges` (FK src·dst ON DELETE RESTRICT) / `aliases` (FK canonical_id)
- **Validation**: `pydantic>=2` via `scripts/schema.py`
- **Fuzzy lookup**: `rapidfuzz.fuzz.WRatio` ≥ 85 (deterministic)
- **Hybrid query**: `paper-rag/scripts/query.py` imported as a module (no subprocess)

## File layout

```
papers/vector_db/
├── kg.sqlite              SQLite triplestore
├── kg-manifest.json       {file → sha256, last_upsert_at, counts}
├── extraction_log.jsonl   append-only audit
├── rejected.jsonl         validation-fail log (consumed by orchestrator)
├── schema.version         "1"
├── kg.stale               KG stale marker (auto-touched by hook)
├── rag.stale              RAG stale marker (auto-touched by hook)
├── chroma/                ChromaDB persistent store
├── manifest.json          RAG hash / mtime incremental state
├── kg-staging/            staging directory for `.kg.json` byproducts
└── .rejected_cursor       rejected.jsonl incremental cursor

.claude/skills/paper-kg/
├── SKILL.md               (this file)
└── scripts/
    ├── schema.py          Pydantic models, ID regex, ALIAS_BOOTSTRAP_THRESHOLD
    ├── db.py              SQLite open / migrate helpers
    ├── index.py           incremental 2-pass upsert
    ├── query.py           node / neighbors / lookup / sql
    ├── hybrid_query.py    RAG + KG joint retrieval
    └── status.py          counts + by_type + manifest + rejected
```

## Sibling placement

| Source file | Sibling `.kg.json` | Author |
|---|---|---|
| `papers/marp-summary/<Venue>/<Year>/<slug>.md` | `papers/vector_db/kg-staging/<slug>.kg.json` | paper-summarizer |
| `research/answers/<date>_<slug>.md` | `research/answers/<date>_<slug>.kg.json` | answer-formulator |
| `research/critiques/<slug>.md` | `research/critiques/<slug>.kg.json` | critic |
| `research/plans/<slug>/PLAN.md` | `research/plans/<slug>/PLAN.kg.json` | experiment-planner |
| `experiments/<slug>/IMPL_MAP.md` | `experiments/<slug>/IMPL_MAP.kg.json` | code-implementer |
| `research/diagnoses/<slug>.md` | `research/diagnoses/<slug>.kg.json` | results-analyst |
| `docs/lessons-<domain>.md` | `docs/lessons-<domain>.kg.json` (append-only per entry) | `lesson.py` |
| `research/loop_state.json` | `research/loop_state.kg.json` (append-only per iteration) | `loop_state.py` |

## `.kg.json` envelope

```json
{
  "version": 1,
  "source_file": "papers/marp-summary/ICLR/2026/attack-lldm.md",
  "source_sha": "abc123...",
  "author_agent": "paper-summarizer",
  "extracted_at": "2026-04-14T17:30:00+09:00",
  "nodes": [...],
  "edges": [...]
}
```

**Required fields**: `version`, `source_file`, `source_sha`, `author_agent`, `extracted_at`, `nodes`, `edges`.

## Incremental ingest algorithm

```
1. Collect every .kg.json (papers/, research/, experiments/, docs/)
2. Compute SHA256 per file
3. Compare with manifest.json
   - new / changed: Pydantic validate → on pass, upsert pipeline; on fail, append to rejected.jsonl
   - removed: DELETE all nodes/edges for that (source_file)
4. Upsert pipeline (transaction):
   a. DELETE existing (source_file, source_sha') nodes/edges (only when source_sha changed)
   b. Pass 1: INSERT all nodes (on id conflict, refresh updated_at only)
   c. Pass 2: INSERT all edges (verify src/dst exist → rollback + reject on dangler)
   d. alias_merge special edges route into the aliases table
5. Update manifest.json + append to extraction_log.jsonl
```

## Query interface

```bash
# Node fetch (quote caveat: ids containing `#` MUST be quoted)
python3 .claude/skills/paper-kg/scripts/query.py node "paper:iclr/2026/attack-lldm"

# Neighbor search
python3 .claude/skills/paper-kg/scripts/query.py neighbors "method:gcg" --hops 2 --edge-type PROPOSES

# Fuzzy lookup (for alias check)
python3 .claude/skills/paper-kg/scripts/query.py lookup --type Method --name-fuzzy "Greedy Coord" --k 5

# Exact-name lookup
python3 .claude/skills/paper-kg/scripts/query.py lookup --type Method --exact-name "GCG"

# Raw SQL (debugging only)
python3 .claude/skills/paper-kg/scripts/query.py sql "SELECT type, COUNT(*) FROM nodes GROUP BY type"
```

## Hybrid query protocol (answer-formulator / critic / planner)

```bash
python3 .claude/skills/paper-kg/scripts/hybrid_query.py "question" --k 5
```

Top-level JSON keys: `query`, `rag`, `kg`, `hybrid`.
Internally invokes `paper-rag.query` via module import — no subprocess.

## Alias Check Protocol (agent instruction)

Before creating a new `Method|Dataset|Model|Metric` node:

1. Call `lookup --type <T> --name-fuzzy "<candidate>" --k 5`
2. Decide from the result:
   - **Reuse**: use the matched existing id as `edges[].dst` (no new node)
   - **New**: new id + record `alias_check: {queried_existing: true, matched: null, rationale: "..."}`
   - **Add alias**: append to the existing node via `type: "alias_merge"` special edge
3. If Jaro-Winkler / WRatio ≥ 0.85 AND same domain, prefer reuse
4. Abbrev vs. full name match → reuse; append the full name into aliases
5. Version difference (v1 vs. v2) → new node + `DERIVED_FROM` edge

**Bootstrap softening**: when KG nodes < 50, `alias_check.queried_existing: false` is tolerated. The `ALIAS_BOOTSTRAP_THRESHOLD` constant in schema.py fixes this boundary.

## Schema enforcement (curator checklist)

1. Pydantic validation (`KGFile`) passes
2. ID regex match (see schema.py ID_REGEX)
3. `nodes[].type` ↔ id prefix consistency
4. New `Method|Dataset|Model|Metric` nodes require `alias_check` (subject to bootstrap)
5. `EVIDENCED_BY` edges enforce `meta.polarity ∈ {support, contradict, mixed}`
6. edges[].src/dst exist in the same file's `nodes[]` or already in the DB
7. Provenance (source_file, source_sha, extracted_at) required
8. Post-ingest exact-name collision detection → flag in `rejected.jsonl` for manual review

Rejected files are appended to `papers/vector_db/rejected.jsonl` with reasons. The orchestrator reads this and re-dispatches to the originating agent.

## Environment setup

```bash
conda activate LLDM
pip install pydantic rapidfuzz
```

sqlite3 is in the Python stdlib, so no extra install.

## Failure modes

- Pydantic validation failure: only that `.kg.json` is rejected; others ingest normally
- Dangling edge (missing src/dst): entire file rejected (transaction rollback)
- `kg.sqlite` corruption: replay `extraction_log.jsonl` or run `index.py --rebuild`
- Corrupt manifest: recompute hashes via `index.py --rebuild-manifest`
- Post-ingest name collision: no silent merge — flag manually in `rejected.jsonl`

## Checklist

- [ ] `pydantic`, `rapidfuzz` installed
- [ ] `papers/vector_db/kg.sqlite` exists (create via `db.open_and_migrate` if not)
- [ ] `manifest.json` initialized or loaded
- [ ] `.kg.json` files collected incrementally
- [ ] 2-pass upsert (nodes → edges)
- [ ] Query smoke test (≥ 1 `query.py node <id>` call)

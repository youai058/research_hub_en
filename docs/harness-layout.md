# Harness Layout (split out of CLAUDE.md §5/§7)

## Directory Structure

```
research_hub/
├── CLAUDE.md                 (this file's parent contract)
├── docs/
│   ├── lessons.md            global lessons
│   ├── lessons-paper.md      paper collection / summarization / RAG
│   ├── lessons-research.md   answer formulation / evidence critique / verification planning
│   ├── lessons-impl.md       code implementation / verification
│   └── lessons-analysis.md   result analysis
├── .claude/
│   ├── settings.json
│   ├── agents/               14 agent definitions (+ harness-engineer, kg-curator, paper-triage, abstract-indexer, codex-reviewer)
│   ├── skills/               22 skill bundles (research 12 + paper-kg + harness-* 7 + experiments 3: experiment-design / impl / report)
│   ├── hooks/                8 hooks (session_start, mark_indices_stale, protect_chroma, protect_kg, protect_external_paths, guard_empty_rag advisory-only, phase_advance_check, inject_lessons)
│   ├── scripts/              utilities (loop_state.py v3 + report_builder.py + lesson.py)
│   └── commands/             10 slash commands (/research-papers, /research-qa, /research-experiments, /research-analyze, /research-status, /research-rag, /research-index, /research-lesson, /research-kg, /research-triage)
├── papers/
│   ├── metadata/<Venue>/<Year>/<slug>.raw.md   paper-hunter raw metadata
│   ├── marp-summary/<Venue>/<Year>/<slug>.md   adaptive Marp summary (PLANNING-first, 4 anchors)
│   ├── digest/<Venue>/<Year>/
│   │   ├── <slug>.digest.md                    Gemini Stage-1 digest
│   │   └── .pdf_cache/<slug>.pdf               PDF cache
│   └── vector_db/
│       ├── chroma/                   ChromaDB persistent store (auto-created by index.py)
│       ├── manifest.json             RAG hash / mtime incremental state
│       ├── kg.sqlite                 SQLite triplestore
│       ├── kg-manifest.json          KG hash / ingest state
│       ├── extraction_log.jsonl      KG audit log
│       ├── rejected.jsonl            KG validation fail log
│       ├── schema.version            KG schema version
│       ├── rag.stale                 RAG stale marker
│       ├── kg.stale                  KG stale marker
│       └── kg-staging/               staging area for .kg.json byproducts
├── research/
│   ├── answers/YYYY-MM-DD_<slug>.md  answer-formulator output (Direct Answer + Evidence Chain)
│   ├── critiques/<slug>.md           4-axis evidence-chain critique
│   ├── diagnoses/<slug>.md           Evidence verification outcome + revision seed
│   ├── topics/<slug>.md              paper-triage run log (append-only, runtime only; created at A-2)
│   ├── plans/
│   │   ├── <slug>/PLAN.md            experiment-level PLAN (consumed by code-implementer; flat legacy path)
│   │   └── <stage>/<slug>/v<N>/PLAN.md   stage-level PLAN (Phase A output, versioned) — stage ∈ {papers, qa, experiments, analyze}
│   ├── reports/
│   │   └── <stage>/<slug>/v<N>/
│   │       ├── Report.md             stage Phase C terminal artifact (md)
│   │       └── Report.slides.md      stage Phase C terminal artifact (Marp slides)
│   └── loop_state.json               current loop position (v3 schema)
├── experiments/
│   └── <slug>/
│       ├── code/
│       ├── configs/
│       ├── run.sh
│       └── IMPL_MAP.md               Evidence ↔ Experiment ↔ Code 3-way mapping
├── harness/
│   └── plans/<name>/                 harness-infra PLAN (orthogonal to the research loop; e.g. stage-split)
└── results_<slug>/                   experiment artifacts
```

> **Discontinued commands**: `/research-start` and `/research-autonomous` were removed in the v3 refactor. Replacement path: start a new cycle with `/research-papers <topic>` (or call the needed stage command directly). Autonomous mode itself was removed, so there is no on/off concept.

## 9 Configuration Surfaces

The Claude Code harness exposes 9 configuration surfaces. research_hub **actively uses 6** and intentionally leaves 3 unused.

### In use (6)

| # | Surface | Path | Purpose |
|---|---|---|---|
| 1 | settings.json | `.claude/settings.json` | permissions, env, hook registration, statusLine |
| 2 | agents | `.claude/agents/*.md` | 14 personas (paper-hunter, paper-triage, abstract-indexer, codex-reviewer, ...) |
| 3 | skills | `.claude/skills/*/SKILL.md` | 22 procedural skills (progressive disclosure) |
| 4 | commands | `.claude/commands/*.md` | 10 slash commands |
| 5 | hooks | `.claude/hooks/*` + settings.json `hooks` | 8 hooks (see table below) |
| 6 | CLAUDE.md / memory | `./CLAUDE.md`, `docs/lessons*.md` | SSOT for role / workflow / self-improvement loop |

### Commands detail (10)

4 stage commands + 6 management/inspection commands:

| # | Command | Type | Role |
|---|---|---|---|
| 1 | `/research-papers <topic>` | stage | `papers` stage Phase A→B→C. paper-hunter → paper-triage → paper-summarizer → rag-curator. |
| 2 | `/research-qa <slug> <question>` | stage | `qa` stage Phase A→B→C. answer-formulator → critic (+ codex-reviewer parallel). |
| 3 | `/research-experiments <slug>` | stage | `experiments` stage Phase A→B→C. 3 internal skills (experiment-design / experiment-impl / experiment-report). E-1 → E-2 → E-3 → report. |
| 4 | `/research-analyze <slug>` | stage | `analyze` stage Phase A→B→C. results-analyst (F-1) → codex-reviewer (F-2). diagnosis + revision seed. |
| 5 | `/research-status` | inspect | Summary of `loop_state.json` v3 fields + RAG index + KG + lessons counts. |
| 6 | `/research-rag <query>` | inspect | Ad-hoc RAG top-k query. Does not index. |
| 7 | `/research-index` | manage | RAG incremental (default) or `--rebuild` full re-index. |
| 8 | `/research-lesson <domain> "<title>"` | manage | Append a 3-line entry (Rule/Why/When) to the appropriate `docs/lessons*.md`. |
| 9 | `/research-kg <build\|query\|node\|lookup\|stats>` | manage | SQLite KG subcommand dispatcher. |
| 10 | `/research-triage` | manage | Score raw.md collections against a topic via Claude-native rubric. |

### Hooks detail (8)

| # | File | Event | Role |
|---|---|---|---|
| 1 | `session_start.sh` | SessionStart | Inject v3 schema (stage/inner_phase/sub_phase/slug/stage_version) + RAG/KG/lessons counts. The autonomous block was removed. |
| 2 | `mark_indices_stale.sh` | PostToolUse(Write\|Edit\|MultiEdit) | On modifications under `papers/`, touch RAG/KG stale markers |
| 3 | `protect_chroma.sh` | PreToolUse(Write\|Edit) | Block direct edits to files inside `papers/vector_db/chroma/` |
| 4 | `protect_kg.sh` | PreToolUse(Write\|Edit) | Block direct edits to `papers/vector_db/kg.sqlite` |
| 5 | `protect_external_paths.sh` | PreToolUse(Write\|Edit\|MultiEdit\|Bash) | Block writes outside research_hub (esp. LLM / LLDM / ~/.claude) and paid API / HF downloads |
| 6 | `guard_empty_rag.sh` | PreToolUse(Bash) | **advisory-only (v3)**: if the RAG manifest is empty, emit a stderr warning (not blocking) for `/answer-formulate` / `/critique` / `/research-qa`. Silenceable via `RESEARCH_HUB_GUARD_QUIET=1`. |
| 7 | `phase_advance_check.sh` | Stop | v3-schema based stage × sub_phase status reporting; emits advisory on when to sub-phase-advance or `stage-complete` (no mutation). |
| 8 | `inject_lessons.sh` | UserPromptSubmit | Inject the last 3 entries of global `lessons.md` + domain counts into the prompt |

### Intentionally unused (3)

| # | Surface | Rationale |
|---|---|---|
| 7 | MCP servers (`.mcp.json`) | All external I/O is executed via Python scripts (`.claude/scripts/`) + hook paths. Adding MCP duplicates the permissions/audit surface, so postponed. The repo-level `.mcp.json` is kept as an intentionally empty stub `{"mcpServers": {}}`. |
| 8 | output-styles (`.claude/output-styles/*.md`) | The paper summary format is already encoded in the `paper-summarize` skill, so a global output-style change is unnecessary. |
| 9 | keybindings (`~/.claude/keybindings.json`) | This is the user global area and is machine/operator specific, so not managed at the repo level. Individual users edit directly if needed. |

## Agent Team

| Agent | Specialization | Active sub-phase | Stage |
|---------|---------|-----------|---|
| paper-hunter | venue API scan / collection | A-1 | papers |
| abstract-indexer | embed raw.md abstracts via bge-m3 and incrementally upsert to ChromaDB `abstracts` collection. Powers the dense-retrieval pre-filter for A-2 triage. | A-1.5 | papers |
| paper-triage | abstract-based Claude-native relevance scoring (0-5) + accepted filter | A-2 | papers |
| paper-summarizer | Adaptive critical summary | A-3 | papers |
| rag-curator | embedding / vector store maintenance | A-4 (primary), optionally at the tail of any sub-phase | papers |
| answer-formulator | hybrid_query → Direct Answer + Evidence Chain (no divergent ideation) | B-1 | qa |
| critic | 4-axis independent evidence critique (Grounding/Support/Counter-Evidence/Verifiability) | B-2, assist during experiment design review | qa, experiments |
| experiment-planner | Evidence 1:1 verification experiment design (Expected Under / If Wrong specified upfront) | C-1 (experiments Phase A) | experiments |
| code-implementer | code implementation / external repo integration (3-way IMPL_MAP + decide_verdict) | E-1 | experiments |
| implementation-verifier | incremental QA + Evidence-verification boundary checks | E-2 | experiments |
| results-analyst | per-Evidence verdict (CONFIRMED/REFUTED/INCONCLUSIVE/IMPL_BUG) + diagnosis / visualization | F-1 | analyze |
| kg-curator | SQLite KG incremental ingest / validation / query | at the tail of every sub-phase (when `kg.stale` is detected) | cross-stage |
| codex-reviewer | Codex CLI based third-party adversarial review | B-2 (parallel to critic), E-3 (final gate), F-2 (final gate) | qa, experiments, analyze |
| harness-engineer | Claude Code harness (9 surface) configuration / modification | out-of-loop | — |

## Stage × Phase summary

| Stage | STAGE_SUBPHASES (Phase C chain) | Artifacts |
|---|---|---|
| `papers` | A-1 → A-2 → A-3 → A-4 | `papers/marp-summary/<V>/<Y>/*.md`, `research/reports/papers/<slug>/v<N>/` |
| `qa` | B-1 → B-2 | `research/answers/`, `research/critiques/`, `research/reports/qa/<slug>/v<N>/` |
| `experiments` | (C-1 satisfied in Phase A) → E-1 → E-2 → E-3 + experiment-report skill | `experiments/<slug>/`, `research/reports/experiments/<slug>/v<N>/` |
| `analyze` | F-1 → F-2 | `research/diagnoses/`, `research/reports/analyze/<slug>/v<N>/` |

`STAGE_SUBPHASES` is defined once in `loop_state.py` as the single SSOT. **No auto-chain between stages.**

## Versioning

- When the same `<stage, slug>` combination is re-run, `loop_state.py stage-enter` globs `research/plans/<stage>/<slug>/v*/` + `research/reports/<stage>/<slug>/v*/` and assigns `max(existing) + 1` to `stage_version`.
- PLAN.md / Report.md / Report.slides.md all live under `v<N>/`. **Do NOT edit or delete previous versions.**
- The `latest` symlink is an optional convenience (non-fatal on failure).
- Manually pruning stage version directories older than 60 days is recommended.

## Phase B trigger whitelist

See CLAUDE.md §4.3 and `.claude/scripts/loop_state.py` TRIGGER_WHITELIST for details (2 SSOT locations — Dedup Stage 1 lesson 2026-04-15).

Detailed workflows live in each stage slash command (`.claude/commands/research-*.md`) and CLAUDE.md §4.

## Dispatch rules (2026-04-16 refactor)

- Phase A PLAN.md writers are the four specialist planners (`paper-hunter`, `answer-formulator`, `experiment-planner`, `results-analyst`), dispatched by the stage slash command with `mode=plan-only` and `run_in_background: true`.
- Phase C sub-phases are owned by the stage slash command, which dispatches each sub-phase as a separate `Agent(..., run_in_background=true)` call and verifies the artifact between dispatches.
- The only main-session (foreground) step is the `topic-refine` skill in `/research-papers`, which is interactive by nature.
- No agent delegates to another agent. Orchestration is a main-session responsibility.

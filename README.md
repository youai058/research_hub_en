# research_hub_en

**An evidence-grounded research-loop harness that produces direct answers and empirically verifies every piece of supporting evidence.**

Given a research question, the harness (1) collects, summarizes, and embeds papers; (2) hybrid-queries RAG + KG to formulate a Direct Answer and an Evidence Chain and critiques each evidence point on four axes; (3) designs and implements a 1:1 verification experiment per evidence; (4) classifies each experiment as CONFIRMED / REFUTED / INCONCLUSIVE and feeds revisions back into the next iteration. Divergent ideation (inventing new topics or hypotheses) is explicitly out of scope. The whole loop runs as a set of Claude Code subagents with a manual-gate Phase A/B/C protocol.

> A Korean-language sibling repo is maintained at [`research_hub`](https://github.com/youai058/research_hub) with the same architecture (timezone defaults to KST, trigger whitelist includes Korean phrases, paper summaries default to Korean prose).

---

## Five-stage research loop

| Stage | Slash command | Primary artifacts |
|---|---|---|
| 1. Paper collection & summary | `/research-papers <topic>` | `papers/marp-summary/<Venue>/<Year>/*.md` + RAG index |
| 2. Evidence-grounded answer + critique | `/research-qa <slug> <question>` | `research/answers/` + `research/critiques/` |
| 3. Verification experiment planning & implementation | `/research-experiments <slug>` | `experiments/<slug>/{code,run.sh,IMPL_MAP.md}` |
| 4. Outcome analysis & diagnosis | `/research-analyze <slug>` | `research/diagnoses/<slug>.md` |

Each stage completes one cycle of **Phase A (write PLAN.md) → Phase B (await user approval) → Phase C (run sub-phase chain) → Report.md + Report.slides.md**. **No autonomous mode, no auto-chaining.** Phase B requires the user to utter an explicit trigger phrase (`proceed`, `go ahead`, `run it`, `execute`, `ok run it`, `ok proceed`) before Phase C starts.

---

## Architecture

- **14 subagents** (`.claude/agents/*.md`): paper-hunter / paper-triage / abstract-indexer / paper-summarizer / rag-curator / kg-curator / answer-formulator / critic / experiment-planner / code-implementer / implementation-verifier / results-analyst / codex-reviewer / harness-engineer
- **Skill bundles** (`.claude/skills/*/SKILL.md`): paper-hunt / paper-summarize / paper-rag / paper-kg / paper-triage / abstract-index / answer-formulate / critique / experiment-{plan,design,impl,report} / code-implement / implementation-verify / results-analyze / topic-refine / harness-* (6)
- **Slash commands** (`.claude/commands/research-*.md`): four stage commands + `/research-{status,rag,index,kg,triage,lesson}` utilities
- **Hooks**: `SessionStart` injects lessons counts; `PreToolUse` blocks writes to external project paths
- **Persistent state**: `research/loop_state.json` (v3 schema: `stage` / `inner_phase` / `sub_phase` / `slug` / `stage_version`)

RAG stack: BAAI/bge-m3 + ChromaDB. KG stack: SQLite with `.kg.json` byproduct-based incremental ingest.

---

## Quick Start

```bash
# 1. Dependencies
conda create -n research_hub python=3.11
conda activate research_hub
pip install chromadb sentence-transformers arxiv openreview-py pymupdf

# 2. API keys
cp .env.example .env          # add OPENREVIEW_USERNAME / OPENREVIEW_PASSWORD / ... as needed

# 3. Paper collection & summary
/research-papers "diffusion language model jailbreak"
# -> Phase A (topic-refine Socratic interview) -> Phase B (review PLAN.md) -> say "proceed" -> Phase C

# 4. Research question answer
/research-qa 2026-04-17_diffusion-llm-jailbreak "Which defense is most effective?"

# 5. Evidence verification experiments
/research-experiments 2026-04-17_diffusion-llm-jailbreak

# 6. Outcome analysis
/research-analyze 2026-04-17_diffusion-llm-jailbreak
```

Status: `/research-status`. Ad-hoc RAG query: `/research-rag "..."`. Each command's detailed contract lives in `.claude/commands/research-*.md`.

---

## Directory layout

```
research_hub_en/
├── CLAUDE.md                # SSOT - every agent and skill reads this
├── .claude/
│   ├── agents/              # 14 subagent personas
│   ├── skills/              # Skill bundles (SKILL.md + scripts/)
│   ├── commands/            # Slash commands
│   ├── hooks/               # SessionStart / PreToolUse hooks
│   ├── scripts/             # loop_state.py, report_builder.py, shared utilities
│   └── tests/               # pytest harness-invariant tests
├── docs/
│   ├── lessons*.md          # Self-improvement loop (append-only)
│   ├── harness-layout.md    # Detailed directory / file map
│   └── superpowers/         # Spec & plan archive
├── papers/
│   ├── metadata/<Venue>/<Year>/*.raw.md
│   ├── marp-summary/<Venue>/<Year>/*.md
│   └── vector_db/           # ChromaDB + kg.sqlite
├── research/
│   ├── plans/<stage>/<slug>/v<N>/PLAN.md
│   ├── answers/ critiques/ diagnoses/ questions/ topics/
│   └── reports/<stage>/<slug>/v<N>/{Report.md, Report.slides.md}
└── experiments/<slug>/      # code / configs / run.sh / IMPL_MAP.md
```

See [`docs/harness-layout.md`](docs/harness-layout.md) for the full map.

---

## Self-improvement loop (lessons)

When the user corrects behavior or a failure pattern is detected, append to `docs/lessons*.md` immediately in a **Rule / Why / When to apply** three-line format. Append-only; obsolete entries get marked `superseded` instead of deleted. Record via `/research-lesson <domain> "<title>"`.

Domain split:
- `lessons.md` - global workflow / meta
- `lessons-paper.md` - paper collection, summary, RAG
- `lessons-research.md` - answer, critique, planning
- `lessons-impl.md` - code implementation and verification
- `lessons-analysis.md` - outcome analysis

---

## Development / testing

```bash
# Harness-invariant tests
python3 -m pytest .claude/tests/ -q

# Full harness structural validation
python3 .claude/skills/harness-validate/scripts/validate.py
```

Add new agents / skills / commands through the `harness-*` skills (see `CLAUDE.md §7`).

---

## Differences from `research_hub` (Korean sibling)

| Axis | `research_hub` (KO) | `research_hub_en` (EN-global) |
|---|---|---|
| Default language | Korean prose, English code | English everywhere |
| Timezone | KST (+09:00) in timestamps | UTC |
| Trigger whitelist | `TRIGGER_WHITELIST_KO + _EN` | `TRIGGER_WHITELIST` (English only) |
| Paper summary output voice | Korean default, code-switched | Concise technical English default |
| `docs/ko-archive/` snapshot | present | absent |

The two repositories are independent; neither auto-syncs to the other. Maintain architectural changes in both when they apply globally; keep language- or locale-specific choices in their respective repo.

---

## License / acknowledgements

- Built on Claude Code (Anthropic) subagent + skill harness.
- When integrating external paper code into `experiments/<slug>/code/`, respect each source's license.

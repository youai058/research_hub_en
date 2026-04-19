# CLAUDE.md — Research Hub

> Always think, reason, and respond in English.

> **SCOPE**: research_hub only. `/home1/irteam/sw/CLAUDE.md` belongs to the LLDM attack project and is unrelated to this harness. Agents and skills must not reference `sw/CLAUDE.md`.

## 1. Role (Research Goals)

This workspace is a standalone harness for **general AI/NLP research loops**. It is **fully isolated** from the legacy LLDM attack research (`/home/irteam/sw/`). The loop's purpose is to **produce evidence-grounded direct answers to user research questions and empirically verify each Evidence point with experiments**. It does NOT divergently generate new research topics or hypotheses. The following 5 stages repeat:

1. **Paper search**: Scan 6 major AI/NLP venues (NeurIPS / AAAI / ICLR / ICML / ACL / EMNLP) as the **default collection target**. A-1 paper-hunter collects accepted papers' **metadata + abstract** to `papers/metadata/<Venue>/<Year>/<slug>.raw.md` (e.g. `ICLR/2025`, `ICML/2025`), then A-3 paper-summarizer generates an **adaptive Marp summary from the full-text PDF** to `papers/marp-summary/<Venue>/<Year>/<slug>.md`. The default behavior is limited to the 6 whitelist venues; workshops / ACL Findings / arXiv preprints and keyword-based arXiv collection are **opt-in only when the user explicitly passes the `/research-papers <topic> --include-arxiv` flag**, in which case hunter output goes to `papers/metadata/etc/<Year>/<slug>.raw.md` and summarizer output to `papers/marp-summary/etc/<Year>/<slug>.md` (year only under the etc tier, flat structure; frontmatter `venue` preserves the original, `venue_class: "etc"`). Without the flag, etc-classified results from openreview/anthology scans are dropped and the arXiv source is not even executed. **Listing (paper-hunter) may judge, classify, and dedup using abstract + API metadata alone; PDF first 2–3 pages are fetched only optionally when venue classification is impossible, near-duplicate is suspected, or relevance is ambiguous.** The actual 5-part summary (paper-summarizer) **must parse the full-text PDF** with pymupdf, write the Marp file, and index it in the RAG vector store. Do NOT create source- or attribute-based directories like `papers/arXiv/`, `papers/OpenReview/`, `papers/preprint/`, `papers/workshop/`, `papers/findings/`.
2. **Answer formulation + evidence critique**: Take the user question as seed_question, gather evidence via hybrid_query (RAG+KG). answer-formulator writes a Direct Answer (one paragraph with concrete numbers/conditions) + Evidence Chain (3–7 items, each with grounding / confidence / verifiability / verification_sketch). **No divergent ideation** — do not invent new hypotheses, methods, or datasets. Then critic independently critiques each Evidence along 4 axes (Grounding Validity / Support Strength / Counter-Evidence / Verifiability); each Evidence must pass Grounding≥3 AND Support≥3 AND Verifiability≥3.
3. **Evidence verification experiment planning**: For each passing Evidence point, design a **1:1 verification experiment**. Each cell of PLAN.md = exactly one Evidence. Specify IV / DV / control / baseline / ablation and **Expected Under (evidence true) / If Wrong (refutation)** numeric ranges upfront to eliminate post-hoc interpretation. Weak-flagged Evidence is prioritized.
4. **Experiment code implementation**: Integrate external paper code, minimally invasively, into `experiments/<slug>/code/`. Track **Evidence ↔ Experiment ↔ Code 3-way mapping** in `IMPL_MAP.md`. Each Experiment has a `decide_verdict()` function that uses PLAN's Expected Under / If Wrong numbers verbatim to return CONFIRMED / REFUTED / INCONCLUSIVE. implementation-verifier runs incremental QA.
5. **Evidence verification outcome analysis**: Judge each Experiment × Evidence pair as CONFIRMED / REFUTED / INCONCLUSIVE / IMPL_BUG. Direct Answer status = one of {fully supported / partially supported / needs revision / fully refuted}. If REFUTED, run a second 4-way failure classification (claim wrong → B-1 revision / impl bug → E-1 / setup error → C-1 / data issue → A-1), produce PNG + HTML visualizations and a diagnosis. Specify the revision seed (Evidence ids to drop, conditions to add) for the next iteration's answer-formulator.

---

## 2. Working Principles

### Phase A/B/C Gates (explicit user approval required, no exceptions)

This harness operates in **stage-scoped manual-gate mode**. The 4 independent stage commands (`/research-papers`, `/research-qa`, `/research-experiments`, `/research-analyze`) each complete one cycle of Phase A (PLAN.md) → Phase B (wait for user approval) → Phase C (sub-phase chain, blocking) → Report.md + Report.slides.md pair generation. **Autonomous mode, auto-chains, flags, and toggles are all deprecated** (v3 refactor). For each stage, the user MUST utter an explicit trigger phrase (§4 "Phase B trigger whitelist") before Phase C begins. The following additionally require user confirmation:

- Modifying external project paths like `LLM/` or `LLDM/`
- Changing `~/.claude/` user global settings
- Paid external API calls

### Plan First
- 3+ step structural decisions → start from Phase A. The responsible agent (mode=plan-only) manages it.
- If something is wrong, stop and replan immediately. Do not push through.

### Verify Before Completion
- Never mark as complete without proof of operation.
- Confirm artifact existence before each Phase ends.

### Simplicity First
- Minimally invasive implementation. Preserve existing conventions.
- Investigate root causes. No stopgaps.

### Self-Improvement Loop (lessons)

When the user corrects behavior or a failure pattern is detected, **append immediately** to the appropriate domain file under `docs/lessons*.md`. Repeating the same mistake is treated as an agent design failure.

| File | Domain | Covered agents |
|---|---|---|
| `docs/lessons.md` | Global (workflow/meta) | all |
| `docs/lessons-paper.md` | Paper collection/summary/RAG | paper-hunter, paper-summarizer, rag-curator |
| `docs/lessons-research.md` | Answer/evidence critique/planning | answer-formulator, critic, experiment-planner |
| `docs/lessons-impl.md` | Code implementation/verification | code-implementer, implementation-verifier |
| `docs/lessons-analysis.md` | Result analysis | results-analyst |

Each `lessons-*.md` may optionally carry a sibling `<name>.kg.json` byproduct, which kg-curator incrementally ingests. Promotion criterion: when an agent writes a Rule/Why/When-to-apply 3-line entry and that entry contains a **reusable knowledge node** (Method / Dataset / Metric / Failure-mode etc.), also emit it as a KG node.

Rules:
1. **On session start**: The SessionStart hook auto-injects the entry count of `lessons.md`. Agents MUST Read the global `lessons.md` + their own domain file upon activation.
2. **On receiving correction**: Use `/research-lesson <domain> "<title>"` or append manually. Format is 3 lines (Rule/Why/When to apply).
3. **Append-only**: Never delete existing entries. If an entry becomes obsolete, mark it `superseded` only.
4. **Fallback**: If the domain is unclear, record under `lessons.md` (global).

---

## 3. Environment

- **Conda env**: `LLDM` (reusing the existing env). Required packages: `chromadb`, `sentence-transformers` (bge-m3), `arxiv`, `openreview-py`, `pymupdf` (PDF parsing).
- **Path**: `/home/irteam/sw/research_hub/` (symlink origin: `/home1/irteam/sw/research_hub/`)
- **API keys**: `/home/irteam/sw/.env` (shared). If an OpenReview account is needed: `OPENREVIEW_USERNAME`, `OPENREVIEW_PASSWORD`.
- **HF cache**: `/home/irteam/.cache/huggingface` (shared)

---

## 4. Standard Workflow (4 stage × 3 phase × sub-phase)

All non-trivial work proceeds in units of **stage commands**. Each stage command directly manages the full Phase A/B/C cycle. **Auto-chaining between stages, autonomous branching, and "suggest next command" output are all forbidden.** Re-runs accumulate as versions under `research/plans/<stage>/<slug>/v<N>/` and `research/reports/<stage>/<slug>/v<N>/`.

### 4.1 Stage × Phase mapping

| Stage | Command | Phase A (Planning) | Phase C (Execution — STAGE_SUBPHASES) | Artifacts |
|---|---|---|---|---|
| `papers` | `/research-papers <topic>` | **Step 1.5 topic-refine (Socratic interview, main session)** → paper-hunter (mode=plan-only) directly writes `research/plans/papers/<slug>/v<N>/PLAN.md` (based on topic.json) | Main session sequentially dispatches Agent(run_in_background=true) per sub-phase: A-1 paper-hunter → A-1.5 abstract-indexer → A-2 paper-triage (`--topic-spec`) → A-3 paper-summarizer → A-4 rag-curator | `research/topics/<slug>.topic.json` + `papers/marp-summary/<V>/<Y>/*.md` + `research/reports/papers/<slug>/v<N>/{Report.md, Report.slides.md}` |
| `qa` | `/research-qa <slug> <question>` | answer-formulator (mode=plan-only) directly writes `research/plans/qa/<slug>/v<N>/PLAN.md` (hybrid_query dry-run, no answer body) | Main session sequentially dispatches Agent(run_in_background=true) per sub-phase: B-1 answer-formulator (Direct Answer + Evidence Chain 3–7) → B-2 critic (+ codex-reviewer in parallel, 4 axes) | `research/answers/`, `research/critiques/` + `research/reports/qa/<slug>/v<N>/{Report.md, Report.slides.md}` |
| `experiments` | `/research-experiments <slug>` | experiment-planner (mode=plan-only) directly writes `research/plans/experiments/<slug>/v<N>/PLAN.md` (Evidence ↔ Experiment 1:1, Expected Under / If Wrong numbers) | Main session sequentially dispatches Agent(run_in_background=true) per sub-phase: `experiment-impl`: E-1 code-implementer → E-2 implementation-verifier → E-3 codex-reviewer → smoke test; followed by `experiment-report` skill | `experiments/<slug>/{code,configs,run.sh,IMPL_MAP.md}` + `research/reports/experiments/<slug>/v<N>/{Report.md, Report.slides.md}` |
| `analyze` | `/research-analyze <slug>` | results-analyst (mode=plan-only) directly writes `research/plans/analyze/<slug>/v<N>/PLAN.md` (verdict rules, REFUTED 4-way classification, revision-seed format) | Main session sequentially dispatches Agent(run_in_background=true) per sub-phase: F-1 results-analyst → F-2 codex-reviewer | `research/diagnoses/<slug>.md` + `research/reports/analyze/<slug>/v<N>/{Report.md, Report.slides.md}` |

### 4.2 Phase A/B/C protocol (common)

- **Phase A**: The responsible agent writes only PLAN.md. No side effects (paper download, answer writing, code generation, experiment execution) are allowed. If a prerequisite artifact is missing, insert a `⚠ Prerequisite Missing` block (warning only, not blocking). **For the papers stage, a Step 1.5 topic-refine interview runs before Phase A and produces `research/topics/<slug>.topic.json`; PLAN.md uses this spec as canonical input.**
- **Phase B**: Reflect user feedback → prompt "Proceed with implementation as-is?". **Never enter Phase C without an explicit trigger phrase.**
- **Phase C**: The main session sequentially blocking-dispatches the `STAGE_SUBPHASES` chain. Each sub-phase is sent as `Agent(..., run_in_background=true)`; the main session waits for task-notification, verifies artifacts, then dispatches the next sub-phase. After the final sub-phase, the main session directly invokes `report_builder.py` to create the Report pair, then calls `loop_state.py stage-complete` to return to `idle`. **Do NOT print a "next stage recommended" line** (Decision #6). If a user-interrupt arrives mid-chain, the in-flight Agent is NOT cancelled (because `run_in_background: true`); dialog with the user, read the current artifact, and choose (a) wait for completion then stop, (b) continue, or (c) abort. Do NOT dispatch the next sub-phase without intent.

### 4.3 Phase B trigger whitelist (case-insensitive, exact match after trim)

- `proceed`, `go ahead`, `run it`, `execute`, `ok run it`, `ok proceed`

Judgement via `python3 .claude/scripts/loop_state.py trigger-check "<phrase>"`. Any other utterance is treated as feedback → re-enter Phase A.

> The list above stays in sync with the `TRIGGER_WHITELIST_EN` constant in `.claude/scripts/loop_state.py`. When adding or removing English phrases, update only these two locations (this §4.3 + `loop_state.py`). Do NOT copy the list into prompt files under `.claude/agents` or `.claude/skills`. (The Korean archive at `docs/ko-archive/CLAUDE.md` documents `TRIGGER_WHITELIST_KO` separately; the two whitelists are independent.)

### 4.4 loop_state.json v3 schema (5 core fields)

`stage` / `inner_phase` / `sub_phase` / `slug` / `stage_version`. The `iteration` field and autonomous references are fully removed. v1/v2 states are migrated in-place by `loop_state.py migrate_to_v3()` on first read, with a backup.

### 4.5 Abort conditions

- `qa` B-2: 0 passing Evidence for 3 consecutive cycles
- `experiments` E-2: verifier failure 2 cycles in a row
- `experiments` E-3 or `analyze` F-2: codex-reviewer `reject` twice
- Resource limit (paid API / external LLM·LLDM modification)
- Explicit user intervention (`stop`, `pause`, `check`)

---

## 5. Directory Structure

For the full directory / file layout, see `docs/harness-layout.md`.

---

## 6. Core Rules

### RAG Stack
- **Embedding**: BAAI/bge-m3 (sentence-transformers)
- **Store**: ChromaDB PersistentClient at `papers/vector_db/chroma`
- **Chunking**: Per-section, preserving equation/table blocks. chunk_size ~1200 tokens.
- **Incremental updates**: Store file path → SHA256 in `manifest.json`. rag-curator upserts only changed files.
- **Query interface**: `python3 .claude/skills/paper-rag/scripts/query.py "<question>" --k 5`

### Paper Sources
- **arXiv**: query via the `arxiv` Python package (keyword + category + date)
- **OpenReview**: paper lists by venue ID via `openreview-py`
- The two sources dedup by normalized title + arXiv ID

### Adaptive Summary Template
Every paper summary has a **per-paper adaptive outline** (details in the `paper-summarize` skill). The fixed 6-part template is deprecated (2026-04-16).

**Common structure**:
- Marp frontmatter (`marp: true`, keeping PPT compatibility)
- Top `<!-- PLANNING: ... -->` comment block (for planning-first verification — contains **both SECTIONS and IMAGE_SOURCES subblocks**)
- H1 lead slide (title, authors, venue, links)

**Planning-first workflow**: Before writing the body, design the PLANNING block first. PLANNING (1) decides every section number, title, and image placement (`[Figure N]` or `[no image]`) upfront in the SECTIONS subblock, and (2) in the IMAGE_SOURCES subblock, records the path and one-line purpose of each figure referenced in SECTIONS. The body then implements PLANNING as-is, with no mid-flight rearrangement.

**4 required anchors (title variants allowed, order fixed)**:
1. **TL;DR** — First content slide right after the H1 lead; one or two sentences as a `> ` blockquote
2. **Method** — Core idea + equations verbatim + pseudocode/figure references
3. **Result** — Numeric tables MUST be Markdown tables (no screenshot images)
4. **Critical Reading** — 3–5 bullets on the paper's weaknesses (based on full text)

**Free sections between anchors** — 0 or more matching the paper's flow: Motivation / Observation / Experiments Setup / Analysis / Discussion / Conclusion, or narrative H2s in the summary's writing language.

**Image rules**:
- **≤1 image per section**. Place mainly under Method / Motivation / Observation / Analysis.
- Result / TL;DR / Critical Reading / Lead default to `[no image]` — even if figures exist, move numeric results to a separate Markdown table.
- Available figures are exactly those listed in the digest frontmatter's `figures:` YAML list (`{label, path, section_hint, reason}`); filename convention is `.figure_cache/<slug>__fig<N>.png`.
- If digest `figures: []` (empty list), mark all PLANNING sections as `[no image]` and skip image insertion.

**Keywords (for RAG)**: optional — if included, append 10–15 items at the end based on the abstract.

**Writing style**: see the `paper-summarize` skill's style rules for paper summary voice conventions (may differ from harness prose).

### Working Norms
- New code uses configurable paths + CLI args — no hardcoded machine paths
- Every agent uses `model: opus`
- Check if a subproject is a git repo before proposing git actions
- From the experiment directory, one must be able to recover the method, target, dataset, seed, and command

### Response Style
- Concise and technical. Specify file paths and commands exactly.

---

## 7. Agent Team Composition

14 agents (12 research-loop + codex-reviewer + harness-engineer). See `docs/harness-layout.md` for the phase mapping table, and each stage slash command (`/research-papers`, `/research-qa`, `/research-experiments`, `/research-analyze`) + `CLAUDE.md §4.2` for detailed workflows.

---

*All dates are in Korea Standard Time (KST).*

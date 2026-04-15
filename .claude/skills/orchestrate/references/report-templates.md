# Report Templates — Stage-split (markdown + Marp pair)

> Loaded by the `orchestrate` skill when generating the stage-completion report pair.
> Generation is delegated to `.claude/scripts/report_builder.py` — this document
> describes what the payload JSON must contain and how each stage's body is rendered.
>
> File pair (both required, no overwrite):
> - `research/reports/<stage>/<slug>/v<N>/Report.md`
> - `research/reports/<stage>/<slug>/v<N>/Report.slides.md`

---

## 0. Common headers

### Markdown frontmatter (`Report.md`)

```yaml
---
stage: papers|qa|experiments|analyze
slug: <slug>
stage_version: <n>
started_at: <kst>
completed_at: <kst>
plan_path: research/plans/<stage>/<slug>/v<n>/PLAN.md
sub_phase_trace: ["A-1", "A-2", ...]
status: success|partial|failed
---
```

### Marp header (`Report.slides.md`)

```yaml
---
marp: true
theme: default
paginate: true
size: 16:9
header: "research_hub | <stage> | <slug> v<n>"
footer: "Generated <completed_at_kst>"
style: |
  section { font-size: 22px; }
  h1 { color: #1a1a1a; }
  code { background: #f4f4f4; }
---
```

### Common markdown body sections (all stages share these)

1. **Executive Summary** — 3–5 lines, plain prose
2. **Success Criteria Check** — table of `criterion | result (✓/✗/NA) | note`
3. **Artifacts Produced** — table of `path | size | note`
4. **Deviations from PLAN** — free text
5. **Known Gaps / Caveats** — free text
6. **Outcome Summary** — 2–4 lines; no next-stage suggestions (Decision #6)

The slide deck mirrors these into 1 opening slide + success-criteria slide + outcome-summary slide, with stage-specific detail slides in between.

---

## 1. `papers` Report

### Body payload keys (`body.*`)

| Key | Type | Content |
|---|---|---|
| `collection_stats` | object | venue×year request/collected/deduped matrix + totals |
| `triage` | object | `threshold`, `accepted[]`, `rejected[]`, optional ASCII `histogram` |
| `summarized[]` | list | per-paper: `slug, venue, year, title, completeness` |
| `rag_delta` | object | `chunks_added, total_files, total_chunks, embed_model` |
| `kg_delta` | object | `nodes_added, by_type{NodeType: count}` |
| `anomalies[]` | list | PDF parse failures, near-dup flags, unclassified venues |

### Markdown layout

- `## Collection Statistics` — JSON block of `collection_stats`
- `## Triage Results` — threshold, accepted/rejected counts, optional histogram code block
- `## Summarized Papers` — table (`Slug | Venue | Year | Title | Completeness`)
- `## RAG Delta`
- `## KG Delta`
- `## Anomalies` (optional, only if non-empty)

### Slide layout (6 slides + common)

1. Title + status + completion timestamp
2. Collection stats
3. Triage
4. Top 10 summarized papers
5. RAG/KG delta
6. Success Criteria
7. Outcome Summary

---

## 2. `qa` Report

### Body payload keys

| Key | Type | Content |
|---|---|---|
| `question_restatement` | str | normalized question |
| `direct_answer` | str | single paragraph, concrete numbers/conditions |
| `evidence_chain[]` | list | `{id, claim, grounding, confidence, verifiability, verification_sketch, cited_papers[]}` |
| `critic_scores[]` | list | `{evidence_id, grounding, support, counter, verifiability, verdict: pass|weak|fail}` |
| `pass_fail_counts` | object | `{pass, weak, fail}` |
| `codex_review` | object | `{agreements[], disagreements[]}` from parallel codex-reviewer |
| `weak_points[]` | list | retrieval gaps to acknowledge (no command suggestion) |

### Markdown layout

- `## Question Restatement`
- `## Direct Answer`
- `## Evidence Chain` — table (`ID | Claim | Grounding | Confidence | Verifiability | Sketch | Citations`)
- `## Critic Scores (4-axis)` — table
- `## Codex-reviewer (parallel) Verdict`
- `## Weak Points`

### Slide layout

1. Title + status
2. Question + Direct Answer (truncated to ~400 chars with `…`)
3. Evidence chain bullets (top 7)
4. Critic 4-axis table
5. Codex review summary
6. Success Criteria
7. Outcome Summary

---

## 3. `experiments` Report (plan + impl + result, single deliverable)

Combines C-1 design (Phase A output), E-1..E-3 execution, and smoke result.

### Body payload keys

| Key | Type | Content |
|---|---|---|
| `plan_mapping[]` | list | `{evidence_id, experiment, iv, dv, expected_under, if_wrong}` |
| `resource_budget` | object | `{time, disk, gpu, api_cost}` |
| `impl_modules[]` | list | `{path, loc, external_repo}` |
| `verifier_results` | object | `{boundary_checks, shape_match}` (implementation-verifier summary) |
| `smoke_result` | object | `{passed, duration_s, log}` |
| `codex_e3_verdict` | object | `{approve, notes}` — E-3 gate |
| `remaining_todos[]` | list | items deferred / skipped |

### Markdown layout

- `## Section 1 — Plan` — mapping table + resource budget line
- `## Section 2 — Implementation` — modules table + verifier line
- `## Section 3 — Smoke Result` — pass/fail, duration, log path
- `**Codex E-3 verdict**`: approve flag + notes
- `### Remaining TODOs / skipped cells` (optional)

### Slide layout

1. Title
2. Plan mapping (compressed table: Ev | Exp | IV | DV)
3. Modules (bullets, top 10)
4. Smoke result
5. Codex E-3
6. Success Criteria
7. Outcome Summary

---

## 4. `analyze` Report

### Body payload keys

| Key | Type | Content |
|---|---|---|
| `verdict_matrix[]` | list | per-Evidence `{evidence_id, CONFIRMED, REFUTED, INCONCLUSIVE, IMPL_BUG}` |
| `answer_status` | str | `fully supported | partially supported | needs revision | fully refuted` |
| `refuted_classification[]` | list | `{evidence_id, class, note}` — only populated when verdict = REFUTED |
| `visualizations[]` | list | `{path, kind}` — png / html |
| `revision_seed` | object | `{drop_evidence_ids[], add_conditions[], reframe_hints[]}` — manual-handoff payload for next `/research-qa` |
| `codex_f2_verdict` | object | `{approve, notes}` |

### Markdown layout

- `## Verdict Matrix (Experiment × Evidence)`
- `## Direct Answer Status`
- `## REFUTED 4-way Classification` (optional, only if non-empty)
- `## Visualizations`
- `## Revision Seed (payload for next qa call, manual delivery)`
- `## Codex F-2 Verdict`

### Slide layout

1. Title
2. Verdict matrix
3. Answer status
4. 4-way classification (if any)
5. Visualizations (top 8)
6. Revision seed (JSON block, truncated to 600 chars)
7. Codex F-2
8. Success Criteria
9. Outcome Summary

---

## 5. Decision rules on missing data

- A payload section that is empty is rendered as `_(none)_` (markdown) or skipped (slides).
- `success_criteria` is REQUIRED by the orchestrator — empty is a builder error (we want explicit "(no criteria)" rather than silent skip).
- `answer_status` is REQUIRED for analyze reports.
- Builder refuses to overwrite existing `Report.md` unless `status=="partial"`. If a re-run is legitimate, the caller should advance to `v<N+1>/` via `stage-enter`.

---

## 6. Payload construction responsibility

Who fills the payload for each stage:

| Stage | Builder of payload body |
|---|---|
| `papers` | orchestrator gathers outputs from paper-hunter (A-1), paper-triage (A-2), paper-summarizer (A-3), rag-curator (A-4) + kg-curator stats (staleness consumer) |
| `qa` | orchestrator consumes answer-formulator (B-1 output) + critic (B-2 output) + codex-reviewer parallel verdict |
| `experiments` | orchestrator + `experiment-report` skill: plan mapping from experiment-design PLAN.md, impl_modules from IMPL_MAP.md, smoke_result from run.sh log, codex_e3_verdict from codex-reviewer |
| `analyze` | orchestrator consumes results-analyst (F-1) + codex-reviewer F-2 verdict |

---

## 7. Example CLI

Build the JSON payload (orchestrator writes it to a tmp file) and call report_builder.py with `--payload /tmp/report_payload.json`. Result: `Report.md` + `Report.slides.md` written, `latest` symlink updated.

---
description: Enter the `analyze` stage. Classifies each Experiment × Evidence outcome (CONFIRMED/REFUTED/INCONCLUSIVE/IMPL_BUG), emits revision seed for the next qa iteration. Requires trigger phrase to advance from B to C. Final stage gate is codex-reviewer (F-2).
argument-hint: <slug>
---

# /research-analyze

Enter the `analyze` stage. Two sub-phases: `F-1 results-analyst → F-2 codex-reviewer`. Produces `research/diagnoses/<slug>.md` + `Report.md` + `Report.slides.md`.

**Raw input**: $ARGUMENTS

## Step 1 — Parse slug

Expect `$1` = slug. If absent, ask. If `results_<slug>/` is missing or empty, warn that analysis will be sparse; still allow proceed.

## Step 2 — Enter the stage

```bash
python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-enter \
    --stage analyze --slug "$1"
```

## Step 3 — Phase A

Dispatch `orchestrator` with stage=`analyze`, slug=`$1`, stage_version (from script). Orchestrator invokes `results-analyst` in planning-only mode to produce `research/plans/analyze/<slug>/v<N>/PLAN.md` covering:

- Verdict decision rules (CONFIRMED / REFUTED / INCONCLUSIVE / IMPL_BUG) — uses `decide_verdict()` thresholds from the experiments IMPL_MAP
- REFUTED 4-way sub-classification rules: claim wrong → qa B-1 / impl bug → experiments E-1 / setup error → experiments C-1 / data issue → papers A-1
- Visualization list (PNG + HTML)
- Revision seed format (`{drop_evidence_ids, add_conditions, reframe_hints}`)
- `⚠ Prerequisite Missing` if results_<slug>/ is empty

No analysis runs yet. Return at inner_phase = `A`.

## Step 4 — Present, wait for trigger

Standard pattern.

## Step 5 — Phase B + C

On trigger:

```bash
python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-advance --to B
python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-advance --to C --trigger "<phrase>"
```

Orchestrator runs:
- **F-1 results-analyst** — applies decide_verdict per Experiment × Evidence, produces verdict matrix, REFUTED classifications, visualizations, revision seed, and `research/diagnoses/<slug>.md`.
- **F-2 codex-reviewer** — adversarial statistical review of verdicts + revision seed. On reject, one recovery cycle: F-1 with `--force`.

## Step 6 — Completion

Orchestrator builds the analyze payload (verdict_matrix, answer_status, refuted_classification, visualizations, revision_seed, codex_f2_verdict) → `report_builder.py` → Report pair.

`stage-complete` → idle.

Print final summary per `stage-gate.md` §4.5:
- Report.md + Report.slides.md absolute paths
- diagnoses/<slug>.md path
- Answer status (`fully supported` / `partially supported` / `needs revision` / `fully refuted`)
- Visualization paths
- **No next-stage suggestion.** The revision seed exists in Report.md for the user to hand-carry if they choose to run `/research-qa` again.

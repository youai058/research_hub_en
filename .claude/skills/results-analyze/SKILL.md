---
name: results-analyze
description: "Evidence verification outcome analysis. Classify each Experiment result as CONFIRMED/REFUTED/INCONCLUSIVE/IMPL_BUG (comparing with PLAN's Expected Under/If Wrong). Per-Evidence verdict summary → Direct Answer revision seed, 4-way failure classification, PNG + self-contained HTML. results-analyst only. Triggers: 'evidence verification outcome', 'diagnosis', 'verification outcome', 'answer revision proposal', 'HTML report'."
---

# Results Analyze Skill

Interpret experiment results through the **Evidence verification outcome** lens. The core question: "Was each Evidence **confirmed or refuted** by the experiment? Is the Direct Answer resting on that evidence still valid?"

## Input

- `results_<slug>/` raw results (follow the path convention defined in PLAN)
- `research/plans/<slug>/PLAN.md`
- `research/answers/YYYY-MM-DD_<slug>.md`
- (optional) `experiments/<slug>/IMPL_MAP.md`

## Evidence Verification Outcome (primary classification)

Compare each Experiment E<i>'s result against PLAN's Expected Under / If Wrong ranges and classify into **exactly one** of four:

| Verdict | Criterion | Follow-up |
|---|---|---|
| **CONFIRMED** | metric ∈ Expected Under range, statistically significant | Evidence confidence +1 (upgrade). Direct Answer preserved. |
| **REFUTED** | metric ∈ Expected If Wrong range (or significant in the opposite direction) | Drop the Evidence. Remove from Direct Answer and propose revision. |
| **INCONCLUSIVE** | Middle ground, CI covers both ranges | Recommend additional experiments (increase N or ablation). Preserve the Evidence with state "pending". |
| **IMPL_BUG** | Code issue (smoke test regression, NaN, save failure) | Return to E-1 (re-dispatch implementer). The verdict itself is void. |

**Verdict obligation**: assign exactly one of the 4 to every Experiment × Evidence pair. Cross-check the `decide_verdict()` code output against the manual review.

Diagnosis answers:
1. How many Evidence are CONFIRMED / REFUTED / INCONCLUSIVE?
2. Is the Direct Answer still valid? (all CONFIRMED → valid; core Evidence REFUTED → revision required)
3. What is the revision seed to hand the next iteration's answer-formulator?

## 4-Way failure classification (secondary — decompose causes when REFUTED)

When the result fails to support the hypothesis, classify the cause into one (or more) bucket. Next action is specified at sub-phase granularity (requires `loop_state.py advance --force`).

| Class | Definition | Diagnosis method | Next action |
|---|---|---|---|
| **claim wrong** | The Evidence itself is inconsistent with reality. Implementation and setup both normal. | Multiple seeds / ablations consistently in If Wrong range | Return to B-1 (re-call answer-formulator, Direct Answer revision — remove the Evidence or add a condition) |
| **impl bug** | Implementation error. Code differs from PLAN. | Smoke-test re-run, abnormal logs | Return to E-1 (code-implementer reimplementation) |
| **setup error** | Baseline / hyperparameter / metric inappropriate. | Baseline numbers diverge from prior paper | Return to C-1 (experiment-planner PLAN revision) |
| **data issue** | Data bias / split error / leakage. | Train/val overlap, class imbalance | Return to A-1 (re-collect data) or C-1 (change split) |

**Evidence-based classification obligation**: for each class, present concrete evidence (log lines, numbers, code snippets).

## diagnosis.md template

`research/diagnoses/<slug>.md`:

```markdown
---
slug: <slug>
answer: research/answers/YYYY-MM-DD_<slug>.md
plan: research/plans/<slug>/PLAN.md
results: results_<slug>/
stage_version: 3
date: 2026-04-15
---

# Diagnosis — {slug}

## TL;DR

**Direct Answer status**: {fully supported / partially supported / needs revision / fully refuted}

**Verification summary**: E1 CONFIRMED, E2 REFUTED, E3 INCONCLUSIVE → answer-formulator should drop E2 and produce a new Direct Answer with E3 conditions tightened.

**Next action**: {B-1 (Answer revision) / E-1 (impl fix) / C-1 (PLAN fix) / A-1 (v<N+1> re-entry) / done}

---

## User Question (for reference)

> <cite the seed_question from answer>

## Current Direct Answer

<cite the answer-formulator's Direct Answer>

---

## Evidence Verification Outcomes

| Evidence | Experiment | Metric value (mean ± CI) | Expected Under | Expected If Wrong | Verdict |
|---|---|---|---|---|---|
| evidence:<slug>--e1 | E1 | 0.82 ± 0.03 | [0.75, 0.95] | < 0.55 | **CONFIRMED** |
| evidence:<slug>--e2 | E2 | 0.15 ± 0.06 | [0.10, 0.30] | N/A (primary metric) | **CONFIRMED** |
| evidence:<slug>--e3 | E3 | 0.51 ± 0.08 | [0.65, 0.90] | < 0.50 | **INCONCLUSIVE** |

## Statistical Detail

- Seeds: 3 runs per condition
- Test: paired t-test (C1 vs C2)
- p-value: 0.42 (not significant for C1), 0.003 (significant for C2)
- Effect size (Cohen's d): C1=0.15, C2=0.82

## Failure Classification (if any)

### C1 gap → claim wrong (probability 0.7)

**Evidence**:
- All 3 seeds consistently near null (log: results_<slug>/seed*/metrics.json)
- Ablation A2 also shows no difference between method A and B
- Impl passed the verifier; baseline numbers match [Paper X] (±0.5%)

**Alternative hypothesis**: setup error (probability 0.2)
- Baseline B may be slightly weaker than the paper's optimal setting

**Alternative hypothesis**: data issue (probability 0.1)
- Class distribution checked, normal

## Re-Experiment Triggers

- **If claim wrong (primary)**: return to B-1 (`loop_state.py advance --to B-1 --force`). Drop C1 and keep only C2, explore C2's follow-up question.
- **If setup error (alt)**: rerun baseline B with hyperparameters from [Paper X] §4.2. +1h.

## Visualizations

- `results_<slug>/plots/accuracy_comparison.png`: bar plot, 3 methods × 3 seeds
- `results_<slug>/plots/learning_curves.png`: train/val loss
- `research/diagnoses/<slug>.html`: self-contained report

## Findings to Accumulate (insights to feed into RAG)

- **Negative result**: Method A gives no significant improvement on this task (effect size 0.15)
- **Positive result**: Method C gives significant improvement over baseline (p=0.003, d=0.82)
- Worth referencing in follow-up research

## Next Loop Entry

- Append to `loop_state.json.history`:
  ```json
  {"stage_version": 3, "outcome": "claim wrong (C1) / claim supported (C2)", "next": "B-1"}
  ```
```

## Visualization conventions

### PNG (matplotlib)

- Raw analysis PNGs saved under `results_<slug>/plots/`
- Filename: `{metric}_{comparison}.png`
- Resolution: `dpi=150`
- Style: `seaborn-v0_8` or default, but consistent

### HTML (self-contained)

- `research/diagnoses/<slug>.html`
- Convention:
  - Complete as a single `.html` file
  - CSS/JS inline (no external CDN)
  - Images embedded as base64
  - If interactive, bundle plotly inline
- Template:
  ```html
  <!DOCTYPE html>
  <html>
  <head>
    <style>body {font-family: sans-serif; max-width: 900px; margin: 2em auto;}</style>
  </head>
  <body>
    <h1>Diagnosis — {slug}</h1>
    <p><b>Claim support</b>: ...</p>
    <h2>Accuracy Comparison</h2>
    <img src="data:image/png;base64,{b64}" />
    <h2>Finding</h2>
    ...
  </body>
  </html>
  ```

## Authoring principles

1. **Mandatory Claim support conclusion**: pick one of supported/weakly/rejected/refuted
2. **Evidence-based classification**: cite logs / numbers, not "feel"
3. **Enumerate multiple hypotheses**: when the cause is uncertain, list alternatives with probabilities
4. **Next loop entry is required**: always propose the next action and entry Phase
5. **Findings accumulation**: extract **insights usable in follow-up research**, not per-experiment results

## Failure modes

- Results file corruption: partial recovery from logs + mark Known/Unknown
- Statistical test infeasible (sample of 1): report effect size only + recommend more seeds
- HTML render failure: save PNGs as separate files; retry HTML next run
- Ambiguous claim: re-read the answer-formulator original (`research/answers/<slug>.md`) and re-interpret

## Checklist

- [ ] TL;DR (support conclusion + next action)
- [ ] Claim vs Result table
- [ ] Statistical detail (test, p, effect size)
- [ ] Failure classification with evidence (if any)
- [ ] Re-experiment triggers
- [ ] PNG plots generated
- [ ] Self-contained HTML report
- [ ] Findings to Accumulate
- [ ] loop_state.json update proposal
- [ ] `<slug>.kg.json` written in the same directory (see KG Emission)

---

## KG Emission (byproduct)

Write `<slug>.kg.json` alongside `research/diagnoses/<slug>.md`. Node types owned by this skill:

| Type | Prefix | Required fields |
|---|---|---|
| `Result` | `result:` | experiment_id, evidence_id, metric_id, value (original number), ci (optional), seeds[], verdict (CONFIRMED/REFUTED/INCONCLUSIVE/IMPL_BUG) |
| `Diagnosis` | `diagnosis:` | slug, answer_status (fully supported / partially supported / needs revision / fully refuted), n_confirmed, n_refuted, n_inconclusive, next_action |

**Edges (required)**:
- `Experiment --PRODUCES--> Result`
- `Result --EVIDENCED_BY--> Evidence` (meta.polarity ∈ {support, contradict, mixed})
  - support: verdict == CONFIRMED
  - contradict: verdict == REFUTED
  - mixed: verdict == INCONCLUSIVE
- `Diagnosis --ABOUT--> Experiment` (one per experiment)
- `Diagnosis --CONCERNS--> Answer` (target Answer)
- `Diagnosis --SUGGESTS_NEXT--> Answer` (placeholder Answer id that the next iteration's answer-formulator is expected to produce — or omit)

Example IDs: `result:late-step-generation-gap--c1-seed0`, `diagnosis:late-step-generation-gap#local`

Provenance: `author_agent: "results-analyst"`.

## Polarity decision

**EVIDENCED_BY's `polarity` is required**. Decision rule:

1. Effect-size direction matches PLAN's prediction AND statistically significant (p<0.05) → `support`
2. Effect size in the opposite direction, or null (CI includes 0) → `contradict`
3. Supported only under some condition / seed → `mixed` (record details in meta)

The curator rejects the whole file if `polarity` is missing. When ambiguous, record `mixed` and document the uncertainty in diagnosis.md.

## Alias Check Protocol

If creating a new `Metric` node is needed, lookup is mandatory (typically experiment-planner already registered it). This skill usually performs **only id reuse**.

## Hybrid Query

At the **findings accumulation** step, when comparing with similar prior work:

```bash
python3 .claude/skills/paper-kg/scripts/hybrid_query.py "<metric> <method> negative result" --k 5
```

- Use `kg.matched_nodes` to find existing Result nodes on the same Method / Dataset
- Compare with current numbers and cite in diagnosis.md as "prior paper X reports Y%, this experiment reports Z%"

## Schema Enforcement

For `Result --EVIDENCED_BY--> Evidence`, the dst must be an existing `Evidence` id in the DB (registered by answer-formulator). Missing → dangling reject. Hypothesis nodes were removed from the loop and are not substitutable. Details in `.claude/skills/paper-kg/SKILL.md`.

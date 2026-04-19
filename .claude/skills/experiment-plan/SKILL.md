---
name: experiment-plan
description: "Evidence verification experiment planning. Design a 1:1 experiment per passing Evidence point (PLAN ↔ Evidence mapping). Pre-specify IV/DV/baseline/ablation + Expected Under / If Wrong. Owned by experiment-planner. Triggers: 'evidence-verification experiment', 'write PLAN.md', 'verification plan'."
---

# Experiment Plan Skill

Design **empirical verification experiments** for each **Evidence point** of a passing Answer. Every PLAN.md cell is **Evidence verification**, not a "new hypothesis test".

## Input

- `research/answers/YYYY-MM-DD_<slug>.md` (from answer-formulator)
- `research/critiques/<slug>.md` (critic's per-Evidence scores + weak flag + revision suggestions)
- RAG/KG reference (experimental setups of related papers)

## PLAN.md structural principles

- **Each experiment cell = exactly one Evidence point**, 1:1 traceable.
- IV/DV design is not about "novelty" but **"evidence-verification fidelity"**.
- **Specify Expected result upfront**: numeric range if evidence is true, and if refuted. Prevents post-hoc interpretation.
- Evidence that critic flagged with `FLAGS_WEAK` is scheduled as **priority verification** first.

## PLAN.md template

`research/plans/<slug>/PLAN.md`:

```markdown
---
plan_for: research/answers/YYYY-MM-DD_<slug>.md
critique: research/critiques/<slug>.md
date: 2026-04-15
stage_version: 1
estimated_runtime: "2 hours on 1x A100"
---

# Evidence Verification Plan — {slug}

## Direct Answer (for reference)

<Quote the Direct Answer written by answer-formulator>

## Evidence Verification Map

| Exp | Evidence id | Claim | Priority | Status |
|---|---|---|---|---|
| E1 | evidence:<slug>--e1 | ... | normal | planned |
| E2 | evidence:<slug>--e2 | ... | **weak (counter flagged)** | planned — priority |
| E3 | evidence:<slug>--e3 | ... | normal | planned |

---

## Experiment E1: Verify Evidence Point 1

**Evidence (from answer)**: "<verbatim E1 claim>"
**Claim being verified**: <one sentence of E1>
**Verification logic**:
- If experiment result confirms → Evidence E1 confidence +1 (upgrade), Direct Answer retained
- If experiment result refutes → Evidence E1 discarded, Direct Answer must be revised (drop E1 and shrink, or add a condition)

### Variables

| Type | Name | Values | Justification |
|---|---|---|---|
| IV | <factor> | {A, B, C} | E1's claim is expressed as a function of the factor |
| DV (verification metric) | <metric> | scalar | direct mapping E1 → metric |
| Control | seed | {0, 1, 2} | reproducibility |

### Baseline

| # | Baseline | Source Paper | Why |
|---|---|---|---|
| 1 | BaselineA | [Paper:<id>] | Reproduce the setup of the paper E1 cites |
| 2 | Null model | — | Expected distribution if the Evidence is false |

### Expected Results

- **Under evidence (E1 true)**: `<metric> ∈ [X_low, X_high]` (e.g., accuracy ≥ 0.75)
- **If evidence wrong**: `<metric> < X_null` (e.g., accuracy ≤ 0.55, i.e., indistinguishable from baseline)
- **Inconclusive zone**: `X_null < metric < X_low`
- Statistical test: paired t-test / Wilcoxon / bootstrap CI, α=0.05, power=0.8
- **Power analysis**: minimum N = ... (effect size d=..., α, power)

### Ablations (verification-specific)

- A1: remove IV → confirm regression to null model
- A2: repeat on another dataset → confirm evidence generality

### Resources

- GPU: 1× A100, Estimated runtime: <fill after dry-run>
- Disk: ~2GB

### Implementation Checklist

- [ ] Data loader for `<dataset>`
- [ ] Model wrapper implementing `<method>`
- [ ] `<metric>` computation (returns scalar 0-1)
- [ ] Expected-range assertion script (outputs CONFIRMED / REFUTED / INCONCLUSIVE)
- [ ] Run with 3 seeds

---

## Experiment E2: Verify Evidence Point 2 (**priority — weak**)

Flagged by critic under Counter-Evidence. Run first.

**Evidence**: "..."
**Claim being verified**: ...
**Verification logic**: ...

### Variables ...

### Baseline ...

### Expected Results

- Same format as regular E + also specify the **counter paper's result point**:
  - `<metric> at counter-paper's setting` (does it actually reproduce?)

...

---

## Experiment E3: ...

...

---

## Resources (Total)

- GPU hours: 3× <per-exp estimate> = <sum>
- Disk: ~10GB

> Run weak-priority Experiments first to surface potential evidence collapse early. Report any paid-API / external LLM / LLDM path dependency to the orchestrator ahead of time.

## Reproducibility

- [ ] Seeds fixed (3 repeats) per Experiment
- [ ] Record dataset-split hash
- [ ] Preserve hyperparameter YAML
- [ ] Commands saved in `run.sh`
- [ ] Output path convention: `results_<slug>/E<i>/seed{N}/metrics.json`

## Success Criteria

- Each Experiment has a quantitative rule yielding `CONFIRMED` / `REFUTED` / `INCONCLUSIVE`
- 100% of the Reproducibility checklist
- Format that lets F-1 results-analyst interpret results per-Evidence

## Open Questions / Known Risks

- Hyperparameter disclosure for E2's counter paper is uncertain
- Dataset X license needs confirmation
```

## Authoring rules

1. **PLAN ↔ Evidence 1:1**: if one Experiment bundles multiple Evidence, F-1 cannot attribute the verdict. Must be 1:1.
2. **Expected Under / If Wrong required**: prevents post-hoc interpretation. Fix numerics upfront for confirmed vs. refuted.
3. **Weak-flag first**: Evidence flagged with Counter-Evidence runs first in PLAN order. If it collapses, later experiments may become moot.
4. **RAG reference required**: confirm baseline / metric / hyperparameter settings via rag_query on source papers.
5. **Statistical power**: writing "sufficient" without a power analysis is rejected.
6. **Conservative resource estimate**: 1.5× actual runtime.
7. **run.sh required**: reproducible script, not manual commands.

## Failure modes

- Evidence's verification_sketch too vague → ask answer-formulator to flesh it out (go back to B-1)
- Insufficient basis for Expected range → anchor on reported numbers from prior papers via RAG
- Paid API / external LLM / LLDM dependency required → report to orchestrator
- Baseline not reproducible (no code) → fall back to minimal implementation, note in IMPL_MAP

## Checklist

- [ ] Evidence Verification Map table (every Evidence covered)
- [ ] Each Experiment names Evidence id + verification logic
- [ ] IV/DV/control table
- [ ] Expected Under / If Wrong numbers specified upfront
- [ ] ≥ 2 baselines (RAG-referenced)
- [ ] Power analysis
- [ ] Ablations (verification-specific)
- [ ] Resource estimates
- [ ] Reproducibility checklist
- [ ] Implementation Checklist per Experiment
- [ ] run.sh included in plan
- [ ] Weak-flag Evidence scheduled first
- [ ] `PLAN.kg.json` written in the same directory (see KG Emission)

---

## KG Emission (byproduct)

Write `PLAN.kg.json` next to `research/plans/<slug>/PLAN.md`.

| Type | prefix | required fields |
|---|---|---|
| `Plan` | `plan:` | slug, answer_id, n_experiments, baselines[], metrics[] |
| `Experiment` (shell — filled by code-implementer) | `experiment:` | slug, plan_id, evidence_id, expected_under, expected_if_wrong |

> Note: actual `Experiment` node creation is E-1 code-implementer's responsibility. This skill only emits the Plan node; each Experiment slot is reserved only as an evidence_id list in `meta.pending_experiments`.

**Edges**:
- `Plan --VERIFIES--> Answer`
- `Plan --USES_DATASET--> Dataset`
- `Plan --USES_MODEL--> Model`
- `Plan --USES_METRIC--> Metric`
- `Plan --COMPARES_WITH--> Method` (one per baseline)

Provenance: `author_agent: "experiment-planner"`.

## Alias Check Protocol

When building edges to `Dataset|Model|Metric|Method` (including baselines), look up first:

```bash
python3 .claude/skills/paper-kg/scripts/query.py lookup --type Dataset --name-fuzzy "AdvBench"
```

Reuse the matched id. If no match, defer the edge and let paper-summarizer register it first.

## Hybrid Query

**Required** when choosing baselines / metrics and deriving Expected ranges:

```bash
python3 .claude/skills/paper-kg/scripts/hybrid_query.py "<evidence claim> baselines" --k 10
```

- `kg.matched_nodes` Paper → Method path identifies actually-used baselines / metrics
- `rag.chunks` gives verbatim hyperparameters / reported numbers → anchor for Expected range

## Schema Enforcement

The Answer id in `Plan --VERIFIES--> Answer` must exist in the DB. The answer-formulator `.kg.json` must be ingested first. A dangler rejects the file. See `.claude/skills/paper-kg/SKILL.md` for details.

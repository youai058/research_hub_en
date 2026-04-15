---
description: Enter the `experiments` stage. Phase A uses the experiment-design skill (plan), Phase C runs experiment-impl skill (E-1 implement → E-2 verify → E-3 codex-review + smoke) then experiment-report skill. Trigger phrase required to advance from B to C.
argument-hint: <slug>
---

# /research-experiments

Enter the `experiments` stage. Merges the former `/research-plan` and `/research-implement` commands into a single stage with internal 3-skill pipeline:

- `experiment-design` (Phase A output)
- `experiment-impl` (Phase C, sub-phases E-1 → E-2 → E-3)
- `experiment-report` (Phase C tail — builds Report pair)

**Raw input**: $ARGUMENTS

## Step 1 — Parse slug

Expect `$1` = slug. If absent, ask the user. If the slug has no prior artifacts anywhere (`research/plans/qa/<slug>/`, `papers/.../<slug>...`), proceed but warn that downstream quality will suffer.

## Step 2 — Enter the stage

```bash
python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-enter \
    --stage experiments --slug "$1"
```

## Step 3 — Phase A: experiment-design

Dispatch `orchestrator` with:
- stage: `experiments`
- slug: `$1`
- stage_version: (from script)
- phase: `A`
- skill_to_invoke: `experiment-design`

The orchestrator invokes the `experiment-design` skill, which dispatches `experiment-planner` (+ critic review) to produce `research/plans/experiments/<slug>/v<N>/PLAN.md`. The PLAN.md must contain:

- Evidence ↔ Experiment 1:1 mapping table
- IV / DV / baseline / ablation per cell
- **Expected Under (evidence-true numeric range)** + **If Wrong (refutation numeric range)** per cell — prevents post-hoc interpretation
- Resource budget
- `⚠ Prerequisite Missing` if no prior qa Report exists for this slug

**No code writing, no smoke runs.** Return with inner_phase = `A`.

## Step 4 — Present PLAN, wait for trigger

Same pattern as `/research-papers`: print path, wait for user feedback or trigger phrase.

## Step 5 — Phase B + C

On trigger:

```bash
python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-advance --to B
python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-advance --to C --trigger "<phrase>"
```

Orchestrator dispatches the `experiment-impl` skill:
1. **E-1 code-implementer** — produce `experiments/<slug>/code/`, `configs/`, `run.sh`, `IMPL_MAP.md` (Evidence↔Experiment↔Code 3-way mapping). Each experiment gets `decide_verdict()` using the PLAN's Expected Under / If Wrong numeric thresholds.
2. **E-2 implementation-verifier** — incremental QA: PLAN ↔ IMPL_MAP boundary cross-check (IV/DV/metric shape), smoke test of `run.sh`, edge cases.
3. **E-3 codex-reviewer** — adversarial review. On `reject`, one recovery cycle: fall back to E-1 with `--force` and re-run. Cap at 1 retry; escalate to user after.

Then the `experiment-report` skill builds the Report pair.

## Step 6 — Completion

Orchestrator builds the experiments payload (plan_mapping, resource_budget, impl_modules, verifier_results, smoke_result, codex_e3_verdict, remaining_todos) → `report_builder.py`.

`stage-complete` → idle.

Print final summary per `stage-gate.md` §4.5. **No next-stage suggestion.**

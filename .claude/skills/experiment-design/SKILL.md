---
name: experiment-design
description: "Phase A of the `experiments` stage. Produces research/plans/experiments/<slug>/v<N>/PLAN.md via the experiment-planner agent (+ critic review). Evidence↔Experiment 1:1 mapping, IV/DV/baseline/ablation, Expected Under / If Wrong thresholds. No code, no smoke. Triggers: 'write experiments PLAN', 'design evidence verification experiment', 'Phase A experiments'."
---

# Experiment Design Skill (Phase A of /research-experiments)

Delegates to `experiment-planner` (and optionally `critic` for review) to produce the stage-level PLAN.md for the `experiments` stage. This is a **planning-only** skill — it MUST NOT write code, run smoke tests, or create `experiments/<slug>/` subtree.

## When this fires

- Invoked by the `/research-experiments` command during Phase A.
- Also directly invocable if the user already has a qa Report and wants to draft an experiment plan without committing to execution.

## Inputs

| Input | Source | Required |
|---|---|---|
| `slug` | `loop_state.json.slug` | yes |
| `stage_version` | `loop_state.json.stage_version` | yes |
| qa Report | `research/reports/qa/<slug>/v*/Report.md` (latest) | no — warn if missing |
| critic scores | `research/critiques/<slug>.md` | no |
| revision seed | from prior analyze Report (F-2) if rerunning | no |

## Output

- `research/plans/experiments/<slug>/v<N>/PLAN.md` (single file)

## PLAN.md structure (Phase A common template + experiments-specific sections)

The file MUST include the common Phase A headers (Stage/Slug/Version, Goal, Inputs, Execution Order, Parameters, Expected Artifacts, Resource Bounds, Success Criteria, Risks & Alternatives) as described in `.claude/skills/orchestrate/references/stage-gate.md` §2.3, plus:

### Evidence ↔ Experiment Mapping (required, one row per Evidence point)

```markdown
| evidence_id | evidence_claim (30 chars) | experiment_name | IV | DV | baseline | ablation | Expected Under | If Wrong |
|---|---|---|---|---|---|---|---|---|
| e1 | … | exp_01 | … | … | … | … | acc ≥ 0.85 | acc < 0.60 |
| e2 | … | exp_02 | … | … | … | … | BLEU Δ ≥ +3 | BLEU Δ ≤ 0 |
```

Rules:
- Every passing Evidence from the prior qa critique MUST have exactly one experiment row. Weak-flagged Evidence is placed first in the execution order.
- **Expected Under** and **If Wrong** must be numeric ranges or inequality expressions — NOT prose. The `decide_verdict()` function in E-1 reads these values directly.

### Resource budget (required, per-experiment)

- GPU hours, disk space, API cost estimate.
- If the plan requires paid API calls or edits to external LLM·LLDM repos (CLAUDE.md §2 stop condition "resource limit"), add an explicit `⚠ Requires user approval before E-1` note.

### Prerequisite handling

If the qa Report is missing, prepend:

```markdown
## ⚠ Prerequisite Missing

- Missing: research/reports/qa/<slug>/v*/Report.md
- Effect: Evidence chain is ungrounded; experiments will not be Evidence-verifying.
- Recommendation: run `/research-qa <slug> "<question>"` first. Advisory only.
```

## Who does what

1. Orchestrator calls this skill with stage context.
2. The skill dispatches the `experiment-planner` agent with the inputs above.
3. Optionally, the skill asks `critic` to review the PLAN.md for IV/DV/Expected Under/If Wrong numeric clarity. Critic may annotate issues in place.
4. Return control with PLAN.md written. Phase A ends. Do NOT proceed to Phase B.

## Failure / recovery

- If `experiment-planner` cannot produce a mapping (e.g., zero passing Evidence), write a PLAN.md with only the Prerequisite Missing block and a "No Evidence to verify" Executive Summary.
- The orchestrator will still hand control to the user for Phase B review — the user decides whether to proceed anyway or loop back to qa.

## References

- `.claude/agents/experiment-planner.md` — the dispatched agent
- `.claude/skills/experiment-plan/SKILL.md` — the legacy experiment PLAN skill (unchanged; this new skill calls into experiment-planner, which internally already uses those conventions for the per-experiment PLAN under `research/plans/<slug>/PLAN.md`). The stage-level PLAN at `research/plans/experiments/<slug>/v<N>/PLAN.md` is the gate document; the legacy per-slug PLAN lives alongside the experiment tree for code_implementer consumption.
- `.claude/skills/orchestrate/references/stage-gate.md` — Phase A/B/C protocol

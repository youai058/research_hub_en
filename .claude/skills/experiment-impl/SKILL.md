---
name: experiment-impl
description: "Phase C E-1→E-2→E-3 of the `experiments` stage. Sequential blocking: code-implementer (E-1) → implementation-verifier (E-2) → codex-reviewer (E-3) → run smoke test. Consumes research/plans/experiments/<slug>/v<N>/PLAN.md, produces experiments/<slug>/{code,configs,run.sh,IMPL_MAP.md}. Triggers: 'run experiment impl', 'E-1 implement', 'Phase C experiments', 'run smoke'."
---

# Experiment Implementation Skill (Phase C of /research-experiments)

Blocking sequential execution of the experiment implementation chain. Runs AFTER the user has given a trigger phrase and orchestrator has advanced to inner_phase=C with sub_phase=E-1.

## Inputs

| Input | Source | Required |
|---|---|---|
| stage-level PLAN.md | `research/plans/experiments/<slug>/v<N>/PLAN.md` (latest version) | yes |
| slug, stage_version | `loop_state.json` | yes |
| revision seed | prior analyze Report if rerunning | no |

## Outputs

- `experiments/<slug>/code/` — implementation modules, minimally invasive integrations of external repos
- `experiments/<slug>/configs/` — per-experiment YAML/JSON configs
- `experiments/<slug>/run.sh` — single entry point runnable as `bash run.sh [--smoke]`
- `experiments/<slug>/IMPL_MAP.md` — 3-way mapping `Evidence ↔ Experiment ↔ Code path`. Each experiment has a `decide_verdict()` function whose numeric thresholds are copied verbatim from the PLAN.md's Expected Under / If Wrong columns.
- Smoke test log under `.local/logs/experiments/<slug>-v<N>-smoke.log`
- E-2 verifier report (inline markdown block in IMPL_MAP.md or sibling file)
- E-3 codex-reviewer verdict (recorded in the experiment-report payload)

## Sub-phase chain (blocking)

### E-1: code-implementer

1. Orchestrator dispatches `code-implementer` agent.
2. Agent reads PLAN.md, reuses existing repos where possible (minimal invasion), writes code + configs + run.sh + IMPL_MAP.md.
3. Agent does NOT run smoke — that's E-2's responsibility.
4. `loop_state.py stage-advance --to E-2` after success.

### E-2: implementation-verifier

1. Orchestrator dispatches `implementation-verifier`.
2. Verifier performs:
   - Boundary cross-check PLAN ↔ IMPL_MAP (every Evidence has a code path; every code path has an Evidence)
   - IV/DV shape match (tensor shapes, dtype, units)
   - `decide_verdict()` numeric threshold equality check against PLAN
   - Smoke test: `bash run.sh --smoke` with minimal config, timeout 10 min
   - Edge case spot-checks (empty input, missing config)
3. Verdict: `pass` / `fix_needed` / `fatal`.
4. On `fix_needed`: verifier writes remediation notes to IMPL_MAP.md "verifier_feedback" section; orchestrator re-dispatches code-implementer with `--force` (max 1 cycle). On `fatal`: halt, escalate to user.
5. `loop_state.py stage-advance --to E-3` on pass.

### E-3: codex-reviewer (final gate)

1. Orchestrator dispatches `codex-reviewer` for adversarial review.
2. Focus: reproducibility (seeds? data hashes?), boundary correctness (decide_verdict thresholds match PLAN?), failure modes (what breaks if seed changes?).
3. Verdict: `approve` / `reject`.
4. On `reject`: one recovery cycle: fall back to E-1 with `--force`, re-run chain. Max 1 retry total; then escalate.
5. On `approve`: `loop_state.py stage-advance` (the last sub in STAGE_SUBPHASES[experiments]; next call is stage-complete).

## Smoke test contract

`run.sh --smoke` MUST:
- Run in under 10 minutes on a single GPU or CPU-only.
- Return exit 0 on success, non-zero on any failure.
- Write a human-readable summary to stdout with per-experiment pass/fail and the smoke log path.
- Be deterministic (seed fixed).

## Resource escalation

Per CLAUDE.md §2 stop conditions (resource limit), if the implementation requires external paid API calls or edits to external LLM·LLDM repos, the skill MUST halt and request explicit user approval BEFORE starting E-2.

## Failure / recovery

| Failure | Action |
|---|---|
| E-1 writes no code | Halt, report, do not advance |
| E-2 verifier `fatal` | Halt, escalate to user with verifier notes |
| E-2 verifier `fix_needed` × 2 | Escalate; do not infinite-loop |
| E-3 codex `reject` × 2 | Escalate with codex notes; user decides |
| Smoke timeout (>10min) | Report as fatal, halt |

## References

- `.claude/agents/code-implementer.md`
- `.claude/agents/implementation-verifier.md`
- `.claude/agents/codex-reviewer.md`
- `.claude/skills/code-implement/SKILL.md` — reuses existing conventions
- `.claude/skills/implementation-verify/SKILL.md`
- `.claude/skills/orchestrate/references/stage-gate.md`

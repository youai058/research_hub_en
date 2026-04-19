---
name: experiment-report
description: "Phase C tail of the `experiments` stage. Aggregates plan + impl + smoke results into research/reports/experiments/<slug>/v<N>/{Report.md, Report.slides.md} via .claude/scripts/report_builder.py. Runs after E-3 codex-reviewer approves. No agent; orchestrator executes directly. Triggers: 'generate experiment report', 'experiments Report.md', 'write experiments slides'."
---

# Experiment Report Skill (Phase C tail of /research-experiments)

Aggregates Phase A PLAN, E-1 implementation, E-2 verifier, E-3 codex-reviewer output, and smoke results into the mandatory Report pair. This skill has **no dedicated agent** — the orchestrator executes it directly by constructing the payload JSON and invoking `.claude/scripts/report_builder.py`.

## When this fires

After `experiment-impl` completes (E-3 approved, smoke passed) and BEFORE `loop_state.py stage-complete` is called. It is the last Phase C action.

## Inputs (collected by orchestrator)

| Source | What we extract |
|---|---|
| `research/plans/experiments/<slug>/v<N>/PLAN.md` | Evidence↔Experiment mapping, Expected Under / If Wrong, resource_budget |
| `experiments/<slug>/IMPL_MAP.md` | Final 3-way mapping, module list (path + LoC + external_repo) |
| `.local/logs/experiments/<slug>-v<N>-smoke.log` | Smoke pass/fail, duration |
| `experiments/<slug>/run.sh` | (header only — for reproducibility link) |
| implementation-verifier summary | E-2 boundary check results, shape_match |
| codex-reviewer E-3 verdict | approve flag + notes |

## Output

Pair (both required, atomic):
- `research/reports/experiments/<slug>/v<N>/Report.md`
- `research/reports/experiments/<slug>/v<N>/Report.slides.md`

Follows `.claude/skills/orchestrate/references/report-templates.md` §3 (`experiments` body spec).

## Procedure

1. Read each input above.
2. Build payload JSON in memory with the shape documented in `report_builder.py` module docstring (search for `experiments` body keys):
   - `plan_mapping[]`
   - `resource_budget`
   - `impl_modules[]`
   - `verifier_results`
   - `smoke_result`
   - `codex_e3_verdict`
   - `remaining_todos[]`
   - Plus common fields: `stage`, `slug`, `stage_version`, `started_at`, `completed_at`, `plan_path`, `sub_phase_trace`, `status`, `executive_summary`, `success_criteria`, `artifacts`, `deviations`, `known_gaps`, `outcome_summary`.
3. Write payload to a temp file under `/tmp/research_hub_report_<slug>_v<N>.json`.
4. Invoke:
   ```bash
   python3 /home/irteam/sw/research_hub/.claude/scripts/report_builder.py --payload /tmp/research_hub_report_<slug>_v<N>.json
   ```
5. Verify both output files exist and `latest` symlink updated.
6. Delete the temp payload file (best-effort).

## Payload-building rules

### Executive Summary (3–5 lines)

- Number of experiments run, number passed smoke, E-3 verdict summary.
- If any Evidence was not implemented (orphan), mention it.

### Success Criteria

Copy verbatim from Phase A PLAN.md's Success Criteria section. Fill in `result` (pass/fail/na) based on actual outcome:
- `pass` = smoke passed AND E-2 boundary OK AND E-3 approved AND every Evidence has a mapped experiment
- `fail` = any of the above is not met
- `na` = criterion could not be evaluated (e.g., smoke skipped due to resource escalation)

### Artifacts

Absolute paths (via realpath under research_hub root):
- `experiments/<slug>/code/**/*.py` — list top-level module paths
- `experiments/<slug>/configs/*.yaml|*.json`
- `experiments/<slug>/run.sh`
- `experiments/<slug>/IMPL_MAP.md`
- `.local/logs/experiments/<slug>-v<N>-smoke.log`

### Outcome Summary (2–4 lines)

Concrete: "N/M experiments passed smoke; E-3 approved; verdicts ready for analyze." NO next-stage suggestion.

## Failure handling

- If any input is missing, the skill still builds a report with `status: "partial"` and writes `known_gaps` accordingly. The report_builder.py allows overwrite only when status=="partial".
- If `report_builder.py` exits non-zero, halt Phase C and surface the error. Do NOT `stage-complete`.

## References

- `.claude/scripts/report_builder.py` — generator
- `.claude/skills/orchestrate/references/report-templates.md` — spec
- `.claude/skills/orchestrate/references/stage-gate.md` — Phase C tail contract

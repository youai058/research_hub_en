---
description: Enter the `experiments` stage (Phase A → B → C). Phase A dispatches experiment-planner in plan-only mode; Phase C chains E-1 code-implementer → E-2 implementation-verifier → E-3 codex-reviewer then emits a Report pair. Trigger phrase required to advance from B to C.
argument-hint: <slug>
---

# /research-experiments

Enter the `experiments` stage. Three sub-phases run in Phase C: `E-1 code-implementer → E-2 implementation-verifier → E-3 codex-reviewer`. Before those run, Phase A (PLAN) and Phase B (alignment) MUST happen, and Phase B REQUIRES a trigger phrase.

**Raw input**: $ARGUMENTS

## Step 1 — Parse slug

Expect `$1` = slug. If absent, ask the user. If the slug has no prior artifacts anywhere (`research/plans/qa/<slug>/`, `papers/.../<slug>...`), proceed but warn that downstream quality (evidence grounding) will suffer.

## Step 2 — Enter the stage

```bash
python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-enter \
    --stage experiments --slug "$1"
```

Parse the returned JSON (`slug`, `stage_version`, `plan_dir`, `report_dir`). If `status: "busy"`, the previous stage did not complete — ask the user whether to (a) `stage-complete --force` the previous one, or (b) abort. Do not pick silently.

## Step 3 — Phase A: dispatch experiment-planner (plan-only)

Dispatch `experiment-planner` with `run_in_background: true`, `mode: plan-only`, `stage: experiments`, `slug`, `stage_version`, `plan_dir: research/plans/experiments/<slug>/v<N>/`, `answer_path: research/answers/<YYYY-MM-DD>_<slug>.md`, `critique_path: research/critiques/<slug>.md`. 

Agent writes PLAN.md with Evidence↔Experiment 1:1 table, per-cell IV/DV/baseline/ablation, **Expected Under (evidence true)** / **If Wrong (refutation)** numeric ranges, resource budget, and `⚠ Prerequisite Missing` block if needed. No code, no smoke runs, no side effects.

Verify: PLAN.md exists and contains `^## Experiment E[0-9]+` headers. Exit 4 on fail. Do NOT self-advance to Phase B or C.

## Step 4–5 — Present PLAN, await trigger, Phase B gate

Print PLAN.md path + 3-line summary (Evidence count, resource budget, success criteria) + prerequisite warning (if any). Hard stop — do not advance to Phase C without trigger phrase.

When user responds: if phrase is whitelisted (check `python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py trigger-check "<phrase>"`), run `stage-advance --to B` then `stage-advance --to C --trigger "<phrase>"` and continue to Step 6. Otherwise re-dispatch experiment-planner in plan-only mode to rewrite PLAN.md, return to Step 4.

## Step 6 — Phase C: main session dispatches E-1 → E-2 → E-3

(E-1 → code-implementer, E-2 → implementation-verifier, E-3 → codex-reviewer). Throughout, `<slug>` is the value from stage-enter — substitute literally. The main session owns the chain; for each sub-phase dispatch one Agent with `run_in_background: true`, wait for task-notification, verify the expected artifact exists, then `stage-advance --to <next-subphase>` before dispatching the next.

**E-1 — code-implementer (execute)**

Before dispatch, compute PLAN path and Evidence id list:

```bash
PLAN_PATH=/home/irteam/sw/research_hub/research/plans/experiments/<slug>/v<N>/PLAN.md
EVIDENCE_IDS=$(grep -oE '^## Experiment E[0-9]+' "$PLAN_PATH" | awk '{print $3}' | tr '\n' ',' | sed 's/,$//')
```

Snapshot: `python3 .claude/scripts/verify_sub_phase.py snapshot E-1 --slug <slug>` *(run before dispatch)*

Dispatch `code-implementer` with:
- `run_in_background: true`
- `stage: experiments`, `slug`, `stage_version`, `plan_dir`
- `plan_path: research/plans/experiments/<slug>/v<N>/PLAN.md`
- `evidence_ids: <EVIDENCE_IDS>` (comma-separated, for IMPL_MAP 3-way mapping enforcement)
- `codex_feedback: <REVIEW_PATH>` *(optional — populated only on retry after E-3 reject so code-implementer can read the adversarial review)*

The agent reads PLAN.md, produces `experiments/<slug>/code/` modules + `configs/` + `run.sh` + `IMPL_MAP.md` (Evidence↔Experiment↔Code 3-way mapping), and implements `decide_verdict()` using the PLAN's Expected Under / If Wrong numeric thresholds verbatim.

Verify: `python3 .claude/scripts/verify_sub_phase.py verify E-1 --slug <slug>` (exit 12 on fail; checks `experiments/<slug>/code/**` grew and `IMPL_MAP.md` exists)

Advance:
```bash
python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-advance --to E-2
```

**E-2 — implementation-verifier**

`implementation-verifier` reports outcome via artifact: on **success** it returns a pass verdict in the agent body only (no file side-effect); on **failure** it writes `experiments/<slug>/qa_fail_<timestamp>.md`. The main session detects failure by snapshotting the `qa_fail_*.md` count pre/post dispatch.

Snapshot: `python3 .claude/scripts/verify_sub_phase.py snapshot E-2 --slug <slug>` *(run before dispatch)*

Dispatch `implementation-verifier` with:
- `run_in_background: true`
- `stage: experiments`, `slug`, `stage_version`
- `plan_path: research/plans/experiments/<slug>/v<N>/PLAN.md`
- `impl_map_path: experiments/<slug>/IMPL_MAP.md`
- `changed_files: <comma-separated list captured from E-1 post-state>` (omit to verify full directory)

The agent performs PLAN↔IMPL_MAP boundary cross-check (IV/DV/metric shape, Evidence id 1:1, `decide_verdict()` numeric equivalence) plus smoke test of `run.sh` and edge cases.

Verify: `python3 .claude/scripts/verify_sub_phase.py verify E-2 --slug <slug>` (exit 13 if any new `qa_fail_*.md` appeared)

**Stop rule** (CLAUDE.md §4.5): on exit 13, re-dispatch E-1 with newest `qa_fail_*.md` as `verifier_feedback`; re-run E-2. Consecutive fail limit = 2 (session-local).

On pass, advance:
```bash
python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-advance --to E-3
```

**E-3 — codex-reviewer**

`codex-reviewer` emits `research/reviews/experiments_<slug>_codex_review.md` with a YAML frontmatter `verdict: approve|approve_with_revisions|reject` field (mandatory — see `.claude/agents/codex-reviewer.md` "Frontmatter verdict contract"). The main session parses that frontmatter to decide whether to advance to report or re-dispatch E-1.

Snapshot: `python3 .claude/scripts/verify_sub_phase.py snapshot E-3 --slug <slug>` *(run before dispatch)*

Dispatch `codex-reviewer` with:
- `run_in_background: true`
- `phase: E-3`
- `slug`
- `target_paths: ["experiments/<slug>/code/", "experiments/<slug>/IMPL_MAP.md", "experiments/<slug>/run.sh", "research/plans/experiments/<slug>/v<N>/PLAN.md"]`
- `focus: reproducibility` (optional)

Verify: `python3 .claude/scripts/verify_sub_phase.py verify E-3 --slug <slug>` → prints `verdict: approve|approve_with_revisions|reject` on stdout. Exit 14 on missing/malformed verdict. `approve` / `approve_with_revisions` → advance to Step 7. `reject` → Stop-rule branch below.

**Stop rule** (CLAUDE.md §4.5): on `reject`, re-dispatch E-1 with `codex_feedback: <REVIEW_PATH>`; re-run E-2 + E-3. Consecutive reject limit = 2 (session-local). On abort, do not call `stage-complete`.

## Step 7 — Completion

After E-3 verdict is approve/approve_with_revisions, call:

```bash
python3 /home/irteam/sw/research_hub/.claude/scripts/report_builder.py --payload <tmp.json>
```

Payload aggregates E-1/E-2/E-3 artifacts: `plan_mapping` (Evidence↔Experiment from PLAN.md), `resource_budget` (from PLAN.md), `impl_modules` (files under `experiments/<slug>/code/`), `verifier_results` (E-2 pass/fail + `qa_fail_*.md` paths), `smoke_result` (run.sh verdict), `codex_e3_verdict` (approve/approve_with_revisions/reject + issues), `remaining_todos` (unchecked PLAN items).

Writes `Report.md` + `Report.slides.md` under `research/reports/experiments/<slug>/v<N>/`. Then call `python3 .claude/scripts/loop_state.py stage-complete` (hook blocks if Reports missing).

Print: Report paths + success criteria ✓/✗/NA + artifact list (PLAN + code + IMPL_MAP + codex review). **No next-stage suggestion. Stop.**

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

## Step 3 — Phase A: dispatch experiment-planner in plan-only mode

Dispatch the `experiment-planner` agent with `run_in_background: true` and the following prompt fields:

- `mode: plan-only`
- `stage: experiments`
- `slug: <slug-from-stage-enter>`
- `stage_version: <from-stage-enter>`
- `plan_dir: research/plans/experiments/<slug>/v<N>/`
- `answer_path: research/answers/<YYYY-MM-DD>_<slug>.md` (from prior qa stage; pass latest if multiple)
- `critique_path: research/critiques/<slug>.md` (from prior qa stage)

In `plan-only` mode the agent reads the passed Answer + critique, writes ONLY the PLAN.md with an Evidence-to-Experiment 1:1 table plus per-cell IV / DV / baseline / ablation / **Expected Under (evidence true)** / **If Wrong (refutation)** numeric ranges. **No code writing, no smoke runs, no `experiments/<slug>/` side effects.**

Wait for the background agent to complete via task-notification. Then verify:

```bash
test -f /home/irteam/sw/research_hub/research/plans/experiments/<slug>/v<N>/PLAN.md \
    || { echo "experiment-planner plan-only did not emit PLAN.md"; exit 4; }
grep -qE "^## Experiment E[0-9]+" /home/irteam/sw/research_hub/research/plans/experiments/<slug>/v<N>/PLAN.md \
    || { echo "PLAN.md has no Evidence cell (expected '## Experiment E<N>:' header)"; exit 4; }
```

The PLAN.md must include:
- Evidence ↔ Experiment 1:1 mapping table (Evidence Verification Map)
- Per-cell `## Experiment E<N>:` section with IV / DV / baseline / ablation
- **Expected Under (evidence-true numeric range)** + **If Wrong (refutation numeric range)** per cell — prevents post-hoc interpretation
- Resource budget
- `⚠ Prerequisite Missing` block if no prior qa Report exists for this slug

Do NOT self-advance to Phase B or C.

## Step 4 — Present PLAN and wait for user

Print:
1. PLAN.md absolute path
2. 3-line summary (Evidence count + resource budget + success criteria)
3. Prerequisite warning block (if any)
4. "PLAN.md 검토 후 피드백 주시거나, 이대로 진행하려면 `구현해줘` / `proceed` 같은 트리거 phrase로 응답해주세요."

**Hard stop here.** Do not call `stage-advance --to C` without an explicit trigger phrase from the user.

## Step 5 — Phase B: user alignment and trigger gate

When the user responds after Step 4:

- If their phrase is whitelisted (check via `python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py trigger-check "<phrase>"`), advance the loop state:
  ```bash
  python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-advance --to B
  python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-advance --to C --trigger "<their phrase>"
  ```
  Then continue to Step 6.
- Otherwise, treat the message as feedback: re-dispatch `experiment-planner` in `mode=plan-only` to rewrite PLAN.md in the same `v<N>/` directory, then return to Step 4.

## Step 6 — Phase C: main session dispatches E-1 → E-2 → E-3

**How to read these dispatch specs**: each bulleted block below is the payload for an `Agent(subagent_type: "<agent-name>", run_in_background: true, prompt: "...")` call. Fields under the bullets become `key: value` lines inside the prompt body; `run_in_background: true` is an Agent-tool parameter (not a prompt field); `subagent_type` is implied by the sub-phase header (E-1 → `code-implementer`, E-2 → `implementation-verifier`, E-3 → `codex-reviewer`).

> Throughout Step 6, the literal string `<slug>` in shell commands is a placeholder — substitute the actual slug value returned by `stage-enter` before executing. It is NOT a shell variable.

The main session owns the chain. For each of E-1, E-2, E-3, dispatch one Agent with `run_in_background: true`, wait for task-notification, verify the expected artifact exists, then `stage-advance --to <next-subphase>` before dispatching the next.

**E-1 — code-implementer (execute)**

Before dispatch, capture the PLAN Evidence id list (for downstream 1:1 mapping check) and snapshot the implementation directory:

```bash
PLAN_PATH=/home/irteam/sw/research_hub/research/plans/experiments/<slug>/v<N>/PLAN.md
EVIDENCE_IDS=$(grep -oE '^## Experiment E[0-9]+' "$PLAN_PATH" | awk '{print $3}' | tr '\n' ',' | sed 's/,$//')
PRE_E1_CODE_COUNT=$(find /home/irteam/sw/research_hub/experiments/<slug>/code -type f 2>/dev/null | wc -l)
```

Dispatch `code-implementer` with:
- `run_in_background: true`
- `stage: experiments`, `slug`, `stage_version`, `plan_dir`
- `plan_path: research/plans/experiments/<slug>/v<N>/PLAN.md`
- `evidence_ids: <EVIDENCE_IDS>` (comma-separated, for IMPL_MAP 3-way mapping enforcement)
- `codex_feedback: <REVIEW_PATH>` *(optional — populated only on retry after E-3 reject so code-implementer can read the adversarial review)*

The agent reads PLAN.md, produces `experiments/<slug>/code/` modules + `configs/` + `run.sh` + `IMPL_MAP.md` (Evidence↔Experiment↔Code 3-way mapping), and implements `decide_verdict()` using the PLAN's Expected Under / If Wrong numeric thresholds verbatim.

After task-notification, verify:

```bash
POST_E1_CODE_COUNT=$(find /home/irteam/sw/research_hub/experiments/<slug>/code -type f 2>/dev/null | wc -l)
test "$POST_E1_CODE_COUNT" -gt "$PRE_E1_CODE_COUNT" \
    || { echo "code-implementer did not add any code module under experiments/<slug>/code/"; exit 12; }
test -f /home/irteam/sw/research_hub/experiments/<slug>/IMPL_MAP.md \
    || { echo "code-implementer did not emit IMPL_MAP.md"; exit 12; }
```

Advance:
```bash
python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-advance --to E-2
```

**E-2 — implementation-verifier**

`implementation-verifier` reports outcome via artifact: on **success** it returns a pass verdict in the agent body only (no file side-effect); on **failure** it writes `experiments/<slug>/qa_fail_<timestamp>.md`. The main session detects failure by snapshotting the `qa_fail_*.md` count pre/post dispatch.

Before dispatch, snapshot the qa_fail count:

```bash
PRE_E2_FAIL_COUNT=$(find /home/irteam/sw/research_hub/experiments/<slug> -maxdepth 1 -name 'qa_fail_*.md' 2>/dev/null | wc -l)
```

Dispatch `implementation-verifier` with:
- `run_in_background: true`
- `stage: experiments`, `slug`, `stage_version`
- `plan_path: research/plans/experiments/<slug>/v<N>/PLAN.md`
- `impl_map_path: experiments/<slug>/IMPL_MAP.md`
- `changed_files: <comma-separated list captured from E-1 post-state>` (omit to verify full directory)

The agent performs PLAN↔IMPL_MAP boundary cross-check (IV/DV/metric shape, Evidence id 1:1, `decide_verdict()` numeric equivalence) plus smoke test of `run.sh` and edge cases.

After task-notification, decide:

```bash
POST_E2_FAIL_COUNT=$(find /home/irteam/sw/research_hub/experiments/<slug> -maxdepth 1 -name 'qa_fail_*.md' 2>/dev/null | wc -l)
if [ "$POST_E2_FAIL_COUNT" -gt "$PRE_E2_FAIL_COUNT" ]; then
    echo "implementation-verifier emitted a new qa_fail_*.md — verification failed"
    exit 13
fi
```

**Stop rule (CLAUDE.md §4.5)**: Track consecutive E-2 failures in the main session's local reasoning, not in loop_state. On failure (exit 13 above), re-dispatch E-1 with the newest `qa_fail_*.md` attached as `verifier_feedback` and re-run E-2. If two consecutive E-2 cycles within the same `stage_version` fail, abort per CLAUDE.md §4.5 (do not call `stage-complete`) and surface the last `qa_fail_*.md` to the user. Any E-2 pass resets the counter. This counter is session-local and does NOT survive a session restart — on restart the counter starts at 0 again.

On pass, advance:
```bash
python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-advance --to E-3
```

**E-3 — codex-reviewer**

`codex-reviewer` emits `research/reviews/experiments_<slug>_codex_review.md` with a YAML frontmatter `verdict: approve|approve_with_revisions|reject` field (mandatory — see `.claude/agents/codex-reviewer.md` "Frontmatter verdict contract"). The main session parses that frontmatter to decide whether to advance to report or re-dispatch E-1.

Dispatch `codex-reviewer` with:
- `run_in_background: true`
- `phase: E-3`
- `slug`
- `target_paths: ["experiments/<slug>/code/", "experiments/<slug>/IMPL_MAP.md", "experiments/<slug>/run.sh", "research/plans/experiments/<slug>/v<N>/PLAN.md"]`
- `focus: reproducibility` (optional)

After task-notification, verify the review file exists and parse the verdict:

```bash
REVIEW_PATH=/home/irteam/sw/research_hub/research/reviews/experiments_<slug>_codex_review.md
test -f "$REVIEW_PATH" \
    || { echo "codex-reviewer did not emit a review file at $REVIEW_PATH"; exit 14; }
VERDICT=$(awk '/^---$/{c++;next} c==1 && /^verdict:/{print $2; exit}' "$REVIEW_PATH")
echo "E-3 verdict: $VERDICT"

case "$VERDICT" in
    approve|approve_with_revisions)
        # pass — advance to Step 7 (report generation). `approve_with_revisions`
        # is treated as `approve` for gating; surface the issues list to the
        # user in the final Step 7 output.
        ;;
    reject)
        # handle reject per Stop rule below (increment reject counter, re-dispatch E-1 or abort)
        :
        ;;
    *)
        # Fail closed: missing frontmatter, typo (e.g. `conditional_approve`), or
        # non-compliant output from codex-reviewer must NOT be silently treated
        # as approve. Exit 14 is reused because the review file is present-but-
        # unusable, which falls under "E-3 review-file issue".
        echo "E-3 verdict missing or unrecognized: '$VERDICT' (review file may lack frontmatter)"
        exit 14
        ;;
esac
```

**Stop rule (CLAUDE.md §4.5)**: If `VERDICT == "reject"`, re-dispatch E-1 with `codex_feedback: <REVIEW_PATH>` attached so `code-implementer` can read the review issues and revise. Track consecutive rejects in the main session's local reasoning. After a revised E-1 run, re-run E-2 then E-3. If E-3 rejects a second consecutive time within the same `stage_version`, abort per CLAUDE.md §4.5 (do not call `stage-complete`) and surface the review file to the user. Any `approve` / `approve_with_revisions` verdict resets the counter and advances to Step 7. This counter is session-local.

**User-interrupt handling**: If the user sends a message mid-chain, the currently-running Agent is NOT cancelled (every dispatch is `run_in_background: true`). Dialogue with the user, optionally read the in-progress artifact, and decide whether to (a) wait for the current sub-phase to finish then stop, (b) continue, or (c) abort. Do not dispatch the next sub-phase without intent.

## Step 7 — Completion

After Phase C chain completes (E-3 verdict approve or approve_with_revisions), the main session calls `report_builder.py` directly:

```bash
python3 /home/irteam/sw/research_hub/.claude/scripts/report_builder.py \
    --payload <tmp.json>
```

The payload JSON is built in the main session by aggregating the E-1/E-2/E-3 artifacts. Required fields:
- `plan_mapping` — Evidence id → Experiment cell id mapping (from PLAN.md Evidence Verification Map)
- `resource_budget` — GPU hours / disk / API cost estimate (from PLAN.md)
- `impl_modules` — list of files under `experiments/<slug>/code/`
- `verifier_results` — E-2 pass/fail summary + any `qa_fail_*.md` paths
- `smoke_result` — `run.sh` smoke verdict (pass/fail/skipped)
- `codex_e3_verdict` — `approve | approve_with_revisions | reject` + issues list
- `remaining_todos` — unchecked items in PLAN.md implementation checklists

Writes `Report.md` + `Report.slides.md` under `research/reports/experiments/<slug>/v<N>/`.

Then call:
```bash
python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-complete
```

`phase_advance_check.sh` (hook) blocks `stage-complete` if either Report file is missing.

Print the final message:
- Report.md + Report.slides.md absolute paths
- Success criteria ✓/✗/NA
- Artifact path list (PLAN + code dir + IMPL_MAP + codex review)
- **No next-stage suggestion.** Stop.

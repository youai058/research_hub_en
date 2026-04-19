---
description: Enter the `qa` stage. Formulates a direct answer with Evidence Chain (3-7) and independently critiques each Evidence on 4 axes (Grounding/Support/Counter-Evidence/Verifiability). Requires explicit trigger phrase to enter Phase C.
argument-hint: <slug> <question>
---

# /research-qa

Enter the `qa` stage. Direct Answer + Evidence Chain + 4-axis critique. Two sub-phases run in Phase C: `B-1 answer-formulator → B-2 critic` (+ codex-reviewer in parallel inside B-2).

**Raw input**: $ARGUMENTS

## Step 1 — Parse arguments

Expected format: `"<slug>" "<question>"` (slug first, quoted; then question text). Parse `$ARGUMENTS` accordingly:
- First token (quoted or first word): `slug`
- Remainder: `question`

If parsing fails or either is missing, ask the user for the structured form. Do not guess.

## Step 2 — Preflight (advisory)

Check prerequisites:
- `papers/vector_db/manifest.json` files_tracked. If 0 or missing, warn that evidence retrieval will be weak. The warning is **advisory**; the user may still proceed.
- Prior summaries for `<slug>` in `papers/marp-summary/*/*/<slug>*.md` — optional.

## Step 3 — Enter the stage

```bash
python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-enter \
    --stage qa \
    --slug "<slug>" \
    --topic "<question>"   # used to emit question.kg.json (qa stage only)
```

Parse the returned JSON (`slug`, `stage_version`, `plan_dir`, `report_dir`). If `status: "busy"`, the previous stage did not complete — ask the user whether to (a) `stage-complete --force` the previous one, or (b) abort. Do not pick silently.

## Step 4 — Phase A: dispatch answer-formulator in plan-only mode

Dispatch the `answer-formulator` agent with `run_in_background: true` and the following prompt fields:

- `mode: plan-only`
- `stage: qa`
- `slug: <slug-from-stage-enter>`
- `stage_version: <from-stage-enter>`
- `plan_dir: research/plans/qa/<slug>/v<N>/`
- `question: <question>`

In `plan-only` mode the agent writes ONLY the PLAN.md (hybrid_query dry-run + evidence count estimate; no Direct Answer, no `research/answers/**` write). After task-notification verify:

```bash
test -f /home/irteam/sw/research_hub/research/plans/qa/<slug>/v<N>/PLAN.md \
    || { echo "answer-formulator plan-only did not emit PLAN.md"; exit 4; }
```

PLAN.md must include: question restatement, target evidence count (3–7), retrieval parameters, 4-axis pass thresholds, and `⚠ Prerequisite Missing` block if RAG is empty.

Do NOT self-advance to Phase B or C.

## Step 5 — Phase B: user alignment and trigger gate

Print PLAN.md absolute path, 3-line summary, prerequisite warning (if any), and "After reviewing PLAN.md, either give feedback or reply with a trigger phrase like `proceed` or `go ahead` to continue."

**Hard stop here.** Do not call `stage-advance --to C` without an explicit trigger phrase from the user.

When the user responds, check via `python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py trigger-check "<phrase>"`. If whitelisted, advance:
```bash
python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-advance --to B
python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-advance --to C --trigger "<their phrase>"
```
Then continue to Step 6. Otherwise treat as feedback — re-dispatch `answer-formulator` in `mode=plan-only` and return to the top of this step.

## Step 6 — Phase C: main session dispatches B-1 then B-2

Each bulleted block below is the payload for `Agent(subagent_type: "<agent>", run_in_background: true, prompt: {...})`. `subagent_type` is implied by the sub-phase header (B-1 → `answer-formulator`, B-2 → `critic` **and** `codex-reviewer` in parallel). In shell commands, `<slug>` is a literal placeholder — substitute before executing. Main session owns the chain: dispatch, wait for task-notification(s), verify artifact(s), `stage-advance --to <next-subphase>`, repeat.

**B-1 — answer-formulator (execute)**

Snapshot: `python3 .claude/scripts/verify_sub_phase.py snapshot B-1 --slug <slug>`

Dispatch `answer-formulator` with:
- `run_in_background: true`
- `mode: execute`
- `stage: qa`, `slug`, `stage_version`, `plan_dir`
- `question: <question>`

Verify: `python3 .claude/scripts/verify_sub_phase.py verify B-1 --slug <slug>` (exit 9 on fail)

Advance:
```bash
python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-advance --to B-2
```

**B-2 — critic AND codex-reviewer in parallel**

Dispatch **both** agents in a SINGLE main-session message (parallel; they must not see each other's output — `critic.md` §Parallelism rule).

Snapshot: `python3 .claude/scripts/verify_sub_phase.py snapshot B-2-critic --slug <slug> && python3 .claude/scripts/verify_sub_phase.py snapshot B-2-codex --slug <slug>`

Parallel dispatch payload:

- `critic` — `run_in_background: true`, `stage: qa`, `slug`, `stage_version`, `answer_path: research/answers/<YYYY-MM-DD>_<slug>.md` (the file emitted by B-1). Output: `research/critiques/<slug>.md` with 4-axis scoring and pass/fail per Evidence.
- `codex-reviewer` — `run_in_background: true`, `phase: qa`, `slug`, `target_paths: ["research/answers/<YYYY-MM-DD>_<slug>.md"]`, `focus: grounding` (optional). Output: `research/reviews/qa_<slug>_codex_review.md` with `verdict` + `issues`.

Wait for **both** task-notifications, then verify: `python3 .claude/scripts/verify_sub_phase.py verify B-2-critic --slug <slug> && python3 .claude/scripts/verify_sub_phase.py verify B-2-codex --slug <slug>` (exit 10 critic / 11 codex on fail)

**Stop rule** (CLAUDE.md §4.5): critic emits frontmatter `pass_count: <int>`. On `pass_count: 0` main session re-dispatches B-1 with critic feedback as `revision_seed`. Consecutive zero-pass limit = 3 (session-local counter, resets on any non-zero pass). On abort, do not call `stage-complete`.

## Step 7 — Completion

After Phase C completes, call `report_builder.py` with a payload JSON aggregating B-1 and B-2 artifacts:

```bash
python3 /home/irteam/sw/research_hub/.claude/scripts/report_builder.py \
    --payload <tmp.json>
```

Writes `Report.md` + `Report.slides.md` under `research/reports/qa/<slug>/v<N>/`. Then call:
```bash
python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-complete
```

`phase_advance_check.sh` (hook) blocks `stage-complete` if either Report file is missing.

Print the final message:
- Report.md + Report.slides.md absolute paths
- Success criteria ✓/✗/NA
- Artifact path list (answer + critique + codex review)
- **No next-stage suggestion.** Stop.

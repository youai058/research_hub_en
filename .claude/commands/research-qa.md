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

In `plan-only` mode the agent performs a hybrid_query dry-run (RAG + KG retrieval parameter design, candidate-evidence count estimate) and writes ONLY the PLAN.md. **No Direct Answer body, no `research/answers/**` write, no Evidence Chain finalization.**

Wait for the background agent to complete via task-notification. Then verify:

```bash
test -f /home/irteam/sw/research_hub/research/plans/qa/<slug>/v<N>/PLAN.md \
    || { echo "answer-formulator plan-only did not emit PLAN.md"; exit 4; }
```

The PLAN.md must include:
- Question restatement (normalized)
- Target evidence count (3–7)
- Retrieval parameters (k, KG depth)
- 4-axis pass thresholds (Grounding≥3 AND Support≥3 AND Verifiability≥3)
- `⚠ Prerequisite Missing` block if RAG is empty or `<slug>` has no prior summaries

Do NOT self-advance to Phase B or C.

## Step 5 — Phase B: user alignment and trigger gate

Print:
1. PLAN.md absolute path
2. 3-line summary (question restatement + expected Evidence count + success criteria)
3. Prerequisite warning block (if any)
4. "PLAN.md 검토 후 피드백 주시거나, 이대로 진행하려면 `구현해줘` / `proceed` 같은 트리거 phrase로 응답해주세요."

**Hard stop here.** Do not call `stage-advance --to C` without an explicit trigger phrase from the user.

When the user responds:

- If their phrase is whitelisted (check via `python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py trigger-check "<phrase>"`), advance the loop state:
  ```bash
  python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-advance --to B
  python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-advance --to C --trigger "<their phrase>"
  ```
  Then continue to Step 6.
- Otherwise, treat the message as feedback: re-dispatch `answer-formulator` in `mode=plan-only` to rewrite PLAN.md in the same `v<N>/` directory, then return to the top of this step.

## Step 6 — Phase C: main session dispatches B-1 then B-2

**How to read these dispatch specs**: each bulleted block below is the payload for an `Agent(subagent_type: "<agent-name>", run_in_background: true, prompt: "...")` call. Fields under the bullets become `key: value` lines inside the prompt body; `run_in_background: true` is an Agent-tool parameter (not a prompt field); `subagent_type` is implied by the sub-phase header (B-1 → `answer-formulator`, B-2 → `critic` **and** `codex-reviewer` in parallel).

> Throughout Step 6, the literal string `<slug>` in shell commands is a placeholder — substitute the actual slug value returned by `stage-enter` before executing. It is NOT a shell variable.

The main session owns the chain. For B-1 and B-2, dispatch as described, wait for task-notification(s), verify the expected artifact(s) exist, then `stage-advance --to <next-subphase>` before the next dispatch.

**B-1 — answer-formulator (execute)**

Before dispatch, snapshot the current answer-file count so we can compare afterward:

```bash
PRE_B1_ANSWER_COUNT=$(find research/answers -name '*.md' 2>/dev/null | wc -l)
```

Dispatch `answer-formulator` with:
- `run_in_background: true`
- `mode: execute`
- `stage: qa`, `slug`, `stage_version`, `plan_dir`
- `question: <question>`

The agent reads `research/plans/qa/<slug>/v<N>/PLAN.md` and writes the Direct Answer + Evidence Chain (3–7 items) + Open Sub-Questions to `research/answers/YYYY-MM-DD_<slug>.md`, emitting `answer:` / `evidence:` KG nodes.

After task-notification, verify a new answer file appeared:

```bash
POST_B1_ANSWER_COUNT=$(find research/answers -name '*.md' 2>/dev/null | wc -l)
test "$POST_B1_ANSWER_COUNT" -gt "$PRE_B1_ANSWER_COUNT" \
    || { echo "answer-formulator did not emit an answer file"; exit 9; }
```

Advance:
```bash
python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-advance --to B-2
```

**B-2 — critic AND codex-reviewer in parallel**

Dispatch **both** agents in a SINGLE main-session message (two Agent tool calls in one block), both `run_in_background: true`. They must not see each other's output — codex-reviewer is an independent 3rd-party critique (per `critic.md` §팀 통신 프로토콜: "병렬 규칙: B-2에서 critic과 동시 호출 시 서로의 critique를 보지 않는다").

Before dispatch, snapshot both output locations:

```bash
PRE_B2_CRITIQUE_COUNT=$(find research/critiques -name '*.md' 2>/dev/null | wc -l)
PRE_B2_CODEX_COUNT=$(find research/reviews -name "*_<slug>_codex_review.md" 2>/dev/null | wc -l)
```

Parallel dispatch payload:

- `critic` — `run_in_background: true`, `stage: qa`, `slug`, `stage_version`, `answer_path: research/answers/<YYYY-MM-DD>_<slug>.md` (the file emitted by B-1). Output: `research/critiques/<slug>.md` with 4-axis scoring and pass/fail per Evidence.
- `codex-reviewer` — `run_in_background: true`, `phase: qa`, `slug`, `target_paths: ["research/answers/<YYYY-MM-DD>_<slug>.md"]`, `focus: grounding` (optional). Output: `research/reviews/qa_<slug>_codex_review.md` with `verdict` + `issues`.

Wait for **both** task-notifications before proceeding.

After both complete, verify each side grew:

```bash
POST_B2_CRITIQUE_COUNT=$(find research/critiques -name '*.md' 2>/dev/null | wc -l)
POST_B2_CODEX_COUNT=$(find research/reviews -name "*_<slug>_codex_review.md" 2>/dev/null | wc -l)
test "$POST_B2_CRITIQUE_COUNT" -gt "$PRE_B2_CRITIQUE_COUNT" \
    || { echo "critic did not emit a critique file"; exit 10; }
test "$POST_B2_CODEX_COUNT" -gt "$PRE_B2_CODEX_COUNT" \
    || { echo "codex-reviewer did not emit a review file"; exit 11; }
```

**Stop rule (CLAUDE.md §4.5)**:

*Pass-count contract*: The critic MUST emit a frontmatter field `pass_count: <int>` (number of Evidence that passed Grounding≥3 AND Support≥3 AND Verifiability≥3) at the top of `research/critiques/<slug>.md`. The main session reads that field after task-notification to decide whether to re-dispatch B-1 or proceed to report.

*Zero-pass retry*: if `pass_count: 0`, the main session may re-dispatch B-1 with the critic's feedback attached as `revision_seed`, then re-run B-2.

*Consecutive zero-pass counter*: Track consecutive zero-pass cycles in the main session's local reasoning, not in loop_state. Each time B-2 returns `pass_count: 0`, increment a local counter and re-dispatch B-1 with the critic feedback attached. If the counter reaches 3, abort per CLAUDE.md §4.5 (do not call `stage-complete`) and flag the question as unanswerable with the current corpus. Any non-zero `pass_count` resets the counter. This counter is session-local and does NOT survive a session restart — on restart the counter starts at 0 again, which is the desired behavior (restart = fresh attempt). Do not encode the retry loop inline; the main session decides per cycle.

**User-interrupt handling**: If the user sends a message mid-chain, the currently-running Agent is NOT cancelled (every dispatch is `run_in_background: true`). Dialogue with the user, optionally read the in-progress artifact, and decide whether to (a) wait for the current sub-phase to finish then stop, (b) continue, or (c) abort. Do not dispatch the next sub-phase without intent.

## Step 7 — Completion

After Phase C chain completes, the main session calls `report_builder.py` directly:

```bash
python3 /home/irteam/sw/research_hub/.claude/scripts/report_builder.py \
    --payload <tmp.json>
```

The payload JSON is built in the main session by aggregating the B-1 and B-2 artifacts (question_restatement, direct_answer, evidence_chain, critic_scores, pass_fail_counts, codex_review verdict + issues, weak_points). Writes `Report.md` + `Report.slides.md` under `research/reports/qa/<slug>/v<N>/`.

Then call:
```bash
python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-complete
```

`phase_advance_check.sh` (hook) blocks `stage-complete` if either Report file is missing.

Print the final message:
- Report.md + Report.slides.md absolute paths
- Success criteria ✓/✗/NA
- Artifact path list (answer + critique + codex review)
- **No next-stage suggestion.** Stop.

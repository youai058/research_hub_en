---
description: Enter the `papers` stage (Phase A → B → C). Collects papers, triages, summarizes, and indexes into RAG. Each stage requires explicit user approval to advance from Phase B (planning) to Phase C (execution). No autonomous bypass.
argument-hint: <topic description> [--include-arxiv]  OR  --slug <existing-slug> [--include-arxiv]
---

# /research-papers

Enter the `papers` stage. Four sub-phases run in Phase C: `A-1 paper-hunter → A-2 paper-triage → A-3 paper-summarizer → A-4 rag-curator`. Before those run, Phase A (PLAN) and Phase B (alignment) MUST happen, and Phase B REQUIRES a trigger phrase.

**Raw input**: $ARGUMENTS

## Step 1 — Preflight (advisory only, not blocking)

Check if a search topic is present. If `$ARGUMENTS` is empty and no `--slug <existing>` flag is given, ask the user for a topic before proceeding.

If `papers/vector_db/manifest.json` already exists with many files, still proceed — `papers` may re-run to extend the corpus.

## Step 1.5 — Topic Refinement (Socratic interview)

Invoke the `topic-refine` skill **in the main session** (not a subagent — the interview needs TUI interactivity). Pass `$ARGUMENTS` as `raw_input`.

```bash
# The skill is self-contained; Claude reads its SKILL.md and runs the interview.
# No CLI invocation here — the main session calls the skill directly.
```

The skill will:

1. Run 2–5 adaptive rounds asking from 3 perspectives (Scope Definer / Keyword Strategist / Triage Sharpener).
2. Write `research/topics/.pending.topic.json` on termination.
3. Validate it with `topic_spec.py validate`.

After the skill returns, confirm the staging file exists:

```bash
test -f /home/irteam/sw/research_hub/research/topics/.pending.topic.json \
    || { echo "topic-refine did not emit .pending.topic.json"; exit 3; }
python3 /home/irteam/sw/research_hub/.claude/skills/topic-refine/scripts/topic_spec.py \
    validate /home/irteam/sw/research_hub/research/topics/.pending.topic.json
```

**Halting rules (Step 1.5)** — if any of the following occur, surface the error to the user and stop **before** Step 2 runs. Do not call `stage-enter`.

- User interrupts the interview (Ctrl+C, explicit "취소" / "abort" / "stop") → `.pending.topic.json` may not exist; the `test -f` check fails with `exit 3`. Do not retry silently.
- `topic_spec.py validate` exits non-zero → the spec is malformed. Report the validation error verbatim and stop. Do not proceed with a broken spec.
- In both cases, remove any partial `.pending.topic.json` (`rm -f /home/irteam/sw/research_hub/research/topics/.pending.topic.json`) before exiting so the next `/research-papers` run starts clean.

**Skip conditions** (do NOT run interview):

- User passes `--slug <existing>` AND `research/topics/<existing>.topic.json` already exists → skip refinement entirely (no staging file written); Step 2 reuses the existing spec.
- User types a valid trigger phrase (`proceed` / `진행해줘` etc. — see CLAUDE.md §4.3 whitelist) **immediately** on the first interview prompt — treat as early exit, emit a minimal `.pending.topic.json` (clarity_scores all 0, termination_reason `user_early_exit`) from the raw input, then continue to Step 2.

## Step 2 — Enter the stage (allocate v<N>)

```bash
# Option A: new slug derived from topic
python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-enter \
    --stage papers \
    --topic "$ARGUMENTS"

# Option B: re-run an existing slug (user passed --slug)
# python3 .../loop_state.py stage-enter --stage papers --slug <existing-slug>
```

Parse the returned JSON (`slug`, `stage_version`, `plan_dir`, `report_dir`). If `status: "busy"`, the previous stage did not complete — ask the user whether to (a) `stage-complete --force` the previous one, or (b) abort. Do not pick silently.

**On abort (busy-status path)**: remove the orphaned staging file before returning control to the user, so the next `/research-papers` run does not silently consume a stale interview result:

```bash
rm -f /home/irteam/sw/research_hub/research/topics/.pending.topic.json
```

After successful slug allocation, rename the staging topic spec into its canonical location (shell variables below are the literal `slug` value returned by `stage-enter`):

```bash
mv /home/irteam/sw/research_hub/research/topics/.pending.topic.json \
   /home/irteam/sw/research_hub/research/topics/<slug>.topic.json
```

If the rename fails because `.pending.topic.json` is missing, this is only expected when Step 1.5 was skipped via `--slug <existing>` with a pre-existing `<slug>.topic.json`. In that case, proceed using the existing spec. Any other missing-file case is a bug — stop and report.

## Step 3 — Phase A: delegate to orchestrator

Dispatch the `orchestrator` agent with:

- stage: `papers`
- slug: (from script output)
- stage_version: (from script output)
- plan_dir: (from script output)
- topic_spec: `research/topics/<slug>.topic.json` (canonical — consumed by paper-hunter A-1 and paper-triage A-2)
- topic (legacy fallback): $ARGUMENTS (raw user string, used only if orchestrator cannot find the spec)

Orchestrator MUST produce `research/plans/papers/<slug>/v<N>/PLAN.md` via the paper-hunter agent (planning-only mode — no downloads yet). It MUST include:

- venues/years/keywords/max-per-venue/triage-threshold
- expected collected count
- RAG reindex flag
- `include_arxiv: true/false` (true only if the raw `$ARGUMENTS` contained `--include-arxiv`). This flag is propagated verbatim to `hunt.py --include-arxiv` in Phase C. When false, hunt.py restricts itself to the 6-venue whitelist (NeurIPS/AAAI/ICLR/ICML/ACL/EMNLP) and drops any etc emissions.
- `⚠ Prerequisite Missing` block if `papers/vector_db/` is empty and this would create an unusually isolated corpus

When orchestrator returns, inner_phase must be `A`. DO NOT self-advance to B or C.

## Step 4 — Present PLAN and wait for user

Print:
1. PLAN.md absolute path
2. 3-line summary (goal + expected artifacts + success criteria)
3. Prerequisite warning block (if any)
4. "PLAN.md 검토 후 피드백 주시거나, 이대로 진행하려면 `구현해줘` / `proceed` 같은 트리거 phrase로 응답해주세요."

**Hard stop here.** Do not call `stage-advance --to C` without an explicit trigger phrase from the user.

## Step 5 — Phase B + C (after trigger)

When the user responds with feedback:
- If it matches the trigger whitelist (`구현해줘`, `proceed`, etc.), run:
  ```bash
  python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-advance --to B
  python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-advance --to C --trigger "<their phrase>"
  ```
  Then re-dispatch the orchestrator for Phase C execution (`A-1 → A-2 → A-3 → A-4` blocking sequential).
- Otherwise, treat as feedback: re-dispatch orchestrator to rewrite PLAN.md in place (same `v<N>/`), then return to Step 4.

The trigger whitelist is enforced by `loop_state.py` — if the phrase is wrong, `stage-advance --to C` exits 2 with an error listing the allowed phrases.

## Step 6 — Completion

After orchestrator reports all sub-phases done, it must:
1. Generate payload JSON for `.claude/scripts/report_builder.py`.
2. Call `report_builder.py --payload <tmp.json>` to write `Report.md` + `Report.slides.md`.
3. Call `python3 .../loop_state.py stage-complete` → `loop_state.json.stage == "idle"`.

Print the final message per `stage-gate.md` §4.5:
- Report.md + Report.slides.md absolute paths
- Success criteria ✓/✗/NA
- Artifact path list
- **No next-stage suggestion.** Stop.

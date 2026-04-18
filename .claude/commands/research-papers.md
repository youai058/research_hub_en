---
description: Enter the `papers` stage (Phase A → B → C). Collects papers, triages, summarizes, and indexes into RAG. Each stage requires explicit user approval to advance from Phase B (planning) to Phase C (execution). No autonomous bypass.
argument-hint: <topic description> [--include-arxiv]  OR  --slug <existing-slug> [--include-arxiv]
---

# /research-papers

Enter the `papers` stage. Five sub-phases run in Phase C: `A-1 paper-hunter → A-1.5 abstract-indexer → A-2 paper-triage → A-3 paper-summarizer → A-4 rag-curator`. Before those run, Phase A (PLAN) and Phase B (alignment) MUST happen, and Phase B REQUIRES a trigger phrase.

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

## Step 3 — Phase A: dispatch paper-hunter in plan-only mode

Dispatch the `paper-hunter` agent with `run_in_background: true` and the following prompt fields:

- `mode: plan-only`
- `stage: papers`
- `slug: <slug-from-stage-enter>`
- `stage_version: <from-stage-enter>`
- `plan_dir: research/plans/papers/<slug>/v<N>/`
- `topic_spec: research/topics/<slug>.topic.json` (canonical)
- `raw_topic: $ARGUMENTS` (legacy fallback)

Wait for the background agent to complete via task-notification. Then verify:

```bash
test -f /home/irteam/sw/research_hub/research/plans/papers/<slug>/v<N>/PLAN.md \
    || { echo "paper-hunter plan-only did not emit PLAN.md"; exit 4; }
```

The PLAN.md must include:
- venues / years / keyword groups / `max-per-venue-year` / triage threshold
- expected collected count
- RAG reindex flag
- `include_arxiv: true/false` (true iff `$ARGUMENTS` contained `--include-arxiv`)
- `⚠ Prerequisite Missing` block if `papers/vector_db/` is empty

Do NOT self-advance to Phase B or C.

## Step 4 — Present PLAN and wait for user

Print:
1. PLAN.md absolute path
2. 3-line summary (goal + expected artifacts + success criteria)
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
- Otherwise, treat the message as feedback: re-dispatch `paper-hunter` in `mode=plan-only` to rewrite PLAN.md in the same `v<N>/` directory, then return to Step 4.

## Step 6 — Phase C: main session dispatches the 4 sub-phases sequentially

**How to read these dispatch specs**: each bulleted block below is the payload for an `Agent(subagent_type: "<agent-name>", run_in_background: true, prompt: "...")` call. Fields under the bullets become `key: value` lines inside the prompt body; `run_in_background: true` is an Agent-tool parameter (not a prompt field); `subagent_type` is implied by the sub-phase header (A-1 → `paper-hunter`, A-1.5 → `abstract-indexer`, A-2 → `paper-triage`, A-3 → `paper-summarizer`, A-4 → `rag-curator`).

The main session owns the chain. For each of A-1, A-1.5, A-2, A-3, A-4, dispatch one Agent with `run_in_background: true`, wait for task-notification, verify the expected artifact exists, then `stage-advance --to <next-subphase>` before dispatching the next.

**A-1 — paper-hunter (execute)**

Before dispatch, snapshot the current raw-metadata file count so we can compare afterward:

```bash
PRE_A1_RAW_COUNT=$(find papers/metadata -name '*.raw.md' 2>/dev/null | wc -l)
```

Dispatch `paper-hunter` with:
- `run_in_background: true`
- `mode: execute`
- `stage: papers`, `slug`, `stage_version`, `plan_dir`
- `topic_spec: research/topics/<slug>.topic.json`

After task-notification, verify that the set of `papers/metadata/**/*.raw.md` files grew since the pre-dispatch snapshot (per-paper slugs, not the stage slug):

```bash
POST_A1_RAW_COUNT=$(find papers/metadata -name '*.raw.md' 2>/dev/null | wc -l)
test "$POST_A1_RAW_COUNT" -gt "$PRE_A1_RAW_COUNT" \
    || { echo "paper-hunter did not collect any new raw.md"; exit 6; }
```

Advance:
```bash
python3 .../loop_state.py stage-advance --to A-1.5
```

**A-1.5 — abstract-indexer**

Incrementally embeds every new or changed `papers/metadata/**/*.raw.md` into the ChromaDB `abstracts` collection. paper-triage (A-2) uses this collection for its dense-retrieval pre-filter. Without A-1.5, A-2 would exit 5.

Before dispatch, snapshot the abstracts manifest file count so we can verify growth:

```bash
PRE_A15_COUNT=$(python3 -c "
import json, os
p = 'papers/vector_db/abstracts_manifest.json'
print(len(json.load(open(p)).get('files', {})) if os.path.isfile(p) else 0)
" )
```

Dispatch `abstract-indexer` with:
- `run_in_background: true`
- `stage: papers`, `slug`, `stage_version`

After task-notification, verify the manifest grew (or remained equal only if A-1 emitted no new raw.md — diff against `$PRE_A1_RAW_COUNT` vs `$POST_A1_RAW_COUNT` to decide):

```bash
POST_A15_COUNT=$(python3 -c "import json; print(len(json.load(open('papers/vector_db/abstracts_manifest.json')).get('files', {})))")
test "$POST_A15_COUNT" -ge "$PRE_A15_COUNT" \
    || { echo "abstract-indexer did not preserve/grow manifest ($PRE_A15_COUNT → $POST_A15_COUNT)"; exit 10; }
```

Advance:
```bash
python3 .../loop_state.py stage-advance --to A-2
```

**A-2 — paper-triage**

`paper-triage` emits accepted paths to **stdout** and appends a triage log entry to `research/topics/<slug>.md` (see `.claude/skills/paper-triage/SKILL.md`). There is no `papers/triage/` directory; A-3 receives the accepted list via the agent's return body.

Before dispatch, snapshot the triage-log line count:

```bash
PRE_A2_TOPIC_LINES=$(wc -l < research/topics/<slug>.md)
```

Dispatch `paper-triage` with:
- `run_in_background: true`
- `stage: papers`, `slug`, `stage_version`
- `topic_spec: research/topics/<slug>.topic.json`

After task-notification, capture the agent's return body (the accepted-paths list — pass this into A-3 via the `accepted_paths` prompt field) and confirm the triage log grew:

```bash
test $(wc -l < research/topics/<slug>.md) -gt "$PRE_A2_TOPIC_LINES" \
    || { echo "paper-triage did not append a log line"; exit 5; }
```

Advance to A-3.

**A-3 — paper-summarizer**

A-3 now runs in three phases: (1) classify accepted papers via cache_gate.py, (2) chunk the stale+miss set into batches of 5, (3) dispatch paper-summarizer sequentially with `run_in_background: true` for each batch.

```bash
# --- Phase 1: snapshot + cache classification ---
PRE_A3_SUMMARY_COUNT=$(find papers/marp-summary -name '*.md' 2>/dev/null | wc -l)
CACHE_OUT=$(mktemp --suffix=.json)

# ACCEPTED_PATHS is a bash array of absolute raw.md paths from A-2's return body.
# Build it by splitting the agent return body on newlines (one path per line).
# Guard against empty array: A-2 may legitimately return 0 accepted papers
# (tight triage threshold or narrow topic). Skip A-3 gracefully in that case.
if [ "${#ACCEPTED_PATHS[@]}" -eq 0 ]; then
  echo "[A-3] no accepted papers from A-2 — skipping summarizer dispatch"
  python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-advance --to A-4
  # (skip the rest of Phase 1/2/3; A-4 proceeds on whatever papers already exist)
  return 0 2>/dev/null || exit 0
fi

python3 /home/irteam/sw/research_hub/.claude/skills/paper-summarize/scripts/cache_gate.py \
    --paths "${ACCEPTED_PATHS[@]}" \
    --out "$CACHE_OUT"

HITS_N=$(python3 -c "import json, sys; print(len(json.load(open('$CACHE_OUT'))['hits']))")
STALE_N=$(python3 -c "import json, sys; print(len(json.load(open('$CACHE_OUT'))['stale']))")
MISS_N=$(python3 -c "import json, sys; print(len(json.load(open('$CACHE_OUT'))['misses']))")
echo "[A-3 cache] hits=$HITS_N stale=$STALE_N misses=$MISS_N"

# TO_RUN = stale + misses (absolute raw.md paths, as JSON list)
TO_RUN_JSON=$(python3 -c "
import json, sys
d = json.load(open('$CACHE_OUT'))
print(json.dumps(d['stale'] + d['misses']))
")
TO_RUN_COUNT=$(python3 -c "import json, sys; print(len(json.loads('$TO_RUN_JSON')))")

if [ "$TO_RUN_COUNT" -eq 0 ]; then
  echo "[A-3] fully cached — no dispatch needed"
else
  # --- Phase 2: chunk into B=5 batches ---
  BATCHES_JSON=$(python3 -c "
import json, sys
sys.path.insert(0, '/home/irteam/sw/research_hub/.claude/scripts')
from chunk_helper import chunk_paths
print(json.dumps(chunk_paths(json.loads('$TO_RUN_JSON'), batch_size=5)))
")
  N_BATCHES=$(python3 -c "import json; print(len(json.loads('$BATCHES_JSON')))")
  echo "[A-3] chunked $TO_RUN_COUNT papers into $N_BATCHES batches of ≤5"
fi
```

**Phase 3 — sequential dispatch (main session, one Agent call per batch):**

For each batch index `i ∈ [0, N_BATCHES)`:

1. Compute `PRE_BATCH_COUNT = find papers/marp-summary -name '*.md' | wc -l`.
2. Extract the i-th batch as a JSON list: `BATCH_I=$(python3 -c "import json; print(json.dumps(json.loads('$BATCHES_JSON')[$i]))")`.
3. Dispatch the agent:

   ```
   Agent(
     subagent_type: "paper-summarizer",
     run_in_background: true,
     prompt: {
       stage: papers,
       slug: <slug>,
       stage_version: <N>,
       batch_paths: <BATCH_I as JSON array>,
     }
   )
   ```

4. Wait for task-notification.
5. Re-classify the batch paths to verify every one now produces a fresh cached summary:
   ```bash
   VERIFY_OUT=$(mktemp --suffix=.json)
   # Extract batch paths as newline-separated list for cache_gate --paths
   BATCH_I_ARR=$(python3 -c "import json,sys; print('\n'.join(json.loads('$BATCH_I')))")
   IFS=$'\n' read -r -d '' -a _BATCH_ARR < <(printf '%s\0' "$BATCH_I_ARR")
   python3 /home/irteam/sw/research_hub/.claude/skills/paper-summarize/scripts/cache_gate.py \
       --paths "${_BATCH_ARR[@]}" \
       --out "$VERIFY_OUT"
   VERIFY_HITS=$(python3 -c "import json; print(len(json.load(open('$VERIFY_OUT'))['hits']))")
   BATCH_SIZE=$(python3 -c "import json; print(len(json.loads('$BATCH_I')))")
   ```
6. **If `VERIFY_HITS != BATCH_SIZE`**: FAIL FAST. Do not dispatch subsequent batches. Surface the stale/miss subset (from `$VERIFY_OUT`) to the user, exit 9.
7. Otherwise continue to batch `i+1`.

After all batches complete:

```bash
# Re-classify the complete TO_RUN set; every path must be a hit.
FINAL_OUT=$(mktemp --suffix=.json)
TO_RUN_ARR=$(python3 -c "import json,sys; print('\n'.join(json.loads('$TO_RUN_JSON')))")
IFS=$'\n' read -r -d '' -a _TO_RUN_ARR < <(printf '%s\0' "$TO_RUN_ARR")
python3 /home/irteam/sw/research_hub/.claude/skills/paper-summarize/scripts/cache_gate.py \
    --paths "${_TO_RUN_ARR[@]}" \
    --out "$FINAL_OUT"
FINAL_HITS=$(python3 -c "import json; print(len(json.load(open('$FINAL_OUT'))['hits']))")
if [ "$FINAL_HITS" -ne "$TO_RUN_COUNT" ]; then
  echo "A-3 aggregate verification mismatch: $FINAL_HITS/$TO_RUN_COUNT classified as cache hits"
  exit 9
fi
```

Advance to A-4:
```bash
python3 .../loop_state.py stage-advance --to A-4
```

**User-interrupt handling within A-3**: because each batch is a single `run_in_background: true` Agent call, a user mid-batch message does not cancel the batch. Between batches, if the user has intervened, dialogue first and only dispatch batch `i+1` with the user's intent.

**A-4 — rag-curator**

Before dispatch, snapshot the RAG manifest `files` dict length (this is what `.claude/hooks/session_start.sh` prints as `rag_indexed_papers`; it is NOT a field on `research/loop_state.kg.json`):

```bash
PRE_A4_COUNT=$(python3 -c "import json; print(len(json.load(open('papers/vector_db/manifest.json')).get('files', {})))")
```

Dispatch `rag-curator` with:
- `run_in_background: true`
- `stage: papers`, `slug`, `stage_version`

After task-notification, verify the manifest grew:

```bash
POST_A4_COUNT=$(python3 -c "import json; print(len(json.load(open('papers/vector_db/manifest.json')).get('files', {})))")
test "$POST_A4_COUNT" -gt "$PRE_A4_COUNT" \
    || { echo "rag-curator did not grow manifest"; exit 7; }
```

**User-interrupt handling**: If the user sends a message mid-chain, the currently-running Agent is NOT cancelled (every dispatch is `run_in_background: true`). Dialogue with the user, optionally read the in-progress artifact, and decide whether to (a) wait for the current sub-phase to finish then stop, (b) continue, or (c) abort. Do not dispatch the next sub-phase without intent.

## Step 7 — Completion

After Phase C chain completes, the main session calls `report_builder.py` directly:

```bash
python3 /home/irteam/sw/research_hub/.claude/scripts/report_builder.py \
    --payload <tmp.json>
```

The payload JSON is built in the main session by aggregating the A-1..A-4 artifact summaries. Writes `Report.md` + `Report.slides.md` under `research/reports/papers/<slug>/v<N>/`.

Then call:
```bash
python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-complete
```

`phase_advance_check.sh` (hook) blocks `stage-complete` if either Report file is missing.

Print the final message:
- Report.md + Report.slides.md absolute paths
- Success criteria ✓/✗/NA
- Artifact path list
- **No next-stage suggestion.** Stop.

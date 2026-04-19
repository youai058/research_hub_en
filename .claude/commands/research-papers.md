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

Invoke the `topic-refine` skill in main session (needs TUI). Pass `$ARGUMENTS` as `raw_input`. It writes `research/topics/.pending.topic.json` then validate:

```bash
test -f /home/irteam/sw/research_hub/research/topics/.pending.topic.json \
    || { echo "topic-refine did not emit .pending.topic.json"; exit 3; }
python3 /home/irteam/sw/research_hub/.claude/skills/topic-refine/scripts/topic_spec.py \
    validate /home/irteam/sw/research_hub/research/topics/.pending.topic.json
```

**Halting rules**: On user interrupt (Ctrl+C / "cancel") or validation fail, stop and `rm -f /home/irteam/sw/research_hub/research/topics/.pending.topic.json` before exit.

**Skip interview**: if `--slug <existing>` with pre-existing spec, or user types a trigger phrase ("proceed" / "go ahead") on the first prompt.

## Step 2 — Enter the stage (allocate v<N>)

Call `stage-enter --stage papers --topic "$ARGUMENTS"` (or `--slug <existing-slug>` if re-running). If busy-status, ask user to force-complete or abort, then clean up `.pending.topic.json`. After successful slug allocation, move it to canonical location `research/topics/<slug>.topic.json`.

## Step 3 — Phase A: dispatch paper-hunter in plan-only mode

Dispatch `paper-hunter` with `mode: plan-only`, `stage: papers`, `slug`, `stage_version`, `plan_dir`, `topic_spec`. Verify PLAN.md exists (must contain: venues, years, keywords, triage threshold, RAG reindex flag, `include_arxiv`, and prerequisite warning if empty). Do NOT self-advance.

## Step 4 — Present PLAN and wait for user

Print:
1. PLAN.md absolute path
2. 3-line summary (goal + expected artifacts + success criteria)
3. Prerequisite warning block (if any)
4. "After reviewing PLAN.md, either give feedback or reply with a trigger phrase like `proceed` or `go ahead` to continue."

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

Each bulleted block below is the payload for an `Agent(subagent_type: "<agent-name>", run_in_background: true, prompt: "...")` call (A-1 → paper-hunter, A-1.5 → abstract-indexer, A-2 → paper-triage, A-3 → paper-summarizer, A-4 → rag-curator). Throughout, `<slug>` is the value from stage-enter — substitute literally.

**A-1 — paper-hunter (execute)**

Snapshot: `python3 .claude/scripts/verify_sub_phase.py snapshot A-1 --slug <slug>` *(run before dispatch)*

Dispatch `paper-hunter` with:
- `run_in_background: true`
- `mode: execute`
- `stage: papers`, `slug`, `stage_version`, `plan_dir`
- `topic_spec: research/topics/<slug>.topic.json`

Verify: `python3 .claude/scripts/verify_sub_phase.py verify A-1 --slug <slug>` (exit 6 on fail)

Advance:
```bash
python3 .../loop_state.py stage-advance --to A-1.5
```

**A-1.5 — abstract-indexer**

Incrementally embeds every new or changed `papers/metadata/**/*.raw.md` into the ChromaDB `abstracts` collection. paper-triage (A-2) uses this collection for its dense-retrieval pre-filter. Without A-1.5, A-2 would exit 5.

Snapshot: `python3 .claude/scripts/verify_sub_phase.py snapshot A-1.5 --slug <slug>` *(run before dispatch)*

Dispatch `abstract-indexer` with:
- `run_in_background: true`
- `stage: papers`, `slug`, `stage_version`

Verify: `python3 .claude/scripts/verify_sub_phase.py verify A-1.5 --slug <slug>` (exit 10 on fail; mtime-mode on abstracts_manifest.json)

Advance:
```bash
python3 .../loop_state.py stage-advance --to A-2
```

**A-2 — paper-triage**

`paper-triage` emits accepted paths to **stdout** and appends a triage log entry to `research/topics/<slug>.md` (see `.claude/skills/paper-triage/SKILL.md`). There is no `papers/triage/` directory; A-3 receives the accepted list via the agent's return body.

Snapshot: `python3 .claude/scripts/verify_sub_phase.py snapshot A-2 --slug <slug>` *(run before dispatch)*

Dispatch `paper-triage` with:
- `run_in_background: true`
- `stage: papers`, `slug`, `stage_version`
- `topic_spec: research/topics/<slug>.topic.json`

After task-notification, capture the agent's return body (the accepted-paths list — pass this into A-3 via the `accepted_paths` prompt field).

Verify: `python3 .claude/scripts/verify_sub_phase.py verify A-2 --slug <slug>` (exit 5 on fail)

Advance to A-3.

**A-3 — paper-summarizer**

A-3 now runs in three phases: (1) classify accepted papers via cache_gate.py, (2) chunk the stale+miss set into batches of 5, (3) dispatch paper-summarizer sequentially with `run_in_background: true` for each batch.

```bash
# --- Phase 1: snapshot + cache classification ---
CACHE_OUT=$(mktemp --suffix=.json)

# Guard against empty: A-2 may return 0 accepted papers (tight triage / narrow topic).
if [ "${#ACCEPTED_PATHS[@]}" -eq 0 ]; then
  echo "[A-3] no accepted papers from A-2 — skipping dispatch"
  python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-advance --to A-4
  return 0 2>/dev/null || exit 0
fi

python3 /home/irteam/sw/research_hub/.claude/skills/paper-summarize/scripts/cache_gate.py \
    --paths "${ACCEPTED_PATHS[@]}" --out "$CACHE_OUT"
HITS_N=$(python3 -c "import json; print(len(json.load(open('$CACHE_OUT'))['hits']))")
STALE_N=$(python3 -c "import json; print(len(json.load(open('$CACHE_OUT'))['stale']))")
MISS_N=$(python3 -c "import json; print(len(json.load(open('$CACHE_OUT'))['misses']))")
echo "[A-3 cache] hits=$HITS_N stale=$STALE_N misses=$MISS_N"
TO_RUN_JSON=$(python3 -c "import json; d=json.load(open('$CACHE_OUT')); print(json.dumps(d['stale']+d['misses']))")
TO_RUN_COUNT=$(python3 -c "import json; print(len(json.loads('$TO_RUN_JSON')))")

if [ "$TO_RUN_COUNT" -eq 0 ]; then
  echo "[A-3] fully cached — no dispatch needed"
else
  BATCHES_JSON=$(python3 -c "import json,sys; sys.path.insert(0,'/home/irteam/sw/research_hub/.claude/scripts'); from chunk_helper import chunk_paths; print(json.dumps(chunk_paths(json.loads('\$TO_RUN_JSON'),batch_size=5)))")
  N_BATCHES=$(python3 -c "import json; print(len(json.loads('\$BATCHES_JSON')))")
  echo "[A-3] chunked \$TO_RUN_COUNT papers into \$N_BATCHES batches"
fi
```

**Phase 3 — sequential dispatch (main session, one Agent call per batch):**

For each batch index `i ∈ [0, N_BATCHES)`:

1. Snapshot: `python3 .claude/scripts/verify_sub_phase.py snapshot A-3 --slug <slug> --batch-i <i>` *(run before dispatch)*
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
5. Verify: `python3 .claude/scripts/verify_sub_phase.py verify A-3 --slug <slug> --batch-i <i>` (exit 9 on fail). Additionally run the existing cache_gate re-classification to confirm `VERIFY_HITS == BATCH_SIZE`; on mismatch, surface the stale subset and exit 9.
6. Otherwise continue to batch `i+1`.

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

**A-4 — rag-curator**

Snapshot: `python3 .claude/scripts/verify_sub_phase.py snapshot A-4 --slug <slug>` *(run before dispatch)*

Dispatch `rag-curator` with:
- `run_in_background: true`
- `stage: papers`, `slug`, `stage_version`

Verify: `python3 .claude/scripts/verify_sub_phase.py verify A-4 --slug <slug>` (exit 7 on fail; mtime-mode on manifest.json)

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

---
description: Enter the `papers` stage (Phase A → B → C). Collects papers, triages, summarizes, and indexes into RAG. Each stage requires explicit user approval to advance from Phase B (planning) to Phase C (execution). No autonomous bypass.
argument-hint: <topic description> [--include-arxiv]  OR  --slug <existing-slug> [--include-arxiv]
---

# /research-papers

Enter the `papers` stage. Four sub-phases run in Phase C: `A-1 paper-hunter → A-2 paper-triage → A-3 paper-summarizer → A-4 rag-curator`. Before those run, Phase A (PLAN) and Phase B (alignment) MUST happen, and Phase B REQUIRES a trigger phrase.

**Raw input**: $ARGUMENTS

## Step 1 — Preflight (advisory only, not blocking)

Check if a search topic is present. If `$ARGUMENTS` is empty and no `--slug <existing>` flag is given, ask the user for a topic before proceeding.

If `papers/rag/manifest.json` already exists with many files, still proceed — `papers` may re-run to extend the corpus.

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

## Step 3 — Phase A: delegate to orchestrator

Dispatch the `orchestrator` agent with:

- stage: `papers`
- slug: (from script output)
- stage_version: (from script output)
- plan_dir: (from script output)
- topic: $ARGUMENTS

Orchestrator MUST produce `research/plans/papers/<slug>/v<N>/PLAN.md` via the paper-hunter agent (planning-only mode — no downloads yet). It MUST include:

- venues/years/keywords/max-per-venue/triage-threshold
- expected collected count
- RAG reindex flag
- `include_arxiv: true/false` (true only if the raw `$ARGUMENTS` contained `--include-arxiv`). This flag is propagated verbatim to `hunt.py --include-arxiv` in Phase C. When false, hunt.py restricts itself to the 6-venue whitelist (NeurIPS/AAAI/ICLR/ICML/ACL/EMNLP) and drops any etc emissions.
- `⚠ Prerequisite Missing` block if `papers/rag/` is empty and this would create an unusually isolated corpus

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

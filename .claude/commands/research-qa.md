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

Parse the returned `stage_version`. If `status: "busy"`, handle same as `/research-papers`.

## Step 4 — Phase A: orchestrator dispatch

Dispatch `orchestrator` with:
- stage: `qa`
- slug: `<slug>`
- stage_version: (from script)
- question: `<question>`

Orchestrator invokes `answer-formulator` in **hybrid_query dry-run mode** — it collects candidate evidence but writes ONLY the PLAN.md. PLAN.md must cover:
- Question restatement (normalized)
- Target evidence count (3–7)
- Retrieval parameters (k, KG depth)
- 4-axis pass thresholds (Grounding≥3 AND Support≥3 AND Verifiability≥3)
- `⚠ Prerequisite Missing` if RAG is empty or slug has no prior summaries

Return with inner_phase = `A`.

## Step 5 — Present and wait for trigger

Print PLAN.md path + 3-line summary. Ask for feedback or trigger phrase.

**Hard stop.** Do not execute B-1/B-2 without a whitelisted trigger.

## Step 6 — Phase B + C

On trigger:
```bash
python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-advance --to B
python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-advance --to C --trigger "<phrase>"
```

Orchestrator runs:
- `B-1 answer-formulator` — Direct Answer (single paragraph, concrete) + Evidence Chain (3-7 items). NO divergent ideation.
- `B-2 critic` — 4-axis per-Evidence scoring. Plus codex-reviewer parallel.
- If pass count is 0 after B-2, orchestrator may loop `B-1 → B-2` up to **3 cycles total** before giving up and flagging the question as unanswerable with current corpus.

## Step 7 — Completion

Orchestrator builds the qa payload (question_restatement, direct_answer, evidence_chain, critic_scores, pass_fail_counts, codex_review, weak_points) → `report_builder.py` → Report.md + Report.slides.md.

Then `stage-complete` → idle.

Print final summary per `stage-gate.md` §4.5. **No next-stage suggestion.**

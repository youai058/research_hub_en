---
description: Enter the `analyze` stage (Phase A → B → C). Phase A dispatches results-analyst in plan-only mode; Phase C chains F-1 results-analyst → F-2 codex-reviewer then emits a Report pair. Trigger phrase required to advance from B to C. Final stage gate is codex-reviewer (F-2).
argument-hint: <slug>
---

# /research-analyze

Enter the `analyze` stage. Two sub-phases run in Phase C: `F-1 results-analyst → F-2 codex-reviewer`. Before those run, Phase A (PLAN) and Phase B (alignment) MUST happen, and Phase B REQUIRES a trigger phrase.

**Raw input**: $ARGUMENTS

## Step 1 — Parse slug

Expect `$1` = slug. If absent, ask the user. If `experiments/<slug>/results/` is missing or empty, proceed but warn that analysis will be sparse.

## Step 2 — Enter the stage

```bash
python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-enter \
    --stage analyze --slug "$1"
```

Parse the returned JSON (`slug`, `stage_version`, `plan_dir`, `report_dir`). If `status: "busy"`, the previous stage did not complete — ask the user whether to (a) `stage-complete --force` the previous one, or (b) abort. Do not pick silently.

## Step 3 — Phase A: dispatch results-analyst in plan-only mode

Dispatch the `results-analyst` agent with `run_in_background: true` and the following prompt fields:

- `mode: plan-only`
- `stage: analyze`
- `slug: <slug-from-stage-enter>`
- `stage_version: <from-stage-enter>`
- `plan_dir: research/plans/analyze/<slug>/v<N>/`
- `impl_map_path: experiments/<slug>/IMPL_MAP.md` (from prior experiments stage)
- `plan_experiments_path: research/plans/experiments/<slug>/v<N>/PLAN.md` (for Expected Under / If Wrong thresholds)
- `results_dir: experiments/<slug>/results/` (may be empty — surface `⚠ Prerequisite Missing` if so)

In `plan-only` mode the agent reads the passed experiments artifacts and writes ONLY the PLAN.md covering:

- **Verdict decision rules** (CONFIRMED / REFUTED / INCONCLUSIVE / IMPL_BUG) — uses `decide_verdict()` thresholds from the experiments IMPL_MAP
- **REFUTED 4-way sub-classification decision tree** (claim wrong → qa B-1 / impl bug → experiments E-1 / setup error → experiments C-1 / data issue → papers A-1)
- **Visualization list** (PNG + self-contained HTML inventory)
- **Revision seed format** (`{drop_evidence_ids, add_conditions, reframe_hints}`)

**No verdict classification yet, no `research/diagnoses/**` write, no PNG/HTML generation.**

Wait for the background agent to complete via task-notification. Then verify:

```bash
test -f /home/irteam/sw/research_hub/research/plans/analyze/<slug>/v<N>/PLAN.md \
    || { echo "results-analyst plan-only did not emit PLAN.md"; exit 4; }
```

The PLAN.md must include:
- Verdict decision rules + thresholds
- REFUTED 4-way classifier decision tree
- Visualization list
- Revision seed JSON schema
- `⚠ Prerequisite Missing` block if `experiments/<slug>/results/` is empty

Do NOT self-advance to Phase B or C.

## Step 4 — Present PLAN and wait for user

Print:
1. PLAN.md absolute path
2. 3-line summary (Evidence/Experiment count to judge + verdict rule preview + revision-seed schema)
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
- Otherwise, treat the message as feedback: re-dispatch `results-analyst` in `mode=plan-only` to rewrite PLAN.md in the same `v<N>/` directory, then return to Step 4.

## Step 6 — Phase C: main session dispatches F-1 then F-2

**How to read these dispatch specs**: each bulleted block below is the payload for an `Agent(subagent_type: "<agent-name>", run_in_background: true, prompt: "...")` call. Fields under the bullets become `key: value` lines inside the prompt body; `run_in_background: true` is an Agent-tool parameter (not a prompt field); `subagent_type` is implied by the sub-phase header (F-1 → `results-analyst`, F-2 → `codex-reviewer`).

> Throughout Step 6, the literal string `<slug>` in shell commands is a placeholder — substitute the actual slug value returned by `stage-enter` before executing. It is NOT a shell variable.

The main session owns the chain. For F-1 and F-2, dispatch one Agent with `run_in_background: true`, wait for task-notification, verify the expected artifact exists, then `stage-advance --to <next-subphase>` before dispatching the next.

**F-1 — results-analyst (execute)**

Dispatch `results-analyst` with:
- `run_in_background: true`
- `mode: execute`
- `stage: analyze`, `slug`, `stage_version`, `plan_dir`
- `plan_path: research/plans/analyze/<slug>/v<N>/PLAN.md`
- `impl_map_path: experiments/<slug>/IMPL_MAP.md`
- `plan_experiments_path: research/plans/experiments/<slug>/v<N>/PLAN.md`
- `results_dir: experiments/<slug>/results/`
- `codex_feedback: <REVIEW_PATH>` *(optional — populated only on retry after F-2 reject so results-analyst can read the adversarial review)*

The agent applies `decide_verdict()` per Experiment × Evidence pair, runs the 4-way REFUTED classifier where applicable, produces visualizations (PNG plus self-contained HTML), writes the revision seed, and emits `research/diagnoses/<slug>.md` + `<slug>.html` + `<slug>.kg.json`.

After task-notification, verify the core diagnosis artifacts exist (the filename is deterministic, so `test -f` is the right check — PNG count is variable because multiple plots may exist and may be embedded base64 in the HTML):

```bash
test -f /home/irteam/sw/research_hub/research/diagnoses/<slug>.md \
    || { echo "results-analyst did not emit diagnosis markdown at research/diagnoses/<slug>.md"; exit 15; }
test -f /home/irteam/sw/research_hub/research/diagnoses/<slug>.html \
    || { echo "results-analyst did not emit self-contained HTML at research/diagnoses/<slug>.html"; exit 15; }
```

Advance:
```bash
python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-advance --to F-2
```

**F-2 — codex-reviewer**

`codex-reviewer` emits `research/reviews/analyze_<slug>_codex_review.md` with a YAML frontmatter `verdict: approve|approve_with_revisions|reject` field (mandatory — see `.claude/agents/codex-reviewer.md` "Frontmatter verdict contract"). The main session parses that frontmatter to decide whether to advance to report or re-dispatch F-1.

Dispatch `codex-reviewer` with:
- `run_in_background: true`
- `phase: F-2`
- `slug`
- `target_paths: ["research/diagnoses/<slug>.md", "research/diagnoses/<slug>.html", "research/plans/analyze/<slug>/v<N>/PLAN.md"]`
- `focus: statistical_validity` (optional)

After task-notification, verify the review file exists and parse the verdict:

```bash
REVIEW_PATH=/home/irteam/sw/research_hub/research/reviews/analyze_<slug>_codex_review.md
test -f "$REVIEW_PATH" \
    || { echo "codex-reviewer did not emit a review file at $REVIEW_PATH"; exit 16; }
VERDICT=$(awk '/^---$/{c++;next} c==1 && /^verdict:/{print $2; exit}' "$REVIEW_PATH")
echo "F-2 verdict: $VERDICT"

case "$VERDICT" in
    approve|approve_with_revisions)
        # pass — advance to Step 7 (report generation). `approve_with_revisions`
        # is treated as `approve` for gating; surface the issues list to the
        # user in the final Step 7 output.
        ;;
    reject)
        # handle reject per Stop rule below (increment reject counter, re-dispatch F-1 or abort)
        :
        ;;
    *)
        # Fail closed: missing frontmatter, typo (e.g. `conditional_approve`), or
        # non-compliant output from codex-reviewer must NOT be silently treated
        # as approve. Exit 16 is reused because the review file is present-but-
        # unusable, which falls under "F-2 review-file issue".
        echo "F-2 verdict missing or unrecognized: '$VERDICT' (see $REVIEW_PATH — frontmatter may be absent)"
        exit 16
        ;;
esac
```

**Stop rule (CLAUDE.md §4.5)**: If `VERDICT == "reject"`, re-dispatch F-1 with `codex_feedback: <REVIEW_PATH>` attached so `results-analyst` can read the review issues and revise (overwriting `research/diagnoses/<slug>.md` + companions in place). Track consecutive rejects in the main session's local reasoning, not in loop_state. After a revised F-1 run, re-run F-2. If F-2 rejects a second consecutive time within the same `stage_version`, abort per CLAUDE.md §4.5 (do not call `stage-complete`) and surface the review file to the user. Any `approve` / `approve_with_revisions` verdict resets the counter and advances to Step 7. This counter is session-local and does NOT survive a session restart — on restart the counter starts at 0 again.

**User-interrupt handling**: If the user sends a message mid-chain, the currently-running Agent is NOT cancelled (every dispatch is `run_in_background: true`). Dialogue with the user, optionally read the in-progress artifact, and decide whether to (a) wait for the current sub-phase to finish then stop, (b) continue, or (c) abort. Do not dispatch the next sub-phase without intent.

## Step 7 — Completion

After Phase C chain completes (F-2 verdict approve or approve_with_revisions), the main session calls `report_builder.py` directly:

```bash
python3 /home/irteam/sw/research_hub/.claude/scripts/report_builder.py \
    --payload <tmp.json>
```

The payload JSON is built in the main session by aggregating the F-1 and F-2 artifacts. Required fields:
- `verdict_matrix` — per Experiment × Evidence verdict (CONFIRMED / REFUTED / INCONCLUSIVE / IMPL_BUG)
- `answer_status` — one of `fully supported` / `partially supported` / `needs revision` / `fully refuted`
- `refuted_classification` — 4-way sub-classification per REFUTED cell (claim wrong / impl bug / setup error / data issue)
- `visualizations` — PNG + HTML paths
- `revision_seed` — `{drop_evidence_ids, add_conditions, reframe_hints}` for the next qa iteration
- `codex_f2_verdict` — `approve | approve_with_revisions | reject` + issues list

Writes `Report.md` + `Report.slides.md` under `research/reports/analyze/<slug>/v<N>/`.

Then call:
```bash
python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-complete
```

`phase_advance_check.sh` (hook) blocks `stage-complete` if either Report file is missing.

Print the final message:
- Report.md + Report.slides.md absolute paths
- `research/diagnoses/<slug>.md` path
- Answer status (`fully supported` / `partially supported` / `needs revision` / `fully refuted`)
- Visualization paths (PNG + HTML)
- **No next-stage suggestion.** The revision seed exists in Report.md for the user to hand-carry if they choose to run `/research-qa` again.

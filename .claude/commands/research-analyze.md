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

Dispatch `results-analyst` with `run_in_background: true` and the following prompt fields:
- `mode: plan-only`
- `stage: analyze`
- `slug`, `stage_version`, `plan_dir: research/plans/analyze/<slug>/v<N>/`
- `impl_map_path: experiments/<slug>/IMPL_MAP.md`
- `plan_experiments_path: research/plans/experiments/<slug>/v<N>/PLAN.md`
- `results_dir: experiments/<slug>/results/`

Agent writes ONLY PLAN.md covering verdict decision rules (CONFIRMED / REFUTED / INCONCLUSIVE / IMPL_BUG), REFUTED 4-way classifier, visualization list, and revision seed format. **No verdict execution, no `research/diagnoses/**` write.** Wait for task-notification, then verify:

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

## Step 4 — Phase B: present PLAN and user gate

Print PLAN.md path, 3-line summary, prerequisite warning (if any), and "After reviewing PLAN.md, either give feedback or reply with a trigger phrase like `proceed` or `go ahead` to continue."

**Hard stop.** When user responds, check via `python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py trigger-check "<phrase>"`. If whitelisted, advance to C:
```bash
python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-advance --to B
python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py stage-advance --to C --trigger "<phrase>"
```
Then continue to Step 5. Otherwise treat as feedback — re-dispatch `results-analyst` in `mode=plan-only` and return here.

## Step 5 — Phase C: main session dispatches F-1 then F-2

(F-1 → results-analyst, F-2 → codex-reviewer). Throughout, `<slug>` is the value from stage-enter — substitute literally. Main session owns the chain: dispatch, wait for task-notification(s), verify artifact(s), `stage-advance --to <next-subphase>`, repeat.

**F-1 — results-analyst (execute)**

Snapshot: `python3 .claude/scripts/verify_sub_phase.py snapshot F-1 --slug <slug>` *(run before dispatch)*

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

Verify: `python3 .claude/scripts/verify_sub_phase.py verify F-1 --slug <slug>` (exit 15 on fail; checks `<slug>.md` grew and `<slug>.html` exists)

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

Snapshot: `python3 .claude/scripts/verify_sub_phase.py snapshot F-2 --slug <slug>` *(run before dispatch)*

Verify: `python3 .claude/scripts/verify_sub_phase.py verify F-2 --slug <slug>` → prints `verdict: approve|approve_with_revisions|reject` on stdout. Exit 16 on missing/malformed verdict. `approve` / `approve_with_revisions` → Step 7. `reject` → Stop-rule branch below.

**Stop rule** (CLAUDE.md §4.5): on `reject`, re-dispatch F-1 with `codex_feedback: <REVIEW_PATH>`; re-run F-2. Consecutive reject limit = 2 (session-local). On abort, do not call `stage-complete`.

## Step 6 — Completion

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

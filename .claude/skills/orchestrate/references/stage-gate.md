# Stage-Gate Protocol — Phase A / B / C (autonomous-free)

> Loaded by the `orchestrate` skill when managing any of the 4 stage commands.
> Enforces per-stage user-explicit gating. **No autonomous branch exists.**
> Every stage, every time, requires a trigger phrase to move from B → C.

---

## 1. Stage surface

| Stage | Command | Phase C sub-phases | Primary agents |
|---|---|---|---|
| `papers` | `/research-papers <topic>` | `A-1 A-2 A-3 A-4` | paper-hunter, paper-triage, paper-summarizer, rag-curator |
| `qa` | `/research-qa <slug> <question>` | `B-1 B-2` | answer-formulator, critic (+ codex-reviewer parallel) |
| `experiments` | `/research-experiments <slug>` | `E-1 E-2 E-3` (C-1 absorbed into design Phase A) | experiment-planner, code-implementer, implementation-verifier, codex-reviewer |
| `analyze` | `/research-analyze <slug>` | `F-1 F-2` | results-analyst, codex-reviewer |

Sub-phase lists are enforced by `loop_state.py:STAGE_SUBPHASES`.

---

## 2. Phase A — Planning (the stage agent writes PLAN.md and nothing else)

### 2.1 Enter

1. Command calls `python3 .claude/scripts/loop_state.py stage-enter --stage <stage> --slug <slug> [--topic <topic>]`.
2. `loop_state.py` scans `research/plans/<stage>/<slug>/v*/` + `research/reports/<stage>/<slug>/v*/` and allocates the next `v<N>/` for both plan and report dirs.
3. `loop_state.json` now holds: `{stage, inner_phase:"A", sub_phase:null, slug, stage_version}`.

### 2.2 What the stage agent does

- **Writes only** `research/plans/<stage>/<slug>/v<N>/PLAN.md`.
- Must NOT download papers, answer the question, generate code, run smoke, or render analysis visualizations.
- If a prerequisite artifact is missing (e.g., `papers/rag/manifest.json` empty before `/research-qa`, or `results_<slug>/` empty before `/research-analyze`), prepend a block:

  ```markdown
  ## ⚠ Prerequisite Missing

  - Missing: <what>
  - Effect if ignored: <quality degradation>
  - Recommendation: run `<preceding command>` first (advisory — not blocking)
  ```

### 2.3 PLAN.md common template

```markdown
# PLAN — <stage> | <slug> v<N>

## Stage & Version
stage: <stage>
slug: <slug>
stage_version: <N>
entered_at: <kst>

## Goal
<1–3 lines>

## Inputs
- <path or (missing)>
- …

## Execution Order
- [ ] sub-phase 1: <owner agent> — <what>
- [ ] sub-phase 2: …

## Parameters
- retrieval k: …
- venue filter: …
- threshold: …

## Expected Artifacts
- `<absolute path>` — type, expected size / count
- …

## Resource Bounds
- time: …
- disk: …
- gpu: …
- api cost estimate: …

## Success Criteria
- <criterion 1, verifiable>
- …

## Risks & Alternatives
- …
```

### 2.4 Exit Phase A

- Orchestrator prints:
  1. PLAN.md absolute path
  2. 3-line summary (Goal · Expected Artifacts · Success Criteria)
  3. Prerequisite warning block if any
  4. "PLAN.md 검토 후 피드백 주세요."
- Control returns to the user. **Do not self-advance.** Inner phase stays at `A`.

---

## 3. Phase B — Alignment (explicit user approval required)

### 3.1 Feedback modes

- (a) User edits PLAN.md directly (orchestrator detects via re-read on next user turn).
- (b) User sends a revision message → orchestrator delegates back to the same stage agent to rewrite PLAN.md in place (same `v<N>/`).

### 3.2 Alignment prompt

After ingesting feedback, orchestrator emits:

> `research/plans/<stage>/<slug>/v<N>/PLAN.md` 이대로 구현해도 될까요?
>
> 변경 요약: <3 bullets>
>
> Phase C 진입 트리거 예시: `구현해줘` · `proceed` · `go ahead`

### 3.3 Trigger phrase whitelist (hard gate)

The user's next utterance must match **exactly** one of:

- Korean: `구현해줘`, `실행해줘`, `진행해줘`, `ok 해`, `시작해`, `좋아 진행`, `ok 진행`
- English: `proceed`, `go ahead`, `run it`, `execute`, `ok run it`, `ok proceed`

Matching rules:
- Case-insensitive.
- Leading/trailing whitespace stripped.
- Exact match (no substring / fuzzy). Anything else is treated as feedback and routes back to Phase A.
- Validated via `loop_state.py trigger-check "<phrase>"` (exit 0 = match, 2 = not match).

### 3.4 Hard stop invariant

- There is **no autonomous branch**. `.local/feedback_autonomous.md` does not exist (deleted).
- Even the harness-engineer cannot bypass this without `--force` on `stage-advance`, which is for recovery use only (not normal flow).
- Every stage, every iteration, requires a fresh trigger phrase.

### 3.5 Advance

On valid trigger:
```bash
python3 .claude/scripts/loop_state.py stage-advance --to C --trigger "<phrase>"
```
`inner_phase` flips to `C`, `sub_phase` is initialized to the first entry of `STAGE_SUBPHASES[stage]`.

---

## 4. Phase C — Execution (sequential blocking sub-phase chain)

### 4.1 Sub-phase loop

```
for sub in STAGE_SUBPHASES[stage]:
    dispatch agent(sub)                 # blocking — wait for completion
    python3 loop_state.py stage-advance # move to next sub (or exit loop)
```

- Jumps beyond the next sub-phase require `--force` (reserved for recovery).
- Failures in a sub-phase halt the chain. Orchestrator reports the failure and stays at the current `sub_phase`. User decides whether to `stage-restart --to B` or debug in place.

### 4.2 Stage-specific chains

- `papers`: `A-1 → A-2 → A-3 → A-4`
- `qa`: `B-1 → B-2` (critic + codex-reviewer run in parallel within `B-2`; orchestrator awaits both before completing)
- `experiments`: `E-1 → E-2 → E-3`. The `experiment-report` skill runs after E-3 as part of the completion step (still inside Phase C, before `stage-complete`).
- `analyze`: `F-1 → F-2`.

### 4.3 Report pair generation

When the last sub-phase succeeds, orchestrator:
1. Builds the payload JSON matching `report_builder.py`'s schema (see `report-templates.md`).
2. Invokes `python3 .claude/scripts/report_builder.py --payload <tmp.json>`.
3. Confirms that `research/reports/<stage>/<slug>/v<N>/Report.md` **and** `Report.slides.md` exist.

### 4.4 Stage completion

```bash
python3 .claude/scripts/loop_state.py stage-complete
```
Resets to `{stage: "idle", inner_phase: null, sub_phase: null, stage_version: null}`. `slug` is preserved by default for status-reporting continuity (pass `--reset-slug` to clear).

### 4.5 Exit message (suggestion-free, per Decision #6)

Orchestrator prints exactly:
1. `Report.md` + `Report.slides.md` absolute paths
2. Success criteria check summary (✓/✗/NA per bullet)
3. Artifact path list

**Do NOT output**: "다음은 `/research-<something>` 실행하세요", "이어서 ~~ 를 추천합니다", or any auto-chain suggestion. Stage chaining is the user's decision; the orchestrator's job ends at `idle`.

---

## 5. Version discipline

- Every `stage-enter` allocates a fresh `v<N>/`. Existing `v<k>` dirs are never modified.
- `latest` symlinks in `research/plans/<stage>/<slug>/` and `research/reports/<stage>/<slug>/` track the highest `v<N>/`. Non-fatal if symlink creation fails (e.g., read-only fs).
- Same `(stage, slug)` re-run → `v<max+1>/`. Cross-stage reuse of the same `slug` is the common case (the slug is a cycle identifier, not a stage identifier).

---

## 6. Recovery paths

| Situation | Action |
|---|---|
| User wants to revise PLAN after trigger | `stage-restart --to B` (stays on same `v<N>`) |
| User wants a fresh plan | `stage-restart --to A` (stays on same `v<N>`); agent re-writes PLAN.md |
| Completely start over with new topic | `stage-complete [--reset-slug]` → new `stage-enter` call |
| Force-skip a sub-phase | `stage-advance --to <sub> --force` (reserved; log to history with reason) |
| Illegal state (corrupt JSON) | Human intervention — restore from `loop_state.v2.bak.json` or delete the file |

---

## 7. References

- State machine: `.claude/scripts/loop_state.py`
- Report templates: `.claude/skills/orchestrate/references/report-templates.md`
- Command surfaces: `.claude/commands/research-{papers,qa,experiments,analyze}.md`
- Session status hook: `.claude/hooks/session_start.sh`

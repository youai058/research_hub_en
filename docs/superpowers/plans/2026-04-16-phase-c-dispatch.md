# Phase C Dispatch Refactor Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Delete the `orchestrator` agent and `orchestrate` skill; move Phase A (PLAN.md) to specialist agents with a `mode` parameter; move Phase C sub-phase chain ownership into the four `/research-*` slash commands, which dispatch each sub-phase with `run_in_background: true`.

**Architecture:** A single TDD driver test (`.claude/tests/test_phase_c_refactor.py`) holds all invariants (orchestrator removed, 4 specialists have `mode` param, 4 commands dispatch sub-phases as separate bg Agents, docs consistent). Each implementation task flips one group of assertions from red to green and commits. Final task runs the existing harness-validate + loop_state tests + the new refactor test as one green-bar regression.

**Tech Stack:** Python 3 stdlib (pathlib, re, unittest), bash (git, rm), Claude Code prompt markdown.

---

## File Structure

**Created (new):**
- `.claude/tests/test_phase_c_refactor.py` — single-file assertion suite driving the refactor TDD-style.

**Deleted:**
- `.claude/agents/orchestrator.md`
- `.claude/skills/orchestrate/` (recursively, including `SKILL.md` and `references/`)

**Modified (content rewrite):**
- `.claude/commands/research-papers.md`
- `.claude/commands/research-qa.md`
- `.claude/commands/research-experiments.md`
- `.claude/commands/research-analyze.md`

**Modified (targeted edits — add `mode` section + remove orchestrator references):**
- `.claude/agents/paper-hunter.md`
- `.claude/agents/answer-formulator.md`
- `.claude/agents/experiment-planner.md`
- `.claude/agents/results-analyst.md`

**Modified (documentation sync):**
- `CLAUDE.md` — §4.1 (stage mapping), §4.2 (protocol), §7 (agent count 14 → 13)
- `docs/harness-layout.md` — agent list + dispatch rules
- `docs/lessons.md` — append new lesson on Phase C bg-default

**Unchanged (verified):**
- `.claude/scripts/loop_state.py` — v3 API stays; only orchestrator-specific comments (if any) removed
- `.claude/scripts/report_builder.py` — payload format unchanged
- `.claude/hooks/phase_advance_check.sh` — validation continues to work
- All 9 non-planner specialist agents (`paper-triage`, `paper-summarizer`, `rag-curator`, `critic`, `code-implementer`, `implementation-verifier`, `codex-reviewer`, `kg-curator`, `harness-engineer`)

---

## Task 1: TDD Driver — Write Refactor Assertion Suite

**Files:**
- Create: `.claude/tests/test_phase_c_refactor.py`

- [ ] **Step 1.1: Write the failing test**

Create `.claude/tests/test_phase_c_refactor.py` with the following content:

```python
#!/usr/bin/env python3
"""Refactor invariants for the Phase C dispatch refactor (2026-04-16).

Run: python3 .claude/tests/test_phase_c_refactor.py

This test intentionally fails before the refactor is applied and must pass
when every task in docs/superpowers/plans/2026-04-16-phase-c-dispatch.md is
complete.
"""
from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent  # research_hub/
AGENTS = REPO / ".claude" / "agents"
SKILLS = REPO / ".claude" / "skills"
COMMANDS = REPO / ".claude" / "commands"
DOCS = REPO / "docs"

PLANNER_AGENTS = [
    "paper-hunter.md",
    "answer-formulator.md",
    "experiment-planner.md",
    "results-analyst.md",
]

STAGE_COMMANDS = {
    "research-papers.md": ["A-1", "A-2", "A-3", "A-4"],
    "research-qa.md": ["B-1", "B-2"],
    "research-experiments.md": ["E-1", "E-2", "E-3"],
    "research-analyze.md": ["F-1", "F-2"],
}


class OrchestratorRemoved(unittest.TestCase):
    def test_orchestrator_agent_file_deleted(self):
        self.assertFalse(
            (AGENTS / "orchestrator.md").exists(),
            ".claude/agents/orchestrator.md must be deleted",
        )

    def test_orchestrate_skill_dir_deleted(self):
        self.assertFalse(
            (SKILLS / "orchestrate").exists(),
            ".claude/skills/orchestrate/ must be deleted recursively",
        )

    def test_no_orchestrator_agent_references_in_commands(self):
        # Commands must not dispatch Agent(subagent_type="orchestrator")
        pat = re.compile(r"subagent[_\s]*type\s*[:=]\s*[\"']?orchestrator", re.I)
        for name in STAGE_COMMANDS:
            text = (COMMANDS / name).read_text(encoding="utf-8")
            self.assertFalse(
                pat.search(text),
                f"{name} must not dispatch the orchestrator agent",
            )

    def test_no_orchestrator_agent_references_in_agents(self):
        # Surviving agents must not delegate to orchestrator
        pat = re.compile(r"subagent[_\s]*type\s*[:=]\s*[\"']?orchestrator", re.I)
        for md in AGENTS.glob("*.md"):
            self.assertFalse(
                pat.search(md.read_text(encoding="utf-8")),
                f"{md.name} must not reference the orchestrator agent",
            )


class PlannerAgentsHaveModeParam(unittest.TestCase):
    """Each of the four planner agents must declare a `mode` parameter."""

    def test_mode_section_present(self):
        for name in PLANNER_AGENTS:
            text = (AGENTS / name).read_text(encoding="utf-8")
            self.assertRegex(
                text,
                r"##\s*Mode\b",
                f"{name} must contain a '## Mode' section",
            )
            self.assertIn(
                "plan-only", text,
                f"{name} must document mode=plan-only",
            )
            self.assertIn(
                "execute", text,
                f"{name} must document mode=execute",
            )


class CommandsDispatchSubphasesAsBackgroundAgents(unittest.TestCase):
    """Each /research-* command owns the Phase C chain and dispatches
    every sub-phase as a separate Agent(..., run_in_background=true)."""

    def test_each_command_mentions_every_subphase(self):
        for name, subphases in STAGE_COMMANDS.items():
            text = (COMMANDS / name).read_text(encoding="utf-8")
            for sp in subphases:
                self.assertIn(
                    sp, text,
                    f"{name} must name sub-phase {sp} explicitly",
                )

    def test_each_command_requires_run_in_background(self):
        for name in STAGE_COMMANDS:
            text = (COMMANDS / name).read_text(encoding="utf-8")
            self.assertIn(
                "run_in_background", text,
                f"{name} must dispatch sub-phase Agents with run_in_background",
            )
            # The refactor mandates bg=true by default for every sub-phase;
            # the literal token "true" must appear near the flag.
            self.assertRegex(
                text,
                r"run_in_background[^\n]{0,40}true",
                f"{name} must set run_in_background: true on sub-phase dispatch",
            )

    def test_papers_still_has_topic_refine_step(self):
        text = (COMMANDS / "research-papers.md").read_text(encoding="utf-8")
        self.assertIn(
            "topic-refine", text,
            "research-papers.md must keep the topic-refine skill step",
        )


class DocsAgentCountConsistent(unittest.TestCase):
    def test_claude_md_says_13_agents(self):
        text = (REPO / "CLAUDE.md").read_text(encoding="utf-8")
        self.assertRegex(
            text,
            r"13\s*에이전트",
            "CLAUDE.md §7 must say '13 에이전트' after orchestrator removal",
        )
        self.assertNotIn(
            "14 에이전트", text,
            "CLAUDE.md must no longer say '14 에이전트'",
        )

    def test_harness_layout_has_13_agents(self):
        text = (DOCS / "harness-layout.md").read_text(encoding="utf-8")
        self.assertNotIn(
            "14 에이전트", text,
            "docs/harness-layout.md must no longer claim 14 agents",
        )
        self.assertNotRegex(
            text,
            r"(?mi)^\s*[\|\-]?\s*orchestrator\b",
            "docs/harness-layout.md must not list the orchestrator agent",
        )

    def test_lesson_appended(self):
        text = (DOCS / "lessons.md").read_text(encoding="utf-8")
        self.assertIn(
            "Phase C subagent dispatch", text,
            "docs/lessons.md must record the new bg-default lesson",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
```

- [ ] **Step 1.2: Run the test suite and confirm everything fails**

Run: `python3 .claude/tests/test_phase_c_refactor.py`
Expected: Multiple failures across all four test classes (orchestrator.md still exists, mode section missing, commands still say "dispatch orchestrator", docs still say "14 에이전트"). Exit code non-zero.

- [ ] **Step 1.3: Commit the failing test**

```bash
git add .claude/tests/test_phase_c_refactor.py
git commit -m "test: add Phase C dispatch refactor invariants (TDD driver, all red)

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 2: Add `mode` parameter to `paper-hunter` agent

**Files:**
- Modify: `.claude/agents/paper-hunter.md` (insert new `## Mode` section after the `## 핵심 역할` section, before `## 작업 원칙`)

- [ ] **Step 2.1: Read current structure**

Read `.claude/agents/paper-hunter.md` and locate the end of the `## 핵심 역할` section and the start of `## 작업 원칙`. The new `## Mode` section goes between them.

- [ ] **Step 2.2: Insert the Mode section**

Immediately before `## 작업 원칙`, insert:

```markdown
## Mode

Dispatchers (slash commands) pass `mode` in the Agent prompt. Two values:

- **`mode=plan-only`** (Phase A): Write `research/plans/papers/<slug>/v<N>/PLAN.md` and return. **No side effects** — do not invoke `hunt.py`, do not download PDFs, do not touch `papers/metadata/**`, do not update `papers/vector_db/manifest.json`. The PLAN.md must include venues, years, keyword groups (3-variant expansion), `max-per-venue-year`, triage threshold, and `include_arxiv: true/false`.
- **`mode=execute`** (Phase C sub-phase A-1): Read the PLAN.md at `research/plans/papers/<slug>/v<N>/PLAN.md` and run the full `hunt.py` flow to produce `papers/metadata/<Venue>/<Year>/<slug>.raw.md` (+ `etc/<Year>/` if `--include-arxiv`). Update `manifest.json`. Do not rewrite PLAN.md.

If the calling prompt omits `mode`, abort and return an error — every dispatch must be explicit.
```

- [ ] **Step 2.3: Run the refactor test and confirm paper-hunter passes**

Run: `python3 .claude/tests/test_phase_c_refactor.py PlannerAgentsHaveModeParam -v`
Expected: Three sub-assertions for `paper-hunter.md` pass (Mode section, `plan-only`, `execute`). The other three planner agents still fail.

- [ ] **Step 2.4: Commit**

```bash
git add .claude/agents/paper-hunter.md
git commit -m "feat(paper-hunter): add mode=plan-only|execute parameter

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 3: Add `mode` parameter to `answer-formulator` agent

**Files:**
- Modify: `.claude/agents/answer-formulator.md` (insert `## Mode` before `## 작업 원칙`)

- [ ] **Step 3.1: Insert the Mode section**

Immediately before `## 작업 원칙` in `.claude/agents/answer-formulator.md`, insert:

```markdown
## Mode

Dispatchers pass `mode` in the Agent prompt. Two values:

- **`mode=plan-only`** (Phase A): Write `research/plans/qa/<slug>/v<N>/PLAN.md` describing the hybrid_query dry-run (what indices to query, expected Evidence count, open sub-questions to probe) and return. **No answer body.** Do not write to `research/answers/**`, do not emit KG nodes, do not finalize an Evidence Chain.
- **`mode=execute`** (Phase C sub-phase B-1): Read the PLAN.md at `research/plans/qa/<slug>/v<N>/PLAN.md` and produce the Direct Answer + Evidence Chain (3–7 items) + Open Sub-Questions. Save to `research/answers/YYYY-MM-DD_<slug>.md`. Emit `answer:` / `evidence:` KG nodes.

If the calling prompt omits `mode`, abort and return an error.
```

- [ ] **Step 3.2: Run test and commit**

Run: `python3 .claude/tests/test_phase_c_refactor.py PlannerAgentsHaveModeParam -v`
Expected: `paper-hunter` + `answer-formulator` pass; `experiment-planner` + `results-analyst` still fail.

```bash
git add .claude/agents/answer-formulator.md
git commit -m "feat(answer-formulator): add mode=plan-only|execute parameter

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 4: Add `mode` parameter to `experiment-planner` agent

**Files:**
- Modify: `.claude/agents/experiment-planner.md` (insert `## Mode` before `## 작업 원칙`)

- [ ] **Step 4.1: Insert the Mode section**

Immediately before `## 작업 원칙` (or the first `##` subsection after the intro) in `.claude/agents/experiment-planner.md`, insert:

```markdown
## Mode

Dispatchers pass `mode` in the Agent prompt. Two values:

- **`mode=plan-only`** (Phase A): Write `research/plans/experiments/<slug>/v<N>/PLAN.md` with one cell per Evidence (1:1 mapping), IV / DV / baseline / ablation, and numeric **Expected Under (evidence true)** / **If Wrong (refutation)** ranges. **Do not implement code**, do not touch `experiments/<slug>/code/`, do not write IMPL_MAP.md. Flag weak Evidence first.
- **`mode=execute`**: Not used. `experiment-planner` is a Phase A planner only. The Phase C chain (E-1 code-implementer → E-2 implementation-verifier → E-3 codex-reviewer) is owned by other agents. If invoked with `mode=execute`, abort with an error instructing the caller to dispatch `code-implementer` instead.

If the calling prompt omits `mode`, abort and return an error.
```

- [ ] **Step 4.2: Run test and commit**

Run: `python3 .claude/tests/test_phase_c_refactor.py PlannerAgentsHaveModeParam -v`
Expected: Three planners pass; `results-analyst` still fails.

```bash
git add .claude/agents/experiment-planner.md
git commit -m "feat(experiment-planner): add mode=plan-only|execute parameter

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 5: Add `mode` parameter to `results-analyst` agent

**Files:**
- Modify: `.claude/agents/results-analyst.md` (insert `## Mode` before `## 작업 원칙`)

- [ ] **Step 5.1: Insert the Mode section**

Immediately before `## 작업 원칙` in `.claude/agents/results-analyst.md`, insert:

```markdown
## Mode

Dispatchers pass `mode` in the Agent prompt. Two values:

- **`mode=plan-only`** (Phase A): Write `research/plans/analyze/<slug>/v<N>/PLAN.md` describing the verdict rules (CONFIRMED / REFUTED / INCONCLUSIVE / IMPL_BUG bounds), REFUTED 4-way failure-classification decision tree, and the revision-seed format that will feed the next `answer-formulator` iteration. **No analysis of experimental results yet** — do not read `experiments/<slug>/results/**`, do not write `research/diagnoses/**`, do not generate PNG/HTML.
- **`mode=execute`** (Phase C sub-phase F-1): Read the PLAN.md and analyze each Experiment × Evidence pair. Assign verdicts, run the 4-way REFUTED classifier when applicable, produce `research/diagnoses/<slug>.md` + accompanying PNG + self-contained HTML. Emit revision seed JSON for the next answer-formulator cycle.

If the calling prompt omits `mode`, abort and return an error.
```

- [ ] **Step 5.2: Run test and confirm all planner assertions pass**

Run: `python3 .claude/tests/test_phase_c_refactor.py PlannerAgentsHaveModeParam -v`
Expected: All four planner agents pass. The other three test classes still have failures.

- [ ] **Step 5.3: Commit**

```bash
git add .claude/agents/results-analyst.md
git commit -m "feat(results-analyst): add mode=plan-only|execute parameter

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 6: Rewrite `/research-papers` command to own the Phase C chain

**Files:**
- Modify: `.claude/commands/research-papers.md` (full rewrite of Steps 3 through 6)

- [ ] **Step 6.1: Rewrite Step 3 (Phase A)**

Replace the current `## Step 3 — Phase A: delegate to orchestrator` section with:

```markdown
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
```

- [ ] **Step 6.2: Rewrite Step 5 (Phase B+C)**

Replace the current `## Step 5 — Phase B + C (after trigger)` section with:

```markdown
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

**How to read these dispatch specs**: each bulleted block below is the payload for an `Agent(subagent_type: "<agent-name>", run_in_background: true, prompt: "...")` call. Fields under the bullets become `key: value` lines inside the prompt body; `run_in_background: true` is an Agent-tool parameter (not a prompt field); `subagent_type` is implied by the sub-phase header (A-1 → `paper-hunter`, A-2 → `paper-triage`, A-3 → `paper-summarizer`, A-4 → `rag-curator`).

The main session owns the chain. For each of A-1, A-2, A-3, A-4, dispatch one Agent with `run_in_background: true`, wait for task-notification, verify the expected artifact exists, then `stage-advance --to <next-subphase>` before dispatching the next.

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

Before dispatch, snapshot the current Marp summary file count:

```bash
PRE_A3_SUMMARY_COUNT=$(find papers/marp-summary -name '*.md' 2>/dev/null | wc -l)
```

Dispatch `paper-summarizer` with:
- `run_in_background: true`
- `stage: papers`, `slug`, `stage_version`
- `accepted_paths: <return body from A-2>` (the filtered subset)

After task-notification, verify that new summary files exist:

```bash
POST_A3_SUMMARY_COUNT=$(find papers/marp-summary -name '*.md' 2>/dev/null | wc -l)
test "$POST_A3_SUMMARY_COUNT" -gt "$PRE_A3_SUMMARY_COUNT" \
    || { echo "paper-summarizer did not emit any new summaries"; exit 8; }
```

Advance to A-4.

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
```

- [ ] **Step 6.3: Rewrite Step 6 (Completion) — renumber to Step 7**

Rename the current `## Step 6 — Completion` to `## Step 7 — Completion` and replace its body with:

```markdown
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
```

- [ ] **Step 6.4: Run test for research-papers**

Run: `python3 .claude/tests/test_phase_c_refactor.py CommandsDispatchSubphasesAsBackgroundAgents.test_each_command_requires_run_in_background -v`
Expected: `research-papers.md` assertion passes; other three commands still fail.

Also run:
```bash
python3 .claude/tests/test_phase_c_refactor.py OrchestratorRemoved.test_no_orchestrator_agent_references_in_commands -v
```
Expected: `research-papers.md` no longer references orchestrator.

- [ ] **Step 6.5: Commit**

```bash
git add .claude/commands/research-papers.md
git commit -m "refactor(research-papers): main session owns Phase C chain, bg=true dispatch

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 7: Rewrite `/research-qa` command

**Files:**
- Modify: `.claude/commands/research-qa.md`

- [ ] **Step 7.1: Read current command**

Read `.claude/commands/research-qa.md` to identify the sections that currently delegate to orchestrator. Structure will be: preflight → stage-enter → Phase A → Phase B gate → Phase C (B-1 → B-2) → report.

- [ ] **Step 7.2: Rewrite Phase A step**

Replace the orchestrator dispatch in Phase A with:

```markdown
Dispatch the `answer-formulator` agent with `run_in_background: true` and `mode: plan-only` to produce `research/plans/qa/<slug>/v<N>/PLAN.md` (hybrid_query dry-run, Evidence count estimate, no answer body). After task-notification, verify the PLAN.md exists.
```

- [ ] **Step 7.3: Rewrite Phase B+C step**

Replace the orchestrator-dispatched Phase C with a main-session chain:

```markdown
## Step 5 — Phase B: trigger gate (unchanged)

## Step 6 — Phase C: main session dispatches B-1 then B-2

**B-1 — answer-formulator (execute)**

Dispatch `answer-formulator` with `run_in_background: true`, `mode: execute`, slug/stage_version/plan_dir. After task-notification, verify `research/answers/*_<slug>.md` exists. Advance to B-2.

**B-2 — critic + codex-reviewer (parallel)**

Dispatch `critic` AND `codex-reviewer` in the same main-session message, both `run_in_background: true`. Wait for both task-notifications. Verify `research/critiques/<slug>.md` and the codex review JSON both exist.

Apply the stop rule from CLAUDE.md §4.5: if 3 consecutive cycles pass 0 Evidence, abort. Otherwise proceed to report generation.

**User-interrupt handling**: bg Agents do NOT cancel on user message. Dialogue, then decide continue / pause / abort.
```

- [ ] **Step 7.4: Rewrite completion step**

Replace orchestrator-owned `report_builder.py` call with a main-session call, identical in shape to Task 6 Step 6.3 but for the `qa` stage paths.

- [ ] **Step 7.5: Run test**

Run: `python3 .claude/tests/test_phase_c_refactor.py CommandsDispatchSubphasesAsBackgroundAgents -v`
Expected: `research-papers.md` + `research-qa.md` pass; `research-experiments.md` + `research-analyze.md` still fail.

- [ ] **Step 7.6: Commit**

```bash
git add .claude/commands/research-qa.md
git commit -m "refactor(research-qa): main session owns B-1/B-2, bg=true dispatch

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 8: Rewrite `/research-experiments` command

**Files:**
- Modify: `.claude/commands/research-experiments.md`

- [ ] **Step 8.1: Rewrite Phase A step**

Replace orchestrator dispatch with:

```markdown
Dispatch the `experiment-planner` agent with `run_in_background: true` and `mode: plan-only` to produce `research/plans/experiments/<slug>/v<N>/PLAN.md` (one cell per Evidence, IV/DV/baseline/ablation, Expected Under / If Wrong numeric ranges). After task-notification, verify the PLAN.md exists and contains at least one Evidence cell.
```

- [ ] **Step 8.2: Rewrite Phase B+C step**

Replace orchestrator-owned Phase C with a main-session chain:

```markdown
## Step 6 — Phase C: main session dispatches E-1 → E-2 → E-3 sequentially

**E-1 — code-implementer**

Dispatch `code-implementer` with `run_in_background: true`, slug/stage_version/plan_dir, and the Evidence list from PLAN.md. After task-notification, verify `experiments/<slug>/code/` contains at least one module and `experiments/<slug>/IMPL_MAP.md` exists. Advance to E-2.

**E-2 — implementation-verifier**

Dispatch `implementation-verifier` with `run_in_background: true`. After task-notification, inspect the verdict file. If `status == fail`, increment the E-2 fail counter; on the second consecutive fail, abort per CLAUDE.md §4.5. Otherwise advance to E-3.

**E-3 — codex-reviewer (final gate)**

Dispatch `codex-reviewer` with `run_in_background: true`. After task-notification, parse the verdict. On `reject`, re-dispatch E-1 with the review feedback attached; on the second reject, abort per CLAUDE.md §4.5. On `accept`, advance to report generation.

**User-interrupt handling**: as in other stages — bg Agents do not cancel on user message.
```

- [ ] **Step 8.3: Rewrite completion step (main-session report_builder call)**

Same shape as Tasks 6–7, but for `experiments` stage paths.

- [ ] **Step 8.4: Run test and commit**

Run: `python3 .claude/tests/test_phase_c_refactor.py CommandsDispatchSubphasesAsBackgroundAgents -v`
Expected: Three commands pass; only `research-analyze.md` still fails.

```bash
git add .claude/commands/research-experiments.md
git commit -m "refactor(research-experiments): main session owns E-1/E-2/E-3 chain

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 9: Rewrite `/research-analyze` command

**Files:**
- Modify: `.claude/commands/research-analyze.md`

- [ ] **Step 9.1: Rewrite Phase A step**

Replace orchestrator dispatch with:

```markdown
Dispatch the `results-analyst` agent with `run_in_background: true` and `mode: plan-only` to produce `research/plans/analyze/<slug>/v<N>/PLAN.md` (verdict rules, REFUTED 4-way classifier decision tree, revision-seed format). After task-notification, verify the PLAN.md exists.
```

- [ ] **Step 9.2: Rewrite Phase B+C step**

Replace orchestrator-owned Phase C with:

```markdown
## Step 6 — Phase C: main session dispatches F-1 → F-2 sequentially

**F-1 — results-analyst (execute)**

Dispatch `results-analyst` with `run_in_background: true`, `mode: execute`. After task-notification, verify `research/diagnoses/<slug>.md` exists along with the PNG/HTML companions. Advance to F-2.

**F-2 — codex-reviewer (final gate)**

Dispatch `codex-reviewer` with `run_in_background: true`. Parse verdict on task-notification. On `reject`, re-dispatch F-1; on second reject, abort per CLAUDE.md §4.5. On `accept`, advance to report generation.

**User-interrupt handling**: bg Agents do not cancel on user message.
```

- [ ] **Step 9.3: Rewrite completion step (main-session report_builder call)**

Same shape as Tasks 6–8, for `analyze` stage paths.

- [ ] **Step 9.4: Run test**

Run: `python3 .claude/tests/test_phase_c_refactor.py CommandsDispatchSubphasesAsBackgroundAgents -v`
Expected: All four commands pass.

Also run:
```bash
python3 .claude/tests/test_phase_c_refactor.py OrchestratorRemoved.test_no_orchestrator_agent_references_in_commands -v
```
Expected: pass for all four commands (orchestrator no longer referenced anywhere in `.claude/commands/`).

- [ ] **Step 9.5: Commit**

```bash
git add .claude/commands/research-analyze.md
git commit -m "refactor(research-analyze): main session owns F-1/F-2 chain

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 10: Delete `orchestrator` agent

**Files:**
- Delete: `.claude/agents/orchestrator.md`

- [ ] **Step 10.1: Sanity-check no remaining references in agents**

Run:
```bash
python3 .claude/tests/test_phase_c_refactor.py OrchestratorRemoved.test_no_orchestrator_agent_references_in_agents -v
```
Expected: pass (no other agent delegates to orchestrator). If it fails, fix the offending agent file before deleting orchestrator.md.

- [ ] **Step 10.2: Delete the file**

```bash
rm /home/irteam/sw/research_hub/.claude/agents/orchestrator.md
```

- [ ] **Step 10.3: Verify**

Run: `python3 .claude/tests/test_phase_c_refactor.py OrchestratorRemoved.test_orchestrator_agent_file_deleted -v`
Expected: pass.

- [ ] **Step 10.4: Commit**

```bash
git add -A .claude/agents/
git commit -m "refactor: delete orchestrator agent (role absorbed into stage commands)

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 11: Delete `orchestrate` skill directory

**Files:**
- Delete: `.claude/skills/orchestrate/` (entire directory including `SKILL.md` and `references/`)

- [ ] **Step 11.1: Confirm dir contents**

```bash
ls /home/irteam/sw/research_hub/.claude/skills/orchestrate/
```
Expected output: `SKILL.md  references`. If anything else is present, inspect before deleting.

- [ ] **Step 11.2: Delete recursively**

```bash
rm -rf /home/irteam/sw/research_hub/.claude/skills/orchestrate/
```

- [ ] **Step 11.3: Verify**

Run: `python3 .claude/tests/test_phase_c_refactor.py OrchestratorRemoved.test_orchestrate_skill_dir_deleted -v`
Expected: pass.

- [ ] **Step 11.4: Commit**

```bash
git add -A .claude/skills/
git commit -m "refactor: delete orchestrate skill (workflow moved into stage commands)

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 12: Update `CLAUDE.md` (agent count + protocol)

**Files:**
- Modify: `/home/irteam/sw/research_hub/CLAUDE.md`

- [ ] **Step 12.1: Update §4.1 table**

In `CLAUDE.md` §4.1 (Stage × Phase 매핑 table), change the Phase A column from "orchestrator가 paper-hunter를 호출" phrasing to "paper-hunter (mode=plan-only)가 직접 PLAN.md를 작성". Do the same for qa / experiments / analyze rows, referencing `answer-formulator` / `experiment-planner` / `results-analyst` respectively with `mode=plan-only`.

Change the Phase C column description so it no longer mentions orchestrator — use wording like "메인 세션이 sub-phase별 Agent(run_in_background=true)를 순차 dispatch".

- [ ] **Step 12.2: Update §4.2 protocol**

In `CLAUDE.md` §4.2 (Phase A/B/C 프로토콜 공통), rewrite the Phase C paragraph to:

> **Phase C**: 메인 세션이 `STAGE_SUBPHASES` 체인을 순차 blocking dispatch한다. 각 sub-phase는 `Agent(..., run_in_background=true)`로 보내고 task-notification을 받아 artifact 검증 후 다음 sub-phase를 dispatch한다. 마지막 sub-phase 종료 후 메인 세션이 직접 `report_builder.py`를 호출해 Report 쌍을 만들고 `loop_state.py stage-complete`로 `idle` 복귀한다. **다음 stage 권장 문구 출력 금지** (Decision #6).

- [ ] **Step 12.3: Update §7 agent count**

Change the §7 sentence from "14 에이전트 (연구 루프 12 + codex-reviewer + harness-engineer)" to "13 에이전트 (연구 루프 11 + codex-reviewer + harness-engineer)".

- [ ] **Step 12.4: Run test**

Run: `python3 .claude/tests/test_phase_c_refactor.py DocsAgentCountConsistent.test_claude_md_says_13_agents -v`
Expected: pass.

- [ ] **Step 12.5: Commit**

```bash
git add CLAUDE.md
git commit -m "docs(CLAUDE): sync §4.1/§4.2/§7 with orchestrator removal (14→13 agents)

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 13: Update `docs/harness-layout.md`

**Files:**
- Modify: `/home/irteam/sw/research_hub/docs/harness-layout.md`

- [ ] **Step 13.1: Find and remove orchestrator row**

Open the agent table in `docs/harness-layout.md` and delete the row listing `orchestrator`.

- [ ] **Step 13.2: Update the total count**

If any sentence says "총 14 에이전트" or "14 agents", change to "13".

- [ ] **Step 13.3: Add dispatch rules section**

Near the end of the file (or in an appropriate "Dispatch rules" section if it exists), append:

```markdown
## Dispatch rules (2026-04-16 refactor)

- Phase A PLAN.md writers are the four specialist planners (`paper-hunter`, `answer-formulator`, `experiment-planner`, `results-analyst`) dispatched by the stage slash command with `mode=plan-only` and `run_in_background: true`.
- Phase C sub-phases are owned by the stage slash command, which dispatches each sub-phase as a separate `Agent(..., run_in_background=true)` call and verifies the artifact between dispatches.
- The only main-session (foreground) step is the `topic-refine` skill in `/research-papers`, which is interactive by nature.
- No agent delegates to another agent. Orchestration is a main-session responsibility.
```

- [ ] **Step 13.4: Run test**

Run: `python3 .claude/tests/test_phase_c_refactor.py DocsAgentCountConsistent.test_harness_layout_has_13_agents -v`
Expected: pass.

- [ ] **Step 13.5: Commit**

```bash
git add docs/harness-layout.md
git commit -m "docs(harness-layout): drop orchestrator row, add dispatch-rules section

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 14: Append lesson to `docs/lessons.md`

**Files:**
- Modify: `/home/irteam/sw/research_hub/docs/lessons.md`

- [ ] **Step 14.1: Append new lesson at the end of the file**

```markdown

## 2026-04-16 — Phase C subagent dispatch is `run_in_background: true` by harness default

- **Rule**: Every Phase C sub-phase dispatch (A-1..A-4, B-1, B-2, E-1..E-3, F-1, F-2) is a separate `Agent(..., run_in_background=true)` call owned by the stage slash command in the main session. The only main-session-foreground step is the `topic-refine` skill in `/research-papers` (interactive). The `orchestrator` agent and `orchestrate` skill are deleted; Phase A planning is done by the four specialist planners (`paper-hunter`, `answer-formulator`, `experiment-planner`, `results-analyst`) with a new `mode=plan-only` parameter.
- **Why**: Foreground `Agent(...)` dispatches get auto-cancelled when the user sends a message while the agent is running. The pre-refactor pattern (orchestrator = one-big-call that internally ran the whole Phase C chain) made Phase C a single opaque 30+ minute foreground call: the main session had no way to react to user input, no way to surface sub-phase boundaries, and every user message cancelled the whole chain. Moving chain ownership into the stage slash command + mandating `bg=true` makes sub-phase boundaries addressable, keeps bg agents immune to user messages, and lets the main session dialogue with the user mid-flight without losing work.
- **When to apply**: When writing or editing any `.claude/commands/research-*.md`, every `Agent(...)` dispatch for a Phase A or Phase C sub-phase MUST pass `run_in_background: true` and must be a separate call (no nesting, no one-big-call). Verify with `.claude/tests/test_phase_c_refactor.py`. New specialist planner agents (if added) MUST declare a `## Mode` section with `plan-only` and `execute` semantics. Never delegate orchestration to a subagent.
```

- [ ] **Step 14.2: Run test**

Run: `python3 .claude/tests/test_phase_c_refactor.py DocsAgentCountConsistent.test_lesson_appended -v`
Expected: pass.

- [ ] **Step 14.3: Commit**

```bash
git add docs/lessons.md
git commit -m "docs(lessons): add Phase C bg-default rule (2026-04-16 refactor)

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Task 15: Green-bar regression

**Files:** none modified (test execution only)

- [ ] **Step 15.1: Full refactor test suite**

Run: `python3 .claude/tests/test_phase_c_refactor.py -v`
Expected: All test classes pass. Exit code 0.

- [ ] **Step 15.2: Loop state regression**

Run: `python3 .claude/tests/test_loop_state.py`
Expected: pass. The refactor must not break v3 schema or STAGE_SUBPHASES.

- [ ] **Step 15.3: Topic spec regression**

Run: `python3 .claude/tests/test_topic_spec.py`
Expected: pass.

- [ ] **Step 15.4: Harness validate**

Run: `bash .claude/scripts/harness-validate.sh`
Expected: pass. Confirms all agent frontmatter / skill SKILL.md / hook permissions / settings.json schema are intact after agent + skill deletions.

If the script does not exist at that path, locate it with `find .claude -name "harness-validate*"` and run whatever the harness uses for validation.

- [ ] **Step 15.5: Paused-slug resume sanity check**

The currently paused slug `2026-04-16_discrete-diffusion-llm-vs-ar-lm-comparison` must remain resumable. Read `research/loop_state.json` and confirm:
- `stage: "papers"`
- `inner_phase: "C"`
- `sub_phase: "A-3"`
- `slug: "2026-04-16_discrete-diffusion-llm-vs-ar-lm-comparison"`

These fields are owned by `loop_state.py` which is unchanged, so this should be a no-op check. If any field was accidentally mutated during the refactor, halt and investigate before proceeding.

- [ ] **Step 15.6: Final commit (if any trailing edits)**

If Steps 15.1–15.5 required any fixes, stage and commit. Otherwise skip.

```bash
git status
# If anything is modified:
git add -A
git commit -m "refactor: green-bar fixes from final regression (if applicable)

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
```

---

## Completion criteria

When every task above is complete:

1. `python3 .claude/tests/test_phase_c_refactor.py` — all green.
2. `python3 .claude/tests/test_loop_state.py` — all green.
3. `python3 .claude/tests/test_topic_spec.py` — all green.
4. `rg -l "orchestrator" .claude/ CLAUDE.md docs/` — returns only `docs/superpowers/specs/2026-04-16-phase-c-dispatch-design.md`, `docs/superpowers/plans/2026-04-16-phase-c-dispatch.md`, and `docs/lessons.md` (historical record only).
5. The paused slug can be resumed by re-invoking `/research-papers --slug 2026-04-16_discrete-diffusion-llm-vs-ar-lm-comparison`, which now uses the new main-session-owned chain with `bg=true` dispatches.
6. Separately (not part of this plan): resume A-3 paper-summarizer digest batch — 30 remaining papers. Only after user direction.

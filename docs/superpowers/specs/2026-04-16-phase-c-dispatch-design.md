# Phase C Dispatch Refactor: Main-Session Subagent Chain with Background-Default

**Date**: 2026-04-16
**Status**: Approved (pending implementation plan)

## Problem

During Phase C execution of `/research-papers` (sub-phase A-3 paper-summarizer digest batch), the user observed Agent tool calls being repeatedly rejected / cancelled. Transcript analysis showed 4 foreground `Agent(...)` dispatches that were auto-cancelled when the user sent a message while the agent was running. Mitigating with `run_in_background: true` restored progress, but that was a tactical patch — the structural cause was not addressed.

Five-layer root cause:

| Layer | Cause |
|---|---|
| L1 CLI contract | Foreground tool calls cancel when a new user message arrives. This is runtime design, not a bug. |
| L2 Agent default | `Agent(...)` without `run_in_background=true` defaults to foreground — the default is user-hostile for long-running sub-phases. |
| L3 Visibility | Main session had no durable record that "an agent is mid-flight"; any user message appeared to have nothing to interrupt. |
| L4 One-big-call | The `orchestrator` agent was dispatched once and then internally ran the full Phase C chain. From the main session's view, Phase C was a single opaque foreground call spanning 30+ minutes. |
| L5 Harness gap | No rule in `CLAUDE.md` or any skill mandated `run_in_background=true` for sub-phase dispatches. The topic-refine skill (interactive) is the only natural foreground case, but it was not distinguished from execute-phase dispatches. |

A tactical fix ("always pass `bg=True`") addresses L1/L2 only. L4 is the structural amplifier: even with `bg=True`, a single long-running orchestrator call hides sub-phase boundaries and prevents the main session from reacting to user input between sub-phases.

## Goal

Restructure Phase C execution so that:

1. The **main session owns the sub-phase chain** — it dispatches each of the 4 (papers), 2 (qa), 3 (experiments), or 2 (analyze) sub-phases as a separate `Agent(...)` call.
2. Every Phase C Agent dispatch uses `run_in_background: true` by harness rule.
3. Between sub-phases, the main session can receive user messages, inspect artifacts, and decide whether to dispatch the next sub-phase.
4. The `orchestrator` agent and `orchestrate` skill are removed — their Phase A role moves to specialist agents (mode=plan-only), and their Phase C role moves to the main session.

Non-goals: change loop_state.json schema, change `report_builder.py` output format, refactor specialist agents beyond adding a `mode` parameter, touch LLDM codebase.

## Section 1 — Architecture Overview

Flow for `/research-papers` (the other 3 stage commands follow the same pattern, minus topic-refine):

```
Step 1  Preflight (advisory only)                           [main session]
Step 2  Skill(topic-refine)                                 [main session, INTERACTIVE]
          └─ writes research/topics/.pending.topic.json
Step 3  Bash(loop_state.py stage-enter)                     [main session]
          └─ renames .pending → <slug>.topic.json
Step 4  Phase A: Agent(paper-hunter, bg=true,               [main session → subagent]
          mode=plan-only)
          └─ writes research/plans/papers/<slug>/v<N>/PLAN.md
Step 5  Phase B (user review + trigger whitelist)           [main session]
Step 6  Phase C chain — each sub-phase a separate dispatch: [main session → 4× subagent]
          Agent(paper-hunter,     bg=true, mode=execute)  A-1
          Agent(paper-triage,     bg=true)                A-2
          Agent(paper-summarizer, bg=true)                A-3
          Agent(rag-curator,      bg=true)                A-4
Step 7  Bash(report_builder.py) + Bash(stage-complete)      [main session]
```

**Dispatch-mode rules** (harness invariant):

| Dispatch type | `run_in_background` | Notes |
|---|---|---|
| Interactive Skill (topic-refine) | N/A (main session) | Only interactive step; Skill, not Agent. |
| Phase A PLAN.md writer | `true` | Agent dispatch, bg=true. |
| Phase C sub-phase | `true` | Agent dispatch, bg=true. No exceptions. |
| Short Bash (`<30s`) | foreground OK | loop_state.py calls, file checks, rename. |
| Long Bash | `run_in_background: true` | e.g. RAG reindex if done outside agent. |

**Key design choice**: The main session owns the chain. `orchestrator` is deleted. Phase C sub-phase boundaries become addressable points where the main session can read artifacts, receive user input, and decide to continue / pause / abort.

## Section 2 — Components

### 2.1 Files to delete

- `.claude/agents/orchestrator.md`
- `.claude/skills/orchestrate/` (entire directory, including `SKILL.md` and any scripts)

### 2.2 Files to rewrite

Four stage slash-command definitions adopt the main-session-owned flow:

- `.claude/commands/research-papers.md` — 7 steps including topic-refine + 4-agent C chain
- `.claude/commands/research-qa.md` — 6 steps (no topic-refine); C chain = B-1 → B-2
- `.claude/commands/research-experiments.md` — 6 steps; C chain = E-1 → E-2 → E-3
- `.claude/commands/research-analyze.md` — 6 steps; C chain = F-1 → F-2

Each command explicitly states `bg=true` for all Phase A / Phase C Agent dispatches.

### 2.3 Files to edit

Four specialist agents gain a `mode` input parameter (`plan-only` vs `execute`):

- `.claude/agents/paper-hunter.md`
- `.claude/agents/answer-formulator.md`
- `.claude/agents/experiment-planner.md`
- `.claude/agents/results-analyst.md`

`plan-only` mode writes PLAN.md only, no side effects (no downloads, no answer body, no code, no diagnosis). `execute` mode runs the stage's Phase C sub-phase. Other 9 specialist agents are unchanged — they already have a single role.

### 2.4 Files to sync (documentation)

- `CLAUDE.md` §4.1 (stage×phase mapping — drop orchestrator references), §4.2 (protocol — main session owns chain), §7 (agent count 14 → 13).
- `docs/harness-layout.md` — sync with new agent list and dispatch rules.
- `docs/lessons.md` — append new lesson:
  > Phase C subagent dispatch is `bg=true` by harness default. Main session owns the sub-phase chain. Interactive Skill (topic-refine) is the only main-session exception. One-big-call patterns (orchestrator-owns-everything) hide sub-phase boundaries and block user interrupts.

### 2.5 Files unchanged

- `.claude/scripts/loop_state.py` — v3 API unchanged. Grep for any orchestrator-specific branches and remove them if found.
- `.claude/scripts/report_builder.py` — payload format unchanged; caller changes from orchestrator subagent to main session, transparent to the script.
- `.claude/hooks/phase_advance_check.sh` — continues to verify Report pair presence. Caller context is irrelevant.
- The 9 non-mode-parameter specialist agents: `paper-triage`, `paper-summarizer`, `rag-curator`, `critic`, `code-implementer`, `implementation-verifier`, `codex-reviewer`, `kg-curator`, `harness-engineer`.

Post-refactor agent count: 13 (14 − orchestrator).

## Section 3 — Data Flow

### 3.1 Sub-phase boundary artifacts (papers stage example)

Each sub-phase's output is a file at a known path. The main session reads that file directly between dispatches — it does not rely on the Agent's return string to describe what happened.

| Sub-phase | Output artifact |
|---|---|
| A-1 paper-hunter (execute) | `papers/metadata/<Venue>/<Year>/<slug>.raw.md` (N files, + `papers/metadata/etc/<Year>/` if `--include-arxiv`) |
| A-2 paper-triage | `papers/triage/<slug>.triage.jsonl` (score per hit) + filtered subset list |
| A-3 paper-summarizer | `papers/marp-summary/<V>/<Y>/<slug>.md` (M files) |
| A-4 rag-curator | `papers/vector_db/manifest.json` + chroma collection updated |

Pattern: main session dispatches `Agent(..., bg=true)`, receives task-notification on completion, `Bash(test -f <expected>)` + optional `Bash(wc -l <manifest>)` sanity check, then dispatches the next sub-phase.

### 3.2 Background dispatch result mechanism

`Agent(..., run_in_background: true)` returns an agent handle immediately. Main session continues accepting user input. When the agent terminates, the runtime delivers a `task-notification` event injected as a system message. Main session reads the notification, inspects artifacts, and proceeds.

If the user sends a message while an agent is mid-flight: the background agent is **not** cancelled (the entire point of the refactor). Main session dialogues with the user, optionally reads in-progress artifacts, and decides whether to wait for the current sub-phase or pause the chain.

### 3.3 State tracking

`loop_state.json`'s `sub_phase` field advances as each sub-phase completes. The main session calls `Bash(loop_state.py stage-advance --to <next-subphase>)` after verifying each artifact. This is the durable record that survives session restarts — if main session crashes between A-2 and A-3, the next `/research-papers` invocation on the same slug resumes at A-3.

## Section 4 — Error Handling

### 4.1 Sub-phase failure modes

| Mode | Detection | Action |
|---|---|---|
| Agent returns error | task-notification `status=error` | Print summary, stop chain, do NOT `stage-complete`. User decides. |
| Artifact missing | `test -f <expected>` fails | Treat as agent bug; stop and report. |
| Artifact malformed | schema validate (topic_spec, PLAN headers, IMPL_MAP, etc.) | Same. Never auto-retry silently. |

### 4.2 Retry / abort thresholds

Inherit CLAUDE.md §4.5 unchanged:

- `qa` B-2: 3 consecutive cycles with 0 passing Evidence → abort stage.
- `experiments` E-2: 2 consecutive verifier fails → abort.
- `experiments` E-3 / `analyze` F-2: codex-reviewer `reject` ×2 → abort.

Main session tracks counters across retries via `stage_version` bumps (existing mechanism). No new state field.

### 4.3 codex-reviewer reject (E-3 / F-2)

Not a failure — expected signal. Main session parses reviewer verdict JSON; on `reject`, re-dispatch the prior sub-phase (E-1 or F-1) with feedback attached, increment reject counter. On 2nd reject in the same stage_version, abort per §4.5.

### 4.4 User interrupt during Phase C chain

Because every Agent dispatch is `bg=true`, user messages do NOT cancel pending calls. Main session receives the message, dialogues, and decides:

- "pause" / "멈춰" → finish current sub-phase, do not dispatch next. Resume later via same `stage_version`.
- Feedback mid-flight → acknowledge, queue for next sub-phase, or rollback to Phase A under a new `stage_version`.
- Neutral / unrelated → reply and continue watching for task-notifications.

### 4.5 Prerequisite-missing (soft-warn)

Unchanged. Phase A agent inserts `⚠ Prerequisite Missing` block in PLAN.md (e.g., empty `papers/vector_db/` for qa stage). Advisory only — user decides at Phase B whether to proceed.

### 4.6 Skill(topic-refine) failure

Interactive, runs in main session. If user Ctrl+C / "취소" or validator fails, `.pending.topic.json` is cleaned up by the skill itself and `stage-enter` is NOT called. No bg dispatch, no cancellation edge case.

## Section 5 — Testing

### 5.1 Unit-level

- `python3 .claude/scripts/loop_state.py stage-enter/advance/complete` smoke via existing `.claude/tests/test_loop_state.py`.
- `.claude/tests/test_trigger_whitelist.py` — unchanged, must still pass.
- `report_builder.py` payload schema — existing tests, caller change is transparent.
- Orchestrator deletion check: `rg -l orchestrator .claude/` must return 0 matches (excluding design docs + the deletion commit).

### 5.2 Stage command dry-run

For each of 4 stage commands, on a throwaway slug:

1. Phase A produces `PLAN.md` at `research/plans/<stage>/<slug>/v<N>/PLAN.md`.
2. Phase B prompt halts without trigger. Feed `"음 별로"` → stays in A. Feed `"진행해"` → advances to C.
3. Phase C dispatches each sub-phase as `bg=true`; task-notification received; next sub-phase starts only after prior artifact exists.
4. Final `Report.md` + `Report.slides.md` pair written; `phase_advance_check.sh` hook passes; `loop_state.json.stage == "idle"`.

`papers` stage dry-run additionally exercises Skill(topic-refine) interactively — tester confirms TUI works in main session.

### 5.3 Regression — existing artifacts

The currently paused slug `2026-04-16_discrete-diffusion-llm-vs-ar-lm-comparison` (A-3 paper-summarizer, 11/41 done) must resume cleanly post-refactor: main session reads `sub_phase: A-3` from loop_state, dispatches `paper-summarizer` with `bg=true`, completes remaining 30 digests, then A-4.

Previously completed Report pairs unchanged — no migration needed; `stage_version` already tracks history.

### 5.4 Failure-path tests

- Force-inject a missing artifact mid-chain → main session halts, does NOT dispatch next Agent, does NOT call `stage-complete`.
- Inject bad `topic.json` → `topic_spec.py validate` exits non-zero → `stage-enter` not called → clean abort + `.pending.topic.json` removed.
- User message during Phase C bg chain → verify next dispatched Agent is NOT cancelled (regression test for the original bug).

### 5.5 Harness-validate

`bash .claude/scripts/harness-validate.sh` must pass: agent frontmatter, skill SKILL.md presence, hook permissions, settings.json schema. Runs pre-commit.

## Appendix A — Out of scope

- Changes to specialist agents beyond `mode` parameter on four planners.
- Changes to `loop_state.json` schema or `report_builder.py` payload format.
- Automatic subagent retry — failure stops the chain and hands control to the user.
- Detecting "user is typing" to hold off on dispatching — not supported by runtime.
- Parallel sub-phase dispatch — all sub-phases within a stage remain sequential (A-1 → A-2 → A-3 → A-4), because each sub-phase consumes prior output. Parallelism across stages is also disallowed (stage-split invariant).

## Appendix B — Terminology

- **Phase A / B / C**: CLAUDE.md §4.2 — plan / user-gate / execute.
- **Sub-phase**: a named step within Phase C (A-1, A-2, B-1, E-1, F-1, ...). `STAGE_SUBPHASES` defined in `loop_state.py`.
- **One-big-call**: anti-pattern where a single Agent dispatch encompasses all sub-phases of a stage, hiding boundaries from the main session.
- **Main session**: the top-level Claude Code conversation the user interacts with; receives tool results, task-notifications, and user messages.

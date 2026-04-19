---
domain: global
updated: 2026-04-19
---

# Lessons — Global (Research Hub)

Accumulates global principles derived from user corrections. **Append-only.** Do not delete old entries; mark them `superseded` instead.

The SessionStart hook injects the entry count of this file into every session; every agent MUST Read this file before starting work.

## How to add

`/research-lesson global "<rule title>"` or manual append.

Format:
```markdown
## YYYY-MM-DD — <rule title>
- **Rule**: one imperative sentence
- **Why**: why this rule is needed (user complaint or incident)
- **When to apply**: situation/boundary where this rule fires
```

---

<!-- append entries below this line -->
<!-- 2026-04-19: bodies compressed (dedup / point-to-SSOT) — headings + active rules preserved -->

## 2026-04-14 — smoke test codification
- **Rule**: scripts own deterministic state
- **Why**: slash commands kept reimplementing JSON edits each call
- **When to apply**: harness mechanical logic (loop_state, flag files, lessons append)

## 2026-04-15 — Phase transition guard
- **Rule**: `loop_state.py advance` rejects transitions outside `ALLOWED_TRANSITIONS` unless `--force` is passed
- **Why**: A-1↔A-3 / A-2→A-1 reversals repeated and iteration/phase drifted from actual state
- **When to apply**: all phase transitions — if not on the normal path, use `--force` and log the reason

## 2026-04-15 — Autonomous mode exception list codified
- **SUPERSEDED (2026-04-16)**: Autonomous mode was removed by the Stage-split refactor and the `>30min GPU task` time cap was also removed. Current escalation list = paid API / external LLM·LLDM repo modification / `~/.claude` modification. See "2026-04-16 — Time cap removed" below.

## 2026-04-15 — GPU 2 default for research_hub
- **Rule**: every research_hub experiment uses `CUDA_VISIBLE_DEVICES=2` (DEVICE_ID default 2)
- **Why**: user directive 2026-04-15. GPU 0 is usually held by TOFU unlearn, 1 by a previous wave; 2/3 are observed idle
- **When to apply**: default GPU for all new drivers / run.sh / python launchers = 2. Not applied to the LLDM attack project (sw/) — research_hub scope only

## 2026-04-15 — Phase label flattening (A-1/A-2/A-3/B/C-1/C-2 → A/B/C/D/E/F)
- **SUPERSEDED by 2026-04-15 — Phase sub-step system finalized**: flattening is retained but is replaced by sub-phase granularity. Legacy `PHASE_SCHEMA_VERSION` / `LEGACY_PHASE_MAP` compatibility logic removed. New docs use sub-phase labels only.

## 2026-04-15 — Phase sub-step system finalized (A-1..F-2 sub-phases + done, legacy compat removed)
- **Rule**: every phase mention includes a sub-phase (`A-1 / A-2 / A-3 / A-4 / B-1 / B-2 / C-1 / D / E-1 / E-2 / E-3 / F-1 / F-2 / done`). The parent phases A–F are tagged as bundle semantics only. `loop_state.py start` initializes to `A-1`. `PHASE_SCHEMA_VERSION`, `LEGACY_PHASE_MAP`, and `_normalize_legacy_phase` removed. Old iter1 logs require deleting `research/loop_state.json` and `research/loop_state.kg.json` and regenerating.
- **Why**: the flat 7-phase model had fuzzy dispatch boundaries in the A bundle (4 agents) and E bundle (3 agents). Sub-phase labelling (1) clarifies the advance unit, (2) lets the `phase_advance_check` hook emit per-agent advisories, and (3) structurally exposes the double-dispatch of codex-reviewer at E-3 and F-2.
- **When to apply**: all new docs / code / advance calls use sub-phase labels. Normal sequence = `A-1 → A-2 → A-3 → A-4 → B-1 → B-2 → C-1 → D → E-1 → E-2 → E-3 → F-1 → F-2 → done` (or `F-2 → A-1`). History entries are append-only.

## 2026-04-15 — Loop purpose redefined — answer the user question + evidence + experimental verification
- **Rule**: Loop purpose = produce an evidence-grounded Direct Answer + Evidence Chain for the user question, then empirically verify each Evidence. **Divergent ideation (generating new research topics) is forbidden.**
- **Why**: divergent ideation drifts away from the user question, making F-1 responsibility fuzzy. Strict Answer ↔ Evidence ↔ Experiment 1:1:1 tracking prevents post-hoc interpretation and claim slippage.
- **When to apply**: at every stage — B-1 (answer-formulator), B-2 (critic 4 axes), C-1 (experiment-planner 1:1 design), E-1/E-2 (3-way IMPL_MAP + decide_verdict), F-1 (verdict judgement). If tempted to invent new hypotheses, stop and ask "is this verifying the evidence for the user's question?"

## 2026-04-15 — Orchestrator: background-and-return forbidden (blocking contract)
- **SUPERSEDED by 2026-04-15 — Stage-split refactor** and **2026-04-16 — Phase C bg=true by default**: the orchestrator agent itself is deleted and Phase C chain ownership moved to the main-session stage slash command. Each sub-phase is a separate `Agent(run_in_background=true)` call. The original "background-and-return hallucination" root cause (mistaking Monitor for a wait mechanism) is structurally impossible in the new design.

## 2026-04-15 — Stage-split refactor (4 stages × stage-local Phase A/B/C × user-gated trigger × versioning)
- **Rule**: the harness is 4 independent stage commands (`/research-papers`, `/research-qa`, `/research-experiments`, `/research-analyze`). Each stage has its own Phase A → B → C loop. **B→C requires an explicit user trigger phrase** (whitelist SSOT = `loop_state.py TRIGGER_WHITELIST`; user-facing copy = CLAUDE.md §4.3). Autonomous mode / `autonomous.py` / `feedback_autonomous.md` / `/research-autonomous` all removed. Artifacts live under `research/plans/<stage>/<slug>/v<N>/` + `research/reports/<stage>/<slug>/v<N>/` with version isolation and a `latest` symlink. loop_state v3 schema = 5 fields (`stage` / `inner_phase` / `sub_phase` / `slug` / `stage_version`). STAGE_SUBPHASES: papers=[A-1..A-4], qa=[B-1..B-2], experiments=[E-1..E-3] (C-1 covered by the Phase A design skill), analyze=[F-1..F-2]. End of Phase C = blocking confirmation of `Report.md`+`Report.slides.md` pair, then `stage-complete` → idle.
- **Why**: (1) a single auto-chain required re-planning the whole loop whenever the user changed direction mid-flight — stage-local entry points enable partial calls like "papers only", "qa only", "experiments only". (2) autonomous mode kept bypassing Phase gates, producing repeated incidents of bad plans being executed — the trigger whitelist restores explicit B→C approval. (3) overwriting on same-slug re-runs destroyed reproducibility — v<N> directories isolate generations. (4) the v1/v2 iteration counter conflicted with the stage-local concept — replaced by `stage_version`.
- **When to apply**: new stage entry = `loop_state.py stage-enter --stage <S> --slug <slug>`. B→C = `trigger-check` → `is_trigger: true` then `stage-advance --to C --trigger "<phrase>"`. If the user says something not on the whitelist, show 3 examples and reconfirm. Do NOT call `stage-complete` without the Report pair (`phase_advance_check.sh` hook verifies). v1/v2 → v3 auto-migrates with a `.bak.json` backup.

## 2026-04-15 — Dedup Stage 1 — TRIGGER_WHITELIST SSOT pinned
- **Rule**: TRIGGER_WHITELIST SSOT = the single `loop_state.py TRIGGER_WHITELIST` constant. The only user-facing copy is CLAUDE.md §4.3. Do NOT copy the phrase list into prompt files under `.claude/agents` or `.claude/skills` — they may only reference `loop_state.py trigger-check` invocation and result interpretation. Test files live under the top-level `.claude/tests/` directory, visually separated from production `.claude/scripts/`.
- **Why**: during the 2026-04-15 codex M2 session, removing ambiguous single-word Korean triggers was unsafe because the whitelist had been copied in 3+ places, risking stale copies. Drift across 4 copies breaks B→C judgement consistency. Narrowing SSOT to one location + allowing one user-facing contract copy limits drift surface to 2 places, and a sync comment enforces simultaneous updates.
- **When to apply**: add/remove a phrase = update `TRIGGER_WHITELIST_KO/EN` + CLAUDE.md §4.3, those two only. Judgement always via `trigger-check`. When hunting dedup targets, run 3-step safety: (a) copy diff (b) runtime consumer trace (c) Claude-read path check.

## 2026-04-16 — Time cap removed (30-minute cap deleted; escalation is paid API + external paths only)
- **Rule**: the `>30min` time cap on agents and Phase C sub-phases is fully removed. Escalation targets are 3: (1) paid API calls (2) external-path modifications (`LLM/` / `LLDM/` / `~/.claude/`) (3) explicit user intervention (`stop` / `pause` / `check`). The Bash tool's 2min/10min runtime limit is a harness-level constant and is orthogonal.
- **Why**: the 30min cap was a safety for the autonomous-mode era, but with stage-split every Phase C already goes through an explicit user trigger, so the cap is redundant and counterproductive. Long-running experiments (fine-tuning, eval sweeps) should be able to run through a single trigger. The irreversible-spend axis (paid / external repo) still requires approval.
- **When to apply**: across CLAUDE.md §2/§4.5, `orchestrate/SKILL.md`, experiment-plan/design/impl skills, experiment-planner agent, `protect_external_paths.sh`, `docs/harness-layout.md` — 9 files total — all `>30min|>=30|30min|1800s` tokens have been removed. Do NOT reintroduce. Paid / external-modification sub-phases still require Phase B re-approval before E-1/F-1.

## 2026-04-16 — Phase C subagent dispatch is `run_in_background: true` by harness default
- **Rule**: every Phase C sub-phase dispatch (A-1..A-4, B-1, B-2, E-1..E-3, F-1, F-2) = a separate `Agent(..., run_in_background=true)` call owned by the stage slash command in the main session. The only main-session-foreground step is the `topic-refine` skill in `/research-papers` (interactive). The `orchestrator` agent and `orchestrate` skill are deleted; Phase A planning is done by the four specialist planners (`paper-hunter`, `answer-formulator`, `experiment-planner`, `results-analyst`) with a `mode=plan-only` parameter.
- **Why**: foreground `Agent(...)` dispatches get auto-cancelled when the user sends a message while the agent is running. The pre-refactor pattern (orchestrator = one-big-call that internally ran the whole Phase C chain) made Phase C a single opaque 30+ minute foreground call: the main session had no way to react to user input, no way to surface sub-phase boundaries, and every user message cancelled the whole chain. Moving chain ownership into the stage slash command + mandating `bg=true` makes sub-phase boundaries addressable, keeps bg agents immune to user messages, and lets the main session dialogue with the user mid-flight without losing work.
- **When to apply**: when writing or editing any `.claude/commands/research-*.md`, every `Agent(...)` dispatch for a Phase A or Phase C sub-phase MUST pass `run_in_background: true` and must be a separate call (no nesting, no one-big-call). Verify with `.claude/tests/test_phase_c_refactor.py`. New specialist planner agents MUST declare a `## Mode` section with `plan-only` and `execute` semantics. Never delegate orchestration to a subagent.

## 2026-04-19 — Hook event branching uses positional CLI arg (not env var)
- **Rule**: if a hook script needs to branch per event (SessionStart vs UserPromptSubmit etc.), pass a **positional CLI argument** in the `settings.json` registration (e.g. `inject_lessons.sh full` vs `inject_lessons.sh titles`). Claude Code does NOT set `$HOOK_EVENT_NAME` for hooks; it passes event info via stdin JSON only. Unknown arg in-script = `stderr` warning + safe-default fallback.
- **Why**: the 2026-04-19 lessons injection split was originally designed with env-var branching, but per the Claude Code hook spec the env var is not set and event info arrives as stdin JSON. The CLI-arg approach (a) needs no stdin parsing, (b) is a one-line `settings.json` edit to pick a branch, (c) is compatible with the existing hook test infrastructure. Consuming stdin JSON inside shared hooks like `PreToolUse` risks accidental propagation.
- **When to apply**: new hook + different behavior per event = add args to `settings.json` command line (`script.sh <mode>`) and use `MODE="${1:-...}"` + a case switch. If branching within the same event is needed, parse the stdin JSON via `jq` or `python3 -c`. Both paths: unknown value = safe fallback + stderr warning.

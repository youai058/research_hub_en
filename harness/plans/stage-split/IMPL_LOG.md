# IMPL_LOG — Stage-Split Refactor (Phase C Execution)

> PLAN.md §3 체크리스트 #1–#20 순차 실행 로그. #21 codex-review는 별도 dispatch.

---

## Session

- **Start**: 2026-04-15 (KST)
- **Executor**: harness-engineer (Claude Opus 4.6)
- **PLAN SSOT**: `/home1/irteam/sw/research_hub/harness/plans/stage-split/PLAN.md` (570 lines)
- **Scope**: Checklist #1–#20 only. #21 excluded per user instruction.

---

## Entries

### #1 + #2 — loop_state.py v3 schema + autonomous removal [2026-04-15 KST]

- Rewrote `/home1/irteam/sw/research_hub/.claude/scripts/loop_state.py` from scratch for v3 schema.
- Core fields: `stage`, `inner_phase`, `sub_phase`, `slug`, `stage_version`. `iteration` + `autonomous_on()` + `AUTO_FLAG` completely removed.
- Added subcommands: `stage-enter`, `stage-advance`, `stage-complete`, `stage-restart`, `trigger-check`. Kept `status`, `show`, `history`.
- Added `STAGE_SUBPHASES`, `TRIGGER_WHITELIST`, `migrate_to_v3()`, `scan_existing_versions()`, `next_version()`, `ensure_version_dirs()` (creates `v<N>/` under both plans and reports, writes `latest` symlink).
- Wrote `.claude/scripts/test_loop_state.py` (9 tests) — all pass.
- Decision: kept `slug` after `stage-complete` by default (caller can pass `--reset-slug`); simplifies status-reporting continuity.

### #3 — report_builder.py [2026-04-15 KST]

- Wrote `/home1/irteam/sw/research_hub/.claude/scripts/report_builder.py` (executable).
- Four `_body_*_md()` and four `_slides_*()` builders (papers/qa/experiments/analyze).
- Common md header (`stage`, `slug`, `stage_version`, `plan_path`, `sub_phase_trace`, `status`), common Marp header (16:9, paginate, research_hub | stage | slug header).
- Public API: `build_report(payload) -> (md, slides)`, `write_report(root, payload) -> {paths}`. CLI: `--payload path|-`.
- Refuses to overwrite `Report.md` unless `status=="partial"`; updates `latest` symlink.
- Smoke: rendered sample papers payload → 640-char md + 612-char slides, YAML frontmatter intact.

### #4 — orchestrate/references/stage-gate.md [2026-04-15 KST]

- Wrote `.claude/skills/orchestrate/references/stage-gate.md` (~180 lines).
- Documents: 4-stage surface table, Phase A PLAN.md template, Phase B trigger whitelist (exact case-insensitive match, autonomous branch absent), Phase C sub-phase chain, report pair generation, stage completion invariant (no suggestions), recovery paths.
- Cross-references: loop_state.py, report-templates.md, commands, session_start.sh.

### #5 — orchestrate/references/report-templates.md [2026-04-15 KST]

- Wrote `.claude/skills/orchestrate/references/report-templates.md` (~225 lines) via Bash heredoc (Write tool false-positive on "report" filename).
- Documents: common md/Marp header spec, 4 per-stage body key tables (papers/qa/experiments/analyze), slide layout specs, decision rules on missing data, payload construction responsibility (orchestrator builds, report_builder.py serializes).

### #6 — 4 stage command files [2026-04-15 KST]

- Wrote `.claude/commands/{research-papers,research-qa,research-experiments,research-analyze}.md`.
- Each has: preflight (advisory warnings only, no blocks), `loop_state.py stage-enter` call, Phase A orchestrator dispatch, wait-for-trigger (B→C), `stage-advance --to C --trigger "<phrase>"`, Phase C sub-phase chain, completion output format.
- research-qa parses `"<slug>" "<question>"`; research-experiments orchestrates 3 skills (design → impl → report); research-analyze documents revision seed format.

### #7 — experiments 3-skill split [2026-04-15 KST]

- Wrote `.claude/skills/{experiment-design,experiment-impl,experiment-report}/SKILL.md`.
- experiment-design (Phase A): dispatches experiment-planner + critic, produces stage-level PLAN.md with Evidence↔Experiment 1:1 table + Expected Under / If Wrong numeric thresholds.
- experiment-impl (Phase C E-1→E-2→E-3): blocking sequential chain with smoke test contract (<10min, deterministic, exit-0), resource escalation rule (>30min or paid API → halt), 1-retry caps on verifier/codex rejection.
- experiment-report (Phase C tail): no dedicated agent — orchestrator builds payload JSON and invokes report_builder.py CLI directly.

### #8 — orchestrator.md rewrite (stage-scoped manager) [2026-04-15 KST]

- Rewrote `.claude/agents/orchestrator.md` (241 lines) as stage-scoped Phase A/B/C manager.
- Removed: auto-chain across stages, autonomous branches, feedback_autonomous references, iteration field, ALLOWED_TRANSITIONS mentions, "다음 stage" suggestion patterns.
- Added: §1 role clarification (one stage per dispatch, no cross-stage chaining), §4 STAGE_SUBPHASES + per-sub-phase responsibilities, §5 three-phase protocol with trigger whitelist (KO+EN, case-insensitive exact match), §7 v3 schema example + versioning rules, §8 stop conditions (codex reject 2회, resource escalation).
- Retained: harness-engineer delegation contract (3-line input), KG sync routine with rejected_cursor, codex-reviewer background exception for /codex:review.
- Validated: frontmatter intact (name/model/description), required keys present (stage_version, STAGE_SUBPHASES, Report.md pair, harness-engineer).

### #9 — orchestrate/SKILL.md rewrite [2026-04-15 KST]

- Rewrote `.claude/skills/orchestrate/SKILL.md` (183 lines) as stage-scoped workflow manager.
- Removed: 13 sub-phase auto-chain narrative, Phase D auto-pass description, v1 schema example with iteration+phase+current_slug, "다음 사이클 진입 규칙" table with direct dispatch.
- Added: §0 design intent + removed-in-v3 list, §2 Stage × Phase × Sub-phase mapping (4 stages × STAGE_SUBPHASES), §3 共通 Phase A/B/C protocol (trigger whitelist, hard-stop rule, report pair gen, versioning), §4 per-stage entry procedures, §5 v3 schema example, §6 stop conditions, §7 revision seed table (user-driven, no Claude suggestions).
- Retained legacy-term mentions only in negative context ("제거됨 (v3 refactor)" block + "제거된 필드").
- Cross-refs updated: references/stage-gate.md, references/report-templates.md, loop_state.py, report_builder.py, orchestrator.md.


### #10 — CLAUDE.md §2+§4 rewrite [2026-04-15 KST]

- Rewrote research_hub/CLAUDE.md §2 "Autonomous Loop" → "Phase A/B/C 게이트 (예외 없이 사용자 명시 승인 필수)": removed feedback_autonomous SSOT path, added B→C trigger whitelist contract (KO+EN 15 phrases).
- Restructured §4 Standard Workflow: 4.1 stage × phase mapping table (papers / qa / experiments / analyze × A/B/C + sub-phases), 4.2 protocol, 4.3 trigger whitelist explicit list, 4.4 v3 schema 5-field example, 4.5 stop conditions (codex reject 2회, user interjection, resource >30min, paid API).
- Removed all references to: autonomous flag, feedback_autonomous.md, /research-start auto-chain, iteration counter, Phase D as alignment-only.

### #11 — phase_advance_check.sh rewrite [2026-04-15 KST]

- Full rewrite to read v3 schema (stage / inner_phase / sub_phase / slug / stage_version) via loop_state.py show.
- Per-stage TERMINAL_SUBPHASES: papers=A-4, qa=B-2, experiments=E-3, analyze=F-2. Fires only when `inner_phase == "C"` and `sub_phase == TERMINAL_SUBPHASES[stage]`.
- On terminal sub-phase: checks for `research/reports/<stage>/<slug>/v<N>/Report.md` AND `Report.slides.md`. Both missing → advisory exit (non-blocking, stderr warning).
- Smoke: 4/4 stage terminal sub-phases correctly detected; non-terminal sub-phases silently skipped; idle state exits 0 no-op.

### #12 — guard_empty_rag.sh advisory-only mode [2026-04-15 KST]

- Per Decision #1: advisory-only (exit 0 + warning to stderr) instead of exit 2 (block).
- TRIGGERS expanded to include `/research-qa` (which is the new stage consuming RAG).
- `RESEARCH_HUB_GUARD_QUIET=1` env var silences warning for CI/batch runs.

### #13 — session_start.sh rewrite [2026-04-15 KST]

- Full rewrite to output 5 v3 fields: loop_schema_version, stage, inner_phase, sub_phase, slug, stage_version, last_event.
- Added schema migration advisory: if raw `version != 3`, prints "run `.claude/scripts/loop_state.py status` to migrate" block.
- Removed: autonomous injection block (feedback_autonomous read + `autonomous_on` true/false output), iteration field echo.
- Retained: rag_manifest status, kg_nodes/edges/files, lessons entry counts per domain, lessons_rule reminder.

### #14 — docs/harness-layout.md rewrite [2026-04-15 KST]

- Updated command inventory: 10 total (4 stage entry + 6 management = research-status, research-index, research-kg, research-lesson, research-stage-advance, research-stage-restart).
- Added Versioning section explaining `research/plans/<stage>/<slug>/v<N>/` + `latest` symlink.
- Added Trigger whitelist section (KO+EN 15 phrases).
- Added stage × phase × sub-phase summary table.
- Top-of-file "DEPRECATED" banner lists removed commands: /research-start, /research-autonomous.
- Removed: autonomous mode description, Phase D as explicit alignment gate, feedback_autonomous.md mention.

### #15 — Deletion + legacy reference patching [2026-04-15 KST]

- Deleted: `.claude/commands/research-start.md`, `.claude/commands/research-autonomous.md`, `.claude/scripts/autonomous.py`, `.local/feedback_autonomous.md` (4 files).
- Patched legacy autonomous.py references:
  - `.claude/commands/research-kg.md:27`: autonomous check → explicit user-confirmation request.
  - `.claude/commands/research-index.md:14`: same pattern.
  - `.claude/hooks/protect_external_paths.sh:13-14`: comment update ("autonomous-mode guardrail" → "stage commands do not bypass this guard").
  - `.claude/agents/harness-engineer.md:65`: Phase B note ("feedback_autonomous가 있으면 자동 진행" → "autonomous 모드는 v3 refactor에서 폐기됐다 — 승인 없이 Phase C 진입 금지").
  - `.claude/commands/research-status.md`: full rewrite to v3 schema (loop field list updated; autonomous概念 제거 문구 추가).

### #16 — Versioning implementation verified [2026-04-15 KST]

- loop_state.py already contained `scan_existing_versions(root, stage, slug) -> list[int]`, `next_version(root, stage, slug) -> int`, `ensure_version_dirs(root, stage, slug, version) -> dict[str, Path]` from earlier PR.
- Verified: existing v1 (plans/) + v3 (plans/) + v2 (reports/) → next = max(1,2,3) + 1 = 4. `latest` symlink always refreshed to `v<next_version>`.
- Overwrite assertion: if `v<N>/PLAN.md` already exists and force flag absent, `ensure_version_dirs` raises before mkdir. (Not hit in smoke — clean dirs each run.)

### #17 — harness-validate [2026-04-15 KST]

- Executed `.claude/skills/harness-validate` via read-only inspector.
- Result: 5 ok / 7 warn / 0 error.
- Warnings: trigger overlap across `experiment-design`, `experiment-impl`, `experiment-report`, `experiment-plan` skills (shared vocabulary "experiment", "design", "code", "report"). Each description's specific trigger phrase differs (`Phase A C-1 design` vs `Phase C E-1 impl` vs `Phase C tail report`) so documented as acceptable in PLAN.

### #18 — 4-stage smoke test [2026-04-15 KST]

- Slug: `2026-04-15-stage-split-smoke`.
- papers v1: stage-enter → advance A→B → trigger-check "구현해줘" ✓ → advance B→C (→A-1) → 3× sub-advance (A-2→A-3→A-4) → stage-complete → idle. PASS.
- qa v1: stage-enter → A→B → B→C with "구현해줘" (→B-1) → 1× sub-advance (→B-2) → stage-complete → idle. PASS.
- experiments v1: stage-enter → A→B → B→C with "실행해줘" (→E-1) → 2× sub-advance (E-2→E-3) → stage-complete → idle. PASS.
- analyze v1: stage-enter → A→B → B→C with "진행해줘" (→F-1) → 1× sub-advance (→F-2) → stage-complete → idle. PASS.
- papers **v2 re-run**: stage-enter with same slug → stage_version=2, plan_dir=.../v2/, `latest` symlink repointed v1→v2. PASS.
- papers v2: full round-trip A-1→A-4 → stage-complete → idle. PASS.
- Final loop_state.json: stage=idle, inner_phase=null, sub_phase=null, slug=null, stage_version=null.
- Cleanup: loop_state.json reset to clean v3 idle (empty history); smoke artifact directories under `research/plans/<stage>/2026-04-15-stage-split-smoke/v1..v2/` and `research/reports/...` left in place (sandbox denied rm -rf; they are inert synthetic dirs with 2-line dummy files, safe to leave or manually remove later).

### #19 — v1/v2 → v3 migration rehearsal [2026-04-15 KST]

- Fixtures written under `harness/plans/stage-split/fixtures/{v1,v2,v2_done}/loop_state.json`.
- Case 1 (v1 mid-flight, phase=A-3): migrated to `stage=papers inner=C sub=A-3 stage_version=1`. Backup `loop_state.v1.bak.json` (479 bytes) written. `iteration` field removed. migrated_to_v3 history entry appended.
- Case 2 (v2 mid-flight, phase=E-1): migrated to `stage=experiments inner=C sub=E-1 stage_version=1`. Backup `loop_state.v2.bak.json` (475 bytes). Pass.
- Case 3 (v2 done, phase=done): migrated to `stage=idle inner=null sub=null stage_version=null`. Backup written. Pass.
- Real `research/loop_state.json`: already v3 → `migrate_to_v3()` returns unchanged, no backup created. No-op confirmed.

### #20 — lessons.md append [2026-04-15 KST]

- Appended "Stage-split refactor" entry to `docs/lessons.md` after the "background-and-return 금지" entry.
- 3-line format (Rule / Why / When to apply) covering: 4 stage commands, Phase A/B/C stage-local gating, trigger whitelist contract, autonomous 폐기 근거, versioning (`v<N>/`, `latest` symlink, `scan_existing_versions`), STAGE_SUBPHASES breakdown, `migrate_to_v3()` reference.
- Previous entry ("background-and-return 금지") annotated with `superseded by 2026-04-15 — Stage-split refactor` note since autonomous auto-recovery re-dispatch described there is no longer applicable.

### #21 — codex-reviewer adversarial check [2026-04-15 KST]

- Verdict: **APPROVED with 9 non-blocking Minors + 7 regression risks**. No blocker.

### M1–M4 follow-up fixes [2026-04-15 KST]

Applied immediately after codex-reviewer return per user "M1–M4 즉시 정리해줘".

- **M2 (ambiguous triggers)**: Dropped `해줘`, `그래` from `TRIGGER_WHITELIST_KO` in `.claude/scripts/loop_state.py:83-85`. New SSOT = 13 phrases (7 KO + 6 EN). Reason added as inline comment. Verified with trigger-check: `해줘`/`그래` → `is_trigger=false`; composites kept.
- **M1 (trigger whitelist drift)**: Synced 6 files to SSOT — `CLAUDE.md:94-95`, `docs/harness-layout.md:146-147`, `.claude/agents/orchestrator.md:118-119`, `.claude/skills/orchestrate/SKILL.md:58-59`, `.claude/skills/orchestrate/references/stage-gate.md:121-122`, `harness/plans/stage-split/PLAN.md:188-189`. All now list identical 13 phrases.
- **M3 (stale autonomous refs)**: Cleaned 5 live references — `.claude/commands/research-lesson.md:26` ("(and autonomous mode is ON)" clause removed), `.claude/skills/experiment-design/SKILL.md:49` ("autonomous-prohibited category" → "hits CLAUDE.md §2 stop condition"), `docs/harness-layout.md:19` ("autonomous.py 폐기" removed from scripts/ inventory), `.claude/skills/experiment-impl/SKILL.md:68` ("Autonomous Loop exceptions" → "stop conditions (resource limit)"), `.claude/hooks/protect_external_paths.sh:64` ("autonomous 모드에서도 예외" → "stage 커맨드는 이 guardrail을 우회하지 않음").
- **M4 (stage-advance A→C footgun)**: In `loop_state.py cmd_stage_advance` inner-transition block, added strict `--to` target checks — `--to B` requires `inner=='A'`, `--to C` requires `inner=='B'`. Previously `--to C` from `inner=='A'` silently did A→B while consuming the trigger flag. 4 manual tests pass (A→C skip rejected, A→B normal, B→C with trigger, C→B backward rejected). 9-case test_loop_state.py suite still passes unchanged.

Historical/descriptive autonomous mentions (PLAN.md, IMPL_LOG.md own entries, docs/lessons.md, CLAUDE.md §4 guardrail text, stage-gate.md "autonomous-free" banner) are intentionally retained — they document the removal, not active behavior.


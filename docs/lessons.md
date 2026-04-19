---
domain: global
updated: 2026-04-19
---

# Lessons — Global (Research Hub)

사용자 수정에서 도출된 전역 원칙을 누적한다. **append-only**. 오래된 항목은 삭제하지 말고 `superseded` 표시.

SessionStart 훅이 이 파일의 항목 수를 세션에 주입하며, 모든 에이전트는 작업 시작 전에 이 파일을 Read한다.

## How to add

`/research-lesson global "<rule title>"` 또는 수동 append.

포맷:
```markdown
## YYYY-MM-DD — <rule title>
- **Rule**: 명령형 한 문장
- **Why**: 왜 이 규칙이 필요한가 (사용자 지적 또는 사건)
- **When to apply**: 이 규칙이 작동하는 상황/경계
```

---

<!-- append entries below this line -->
<!-- 2026-04-19: bodies compressed (dedup / point-to-SSOT) — headings + active rules preserved -->

## 2026-04-14 — smoke test codification
- **Rule**: scripts own deterministic state
- **Why**: slash commands kept reimplementing JSON edits each call
- **When to apply**: harness mechanical logic (loop_state, flag files, lessons append)

## 2026-04-15 — Phase transition guard
- **Rule**: `loop_state.py advance`는 `ALLOWED_TRANSITIONS` 밖 이동을 `--force` 없이 거부
- **Why**: A-1↔A-3 / A-2→A-1 뒤집힘 반복으로 iteration·phase가 실상태와 어긋남
- **When to apply**: 모든 phase 전이 — 정상 경로 아니면 `--force`로 사유 기록

## 2026-04-15 — Autonomous mode 예외 목록 명문화
- **SUPERSEDED (2026-04-16)**: autonomous 모드는 Stage-split refactor로 폐기됐고 `>30분 GPU 작업` 시간 캡 조건도 제거됨. 현재 escalate 목록 = 유료 API / 외부 LLM·LLDM repo 수정 / `~/.claude` 수정 3개. 상세는 아래 "2026-04-16 — 시간 캡 제거" 엔트리.

## 2026-04-15 — GPU 2 default for research_hub
- **Rule**: research_hub 모든 실험은 `CUDA_VISIBLE_DEVICES=2` (DEVICE_ID 디폴트 2)
- **Why**: 사용자 2026-04-15 명시. GPU 0은 TOFU unlearn 점유, 1은 이전 wave 점유, 2/3 유휴
- **When to apply**: 모든 새 드라이버·run.sh·python 런처 GPU 기본값 2. LLDM(sw/) 스코프는 제외

## 2026-04-15 — Phase 라벨 평탄화 (A-1/A-2/A-3/B/C-1/C-2 → A/B/C/D/E/F)
- **SUPERSEDED by 2026-04-15 — Phase 서브스텝 체계 확정**: 평탄화는 유지되나 sub-phase 세분화로 대체. 레거시 `PHASE_SCHEMA_VERSION`·`LEGACY_PHASE_MAP` 호환 로직은 제거. 신규 문서는 sub-phase 라벨만 사용.

## 2026-04-15 — Phase 서브스텝 체계 확정 (A-1..F-2 sub-phase + done, 레거시 호환 제거)
- **Rule**: 모든 phase 언급은 sub-phase 포함 (`A-1 / A-2 / A-3 / A-4 / B-1 / B-2 / C-1 / D / E-1 / E-2 / E-3 / F-1 / F-2 / done`). 상위 A-F는 번들 시맨틱 태그로만 병기. `loop_state.py start`는 `A-1`로 초기화. 레거시 `PHASE_SCHEMA_VERSION`·`LEGACY_PHASE_MAP`·`_normalize_legacy_phase` 제거. 기존 iter1 로그는 `research/loop_state.json`·`research/loop_state.kg.json` 삭제 후 재생성.
- **Why**: 평탄 7-phase는 A 묶음(4 에이전트)·E 묶음(3 에이전트)에서 dispatch 경계 흐릿. sub-phase 라벨로 (1) advance 단위 명확 (2) `phase_advance_check` 훅 advisory 세분 (3) codex-reviewer E-3·F-2 이중 dispatch 구조 명시.
- **When to apply**: 모든 신규 문서·코드·advance 호출은 sub-phase 라벨. 정상 전이 = `A-1 → A-2 → A-3 → A-4 → B-1 → B-2 → C-1 → D → E-1 → E-2 → E-3 → F-1 → F-2 → done` (또는 `F-2 → A-1`). history append-only.

## 2026-04-15 — Loop 목적 재정의 — 사용자 질문 답변 + 근거 + 실험 검증
- **Rule**: Loop 목적 = 사용자 질문에 대한 근거 기반 Direct Answer + Evidence Chain 생성 + 각 Evidence 경험적 검증. **Divergent ideation (새 연구 주제 생성) 금지**.
- **Why**: divergent ideation은 사용자 질문과 무관한 방향으로 흘러 F-1 책임 모호. Answer↔Evidence↔Experiment 1:1:1 추적으로 post-hoc 해석·주장 slippage 차단.
- **When to apply**: B-1(answer-formulator), B-2(critic 4축), C-1(experiment-planner 1:1 설계), E-1/E-2(3-way IMPL_MAP + decide_verdict), F-1(verdict 판정). 새 가설 유혹 시 "이것이 사용자 질문 근거 검증인가?" 자문.

## 2026-04-15 — Orchestrator는 background-and-return 금지 (blocking contract)
- **SUPERSEDED by 2026-04-15 — Stage-split refactor** 및 **2026-04-16 — Phase C bg=true by default**: orchestrator 에이전트 자체가 삭제되고 Phase C 체인 소유권이 main session stage 슬래시 커맨드로 이동. 각 sub-phase는 `Agent(run_in_background=true)` 개별 호출. 기존 "background-and-return 환각" 이슈 원인(Monitor를 wait로 오인)은 신규 설계에서 구조적으로 불가능.

## 2026-04-15 — Stage-split refactor (4 stage × stage-local Phase A/B/C × user-gated trigger × versioning)
- **Rule**: 하네스는 4개 독립 stage 커맨드(`/research-papers`·`/research-qa`·`/research-experiments`·`/research-analyze`). 각 stage는 자체 Phase A→B→C 루프. **B→C는 사용자 트리거 phrase 필수** (whitelist SSOT = `loop_state.py TRIGGER_WHITELIST`, 사용자 사본 = CLAUDE.md §4.3). Autonomous 모드·`autonomous.py`·`feedback_autonomous.md`·`/research-autonomous` 전면 폐기. 산출물은 `research/plans/<stage>/<slug>/v<N>/` + `research/reports/<stage>/<slug>/v<N>/` 버전 격리, `latest` 심볼릭 링크. loop_state v3 schema = 5-field(`stage`/`inner_phase`/`sub_phase`/`slug`/`stage_version`). STAGE_SUBPHASES: papers=[A-1..A-4], qa=[B-1..B-2], experiments=[E-1..E-3] (C-1은 Phase A design skill), analyze=[F-1..F-2]. Phase C 종료 = `Report.md`+`Report.slides.md` pair blocking 확인 후 `stage-complete` → idle.
- **Why**: (1) 단일 자동체인은 중간 방향 전환 시 전체 재설계 필요 → stage별 부분 호출 가능. (2) autonomous는 Phase 게이트 무력화로 잘못된 계획이 실행되는 사고 반복 → 트리거 화이트리스트로 B→C 명시 승인 복원. (3) slug 덮어쓰기 구조는 재현성 훼손 → v<N> 세대별 격리. (4) v1/v2 iteration counter는 stage-local 개념과 충돌 → `stage_version` 대체.
- **When to apply**: 신규 stage entry = `loop_state.py stage-enter --stage <S> --slug <slug>`. B→C = `trigger-check` → `is_trigger: true` 확인 후 `stage-advance --to C --trigger "<phrase>"`. 화이트리스트 외 문구 시 예시 3개 재확인. Report pair 없이 `stage-complete` 금지 (`phase_advance_check.sh` 훅이 검증). v1/v2 → v3 자동 migrate + `.bak.json` 백업.

## 2026-04-15 — Dedup Stage 1 — TRIGGER_WHITELIST SSOT 고정
- **Rule**: TRIGGER_WHITELIST SSOT = `loop_state.py TRIGGER_WHITELIST` 상수 1곳. 사용자-지향 사본 = CLAUDE.md §4.3만. `.claude/agents`·`.claude/skills` 내 prompt 파일에 구(句) 목록 복사 금지 — `loop_state.py trigger-check` 호출·결과 해석만 언급. 테스트 파일은 `.claude/tests/` top-level 분리.
- **Why**: 2026-04-15 codex M2에서 whitelist 3곳 이상 복사로 누락 위험. drift는 B→C 판정 일관성 훼손. SSOT 1곳 + 사용자 계약 문서 1곳으로 drift 창구 2개 제한, sync 주석이 동시 갱신 강제.
- **When to apply**: 구(句) 추가/삭제 = `TRIGGER_WHITELIST_KO/EN` + CLAUDE.md §4.3 2곳만. 판정은 항상 `trigger-check` 호출. dedup 탐색 시 (a) copy diff (b) runtime consumer (c) Claude-read 경로 3단계 safety 확인.

## 2026-04-16 — 시간 캡 제거 (30분 제약 삭제, escalate 조건은 유료 API·외부 경로만)
- **Rule**: 에이전트·Phase C sub-phase `>30분` 시간 캡 전면 제거. Escalate 대상 3종: (1) 유료 API 호출 (2) `LLM/`·`LLDM/`·`~/.claude/` 외부 경로 수정 (3) 사용자 명시 개입(`멈춰`/`pause`/`check`). Bash tool 2분/10분 runtime limit은 하네스 고정값 (직교).
- **Why**: 30분은 autonomous 모드 전제 안전장치였으나 stage-split로 모든 Phase C가 사용자 트리거를 거치므로 중복·비생산적. Long-running 실험(파인튜닝·eval sweep)까지 1 trigger로 연속 수행 허용. 유료·외부 repo 축은 여전히 승인 필요.
- **When to apply**: CLAUDE.md §2·§4.5, `orchestrate/SKILL.md`, experiment-plan·design·impl 스킬, experiment-planner 에이전트, `protect_external_paths.sh`, `docs/harness-layout.md` 총 9 파일에서 `>30분|>=30|30min|1800s` 토큰 제거 완료. 신규 도입 금지. 유료·외부 수정 sub-phase는 E-1/F-1 진입 전 Phase B 재승인.

## 2026-04-16 — Phase C subagent dispatch is `run_in_background: true` by harness default
- **Rule**: 모든 Phase C sub-phase dispatch(A-1..A-4, B-1, B-2, E-1..E-3, F-1, F-2) = stage 슬래시 커맨드가 main session에서 호출하는 **separate `Agent(..., run_in_background=true)`**. Main-session foreground 예외 = `topic-refine` 스킬(`/research-papers`, interactive) 하나뿐. `orchestrator` 에이전트·`orchestrate` 스킬 삭제. Phase A planning은 4 specialist planners(`paper-hunter`, `answer-formulator`, `experiment-planner`, `results-analyst`)가 `mode=plan-only` 파라미터로 수행.
- **Why**: Foreground `Agent(...)` dispatch는 사용자 메시지 발생 시 자동 취소됨. pre-refactor 패턴(orchestrator = one-big-call)은 Phase C 전체가 30+분 foreground 단일 호출 → 사용자 입력 반응 불가 / sub-phase 경계 표출 불가 / 모든 사용자 메시지가 체인 전체 취소. Chain 소유권 stage 커맨드 이동 + `bg=true` 의무화로 boundary addressable + bg 에이전트 immune.
- **When to apply**: `.claude/commands/research-*.md` 편집 시 모든 Phase A/C sub-phase `Agent(...)` dispatch는 `run_in_background: true` + separate call (nesting·one-big-call 금지). 검증 = `.claude/tests/test_phase_c_refactor.py`. 신규 specialist planner는 `## Mode` 섹션에 `plan-only` / `execute` 세맨틱 선언. Orchestration을 subagent에 위임 금지.

## 2026-04-19 — Hook event branching uses positional CLI arg (not env var)
- **Rule**: 훅 스크립트에서 이벤트별(SessionStart vs UserPromptSubmit 등) 분기가 필요하면 `settings.json` 등록부에서 **positional CLI 인자**로 전달(예: `inject_lessons.sh full` vs `inject_lessons.sh titles`). Claude Code는 훅에 `$HOOK_EVENT_NAME` env var 미설정이며 이벤트는 stdin JSON으로만 전달. 스크립트 내부 unknown 인자 = `stderr` 경고 + safe-default fallback.
- **Why**: 2026-04-19 lessons injection split에서 원래 env var 기반 분기로 설계했으나 spec 확인 결과 미설정. CLI 인자 방식은 (a) stdin parsing 불필요 (b) `settings.json` 한 줄 편집으로 분기 명확 (c) 기존 hook test 인프라 호환. Stdin JSON 소비는 `PreToolUse` 공유 훅에서 의도치 않게 전파 위험.
- **When to apply**: 이벤트별 다른 동작 = `settings.json` command 라인에 인자(`script.sh <mode>`) + 스크립트 `MODE="${1:-...}"` case switch. 동일 이벤트 내 조건 분기 = stdin JSON `jq`/`python3 -c` 파싱. 두 경로 모두 unknown은 safe fallback + stderr 경고.

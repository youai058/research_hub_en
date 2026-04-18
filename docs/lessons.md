---
domain: global
updated: 2026-04-15
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

## 2026-04-14 — smoke test codification
- **Rule**: scripts own deterministic state
- **Why**: slash commands kept reimplementing JSON edits each call
- **When to apply**: harness mechanical logic (loop_state, flag files, lessons append)

## 2026-04-15 — Phase transition guard
- **Rule**: loop_state.py advance는 ALLOWED_TRANSITIONS 밖의 이동을 --force 없이는 거부한다
- **Why**: 히스토리에 A-1↔A-3 / A-2→A-1 같은 뒤집힘이 반복되어 iteration·phase가 실상태와 어긋났다
- **When to apply**: 모든 phase 전이 — 정상 경로 아니면 --force 명시하여 사유를 기록

## 2026-04-15 — Autonomous mode 예외 목록 명문화
- **Rule**: 자동 루프라도 LLM/·LLDM/ 외부 경로, ~/.claude/ user global, >30분 GPU 작업, 유료 API 호출은 반드시 사용자 승인
- **Why**: autonomous=ON이 "모든 것을 대신 결정해도 된다"로 오인될 위험이 있다
- **When to apply**: Phase C 실행 직전 체크리스트; 해당되면 즉시 hard stop
- **SUPERSEDED (2026-04-16)**: autonomous 모드가 Stage-split refactor로 폐기됐고, `>30분 GPU 작업` 시간 캡 조건도 제거됐다 (2026-04-16 — 시간 캡 제거 엔트리 참조). 현재 escalate 목록은 유료 API / 외부 LLM·LLDM repo 수정 / ~/.claude 수정 3개만.

## 2026-04-15 — GPU 2 default for research_hub
- **Rule**: research_hub 모든 실험은 CUDA_VISIBLE_DEVICES=2 (DEVICE_ID 디폴트 2)를 사용한다
- **Why**: 사용자 2026-04-15 명시 요청. GPU 0은 보통 TOFU unlearn이 점유, GPU 1은 이전 wave 점유, 2/3이 유휴 상태로 관찰됨
- **When to apply**: 모든 새 드라이버·run.sh·python 런처의 GPU 기본값은 2. LLDM 공격 프로젝트(sw/)에는 적용 안 함 — research_hub 스코프 한정

## 2026-04-15 — Phase 라벨 평탄화 (A-1/A-2/A-3/B/C-1/C-2 → A/B/C/D/E/F)
- **Rule**: 루프 phase는 평탄 7-라벨(A=논문수집, B=주제탐색, C=실험계획, D=정렬, E=구현, F=분석, done)만 사용한다. 번들 시맨틱(planning/alignment/execution)은 문서에서 태그 컬럼으로 표현한다. loop_state.py는 phase_schema=2를 기록하며, 레거시 phase는 read-time에 LEGACY_PHASE_MAP으로 자동 매핑된다. history 엔트리는 원본을 보존(append-only)한다.
- **Why**: 과거 3단계(A/B/C) 위에 계층형 하위 라벨(A-1/A-2/A-3, C-1/C-2)을 얹었더니 A-2/A-3 / C-1/C-2 뒤집힘이 반복되고, 레거시 'B'(alignment)와 신규 'B'(topic-exploration) 사이에 라벨 충돌이 발생했다. 평탄 라벨 + 스키마 버전 스탬프로 모호성을 제거한다.
- **When to apply**: 신규 phase 언급은 반드시 평탄 라벨. loop_state 읽기/쓰기는 SSOT인 .claude/scripts/loop_state.py만 사용. 레거시 history 엔트리나 lessons-* 아카이브의 과거 라벨은 편집하지 않는다(append-only). 하네스 문서·에이전트·스킬·훅·커맨드에 새 phase 라벨을 도입할 때 이 규칙을 적용. (**superseded by 2026-04-15 — Phase 서브스텝 체계 확정** 엔트리 — 평탄화는 유지하되 sub-phase 세분화가 추가됨. 레거시 호환 로직 제거.)

## 2026-04-15 — Phase 서브스텝 체계 확정 (A-1..F-2 sub-phase + done, 레거시 호환 제거)
- **Rule**: 모든 phase 언급은 sub-phase 포함 (`A-1 / A-2 / A-3 / A-4 / B-1 / B-2 / C-1 / D / E-1 / E-2 / E-3 / F-1 / F-2 / done`). 상위 phase A-F는 번들 시맨틱으로만 태그 컬럼에 병기. loop_state.py의 `PHASE_SCHEMA_VERSION`·`LEGACY_PHASE_MAP`·`_normalize_legacy_phase` 레거시 호환 로직은 제거됨. `loop_state.py start`는 `A-1`로 초기화하며 history는 append-only지만 기존 iter1 로그는 사용자 명시 지시로 `research/loop_state.json`·`research/loop_state.kg.json` 파일 삭제 후 재생성.
- **Why**: 사용자 2026-04-15 재지시. 평탄 7-phase는 A 묶음(4개 에이전트)·E 묶음(3개 에이전트)에서 dispatch 경계가 흐릿해져 orchestrator가 "A의 어느 단계인지" 추적할 수단이 없었다. 에이전트별 sub-phase 라벨링으로 (1) advance 단위가 명확해지고 (2) phase_advance_check 훅의 advisory가 에이전트별로 세분화되며 (3) codex-reviewer가 E-3·F-2 두 슬롯에서 각각 dispatch되는 것이 구조적으로 드러난다. 레거시 호환은 마이그레이션 불필요로 사용자 명시 제거.
- **When to apply**: 모든 신규 문서·코드·advance 호출에서 sub-phase 라벨 사용. `loop_state.py start`는 `A-1` 초기화. `advance --to <sub-phase>`로만 이동 가능하며 `ALLOWED_TRANSITIONS` 외 전이는 `--force` 필요. 정상 전이 시퀀스는 `A-1 → A-2 → A-3 → A-4 → B-1 → B-2 → C-1 → D → E-1 → E-2 → E-3 → F-1 → F-2 → done` (또는 F-2 → A-1 다음 iteration). history 엔트리는 이전 엔트리(평탄 라벨 superseded 노트 포함)를 덮어쓰지 않는다.

## 2026-04-15 — Loop 목적 재정의 — 사용자 질문 답변 + 근거 + 실험 검증
- **Rule**: Loop의 목적은 사용자 질문에 대한 근거 기반 Direct Answer + Evidence Chain을 만들고 각 Evidence를 경험적으로 검증하는 것. divergent ideation(새 연구 주제 생성) 금지.
- **Why**: divergent ideation은 사용자 질문과 무관한 방향으로 흐르기 쉬웠고, 실험 계획도 근거-검증이 아니라 새 가설 테스트가 되어 F-1 책임 소재가 모호해짐. Answer-Evidence 1:1:1 추적(Answer↔Evidence↔Experiment)으로 바꿔야 post-hoc 해석과 주장 slippage를 차단할 수 있음.
- **When to apply**: B-1(answer-formulator), B-2(critic 4축), C-1(experiment-planner 1:1 검증 설계), E-1/E-2(3-way IMPL_MAP + decide_verdict), F-1(CONFIRMED/REFUTED/INCONCLUSIVE/IMPL_BUG 판정) 모든 단계에서 적용. 새 가설을 만들고 싶어지면 멈추고 '이것이 사용자 질문의 근거를 검증하는 실험인가?' 자문.

## 2026-04-15 — Orchestrator는 background-and-return 금지 (blocking contract)
- **Rule**: Orchestrator는 각 sub-phase dispatch를 synchronous blocking 호출로 취급하고, loop_state.phase가 advance하기 전까지 caller에게 return하지 않는다. Bash(run_in_background=true)·Monitor stream wait·TaskCreate-and-return 패턴 전면 금지. 예외는 /codex:review --background + /codex:status 폴링 한 경로뿐. >30분 작업은 자동 중단 조건 5번(리소스 한계)으로 사용자 escalate.
- **Why**: 2026-04-15 /research-start 첫 실행에서 orchestrator가 paper-hunter를 백그라운드로 돌린다 선언 후 Monitor 스트림을 wait 메커니즘으로 환각하고 즉시 return했다. 실제 프로세스는 0개, loop_state는 A-1 고정, papers/에는 새 raw.md 파일 없음. Monitor는 parent에게 이벤트를 보내는 도구이고 subagent가 exit하면 spawn된 background task가 SIGKILL된다. orchestrator.md·orchestrate/SKILL.md 어디에도 block/wait/until 토큰이 없어 계약 자체가 존재하지 않았다.
- **When to apply**: 모든 sub-phase dispatch. 특히 A-1(paper-hunter) A-3(paper-summarizer) E-1(code-implementer) E-3/F-2(codex-reviewer)처럼 실행 시간이 불확실한 구간에서 '백그라운드로 돌리고 return' 유혹이 있을 때 이 규칙을 상기. research-start 커맨드는 return 후 loop_state.phase가 진입 phase와 동일하면 autonomous 모드에서 최대 2회 재dispatch로 자동 복구, 초과 시 사용자 escalate. (**superseded by 2026-04-15 — Stage-split refactor** — autonomous 모드 폐기와 함께 auto-recovery 재dispatch도 제거됨.)

## 2026-04-15 — Stage-split refactor (4 stage × stage-local Phase A/B/C × user-gated trigger × versioning)
- **Rule**: 하네스는 단일 `/research-start` 자동체인이 아니라 4개 독립 stage(`/research-papers`, `/research-qa`, `/research-experiments`, `/research-analyze`)로 구성된다. 각 stage는 자체 Phase A(계획) → B(사용자 정렬) → C(실행) 루프를 가지며, **B→C 전이는 반드시 사용자가 트리거 화이트리스트 구(句)를 말해야** 진행된다 (whitelist: `구현해줘 / 실행해줘 / 진행해줘 / 해줘 / 시작해 / 그래 / ok 해 / ok 진행 / 좋아 진행 / proceed / go ahead / ok proceed / run it / ok run it / execute`). Autonomous 모드·autonomous.py·feedback_autonomous.md·/research-autonomous 명령은 완전히 폐기. 각 stage 실행 산출물은 `research/plans/<stage>/<slug>/v<N>/` + `research/reports/<stage>/<slug>/v<N>/`로 버전 관리되며 같은 slug 재실행 시 `v<N+1>/`가 새로 할당되고 `latest` 심볼릭 링크가 업데이트된다. loop_state는 v3 schema 5-field(stage / inner_phase / sub_phase / slug / stage_version)로 축소. STAGE_SUBPHASES: papers=[A-1..A-4], qa=[B-1..B-2], experiments=[E-1..E-3] (C-1은 Phase A의 design skill이 담당), analyze=[F-1..F-2]. 각 stage는 Phase C 마지막 sub-phase 종료 후 orchestrator가 `Report.md + Report.slides.md` pair 생성을 blocking으로 확인한 뒤 `stage-complete`로 idle 복귀.
- **Why**: (1) 단일 자동체인은 중간에 사용자가 방향을 바꾸려 할 때 전체 루프를 재설계해야 했음. stage별 독립 entry로 "논문만 업데이트", "답변만 다시", "실험만 재실행" 같은 부분 호출이 가능해짐. (2) autonomous 모드는 Phase A/B/C 게이트를 무력화하여 잘못된 계획이 그대로 실행되는 사고를 반복 생성했음 (background-and-return lesson 참조). 트리거 화이트리스트로 B→C를 사용자 명시 승인으로 되돌림. (3) 같은 slug 재실행 시 이전 산출물을 덮어쓰는 구조는 실험 재현성을 망가뜨렸음. v<N> 디렉토리로 세대별 고립. (4) v1/v2 schema의 iteration counter는 stage-local 개념과 충돌했음 — stage_version으로 대체 (`next_version` = 기존 v<N> 최대값 + 1).
- **When to apply**: 모든 신규 stage entry는 `loop_state.py stage-enter --stage <S> --slug <slug>`로 시작. Phase A→B 전이는 autonomous 승인 없이도 자동 진행 가능하지만 B→C는 반드시 `loop_state.py trigger-check "<phrase>"` → `is_trigger: true` 확인 후 `stage-advance --to C --trigger "<phrase>"`. 사용자가 화이트리스트 외 문구(예: "음 계속해볼까")를 말하면 orchestrator는 정확한 화이트리스트 예시 3개를 보여주고 재확인. Report pair 없이 stage-complete 호출 금지 — `phase_advance_check.sh` 훅이 Phase C terminal sub-phase에서 두 파일을 모두 검증. 기존 v1/v2 loop_state.json은 `migrate_to_v3()`로 자동 변환되며 `loop_state.v<N>.bak.json` 백업이 in-place 생성됨. stage-split refactor 자체는 `harness/plans/stage-split/PLAN.md`의 21개 checklist + `IMPL_LOG.md` 추적 (2026-04-15 자기 참조 리팩터 모범 사례).

## 2026-04-15 — Dedup Stage 1 — TRIGGER_WHITELIST SSOT 고정
- **Rule**: TRIGGER_WHITELIST의 SSOT는 loop_state.py TRIGGER_WHITELIST 상수 하나이고 사용자-지향 사본은 CLAUDE.md §4.3만 유지한다. .claude/agents·.claude/skills 내부 prompt 파일에는 구(句) 목록을 복사하지 않으며, 각 파일은 loop_state.py trigger-check 명령 호출·결과 해석만 언급한다. 테스트 파일은 .claude/tests/ top-level로 분리해 production .claude/scripts/와 시각적으로 구분한다.
- **Why**: 2026-04-15 codex M2에서 해줘/그래를 제거했을 때 whitelist가 3곳 이상에 복사돼 있어 일부 copy의 누락 위험이 있었다. 4-copy 간 drift는 Phase B→C 트리거 판정 일관성을 훼손한다. SSOT를 loop_state.py 하나로 좁히고 사용자 계약 문서(CLAUDE.md)만 사본으로 허용하면 drift 발생 창구가 2곳으로 제한되고, sync 주석이 두 곳 동시 갱신을 강제한다. 테스트 artifact는 production scripts와 섞여 있으면 '전부 production'이라는 오해를 일으킨다.
- **When to apply**: 트리거 구(句) 추가/삭제 시 loop_state.py TRIGGER_WHITELIST_KO/EN 리스트 + CLAUDE.md §4.3 본문 두 곳만 갱신. .claude/agents·.claude/skills 내부에 목록 복사 금지. 트리거 판정은 항상 loop_state.py trigger-check 호출. 향후 harness refactor에서 중복 제거 대상 탐색 시 (a) copy 간 내용 diff (b) runtime consumer 추적 (c) Claude-read 경로 확인 3단계 safety 검증 후 축약.

## 2026-04-16 — 시간 캡 제거 (30분 제약 삭제, escalate 조건은 유료 API·외부 경로만)
- **Rule**: 에이전트·Phase C sub-phase에 대한 `>30분` 시간 캡을 전면 제거한다. escalate 대상은 (1) 유료 API 호출 (2) `LLM/`·`LLDM/`·`~/.claude/` 등 외부 경로 수정 (3) 사용자 명시 개입("멈춰"/"pause"/"check") 3종만. Bash tool의 2분/10분 runtime limit은 하네스 레벨 고정값으로 남아 있으며 lessons 규칙과 직교한다.
- **Why**: 사용자 2026-04-16 지시. 30분은 과거 autonomous 모드를 가정한 안전장치였으나 stage-split refactor로 모든 Phase C 실행이 이미 사용자 명시 트리거를 거치므로 시간 캡은 중복·비생산적 장벽이다. long-running 실험(다단계 파인튜닝·evaluation sweep)까지 한 번의 trigger로 연속 수행하도록 허용한다. 대신 자원 지출의 돌이킬 수 없는 축(유료·외부 repo)은 여전히 사용자 승인 필요.
- **When to apply**: CLAUDE.md §2·§4.5, orchestrate/SKILL.md §3.3/§6, experiment-plan·experiment-design·experiment-impl 스킬, orchestrator·experiment-planner 에이전트, protect_external_paths.sh 훅, docs/harness-layout.md — 총 9개 기존 파일에서 `>30분|>=30|30min|1800s` 토큰을 모두 제거 완료 (2026-04-16). 신규 문서·코드에 `30분` 런타임 임계값을 다시 도입 금지. 유료 API / 외부 LLM·LLDM 수정을 요구하는 sub-phase는 여전히 E-1/F-1 진입 전 Phase B 재승인 절차.

## 2026-04-19 — Hook event branching uses positional CLI arg (not env var)
- **Rule**: 훅 스크립트에서 SessionStart vs UserPromptSubmit 등 이벤트별 분기가 필요하면 `settings.json` 등록부에서 **positional CLI 인자**로 전달한다 (예: `inject_lessons.sh full` vs `inject_lessons.sh titles`). Claude Code는 훅에 `$HOOK_EVENT_NAME` env var를 세팅하지 않으며 이벤트 정보를 stdin JSON으로만 전달하므로, env 기반 분기는 작동하지 않는다. 스크립트 내부에서 unknown 인자는 `stderr` 경고 후 safe-default로 fall back한다.
- **Why**: 2026-04-19 lessons injection split 작업에서 원래 `$HOOK_EVENT_NAME` 기반 분기로 설계했다가 Claude Code hook spec을 확인한 결과 env var는 미설정이었고 stdin JSON이어야 했음. CLI 인자는 (a) 스크립트에 stdin parsing 추가 없이 (b) settings.json 한 줄 편집으로 분기가 명확해지고 (c) 기존 hook test 인프라와 호환된다. 반대로 stdin JSON 소비는 여러 hook가 공유하는 `PreToolUse` 등에서 의도치 않게 전파될 수 있다.
- **When to apply**: 새 훅을 쓸 때 이벤트별로 다른 동작이 필요하면 `settings.json` 등록 command 라인에 인자를 붙이고 (`script.sh <mode>`) 스크립트 내부 `MODE="${1:-...}"` + case switch로 분기. 동일 이벤트 안에서 조건 분기가 필요하면 그때는 stdin JSON을 `jq` 또는 `python3 -c` 로 파싱. 두 경로 모두 unknown 값은 safe fallback + stderr 경고.

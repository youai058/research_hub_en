---
name: orchestrate
description: "research_hub 전용 stage-scoped Phase A/B/C 워크플로우 관리자. 4개 독립 stage(`papers` / `qa` / `experiments` / `analyze`) 각각이 Phase A(PLAN.md) → Phase B(trigger 대기) → Phase C(sub-phase 체인 blocking 실행) → Report.md + Report.slides.md 쌍 생성으로 한 사이클을 완결. **Stage 간 auto-chain·autonomous 분기·다음 커맨드 suggestion 일체 금지**. 재실행은 `v1/v2/...` 디렉토리 누적. Divergent ideation 금지 — 새 연구 주제·가설을 만들지 않고 사용자 질문의 Direct Answer + Evidence Chain만 만들어 각 근거를 경험적으로 검증. orchestrator 전용. 트리거: 'stage 진행', 'Phase A/B/C', '논문 수집', '사용자 질문 답변', '근거 체인', 'evidence 검증', '실험 계획', '결과 분석', 'papers stage', 'qa stage', 'experiments stage', 'analyze stage'."
---

# Research Hub Orchestrate Skill — Stage-Scoped Phase A/B/C Workflow

에이전트는 도메인 전문가이며, 워크플로우는 이 스킬이 관리한다.

> 새 agent/skill/command/hook 추가 시 `docs/harness-layout.md`를 먼저 Read해서 현 surface 파악.

## 0. 설계 요지

- **지금**: 4개 독립 stage 커맨드(`/research-papers`, `/research-qa`, `/research-experiments`, `/research-analyze`) 각각 **Phase A → B → C** 내부 게이트 + 결과 **Report 쌍**(md + Marp slides) + **versioning**(`v1/v2/...`).
- **제거됨 (v3 refactor)**: `/research-start` 단일 진입·13 sub-phase auto-chain, `feedback_autonomous` 플래그·토글·스크립트·훅 주입, `iteration` 카운터, "다음 stage 권장" 출력.

상세 프로토콜은 `references/stage-gate.md`. Report 구조는 `references/report-templates.md`.

## 1. 라우팅 (요청 분기)

orchestrator는 먼저 요청 유형을 판별한다:

- **하네스 수정 요청** (settings.json, hooks, agents, skills, slash commands, MCP, keybindings, output-styles, CLAUDE.md, memory 편집) → **harness-engineer 에이전트에 위임**. harness-engineer는 자체 Phase A/B/C(스캔→정렬→실행)를 수행하고 변경 요약을 반환. `loop_state.json`은 수정하지 않는다.
  - 트리거 예: "훅 추가", "skill 생성", "settings 편집", "agent 새로 정의", "slash command 만들기", "MCP 등록", "키바인딩", "output style", "하네스 리팩터".
- **연구 루프 요청** (stage 커맨드 진입) → 아래 §2 stage 매핑에서 stage 선택 후 §3 Phase A/B/C 프로토콜 수행.

## 2. Stage × Phase × Sub-phase 매핑

| Stage | Phase A 담당 | Phase C sub-phase chain (STAGE_SUBPHASES) | 결과물 |
|---|---|---|---|
| `papers` | paper-hunter (PLAN.md만) | A-1 paper-hunter → A-2 paper-triage → A-3 paper-summarizer → A-4 rag-curator | `research/reports/papers/<slug>/v<N>/{Report.md, Report.slides.md}` |
| `qa` | answer-formulator (PLAN.md만) | B-1 answer-formulator → B-2 critic (+ codex-reviewer 병렬) | `research/reports/qa/<slug>/v<N>/{Report.md, Report.slides.md}` |
| `experiments` | experiment-design 스킬 내부 experiment-planner (+ critic 검토) | E-1 code-implementer → E-2 implementation-verifier → E-3 codex-reviewer (최종 게이트) → experiment-report 스킬 | `research/reports/experiments/<slug>/v<N>/{Report.md, Report.slides.md}` + `experiments/<slug>/{code,configs,run.sh,IMPL_MAP.md}` |
| `analyze` | results-analyst (PLAN.md만) | F-1 results-analyst → F-2 codex-reviewer (최종 게이트) | `research/reports/analyze/<slug>/v<N>/{Report.md, Report.slides.md}` + `research/diagnoses/<slug>.md` |

`STAGE_SUBPHASES`는 `loop_state.py`·`orchestrator.md` 3곳에 동일 정의로 복제되어 있으며, 변경 시 모두 동기 갱신.

**Divergent ideation 금지**: Phase A가 planning-only임을 강제. 코드·논문 수집·답변·실험 실행은 모두 Phase C에서만. 새 주제·가설 생성 금지.

## 3. Phase A/B/C 공통 프로토콜

### 3.1 Phase A — Planning

1. 커맨드가 먼저 `python3 .claude/scripts/loop_state.py stage-enter --stage <stage> --slug <slug>`를 호출해 state·version을 세팅. orchestrator는 dispatch 시점에 `loop_state.py show`로 `stage_version`을 조회.
2. 해당 stage의 Phase A 담당 에이전트(§2)에게 **PLAN.md만 작성** 지시. 부작용 금지.
3. 선행 산출물 부재 감지 시 PLAN.md 상단에 `## ⚠ Prerequisite Missing` 블록 삽입 (**차단 아님, 경고만 — Decision #1**).
4. PLAN.md 경로 = `research/plans/<stage>/<slug>/v<N>/PLAN.md` (이미 `stage-enter`가 `v<N>/` 생성).
5. 공통 템플릿 섹션: Stage/Slug/Version · Goal (1–3줄) · Inputs (절대 경로, missing 표기) · Execution Order (sub-phase 체크리스트) · Parameters (stage knob) · Expected Artifacts · Resource Bounds (시간/디스크/GPU/API 비용) · Success Criteria (Phase C 종료 조건, Report에 그대로 복사) · Risks & Alternatives. Stage-specific 추가 섹션은 각 Phase A 스킬 명세 참조.
6. Phase A 종료 출력: PLAN.md 절대 경로 + 버전 + 목표·Artifacts·성공 기준 3줄 요약 + Prerequisite 경고(있다면) + "PLAN.md 검토 후 피드백 주세요."

### 3.2 Phase B — Alignment (사용자 명시 승인 필수)

1. 사용자 피드백 접수:
   - (a) 사용자가 PLAN.md 직접 편집 → orchestrator가 Read로 diff 감지.
   - (b) 사용자가 수정 요청 → 담당 에이전트 재dispatch해 같은 `v<N>/` 내 PLAN.md 재작성.
2. 피드백 반영 후 "`research/plans/<stage>/<slug>/v<N>/PLAN.md` 이대로 구현해도 될까요?" 프롬프트 + 변경 요약 3줄.
3. **명시 트리거 phrase whitelist**: SSOT = `.claude/scripts/loop_state.py` `TRIGGER_WHITELIST` 상수. 판정은 `python3 .claude/scripts/loop_state.py trigger-check "<phrase>"` (`is_trigger: true` = pass; 대소문자 무관, trim 후 정확 매칭). 매칭 실패 발화는 전부 피드백으로 간주 → Phase A의 (1)로 재진입. 구(句) 추가/삭제 시 loop_state.py와 사용자-지향 사본 `CLAUDE.md` §4.3 두 곳만 갱신 — 그 외 `.claude/` 내부 prompt 파일에는 목록을 복사하지 않는다.
4. **Hard stop**: autonomous 분기 **없음**. 트리거 없이는 Phase C 진입 절대 불가. 4 stage 모두 동일. 매 stage 매 사이클 승인 필요.
5. 트리거 확인 후 `loop_state.py stage-advance --to C --trigger "<phrase>"` 호출.

### 3.3 Phase C — Execution (순차 blocking)

1. 현 stage의 `STAGE_SUBPHASES` 체인을 순차 동기 blocking dispatch.
2. 각 sub-phase 종료 시 `loop_state.py stage-advance` 호출 → `sub_phase` + history 갱신.
3. **금지 패턴**: `Bash(run_in_background=true)`, `TaskCreate` + mid-flight return, background-and-return 선언. 실제 프로세스 증거(`ps`·`loop_state.sub_phase` 변화·새 산출 파일) 없이 진행 선언 금지.
4. **유일 예외**: `/codex:review --background` + `/codex:status` 폴링 (B-2 / E-3 / F-2). orchestrator는 verdict까지 살아서 폴링.
5. 마지막 sub-phase 완료 후 **Report 쌍 생성**:
   - payload JSON 구성 (stage-specific 키는 `references/report-templates.md` 참조).
   - `python3 .claude/scripts/report_builder.py --payload <path.json>` 호출 → `Report.md` + `Report.slides.md` 동시 생성 + `latest` 심볼릭 링크 갱신.
6. `python3 .claude/scripts/loop_state.py stage-complete` 호출 → `stage="idle"`, `inner_phase=null`, `sub_phase=null` 리셋.
7. **최종 출력 (Decision #6 준수)**:
   - `Report.md` + `Report.slides.md` 절대 경로
   - Success Criteria 체크 (✓/✗/NA per 항목)
   - Artifacts 경로 리스트
   - **다음 stage 권장·자동 제안 문구 절대 금지**.

### 3.4 Versioning

- `stage-enter` 시 `research/plans/<stage>/<slug>/v*/` + `research/reports/<stage>/<slug>/v*/`를 glob 스캔 → `max(existing) + 1`을 `stage_version`에 할당.
- PLAN.md·Report.md·Report.slides.md는 전부 `v<N>/` 하위. **기존 버전 수정·삭제 금지**.
- `research/plans/<stage>/<slug>/latest` / `research/reports/<stage>/<slug>/latest` 심볼릭 링크는 최신 버전으로 선택적 갱신 (실패해도 치명적 아님).
- 동일 stage 내 Phase B에서 사용자가 "다시 계획" 요청 시 `stage-restart --to A`로 **같은 `stage_version` 내 재작성** (새 버전 생성 아님).

## 4. Stage별 진입 절차

### 4.1 `/research-papers <topic>`

- 자유 서술형 topic → `YYYY-MM-DD_<slugified-topic>` 자동 slug 생성 또는 `--slug <existing>` 재사용.
- Phase A: paper-hunter가 venue별 쿼리 전략 분해 → PLAN.md(venues·years·keywords·max per venue·triage threshold·예상 수집 개수·RAG reindex 여부). 수집 실행 금지.
- Phase C: A-1 → A-2 → A-3 → A-4. 종료 조건: paper-hunter cursor 완료 OR 신규 0건 연속 2회 OR accepted=0 연속 2회.
- 키워드 전략: orchestrator가 사용자 topic의 canonical 용어 2-3개 축 추출 → paper-hunter `--keywords`. narrow term 금지. 사용자 narrow topic은 A-2 `--topic`에만.

### 4.2 `/research-qa <slug> <question>`

- `$1` = slug (신규 또는 기존), 나머지 = question.
- Phase A: answer-formulator가 hybrid_query dry-run → PLAN.md (질문 재진술·Evidence 개수 타겟 3–7·retrieval 파라미터 k/KG depth·4축 통과 기준 Grounding≥3 AND Support≥3 AND Verifiability≥3). 답변 본문 작성 금지. RAG/KG 비어 있으면 Prerequisite Missing 경고.
- Phase C: B-1 (Direct Answer + Evidence Chain, divergent ideation 금지) → B-2 (critic 4축 + codex-reviewer 병렬 blocking). 통과 Evidence=0이면 최대 3사이클 B-1 재호출.

### 4.3 `/research-experiments <slug>` (내부 3 스킬)

- Phase A: `experiment-design` 스킬 호출 → experiment-planner가 PLAN.md 초안 → critic이 IV/DV/Expected Under/If Wrong 명확성 검토. Evidence↔Experiment 1:1 mapping 테이블 + 수치 범위 사전 명시. 코드·smoke 금지.
- Phase C: `experiment-impl` 스킬 (E-1 code-implementer → E-2 implementation-verifier → E-3 codex-reviewer → smoke test) → `experiment-report` 스킬 (payload JSON → report_builder.py). E-3 reject 시 E-1 `--force` 1회 복귀.
- 리소스 escalation: PLAN이 유료 API 호출을 요구하거나 외부 LLM·LLDM 경로 수정을 요구하면 E-1 진입 전 사용자 명시 승인 대기.

### 4.4 `/research-analyze <slug>`

- Phase A: results-analyst가 PLAN.md (verdict 판정 규칙 CONFIRMED/REFUTED/INCONCLUSIVE/IMPL_BUG · REFUTED 2차 4-way 분류 · 시각화 목록 · revision seed 포맷). 분석 실행 금지.
- Phase C: F-1 results-analyst (verdict matrix + diagnosis.md + revision seed) → F-2 codex-reviewer (adversarial 통계·verdict·seed 재확인). F-2 reject 시 F-1 `--force` 1회.
- 완료 출력에 **Revision seed는 Report.md 본문에 포함**되지만 "다음 커맨드 실행하세요" 제안 금지. 사용자가 수동으로 hand-carry.

## 5. 루프 상태 관리 (v3 schema)

`research/loop_state.json` SSOT: `.claude/scripts/loop_state.py`.

```json
{
  "version": 3,
  "stage": "papers|qa|experiments|analyze|idle",
  "inner_phase": "A|B|C|completed|null",
  "sub_phase": "A-1|A-2|A-3|A-4|B-1|B-2|C-1|E-1|E-2|E-3|F-1|F-2|null",
  "slug": "2026-04-15-dpo-reward-hacking",
  "stage_version": 2,
  "started_at": "...",
  "last_update": "...",
  "history": [
    {"stage":"papers","slug":"...","stage_version":1,"inner_phase":"A","event":"stage-enter","at":"..."},
    {"stage":"papers","slug":"...","stage_version":1,"inner_phase":"C","sub_phase":"A-1","event":"sub-advance","at":"..."}
  ]
}
```

**핵심 필드 5종**: `stage`, `inner_phase`, `sub_phase`, `slug`, `stage_version`. 제거된 필드(v1/v2에서): `iteration`, `autonomous_on` 관련 일체.

**마이그레이션**: `loop_state.py migrate_to_v3()`가 첫 read 시 1회 in-place 변환 + 백업(`loop_state.v<N>.bak.json`).

**서브커맨드**: `stage-enter`, `stage-advance`, `stage-complete`, `stage-restart`, `status`, `show`, `history`, `trigger-check`.

## 6. 중단 조건 (stage별)

다음 중 하나 발생 시 즉시 진행 중단 후 사용자 보고:

1. `qa` B-2에서 3사이클 연속 통과 Evidence 0개 (critic 탈락)
2. `experiments` E-2에서 2회 연속 verifier 실패
3. `experiments` E-3 또는 `analyze` F-2에서 codex-reviewer `reject` 2회
4. `analyze` F-1이 "reproducibility broken" 판정
5. 리소스 한계(유료 API / 외부 LLM·LLDM repo 수정 필요)
6. 사용자 명시 개입 ("멈춰", "pause", "check")

## 7. 다음 사이클 진입 (revision seed)

`analyze` stage가 F-2 approve로 완료되면 Report.md에 revision seed가 기록된다:

| diagnosis outcome | 사용자가 다음에 호출할 수 있는 커맨드 (Claude는 제안하지 않음) |
|---|---|
| 모든 Evidence CONFIRMED (fully supported) | 사이클 종료. 필요 시 새 question으로 `/research-qa` |
| 일부 CONFIRMED, 일부 REFUTED/INCONCLUSIVE (partially supported / needs revision) | `/research-qa` 재호출로 answer revision |
| 모든 Evidence REFUTED (fully refuted, claim wrong) | `/research-qa` 또는 `/research-papers` (주제 재탐색) |
| IMPL_BUG 판정 | `/research-experiments` 재호출 |
| setup error | `/research-experiments` 재호출 (PLAN 수정) |
| data issue | `/research-papers` 재호출 (데이터 재수집) |

**orchestrator는 위 표의 어느 라인도 사용자에게 suggestion으로 출력하지 않는다**. Report.md는 diagnosis + revision seed만 기록하고, 사용자가 표를 읽고 결정.

## 8. 에러 핸들링

- 에이전트 실패: 1회 재시도 후 Report `known_gaps`에 기록하고 진행
- 팀 재구성 실패: 이전 팀 산출물이 파일로 보존되어 있는지 확인 후 재시도
- 파일 산출물 누락: 직전 sub-phase 재실행
- report_builder.py 실패: `stage-complete` 호출 금지, 원인 보고 후 중단
- 컨텍스트 한계: `CLAUDE_APPEND.md` 생성 → `loop_state.json`에 시점 기록 → 재시작

## 9. 참조 문서

- `references/stage-gate.md` — Phase A/B/C 공통 프로토콜, 트리거 whitelist, recovery paths
- `references/report-templates.md` — Report.md + Report.slides.md 4종 템플릿, payload 키
- `.claude/scripts/loop_state.py` — 상태 SSOT (v3 schema)
- `.claude/scripts/report_builder.py` — Report 쌍 생성기
- `.claude/agents/orchestrator.md` — 에이전트 역할
- `docs/harness-layout.md` — 커맨드·에이전트·디렉토리 지도

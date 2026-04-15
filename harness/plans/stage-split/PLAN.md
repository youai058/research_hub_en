# PLAN — Stage-Split Refactor (4 Independent Stage Commands × Per-Stage Phase A/B/C Gate)

> Phase A (계획) 전용 문서 — 이번 revision은 **Phase B 결정 9건을 반영한 최종판**. 구현 금지. 사용자가 "구현해줘" 명시한 이후에만 Phase C(실제 파일 편집)로 이행한다.
>
> 이 파일의 목적: research_hub 하네스를 현재의 단일 자동 체인(`/research-start` → 13 sub-phase auto-advance)에서, **4개 독립 stage 커맨드 + 각 stage 내부 Phase A/B/C 사용자 게이트 + stage별 결과 버전링** 구조로 재설계한다.

---

## 0. 핵심 재설계 한 줄 요약

- **지금**: 한 커맨드(`/research-start`)가 A-1 … F-2 13 sub-phase를 orchestrator를 통해 auto-chain하고, `feedback_autonomous` 플래그가 Phase B 사용자 gate를 우회.
- **이후**: **4개 커맨드** (`/research-papers`, `/research-qa`, `/research-experiments`, `/research-analyze`) 각각이 **독립 단위**로 실행되고, 각 stage 내부에서만 **Phase A(계획) → Phase B(정렬) → Phase C(실행) 사용자 게이트**를 예외 없이 엄수한다. `/research-experiments`는 내부에 **plan/design · impl · report 3 스킬**로 분리된다. stage 간 auto-chain·auto-propose·자동 제안 전면 금지. 재실행은 `v1/ v2/ …` 디렉토리로 누적된다. **autonomous 플래그·`/research-autonomous` 토글·`autonomous.py`·`.local/feedback_autonomous.md`·session_start autonomous 주입 모두 제거**. iteration 카운터도 스키마에서 제거한다.

---

## 1. 현재 구조 요약 (자산과 제약)

### 1.1 지금 있는 것

**Commands (8종)**: `/research-start`, `/research-status`, `/research-rag`, `/research-index`, `/research-autonomous`, `/research-lesson`, `/research-kg`, `/research-triage`.

**Agents (14종)**: orchestrator, paper-hunter, paper-triage, paper-summarizer, rag-curator, answer-formulator, critic, experiment-planner, code-implementer, implementation-verifier, results-analyst, kg-curator, codex-reviewer, harness-engineer.

**Skills (19종)**: research 12 (orchestrate, paper-hunt, paper-triage, paper-summarize, paper-rag, paper-kg, answer-formulate, critique, experiment-plan, code-implement, implementation-verify, results-analyze) + harness-* 7 (skill-author, agent-author, command-author, hooks, mcp, settings, validate).

**Hooks (8종)**: session_start, mark_indices_stale, protect_chroma, protect_kg, protect_external_paths, guard_empty_rag, phase_advance_check, inject_lessons.

**State SSOT**: `.claude/scripts/loop_state.py` — `research/loop_state.json` 관리, 단일 `phase: "A-1".."F-2"|"done"` 값, `ALLOWED_TRANSITIONS`로 정상 전이 강제.

**Autonomous SSOT (제거 예정)**: `.local/feedback_autonomous.md` — `autonomous.py`/`loop_state.py.autonomous_on()`/`session_start.sh`이 참조.

**Artifact 경로** (대부분 유지, 버전링 추가):
- `papers/<V>/<Y>/<slug>.md`·`.raw.md`, `papers/rag/`, `papers/kg/`
- `research/topics/<slug>.md`
- (stage/slug 단위 버전링으로 전환) `research/plans/<stage>/<slug>/v<N>/PLAN.md`
- (stage/slug 단위 버전링으로 전환) `research/reports/<stage>/<slug>/v<N>/{Report.md, Report.slides.md}`
- 기존 평탄 경로 (`research/answers/YYYY-MM-DD_<slug>.md`, `research/critiques/<slug>.md`, `research/diagnoses/<slug>.md`, `research/plans/<slug>/PLAN.md`)는 실험 산출 자체로 남기고 stage 단위 아티팩트는 위 버전 디렉토리로 분리
- `experiments/<slug>/{code,configs,run.sh,IMPL_MAP.md}`, `results_<slug>/` — 기존 유지

### 1.2 지금 아픈 곳

1. **단일 진입점·auto-chain**: `/research-start`는 13 sub-phase 전부를 orchestrator에 맡기고 return. 사용자가 중간에 "답변만 보고 멈춰" 같은 stage 단위 개입 불가.
2. **Autonomous flag의 과대 적용 → 제거 대상**: 현재 autonomous ON이 Phase B 게이트를 없애 A-1부터 F-2까지 통자동화된다. Phase B 원칙이 사실상 무력. **이번 리팩터에서 플래그·토글·스크립트·훅 주입까지 전부 제거**.
3. **Phase A/B/C 게이트 부재**: research_hub의 "Phase A/B/C"가 개별 stage 단위로 존재하지 않고, 각 stage가 자체 PLAN.md와 사용자 승인을 받는 패턴이 없다.
4. **Report 부재 + 버전 관리 없음**: stage 단위 보고서가 없고, 같은 slug를 재실행하면 기존 산출물이 덮어써지거나 헷갈린다.
5. **iteration 개념 불필요**: 전역 iteration 카운터가 stage 간 공유되지만, stage 독립 실행 모델에서는 의미가 없다 — 한 stage 내부에서 재실행 시 version만 증가하면 충분.
6. **선행 조건 검사 산재**: `guard_empty_rag.sh`가 간접 강제하지만 stage 커맨드 수준의 명시적 검사가 없다.
7. **실험 3스킬 미분리**: experiment 관련 작업(plan 설계·구현·보고서)이 하나로 엉켜 있어 재실행·디버그 경로가 불명확.

### 1.3 남길 자산 (건드리지 않음)

- 14 에이전트 페르소나 파일 (dispatch 호출부만 orchestrator/commands에서 재배선).
- 19 skill 중 12 research skill 파일 (orchestrate SKILL.md만 재작성, 그 외는 불변).
- `/research-status`, `/research-rag`, `/research-index`, `/research-lesson`, `/research-kg`, `/research-triage` 6개 커맨드 (관리/조회용). **`/research-autonomous`는 제거 대상이므로 "남길 자산"에서 제외**.
- RAG/KG stack, manifest, SHA256 증분 로직.
- Hooks 중 `mark_indices_stale`, `protect_chroma`, `protect_kg`, `protect_external_paths`, `inject_lessons`는 변경 없음. `session_start`, `phase_advance_check`, `guard_empty_rag`는 신 스키마·autonomous 제거에 맞춰 **수정 필요**.
- `docs/lessons*.md` 및 `.kg.json` append-only 규약.

---

## 2. 새 구조 명세

### A. 4개 Stage 커맨드 인터페이스

각 커맨드는 `.claude/commands/research-<stage>.md` 1개 파일로 정의하고, 내부에서 `python3 .claude/scripts/loop_state.py stage-enter <stage> --slug <slug>`를 호출해 `loop_state.json`을 전이시킨 뒤 orchestrator를 dispatch한다. orchestrator는 **해당 stage의 Phase A/B/C 관리자**로 동작한다.

**공통 규칙**:
- **선행 stage 부재 허용 (Decision #1)**: prerequisite를 강제하지 않는다. 선행 산출물 부재 시에도 stage는 빈 상태로 실행 가능. 단, Phase A 진입 시 orchestrator가 **"선행 산출물 누락 경고"** 블록을 PLAN.md 상단에 삽입하고 사용자에게 "이대로 진행하면 품질이 저하될 수 있다"를 고지.
- **재실행 = 버전 분리 (Decision #5)**: `loop_state.py`가 `research/plans/<stage>/<slug>/`를 스캔해 기존 `v*/` 디렉토리 최대치를 찾아 `v<max+1>/`을 새로 생성한다. Reports도 동일. 덮어쓰기 절대 금지. (옵션) `latest` 심볼릭 링크를 각 stage/slug 디렉토리 루트에 유지.
- **Stage 완료 후 suggestion 금지 (Decision #6)**: Report.md 제시 후 정지. "다음은 `/research-qa` 실행하세요" 류의 제안 문구 금지.

#### A.1 `/research-papers <topic>`

- **입력 인자**: `$ARGUMENTS` = 자유 서술형 topic (예: "DPO fine-tuning reward hacking 2024-2026"). 신규 slug는 커맨드 실행 시 `YYYY-MM-DD_<slugified-topic>` 형식으로 자동 생성, 기존 slug 재사용 시 `--slug <existing>` 플래그.
- **담당 에이전트·스킬**: paper-hunter · paper-triage · paper-summarizer · rag-curator (+ kg-curator staleness 소비). 스킬은 기존 `paper-hunt`, `paper-triage`, `paper-summarize`, `paper-rag` 재사용.
- **Phase A (계획)**: paper-hunter가 topic을 venue별 쿼리 전략으로 분해 → `research/plans/papers/<slug>/v<N>/PLAN.md`에 수집 계획(venues·years·keywords·max per venue·triage threshold·예상 수집 개수·RAG reindex 여부) 작성. **수집 실행 금지**. 사용자에게 PLAN.md 경로 + 3줄 요약 제시.
- **Phase B (정렬)**: 사용자 피드백 반영 → PLAN.md 갱신(버전 동일) → "구현해도 될까요?" 프롬프트. 사용자의 명시 트리거 phrase(§B.2) 대기. **autonomous 경로 없음**.
- **Phase C (실행)**: A-1 paper-hunter → A-2 paper-triage → A-3 paper-summarizer → A-4 rag-curator 순차 blocking 실행. 완료 시 `research/reports/papers/<slug>/v<N>/Report.md` + `Report.slides.md` 생성.
- **산출물 경로**:
  - `research/plans/papers/<slug>/v<N>/PLAN.md`
  - `papers/<V>/<Y>/<slug_per_paper>.raw.md` (A-1)
  - `research/topics/<slug>.md` (A-2 runtime log)
  - `papers/<V>/<Y>/<slug_per_paper>.md` (A-3, 5-part Marp)
  - `papers/rag/manifest.json` 업데이트 (A-4)
  - `research/reports/papers/<slug>/v<N>/Report.md`
  - `research/reports/papers/<slug>/v<N>/Report.slides.md`
- **선행 의존성**: 없음. 언제든 호출 가능.

#### A.2 `/research-qa <slug> <question>`

**기존 `/research-answer` → `/research-qa`로 rename (Decision #3, #9)**. Q&A = Direct Answer + Evidence Chain + 4축 critic 비판.

- **입력 인자**: `$1` = slug (신규 또는 기존). 이후 텍스트 전체는 question. 커맨드 markdown에 `"<slug>" "<question>"` 파싱 규약 명시.
- **담당 에이전트·스킬**: answer-formulator, critic (+ codex-reviewer 병렬). 스킬은 기존 `answer-formulate`, `critique` 재사용.
- **Phase A (계획)**: answer-formulator가 **hybrid_query dry-run**으로 후보 근거 N개를 수집한 뒤, `research/plans/qa/<slug>/v<N>/PLAN.md`에 (1) 질문 재진술, (2) 수집할 Evidence 개수 타겟(3–7), (3) retrieval 파라미터(k, KG depth), (4) 4축 통과 기준(Grounding≥3 AND Support≥3 AND Verifiability≥3) 명세. **답변 본문 작성 금지**. RAG/KG 비어 있으면 선행 산출물 누락 경고를 PLAN.md 상단에 삽입.
- **Phase B (정렬)**: 사용자 피드백 → PLAN.md 갱신 → "구현해도 될까요?".
- **Phase C (실행)**: B-1 answer-formulator (Direct Answer + Evidence Chain 작성, divergent ideation 금지) → B-2 critic 4축 + codex-reviewer 병렬 blocking. 통과 Evidence=0이면 최대 3사이클 B-1 재호출. 완료 시 `research/reports/qa/<slug>/v<N>/{Report.md, Report.slides.md}` 생성.
- **산출물 경로**:
  - `research/plans/qa/<slug>/v<N>/PLAN.md`
  - `research/answers/YYYY-MM-DD_<slug>.md` (실험 산출 본문은 기존 평탄 경로 유지)
  - `research/critiques/<slug>.md`
  - `research/reports/qa/<slug>/v<N>/Report.md`
  - `research/reports/qa/<slug>/v<N>/Report.slides.md`
- **선행 의존성**: 없음이 기본. RAG manifest.files==0 또는 slug 요약 0개면 경고.

#### A.3 `/research-experiments <slug>` — 내부 3스킬 통합

**기존 `/research-plan` + `/research-implement` 통합 (Decision #3)**. Phase A는 plan/design 스킬 산출, Phase B는 사용자 피드백, Phase C는 **구현 스킬 → 보고서 스킬 순차 blocking**.

- **입력 인자**: `$1` = slug.
- **담당 에이전트**: experiment-planner (plan/design), code-implementer (impl), implementation-verifier (impl 내부 QA), codex-reviewer (impl 게이트 + F-2 결과분석 게이트는 analyze에서 담당), results-consolidator 성격의 report 담당(신규 스킬 내부에서 orchestrator가 executes).

##### A.3.1 내부 스킬 분리

| 스킬 | 위치 | 담당 Phase | 호출 에이전트 | 입력 | 출력 |
|---|---|---|---|---|---|
| **experiment-design** | `.claude/skills/experiment-design/SKILL.md` | Phase A | experiment-planner (+ critic 검토) | slug, (있으면) 선행 qa Report, revision seed | `research/plans/experiments/<slug>/v<N>/PLAN.md` (Evidence↔Experiment 매핑, IV/DV/baseline/ablation/Expected Under/If Wrong 사전 명시, 리소스 budget) |
| **experiment-impl** | `.claude/skills/experiment-impl/SKILL.md` | Phase C 전반 | code-implementer → implementation-verifier → codex-reviewer (E-3 gate) → smoke test 실행 | Phase A PLAN.md | `experiments/<slug>/{code,configs,run.sh,IMPL_MAP.md}`, smoke 결과 로그, E-3 verdict 기록 |
| **experiment-report** | `.claude/skills/experiment-report/SKILL.md` | Phase C 후반 | (orchestrator 직접; 별도 에이전트 없음) | Phase A PLAN.md + impl 산출물 + smoke 로그 + IMPL_MAP | `research/reports/experiments/<slug>/v<N>/{Report.md, Report.slides.md}` (plan/impl/result 3섹션 통합) |

각 스킬은 단독 호출 가능해야 하며, 이전 산출물 없이 실행 시 "누락 경고" 블록을 산출물 상단에 삽입 후 진행 (Decision #1).

##### A.3.2 Phase 흐름

- **Phase A (계획)**: `experiment-design` 스킬 호출. experiment-planner가 PLAN.md 초안 작성 → critic이 IV/DV/Expected Under/If Wrong 명확성 검토. **코드 작성·smoke 실행 금지**.
- **Phase B (정렬)**: 사용자 피드백 → PLAN.md 갱신 → "구현해도 될까요?".
- **Phase C (실행)**: 명시 트리거 수신 후:
  1. `experiment-impl` 스킬 실행 — E-1 code-implementer → E-2 implementation-verifier incremental QA → E-3 codex-reviewer adversarial → smoke test `run.sh`. E-3 reject 시 E-1 `--force` 1회 복귀 후 재진행 (최대 1사이클).
  2. `experiment-report` 스킬 실행 — 위 결과를 `research/reports/experiments/<slug>/v<N>/{Report.md, Report.slides.md}` 로 정리.

- **산출물 경로**:
  - `research/plans/experiments/<slug>/v<N>/PLAN.md`
  - `experiments/<slug>/code/`, `configs/`, `run.sh`, `IMPL_MAP.md`
  - `research/reports/experiments/<slug>/v<N>/Report.md`
  - `research/reports/experiments/<slug>/v<N>/Report.slides.md`

- **선행 의존성**: 없음이 기본. qa Report 부재 시 PLAN.md에 경고.

#### A.4 `/research-analyze <slug>`

- **입력 인자**: `$1` = slug.
- **담당 에이전트·스킬**: results-analyst (+ codex-reviewer F-2 최종 게이트). 스킬은 기존 `results-analyze` 재사용.
- **Phase A (계획)**: results-analyst가 `research/plans/analyze/<slug>/v<N>/PLAN.md`에 (1) verdict 판정 규칙(CONFIRMED/REFUTED/INCONCLUSIVE/IMPL_BUG), (2) REFUTED 발생 시 2차 4-way 분류(claim wrong→qa B-1 / impl bug→experiments E-1 / setup error→experiments C-1 / data issue→papers A-1), (3) 시각화 목록(PNG/HTML), (4) revision seed 포맷 정의. **분석 실행 금지**.
- **Phase B (정렬)**: 사용자 피드백 → PLAN.md 갱신 → "구현해도 될까요?".
- **Phase C (실행)**: F-1 results-analyst → F-2 codex-reviewer blocking. F-2 reject 시 F-1 `--force` 1회 복귀. 완료 시 `research/diagnoses/<slug>.md` 확정 + `research/reports/analyze/<slug>/v<N>/{Report.md, Report.slides.md}` 생성. **다음 stage suggestion 출력 금지 (Decision #6)** — Report.md 마지막 섹션은 "Outcome Summary"로 끝내고, 권장 커맨드 라인·자동 chain 전부 제거.
- **산출물 경로**:
  - `research/plans/analyze/<slug>/v<N>/PLAN.md`
  - `research/diagnoses/<slug>.md`
  - 시각화 PNG/HTML (`results_<slug>/` 하위)
  - `research/reports/analyze/<slug>/v<N>/Report.md`
  - `research/reports/analyze/<slug>/v<N>/Report.slides.md`
- **선행 의존성**: 없음이 기본. `results_<slug>/` 비어 있으면 경고.

---

### B. 공통 Phase A/B/C 프로토콜 (Autonomous 경로 전면 제거)

모든 stage 커맨드는 동일한 3-phase 게이트를 따른다. orchestrator 에이전트가 stage context를 받아 이 프로토콜을 강제한다. **Decision #2에 따라 autonomous 분기·feedback_autonomous flag·`.local/feedback_autonomous.md` 참조는 전부 삭제**.

#### B.1 Phase A — Planning

1. 커맨드 진입 시 `loop_state.py stage-enter <stage> --slug <slug>` 호출 → `stage`, `inner_phase="A"`, `version=<new_v>` 기록. 같은 `<stage>/<slug>` 조합이 이미 존재하면 `version = max(existing v) + 1`.
2. 해당 stage의 주 에이전트·스킬이 **PLAN.md만 작성**. 실제 부작용(논문 다운로드, 답변 작성, 코드 생성, 실험 실행, 분석) **금지**.
3. 선행 산출물 부재 감지 시 PLAN.md 상단에 `## ⚠ Prerequisite Missing` 블록 삽입 (무엇이 없고, 진행 시 품질 저하 우려).
4. PLAN.md 템플릿 공통 섹션:
   - **Stage & Slug & Version**: `stage`, `slug`, `version`
   - **목표 (Goal)**: 1–3줄
   - **입력 (Inputs)**: 이전 stage 산출물·사용자 topic/question·외부 의존성 (절대 경로). 누락 항목은 `(missing)` 표기.
   - **실행 순서 (Execution Order)**: sub-phase 체크리스트
   - **파라미터 (Parameters)**: retrieval k, venue list, threshold, smoke scope, judge 등 stage별 knob
   - **예상 산출물 (Expected Artifacts)**: 파일 경로 (버전 디렉토리 포함) + 예상 크기·개수
   - **리소스 한계 (Resource Bounds)**: 시간 상한, 디스크, GPU 여부, API 비용 추정
   - **성공 기준 (Success Criteria)**: Phase C 종료 조건. Report.md에 그대로 복사됨
   - **리스크/대안 (Risks & Alternatives)**
5. 사용자에게 제시 (Phase A 종료 시 화면 출력):
   - PLAN.md 절대 경로 + 버전
   - 목표·Expected Artifacts·성공 기준 3줄 요약
   - 선행 경고 블록 (있다면)
   - "PLAN.md 검토 후 피드백 주세요." 안내

#### B.2 Phase B — Alignment (사용자 명시 승인 필수)

1. 사용자 피드백 방식 2가지 지원:
   - (a) 사용자가 PLAN.md를 직접 편집 (orchestrator가 Read로 diff 감지)
   - (b) 사용자가 Claude에게 수정 요청 → orchestrator가 담당 에이전트에 위임해 PLAN.md 재작성
2. PLAN.md 업데이트 후 orchestrator는 "`research/plans/<stage>/<slug>/v<N>/PLAN.md` 이대로 구현해도 될까요?" 프롬프트 + 변경 요약 3줄.
3. **명시 트리거 phrase whitelist (Decision #2)** — 다음 중 하나와 정확히 매칭되는 발화만 Phase C 진입을 허용:
   - 한국어: `구현해줘`, `실행해줘`, `진행해줘`, `ok 해`, `시작해`, `좋아 진행`, `ok 진행`
   - 영어: `proceed`, `go ahead`, `run it`, `execute`, `ok run it`, `ok proceed`
   - 이외 발화는 전부 피드백으로 간주 → Phase A의 (1)로 재진입.
4. **Hard stop 규칙**: autonomous 분기는 존재하지 않는다. 트리거 phrase 없이는 Phase C 진입 절대 불가. 4개 stage 모두 동일 예외 없음. 사용자가 매 stage마다 승인해야 함 (Decision #2 수용).
5. Phase B 종료 시 사용자에게 제시:
   - 승인된 PLAN.md 경로
   - 다음 수행할 sub-phase 체인 (blocking)
   - "Phase C 시작합니다" 안내 후 즉시 Phase C 진입.

#### B.3 Phase C — Execution

1. `loop_state.py stage-advance --to C` 호출 → `inner_phase="C"`, `sub_phase`를 해당 stage 첫 sub-phase로 설정.
2. orchestrator가 해당 stage의 sub-phase 체인을 **순차 blocking** dispatch. `STAGE_SUBPHASES`(§C.2)로 경계 강제:
   - papers: A-1→A-2→A-3→A-4 → 멈춤
   - qa: B-1→B-2 → 멈춤
   - experiments: C-1(=experiment-design Phase A에서 이미 완료) 이후 Phase C에서는 E-1→E-2→E-3 실행 + experiment-report 스킬 → 멈춤
   - analyze: F-1→F-2 → 멈춤
3. sub-phase 체인 완료 후 orchestrator가 stage별 Report.md + Report.slides.md 생성 (§D 템플릿).
4. `loop_state.py stage-complete` 호출 → `inner_phase="completed"`, `sub_phase=null`, `stage="idle"` 리셋. 다음 stage 진입은 사용자의 다른 slash command 호출로만.
5. Phase C 종료 시 사용자에게 제시 (Decision #6, suggestion 금지):
   - `Report.md` + `Report.slides.md` 절대 경로
   - 성공 기준 체크 요약 (✓/✗/NA)
   - 산출물 경로 리스트
   - **다음 stage 권장·자동 제안 문구 일체 없음**.

---

### C. `loop_state.py` 스키마 변경

#### C.1 신 스키마 (iteration 제거, version 추가 — Decision #7, #5)

```json
{
  "version": 3,
  "stage": "papers|qa|experiments|analyze|idle",
  "inner_phase": "A|B|C|completed",
  "sub_phase": "A-1|A-2|A-3|A-4|B-1|B-2|C-1|E-1|E-2|E-3|F-1|F-2|null",
  "slug": "2026-04-15-dpo-reward-hacking",
  "stage_version": 2,
  "started_at": "2026-04-15T09:00:00+09:00",
  "last_update": "2026-04-15T09:42:00+09:00",
  "history": [
    {"stage":"papers","slug":"...","stage_version":1,"inner_phase":"A","event":"stage-enter","at":"..."},
    {"stage":"papers","slug":"...","stage_version":1,"inner_phase":"C","sub_phase":"A-1","event":"sub-advance","at":"..."}
  ]
}
```

**필드 의미** (5필드 핵심: stage, inner_phase, sub_phase, slug, version):

- `version`: 스키마 버전 (v3 — stage-split + iteration removed + versioning).
- `stage`: 현재 작업 중인 stage. 대기 상태는 `idle`.
- `inner_phase`: stage 내부 A/B/C/completed. `completed`는 stage 종료 직후 상태(다음 커맨드 대기).
- `sub_phase`: `inner_phase=="C"`일 때만 non-null.
- `slug`: 현재 cycle의 slug. stage 간 공유되는 1급 식별자.
- `stage_version`: 현재 `<stage, slug>` 조합의 실행 버전 번호. `stage-enter` 시 `max(existing v of that stage/slug) + 1`로 결정.

**삭제되는 필드 (v1/v2 → v3 마이그레이션)**:
- `iteration` (전역) — 완전 삭제. 전역 cycle 개념 없음.
- `autonomous_on()` 메서드·`.local/feedback_autonomous.md` 참조 — 완전 삭제.

**v1/v2 → v3 마이그레이션**: `phase` / `iteration` 필드를 읽어 `stage`, `inner_phase`, `sub_phase`로 분해하고 `iteration`은 버린다. `stage_version`은 이미 실행된 이전 cycle들을 고려하지 않고 모두 `1`로 초기화 후 `research/plans/<stage>/<slug>/` 스캔으로 덮어쓴다. `loop_state.py`에 `migrate_to_v3()` 함수를 두고 첫 read 시 1회 in-place 변환 + 백업(`loop_state.v1.bak.json` 또는 `.v2.bak.json`).

#### C.2 신 전이 규칙

**Stage 전이** (사용자 커맨드로만):
- `idle → papers|qa|experiments|analyze` : 해당 커맨드 호출.
- `<stage> (inner_phase=completed) → idle` : `stage-complete` 호출 시.
- `X (inner_phase != completed) → Y` : 기본 금지, `--force` 필요.

**Inner phase 전이** (stage 내부):
- `A → B` : PLAN.md 저장 성공 시 자동 (사용자 응답 대기와 독립).
- `B → C` : **명시 트리거 phrase 인식 시에만** (§B.2 whitelist). autonomous 분기 없음.
- `C → completed` : 해당 stage의 마지막 sub-phase 성공 종료 + Report.md·Report.slides.md 작성 완료 시.
- 역방향 (`C → B`, `B → A`) : 사용자가 "다시 계획"·"restart plan" 요청 시 `stage-restart --to A` 허용 (동일 stage_version 내 재작업).

**Sub-phase 전이** (Phase C 내부, stage-bounded):

```python
STAGE_SUBPHASES = {
    "papers":      ["A-1", "A-2", "A-3", "A-4"],
    "qa":          ["B-1", "B-2"],
    "experiments": ["C-1", "E-1", "E-2", "E-3"],  # C-1은 Phase A(design) 완료 시 자동 체크, Phase C에서는 E-1부터 실행
    "analyze":     ["F-1", "F-2"],
}
```

- `sub-advance`는 `STAGE_SUBPHASES[stage]` 내 next만 허용, 경계 넘으면 `stage-complete` 강제.
- `ALLOWED_TRANSITIONS` 구식 FSM은 **전면 폐기**하고 위 mapping + inner phase FSM 2축으로 교체.

**Stage 재실행 규칙 (versioning)**:
- `stage-enter <stage> --slug <existing>` 호출 시 `research/plans/<stage>/<slug>/v*/` 디렉토리를 glob으로 스캔, 최대 번호 + 1을 `stage_version`에 할당.
- PLAN.md·Report.md·Report.slides.md는 모두 `v<N>/` 하위에 생성. 기존 버전 파일 수정·삭제 금지.
- (옵션) `research/plans/<stage>/<slug>/latest` 심볼릭 링크를 최신 버전으로 갱신. 실패해도 치명적 아님.

#### C.3 Autonomous flag 처리 (Decision #2 — 완전 제거)

- `.claude/commands/research-autonomous.md` 삭제.
- `.claude/scripts/autonomous.py` 삭제.
- `.local/feedback_autonomous.md` 삭제 (또는 사용자가 직접 백업).
- `loop_state.py`의 `autonomous_on()`·관련 호출부 삭제.
- `hooks/session_start.sh`에서 autonomous 상태 주입 블록 삭제. 대신 stage·inner_phase·sub_phase·version 4 필드 요약만 출력.
- `CLAUDE.md` §2 "Autonomous Loop" 섹션 삭제, §4 phase 표에서 autonomous 경로 기술 전부 삭제. "Phase A/B/C 게이트는 예외 없이 사용자 명시 승인 필수" 명시.

---

### D. Report 템플릿 (stage별 4종, markdown + Marp 병행 — Decision #4)

Report는 Phase C 종료 시 orchestrator가 두 파일을 동시 생성:
- `research/reports/<stage>/<slug>/v<N>/Report.md` (markdown)
- `research/reports/<stage>/<slug>/v<N>/Report.slides.md` (Marp 슬라이드)

#### D.0 공통 헤더

**Markdown 헤더** (`Report.md`):

```yaml
---
stage: papers|qa|experiments|analyze
slug: <slug>
stage_version: <n>
started_at: <kst>
completed_at: <kst>
plan_path: research/plans/<stage>/<slug>/v<n>/PLAN.md
sub_phase_trace: ["A-1", "A-2", ...]
status: success|partial|failed
---
```

**Marp 헤더** (`Report.slides.md`, 공통 템플릿):

```yaml
---
marp: true
theme: default
paginate: true
size: 16:9
header: "research_hub | <stage> | <slug> v<n>"
footer: "Generated <completed_at_kst>"
style: |
  section { font-size: 22px; }
  h1 { color: #1a1a1a; }
  code { background: #f4f4f4; }
---
```

Marp 본문은 markdown Report의 각 섹션을 슬라이드 단위로 분할 (섹션당 1–3 슬라이드). 테이블은 스크롤 없이 슬라이드 폭에 맞게 축약 (필요 시 "상세: Report.md 참조"로 링크).

**공통 markdown 바디 섹션**:
1. **Executive Summary** (3–5줄)
2. **Success Criteria Check** (PLAN.md의 성공 기준 각 항목에 ✓/✗/NA)
3. **Artifacts Produced** (파일 경로 + 크기/개수)
4. **Deviations from PLAN** (계획 대비 변동 사유)
5. **Known Gaps / Caveats**
6. **Outcome Summary** (이번 실행에서 확인된 결론 — 다음 stage 권장·auto-propose 없음)

#### D.1 `papers` Report

Markdown + Marp 공통 본문 내용:
- 수집 통계: venue×year 매트릭스(요청 vs 실제 수집 vs dedup 후)
- Triage 결과: score 분포 히스토그램(이미지 또는 ASCII), accepted/rejected 목록, threshold
- 요약된 논문 목록 테이블: `slug | venue | year | title | 5-part completeness`
- RAG index 상태: 추가된 chunk 수, 총 files/chunks, embed_model, manifest last_update
- KG delta: 새로 추가된 node 수·type 분포
- 특이사항: PDF 파싱 실패, near-duplicate 의심, venue 분류 불가 사례

Marp 구성: 1 타이틀 슬라이드 → 2 수집통계 → 3 triage 결과 → 4 요약 테이블 (top 10) → 5 RAG/KG delta → 6 Outcome Summary.

#### D.2 `qa` Report

- 질문 재진술 (사용자 원문 + 정규화)
- Direct Answer 전체 본문 (한 문단)
- Evidence Chain 표: `id | claim(30자) | grounding | confidence | verifiability | verification_sketch | cited_papers`
- Critic 4축 점수표: `evidence_id | grounding | support | counter | verifiability | verdict(pass/weak/fail)`
- 통과 Evidence count vs 실패 count
- Codex-reviewer 병렬 verdict 요약 (agreements/disagreements)
- 남은 weak point: 다음 iteration에서 보강할 retrieval gap (단, 권장 커맨드는 안내하지 않음)

Marp 구성: 1 타이틀 → 2 질문·Direct Answer → 3 Evidence Chain (압축) → 4 Critic 점수 → 5 Codex verdict → 6 Outcome Summary.

#### D.3 `experiments` Report (plan/impl/result 3섹션 통합 — Decision #3)

- **Section 1 — Plan**: Evidence → Experiment 매핑 테이블, 각 cell의 IV/DV/Expected Under/If Wrong, resource budget.
- **Section 2 — Implementation**: IMPL_MAP.md 3-way 매핑 요약, 구현 모듈 목록(경로+LoC+외부 repo 통합 여부), verifier 경계 검사 결과(IV/DV shape match).
- **Section 3 — Smoke Result**: smoke test 통과/실패 + 실행 시간, E-3 codex-reviewer verdict(approve/reject + 주요 지적), 남은 TODO 또는 skipped cell.
- Deviations from PLAN (plan→impl 사이 편차)
- Outcome Summary

Marp 구성: 1 타이틀 → 2 Plan 매핑 → 3 IMPL_MAP + 모듈 → 4 Smoke Result → 5 Codex verdict → 6 Outcome Summary.

#### D.4 `analyze` Report

- Experiment × Evidence verdict 매트릭스: `evidence_id | CONFIRMED | REFUTED | INCONCLUSIVE | IMPL_BUG`
- Direct Answer status: fully supported / partially supported / needs revision / fully refuted
- REFUTED 발생 시 2차 4-way 분류 결과 (claim wrong / impl bug / setup error / data issue)
- 시각화 목록 (PNG/HTML 경로)
- Revision seed (다음 qa iteration에 전달할 구조화된 payload: 폐기할 Evidence id, 추가할 조건, reframing 힌트) — **전달은 사용자가 다음 커맨드 호출 시 수동으로. 자동 제안 금지**.
- Codex-reviewer F-2 verdict
- Outcome Summary

Marp 구성: 1 타이틀 → 2 Verdict 매트릭스 → 3 Answer status → 4 4-way 분류 → 5 시각화 썸네일 → 6 Revision seed → 7 Outcome Summary.

---

### E. 에이전트 / 커맨드 / 스킬 / 훅 / 문서 변경 목록 (절대 경로)

#### E.1 신규 파일

**Commands (4개 신규)**:
- `/home1/irteam/sw/research_hub/.claude/commands/research-papers.md`
- `/home1/irteam/sw/research_hub/.claude/commands/research-qa.md`
- `/home1/irteam/sw/research_hub/.claude/commands/research-experiments.md`
- `/home1/irteam/sw/research_hub/.claude/commands/research-analyze.md`

**Skills (3개 신규 — experiments 내부 분리)**:
- `/home1/irteam/sw/research_hub/.claude/skills/experiment-design/SKILL.md` — experiment-planner 호출, Phase A PLAN.md 작성
- `/home1/irteam/sw/research_hub/.claude/skills/experiment-impl/SKILL.md` — code-implementer → implementation-verifier → codex-reviewer → smoke 순차 blocking
- `/home1/irteam/sw/research_hub/.claude/skills/experiment-report/SKILL.md` — plan/impl/result 3섹션 Report.md + Report.slides.md 생성

**Orchestrate 참조 문서 (2개 신규)**:
- `/home1/irteam/sw/research_hub/.claude/skills/orchestrate/references/stage-gate.md` — Phase A/B/C 공통 프로토콜 + 트리거 phrase 판정 규칙 (autonomous 분기 없음)
- `/home1/irteam/sw/research_hub/.claude/skills/orchestrate/references/report-templates.md` — §D 4종 Markdown + Marp 템플릿

**유틸 스크립트 (1개 신규)**:
- `/home1/irteam/sw/research_hub/.claude/scripts/report_builder.py` — Report.md + Report.slides.md 쌍을 자동 생성. stage별 템플릿 선택 + YAML 헤더 주입 + Marp 공통 헤더 적용.

**설계 문서**:
- `/home1/irteam/sw/research_hub/harness/plans/stage-split/PLAN.md` (이 파일)

#### E.2 수정 파일

- `/home1/irteam/sw/research_hub/.claude/agents/orchestrator.md`
  - 자동 chain 로직 제거.
  - 역할을 "stage-scoped Phase A/B/C 관리자"로 재정의.
  - "Phase 진입 규칙" 섹션을 stage별 sub-phase subset으로 교체.
  - autonomous 분기 기술 전체 삭제.
  - stage 완료 시 "다음 커맨드 제안 금지" 규칙 추가.
  - harness-engineer 위임 규칙은 유지.
- `/home1/irteam/sw/research_hub/.claude/skills/orchestrate/SKILL.md`
  - Phase A/B/C 프로토콜과 4 stage 커맨드 매핑 테이블 새로 작성.
  - 트리거 phrase whitelist 명시.
  - Report.md + Report.slides.md 생성 절차(파일 쌍) 명세.
  - versioning 규칙 (`v1/v2/...`) 명시.
  - autonomous 관련 기술 전체 삭제.
- `/home1/irteam/sw/research_hub/CLAUDE.md` §2 / §4
  - §2 "Autonomous Loop" 섹션 **전체 삭제**.
  - §4 Standard Workflow 표를 4 stage × 3 phase × sub-phase 표로 교체 (papers / qa / experiments / analyze).
  - "Phase A/B/C 게이트는 예외 없이 사용자 명시 승인 필수" 문구 추가.
- `/home1/irteam/sw/research_hub/.claude/scripts/loop_state.py`
  - v3 스키마 전환, `migrate_to_v3()` 추가.
  - `iteration` 필드·관련 메서드 완전 삭제.
  - `stage_version` 필드 + `scan_existing_versions()` 로직 추가.
  - `autonomous_on()`·관련 호출부 완전 삭제.
  - `cmd_start` → `cmd_stage_enter`, `cmd_stage_advance`, `cmd_stage_complete`, `cmd_stage_restart`로 분리.
  - `ALLOWED_TRANSITIONS`를 `STAGE_SUBPHASES` + inner-phase FSM으로 교체.
  - `cmd_status` 출력 포맷을 신스키마에 맞춤 (stage/inner_phase/sub_phase/slug/stage_version 5필드만).
  - KG byproduct `_emit_loop_kg`의 node id를 `loop:<slug>-<stage>-v<n>-<inner>-<event>` 형태로 갱신 (iteration 참조 제거).
- `/home1/irteam/sw/research_hub/.claude/hooks/phase_advance_check.sh`
  - 신스키마(`stage`+`inner_phase`+`sub_phase`+`stage_version`) 읽도록 파이썬 블록 수정.
  - advisory 메시지를 "stage-complete 호출 필요" 형태로 재작성.
  - autonomous 관련 분기 삭제.
- `/home1/irteam/sw/research_hub/.claude/hooks/guard_empty_rag.sh`
  - Bash command 정규식 매칭 유지(기존 trigger 목록 그대로).
  - **선행 조건은 경고만, 차단 아님 (Decision #1)** — 사용자가 원하면 빈 상태로도 진행 가능. 훅은 advisory stderr 출력만.
- `/home1/irteam/sw/research_hub/.claude/hooks/session_start.sh`
  - 신스키마 출력 (stage/inner_phase/sub_phase/slug/stage_version).
  - **autonomous 주입 블록 완전 제거** (상태 출력 + 설명 + on/off 메시지 전체).
  - lessons 주입 블록은 유지.
- `/home1/irteam/sw/research_hub/docs/harness-layout.md`
  - Commands 8종 → **10종** (4 신규 stage + 기존 6개: status/rag/index/lesson/kg/triage. research-start·research-autonomous 2종 폐기).
  - 신 디렉토리 `research/reports/<stage>/<slug>/v<N>/` 추가.
  - 신 디렉토리 `research/plans/<stage>/<slug>/v<N>/` (stage-level PLAN, 버전링) vs `research/plans/<slug>/` (experiment-level PLAN, 기존 규약) 구분 명시.
  - Autonomous 관련 기술 전체 삭제.

#### E.3 제거 파일 (Decision #2, #8)

- `/home1/irteam/sw/research_hub/.claude/commands/research-start.md` — **즉시 삭제, 백업 보존 X (Decision #8)**. 대체 경로 안내는 `docs/harness-layout.md`에 "`/research-papers <topic>`으로 cycle 시작" 라인만.
- `/home1/irteam/sw/research_hub/.claude/commands/research-autonomous.md` — **즉시 삭제**.
- `/home1/irteam/sw/research_hub/.claude/scripts/autonomous.py` — **즉시 삭제**.
- `/home1/irteam/sw/research_hub/.local/feedback_autonomous.md` — **즉시 삭제** (또는 사용자가 직접 백업).
- `/home1/irteam/sw/research_hub/.claude/hooks/session_start.sh` 내 autonomous 주입 블록 — **삭제** (위 E.2 수정에 포함).

#### E.4 이름 변경

- `.claude/commands/research-answer.md` (계획상) → `.claude/commands/research-qa.md`로 최종 생성. `/research-answer` 이름은 사용하지 않는다.
- `.claude/commands/research-plan.md` + `.claude/commands/research-implement.md` (계획상) → 통합되어 `.claude/commands/research-experiments.md` 단일 파일.

#### E.5 불변 (참고)

- 14 에이전트 페르소나 파일 내용 불변. 호출부(orchestrator·commands·신규 스킬)만 변경.
- 12개 research skill 중 10개 (paper-hunt, paper-triage, paper-summarize, paper-rag, paper-kg, answer-formulate, critique, experiment-plan, code-implement, implementation-verify, results-analyze) 불변. `orchestrate/SKILL.md`는 수정. `experiment-design/impl/report` 3개는 신규.
- 7개 harness-* skill 불변.
- Hooks `mark_indices_stale.sh`, `protect_chroma.sh`, `protect_kg.sh`, `protect_external_paths.sh`, `inject_lessons.sh` 불변.
- RAG/KG 파일 포맷·매니페스트 불변.

---

## 3. 마이그레이션 체크리스트 (Phase C 진입 시 순차 수행)

- [x] 1. `loop_state.py` v3 스키마 구현 + `migrate_to_v3()` (v1/v2 모두 대응) + `iteration` 필드 제거 + `stage_version` 추가 + `scan_existing_versions()` + unit test
- [x] 2. `loop_state.py`의 `autonomous_on()`·관련 호출부 완전 삭제
- [x] 3. `report_builder.py` 신규 작성 — Report.md + Report.slides.md 쌍 동시 생성, stage별 4 템플릿, Marp 공통 헤더 주입
- [x] 4. `.claude/skills/orchestrate/references/stage-gate.md` 작성 (Phase A/B/C 공통 프로토콜 + 트리거 phrase whitelist, autonomous 분기 없음)
- [x] 5. `.claude/skills/orchestrate/references/report-templates.md` 작성 (§D 4종 markdown + Marp 템플릿)
- [x] 6. 신규 커맨드 4개 작성: `research-papers.md`, `research-qa.md`, `research-experiments.md`, `research-analyze.md` — 각각 (a) preflight 경고 체크(차단 아님), (b) `loop_state.py stage-enter` 호출 + version 할당, (c) orchestrator dispatch 세 블록 구성
- [x] 7. `experiments` 내부 3 스킬 작성: `experiment-design/SKILL.md`, `experiment-impl/SKILL.md`, `experiment-report/SKILL.md` — 각 스킬이 독립 호출 가능하고 PLAN→impl→report 계약을 명시
- [x] 8. `orchestrator.md` 재작성 — stage-scoped Phase A/B/C 관리자로 역할 재정의, 자동 chain·autonomous 분기·suggestion 출력 전부 제거, versioning 규칙 반영
- [x] 9. `orchestrate/SKILL.md` 재작성 — 신 프로토콜·트리거 whitelist·Report 쌍 생성 절차·versioning 반영
- [x] 10. `CLAUDE.md §2 "Autonomous Loop"` 섹션 삭제 + `§4 Standard Workflow` 표 재작성 (4 stage × 3 phase × sub-phase)
- [x] 11. `phase_advance_check.sh` 신스키마 대응 + autonomous 분기 삭제
- [x] 12. `guard_empty_rag.sh` 경고-only 모드로 조정 (차단 해제, Decision #1)
- [x] 13. `session_start.sh` 신스키마 출력 + autonomous 주입 블록 완전 삭제
- [x] 14. `docs/harness-layout.md` 업데이트 (commands 10종, 버전 디렉토리, autonomous 기술 삭제)
- [x] 15. 제거: `/research-start.md`, `/research-autonomous.md`, `autonomous.py`, `.local/feedback_autonomous.md` 4파일 삭제
- [x] 16. versioning 구현 — `research/plans/<stage>/<slug>/v<N>/` 디렉토리 자동 생성 유틸, 덮어쓰기 방지 assert, 선택적 `latest` 심볼릭 링크
- [x] 17. `harness-validate` 스킬 실행 — frontmatter/permissions/hook +x/description 트리거 충돌 없음 확인 (결과: 5 ok / 7 warn / 0 error; warnings는 experiment 계열 신규 스킬의 자연스러운 어휘 중복이며 각 description의 구체 트리거 phrase가 서로 다르므로 허용)
- [x] 18. 4 stage smoke test — 각 stage를 dummy slug로 Phase A→B→C 왕복, Report.md + Report.slides.md 생성 확인, `loop_state.json`이 `idle`로 복귀, 같은 slug 재실행 시 `v2/` 생성 확인
- [x] 19. v1/v2 → v3 마이그레이션 리허설 — 실제 `research/loop_state.json` 백업 후 `migrate_to_v3()` 실행, iteration 필드 제거 및 stage_version 초기화 결과 검증
- [x] 20. `docs/lessons.md`에 "stage-split refactor" 항목 append (설계 원칙 + stage 내부 A/B/C 게이트 엄수 + autonomous 폐기 근거 + versioning 규약)
- [x] 21. codex-reviewer `/codex:review` adversarial 검토 — 전체 변경셋의 재현성·경계 검토 (APPROVED with 9 non-blocking Minors + 7 regression risks, 2026-04-15 KST)

---

## 4. Phase B 결정 반영 (Q1–Q8 해결)

아래 표는 이전 revision §4에 있던 Q1–Q8에 대한 **사용자 확정 결정 (Phase B)** 을 정리한 것이다.

| # | 이전 Q | 사용자 결정 | 근거 | 반영 위치 |
|---|---|---|---|---|
| 1 | Q1. 선행 stage 강제? | **허용 (prerequisite 강제 없음)**. 누락 시 경고만. | 유연성·독립 실행 원칙 | §2.A 공통 규칙, §E.2 `guard_empty_rag.sh` 경고 전환 |
| 2 | Q2. autonomous flag 운명 | **완전 제거** (토글·스크립트·파일·session_start 주입 모두) | stage 게이트 단순화; autonomous의 의미 없음 | §B, §C.3, §E.3 |
| 3 | Q3. stage 이름 | **papers / qa / experiments / analyze (4개)**. `/research-qa`는 기존 answer에서 rename. `experiments`는 plan+implement 통합 + 내부 3 스킬. | Q&A 의미 명확화, plan/impl 엉킴 해소 | §2.A 전체, §E.1, §E.4 |
| 4 | Q4. Report 형식 | **markdown + Marp 병행**. 두 파일 동시 생성. | 문서 보존 + 발표 즉시 활용 | §D, §E.1 `report_builder.py` |
| 5 | Q5. 재실행 = 덮어쓰기 vs 버전 | **버전 분리 (`v1/v2/v3/...`)**, 덮어쓰기 금지, `latest` 선택적 링크. PLAN.md·Report.md·Report.slides.md 모두 버전링. | 재현성·실험 기록 보존 | §2.A 공통 규칙, §C.1 `stage_version`, §C.2 versioning 규칙 |
| 6 | Q6. 다음 stage 자동 제안 UX | **제안 금지 (Outcome Summary에서 종료)**. Claude가 다음 커맨드 라인을 출력하지 않는다. | 사용자 주도권 유지 | §2.A 공통 규칙, §B.3, §D.4 |
| 7 | Q7. iteration 카운터 증가 시점 | **iteration 카운터 자체 제거**. 전역 cycle 개념 폐지. stage 재실행은 `stage_version`만 증가. | 단순화, 오용 방지 | §C.1 (필드 삭제), §E.2 `loop_state.py` |
| 8 | Q8. v1→v2 마이그레이션 백업 보존 | **기존 `/research-start` 즉시 삭제, 백업 X**. autonomous 관련 파일도 동일. | 레거시 정리 | §E.3 |
| 9 | (정리) stage 최종 목록 | **papers / qa / experiments / analyze (4개)** | Decision #3 정규화 | 전 문서 |

**남은 미해결 질문**: 없음. Phase B 결정 완료.

**후속 참고 사항 (결정 불필요, 구현 시 주의)**:
- `v<N>/latest` 심볼릭 링크는 플랫폼(Linux)에서 항상 작동하지만, 일부 편집기·RAG manifest 참조는 실제 버전 경로를 저장하는 것을 권장.
- `stage_version`과 `research/plans/<stage>/<slug>/v<N>/` 디렉토리의 **일관성 검증**은 `loop_state.py stage-enter` 시 assert로 보장. 수동으로 디렉토리를 만든 경우(예: 사용자가 v3 디렉토리 미리 생성) 경고 출력 후 다음 번호로 이동.

---

## 5. 리스크 & 완화

- **리스크 1**: v1/v2 → v3 마이그레이션 중 `loop_state.json` 손상 → 루프 상태 유실.
  - **완화**: 마이그레이션 함수에 atomic write + 백업(`loop_state.v1.bak.json` / `.v2.bak.json`) + schema_version 검증 + rollback 경로.
- **리스크 2**: stage 커맨드가 늘어(4+관리 6=10개) 사용법 혼란.
  - **완화**: `/research-status`에 "현재 stage, 진행 중인 sub_phase, 최신 stage_version" 출력. `docs/harness-layout.md`에 4 stage 의사결정 트리 추가.
- **리스크 3 (신규, autonomous 제거 발 UX 피로)**: 모든 stage마다 사용자가 트리거 phrase를 타이핑해야 함 → 긴 세션에서 피로도 증가.
  - **완화**: (a) stage 수를 5→4로 축소하여 승인 횟수 감소. (b) orchestrator가 Phase B 프롬프트에 "다음 단계 요약 + 트리거 phrase 예시" 3줄을 고정 포맷으로 제시해 타이핑 부담 최소화. (c) whitelist에 짧은 phrase(`proceed`, `진행해줘`) 포함.
- **리스크 4**: 기존 orchestrator.md의 "블로킹 dispatch 계약"이 stage-scoped로 축소되면서 기존 자동 루프 테스트 사례가 깨짐.
  - **완화**: Phase C 마이그레이션 전에 orchestrator.md의 블로킹 계약 섹션을 "stage 내부 Phase C sub-phase chain은 blocking" 으로 한정 재작성. 자동 stage 체인·autonomous 분기 모두 명시적으로 금지.
- **리스크 5**: `/research-start` 즉시 폐기 시 기존 세션 스크립트·shortcut이 깨짐 (Decision #8, 백업 X).
  - **완화**: `docs/harness-layout.md` 맨 앞에 "단종 커맨드" 안내 + 매핑 테이블 삽입 (research-start → research-papers, research-autonomous → 기능 폐지). 유저가 우연히 호출하면 slash command 미인식 에러만 발생.
- **리스크 6**: `guard_empty_rag.sh`가 skill 스크립트 경로 매칭으로 Phase C 중간에 발화 → 경고만 띄우고 중단은 안 됨(Decision #1). 발화 빈도 증가로 stderr 잡음.
  - **완화**: 훅 출력에 `[advisory only]` 프리픽스 + 사용자 설정으로 silencing 가능하도록 env var `RESEARCH_HUB_GUARD_QUIET=1` 지원.
- **리스크 7 (신규, versioning 발 디스크 증가)**: 같은 slug를 수십 번 재실행하면 `v1..vN`이 누적되어 `research/plans/`, `research/reports/` 크기 증가.
  - **완화**: (a) PLAN.md + Report.md + Report.slides.md는 텍스트라 크기 미미(수십 KB). (b) 대용량 산출물(`experiments/<slug>/code`, `results_<slug>/`)은 기존 평탄 경로 유지(버전링 비대상)이므로 디스크 영향 제한적. (c) `docs/harness-layout.md`에 "60일 이상 된 stage 버전 디렉토리는 수동 정리 권장" 가이드 추가.
- **리스크 8 (신규, 선행 stage 없이 호출 시 품질 저하)**: 사용자가 `/research-qa`를 `/research-papers` 없이 호출하면 RAG가 비어 있어 Evidence 수집 불가능 → 실패가 뻔함.
  - **완화**: PLAN.md 상단 `⚠ Prerequisite Missing` 블록 + Phase B에서 사용자에게 "RAG 비어 있음, 그래도 진행하시겠습니까?" 재확인 프롬프트. 결정 권한은 사용자.

---

## 6. 성공 기준 (이 리팩터의)

1. **4개 stage 커맨드**가 각자 단독 실행 가능하며, 끝에서 정확히 정지한다 (auto-chain 금지 증명: stage 완료 후 `loop_state.json.stage == "idle"`, "다음 커맨드 권장" 문구 Report에 없음).
2. 각 stage 실행 시 `research/plans/<stage>/<slug>/v<N>/PLAN.md`가 Phase A에서 생성되고, 사용자 명시 트리거 phrase 없이는 Phase C에 진입하지 않는다 (autonomous 분기 부재 증명 포함, 트리거 테스트 4+ phrase 통과).
3. 각 stage 완료 시 `research/reports/<stage>/<slug>/v<N>/Report.md` + `Report.slides.md` **쌍**이 존재하며 공통 헤더 + 섹션 + Marp 헤더 준수.
4. 같은 `<stage>/<slug>` 조합을 재실행하면 `v<N+1>/`이 새로 생성되고 이전 버전은 그대로 보존된다 (덮어쓰기 없음 증명: v1 Report.md 변경 없음 확인).
5. `loop_state.py` v3 스키마가 v1/v2를 무손실 마이그레이션하며, `iteration` 필드·autonomous 참조가 완전히 사라진다. 5필드(`stage` / `inner_phase` / `sub_phase` / `slug` / `stage_version`)만 유지.
6. autonomous flag·`/research-autonomous`·`autonomous.py`·`.local/feedback_autonomous.md`·`session_start.sh` autonomous 블록이 **파일·코드·문서·훅 전방위에서 모두 삭제**되었고 references 없음 (grep으로 검증).
7. `experiments` 내부 3 스킬(design/impl/report)이 독립 호출 가능하며 각각의 입출력 계약이 문서화.
8. `harness-validate` 스킬이 전체 구조 통과.
9. `/codex:review` adversarial 리뷰 approve.

---

*모든 날짜는 한국 시간(KST). 이 PLAN은 Phase B 결정 9건을 반영한 Phase A 산출물이다. 사용자가 "구현해줘" 명시한 이후에만 Phase C 실행(마이그레이션 체크리스트 21개 항목)으로 들어간다.*

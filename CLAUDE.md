# CLAUDE.md — Research Hub

> Always think and reason in English. 단, 사용자 응답은 한국어.

> **SCOPE**: research_hub 전용. `/home1/irteam/sw/CLAUDE.md`는 LLDM 공격 프로젝트의 것이며 이 하네스와 무관하다. 에이전트·스킬은 sw/CLAUDE.md를 참조하지 않는다.

## 1. 역할 (Research Goals)

이 워크스페이스는 **일반 AI/NLP 연구 루프**를 위한 독립 하네스다. 기존 LLDM 공격 연구(`/home/irteam/sw/`)와 **완전히 분리**되어 있다. 루프의 목적은 **사용자가 준 연구 질문에 대한 근거 기반 직접 답변을 만들고, 그 답변의 각 근거(Evidence)를 실험으로 검증하는 것**이다. 새 연구 주제나 가설을 divergent하게 생성하지 않는다. 다음 5단계를 반복한다.

1. **논문 서치**: 주요 AI/NLP venue 6개(NeurIPS / AAAI / ICLR / ICML / ACL / EMNLP)를 **기본 수집 대상**으로 스캔한다. A-1 paper-hunter는 accepted 논문의 **메타데이터·abstract**를 `papers/metadata/<Venue>/<Year>/<slug>.raw.md` (예: `ICLR/2025`, `ICML/2025`)에 수집하고, 이후 A-3 paper-summarizer가 **full-text PDF 기반 adaptive Marp 요약**을 `papers/marp-summary/<Venue>/<Year>/<slug>.md`로 생성한다. 기본 동작은 whitelist 6개에 한정되며, workshop·ACL Findings·arXiv preprint 등 non-whitelist 논문과 arXiv 키워드 수집은 **사용자가 `/research-papers <topic> --include-arxiv` 플래그를 명시했을 때만 opt-in**으로 hunter 단계는 `papers/metadata/etc/<Year>/<slug>.raw.md`에, summarizer 단계는 `papers/marp-summary/etc/<Year>/<slug>.md`에 함께 수집된다 (연도만 하위 계층, 평탄 구조; frontmatter `venue`는 원문, `venue_class: "etc"`). 플래그가 없으면 openreview/anthology 스캔 중 etc 분류된 결과는 drop하고 arXiv 소스는 실행조차 하지 않는다. **리스팅(paper-hunter)은 abstract·API 메타만으로 판단·분류·dedup해도 되며, venue 분류 불가 / near-duplicate 의심 / relevance 애매 같은 경우에만 PDF 첫 2–3페이지를 optional하게 fetch한다.** 실제 5-part 요약(paper-summarizer)은 **반드시 full-text PDF**를 pymupdf로 파싱해 Marp 포맷으로 작성하고 RAG 벡터 스토어에 인덱싱한다. `papers/arXiv/`·`papers/OpenReview/`·`papers/preprint/`·`papers/workshop/`·`papers/findings/` 같은 소스·속성 기반 디렉토리는 만들지 않는다.
2. **답변 formulate + 근거 비판**: 사용자 질문을 seed_question으로 받아 hybrid_query(RAG+KG)로 근거를 수집. answer-formulator가 Direct Answer(한 문단, 구체 수치·조건) + Evidence Chain(3-7개, 각 grounding/confidence/verifiability/verification_sketch)을 작성. **Divergent ideation 금지** — 새 가설·방법·데이터셋을 발명하지 않음. 이후 critic이 4축(Grounding Validity / Support Strength / Counter-Evidence / Verifiability)으로 각 Evidence를 독립 비판하며 Grounding≥3 AND Support≥3 AND Verifiability≥3를 통과해야 한다.
3. **Evidence verification 실험 계획**: 통과한 각 Evidence point에 대해 **1:1로 검증 실험**을 설계. PLAN.md의 각 cell = 정확히 하나의 Evidence. IV/DV/control/baseline/ablation과 **Expected Under(evidence 참) / If Wrong(반박)** 수치 범위를 사전 명시하여 post-hoc 해석을 원천 차단. weak-flagged Evidence는 우선 배치.
4. **실험 코드 구현**: 외부 논문 코드 통합, `experiments/<slug>/code/`에 최소 침습 통합. `IMPL_MAP.md`로 **Evidence ↔ Experiment ↔ Code 3-way 매핑** 추적. 각 Experiment에 `decide_verdict()` 함수가 PLAN의 Expected Under/If Wrong 수치를 그대로 사용해 CONFIRMED/REFUTED/INCONCLUSIVE 반환. implementation-verifier가 incremental QA.
5. **Evidence 검증 결과 분석**: 각 Experiment × Evidence 쌍을 CONFIRMED/REFUTED/INCONCLUSIVE/IMPL_BUG 중 하나로 판정. Direct Answer status = {fully supported / partially supported / needs revision / fully refuted} 중 하나. REFUTED 발생 시 2차 4-way 실패 분류(claim wrong → B-1 revision / impl bug → E-1 / setup error → C-1 / data issue → A-1), PNG·HTML 시각화, diagnosis 산출. 다음 iteration의 answer-formulator가 쓸 revision seed(폐기할 Evidence id, 추가할 조건)를 명시.

---

## 2. 작업 원칙

### Phase A/B/C 게이트 (예외 없이 사용자 명시 승인 필수)

이 하네스는 **stage-scoped 수동 게이트 모드**로 동작한다. 4개 독립 stage 커맨드(`/research-papers`, `/research-qa`, `/research-experiments`, `/research-analyze`)는 각각 Phase A(PLAN.md) → Phase B(사용자 승인 대기) → Phase C(sub-phase 체인 blocking) → Report.md + Report.slides.md 쌍 생성으로 한 사이클을 완결한다. **Autonomous 모드·자동 chain·플래그·토글은 모두 폐기됐다** (v3 refactor). 각 stage마다 사용자가 명시 트리거 phrase(§4 "Phase B 트리거 whitelist")를 발화해야 Phase C가 시작된다. 다음 항목은 추가로 사용자 확인이 필요하다:

- `LLM/`, `LLDM/` 같은 외부 프로젝트 경로 수정
- `~/.claude/` user global 설정 변경
- 외부 API 유료 호출

### 계획 우선
- 3단계 이상 구조적 결정 → Phase A부터. orchestrator가 관리.
- 잘못되면 즉시 멈추고 재계획. 밀어붙이지 않음.

### 완료 전 검증
- 작동 증명 없이 완료 표시 금지.
- 각 Phase 종료 전에 산출물 존재 확인.

### 단순함 우선
- 최소 침습 구현. 기존 convention 유지.
- 근본 원인 탐색. 임시방편 금지.

### 자기개선 루프 (lessons)

사용자 수정 또는 실패 패턴 발견 시 해당 도메인의 `docs/lessons*.md`에 **즉시 append**한다. 같은 실수를 반복하면 에이전트 설계 실패로 간주.

| 파일 | 도메인 | 커버 에이전트 |
|---|---|---|
| `docs/lessons.md` | 전역 (워크플로우·메타) | 전체 |
| `docs/lessons-paper.md` | 논문 수집·요약·RAG | paper-hunter, paper-summarizer, rag-curator |
| `docs/lessons-research.md` | 답변·근거 비판·계획 | answer-formulator, critic, experiment-planner |
| `docs/lessons-impl.md` | 코드 구현·검증 | code-implementer, implementation-verifier |
| `docs/lessons-analysis.md` | 결과 분석 | results-analyst |

각 `lessons-*.md`는 선택적으로 같은 디렉토리에 `<name>.kg.json` 부산물을 가질 수 있으며, kg-curator가 이를 증분 ingest한다. 승격 기준: 에이전트가 Rule/Why/When to apply 3-line 엔트리를 작성할 때, 해당 엔트리가 **재사용 가능한 지식 노드**(Method / Dataset / Metric / Failure-mode 등)를 포함하면 KG 노드로도 방출한다.

규칙:
1. **세션 시작 시**: SessionStart 훅이 `lessons.md` 항목 수를 자동 주입. 에이전트는 활성화 시 전역 `lessons.md` + 자기 도메인 파일을 반드시 Read.
2. **수정 받으면**: `/research-lesson <domain> "<title>"` 명령 또는 수동 append. 포맷 3-lines (Rule/Why/When to apply).
3. **Append-only**: 기존 항목 삭제 금지. 효력 없어지면 `superseded` 표시만.
4. **폴백**: 도메인 불명확하면 `lessons.md` (전역)에 기록.

---

## 3. Environment

- **Conda env**: `LLDM` (기존 환경 재사용). 필요 패키지: `chromadb`, `sentence-transformers` (bge-m3), `arxiv`, `openreview-py`, `pymupdf` (PDF 파싱).
- **경로**: `/home/irteam/sw/research_hub/` (symlink 원본: `/home1/irteam/sw/research_hub/`)
- **API 키**: `/home/irteam/sw/.env` (공용). OpenReview 계정 필요 시 `OPENREVIEW_USERNAME`, `OPENREVIEW_PASSWORD`.
- **HF cache**: `/home/irteam/.cache/huggingface` (공용)

---

## 4. Standard Workflow (4 stage × 3 phase × sub-phase)

모든 비자명 작업은 **stage 커맨드** 단위로 진행된다. Orchestrator는 한 번 dispatch에 하나의 stage에 대한 Phase A/B/C 전체를 관리하며, **stage 간 auto-chain·autonomous 분기·다음 커맨드 suggestion은 일체 금지**다. 재실행은 `research/plans/<stage>/<slug>/v<N>/`·`research/reports/<stage>/<slug>/v<N>/` 디렉토리로 버전 누적된다.

### 4.1 Stage × Phase 매핑

| Stage | 커맨드 | Phase A (Planning) | Phase C (Execution — STAGE_SUBPHASES) | 산출물 |
|---|---|---|---|---|
| `papers` | `/research-papers <topic>` | **Step 1.5 topic-refine (Socratic interview, main session)** → paper-hunter가 `research/plans/papers/<slug>/v<N>/PLAN.md` 작성 (topic.json 기반) | A-1 paper-hunter → A-2 paper-triage (`--topic-spec`) → A-3 paper-summarizer → A-4 rag-curator | `research/topics/<slug>.topic.json` + `papers/marp-summary/<V>/<Y>/*.md` + `research/reports/papers/<slug>/v<N>/{Report.md, Report.slides.md}` |
| `qa` | `/research-qa <slug> <question>` | answer-formulator가 `research/plans/qa/<slug>/v<N>/PLAN.md` 작성 (hybrid_query dry-run, 답변 본문 금지) | B-1 answer-formulator (Direct Answer + Evidence Chain 3–7) → B-2 critic (+ codex-reviewer 병렬 4축) | `research/answers/`·`research/critiques/` + `research/reports/qa/<slug>/v<N>/{Report.md, Report.slides.md}` |
| `experiments` | `/research-experiments <slug>` | `experiment-design` 스킬 내 experiment-planner + critic이 `research/plans/experiments/<slug>/v<N>/PLAN.md` 작성 (Evidence↔Experiment 1:1, Expected Under / If Wrong 수치) | `experiment-impl`: E-1 code-implementer → E-2 implementation-verifier → E-3 codex-reviewer → smoke test; 후속 `experiment-report` 스킬 | `experiments/<slug>/{code,configs,run.sh,IMPL_MAP.md}` + `research/reports/experiments/<slug>/v<N>/{Report.md, Report.slides.md}` |
| `analyze` | `/research-analyze <slug>` | results-analyst가 `research/plans/analyze/<slug>/v<N>/PLAN.md` 작성 (verdict 규칙·REFUTED 4-way 분류·revision seed 포맷) | F-1 results-analyst → F-2 codex-reviewer | `research/diagnoses/<slug>.md` + `research/reports/analyze/<slug>/v<N>/{Report.md, Report.slides.md}` |

### 4.2 Phase A/B/C 프로토콜 (공통)

- **Phase A**: 담당 에이전트가 PLAN.md만 작성. 부작용(논문 다운로드·답변 작성·코드 생성·실험 실행) 금지. 선행 산출물 부재 시 `⚠ Prerequisite Missing` 블록 삽입 (차단 아님, 경고만). **papers stage는 Phase A 앞에 Step 1.5 topic-refine interview가 실행되어 `research/topics/<slug>.topic.json`을 생성하며, PLAN.md는 이 스펙을 canonical 입력으로 쓴다.**
- **Phase B**: 사용자 피드백 반영 → "이대로 구현해도 될까요?" 프롬프트. **명시 트리거 phrase 없이는 Phase C 진입 절대 불가**.
- **Phase C**: `STAGE_SUBPHASES` 체인을 순차 blocking dispatch → 마지막 sub-phase 종료 후 Report 쌍 생성(`report_builder.py`) → `loop_state.py stage-complete` → `idle` 복귀. **다음 stage 권장 문구 출력 금지** (Decision #6).

### 4.3 Phase B 트리거 whitelist (대소문자 무관, trim 후 정확 매칭)

- 한국어: `구현해줘`, `실행해줘`, `진행해줘`, `ok 해`, `시작해`, `좋아 진행`, `ok 진행`, `진행해`
- 영어: `proceed`, `go ahead`, `run it`, `execute`, `ok run it`, `ok proceed`

판정은 `python3 .claude/scripts/loop_state.py trigger-check "<phrase>"`. 이외 발화는 전부 피드백으로 간주 → Phase A 재진입.

> 위 목록은 `.claude/scripts/loop_state.py`의 `TRIGGER_WHITELIST` 상수와 동기 유지. 구(句) 추가/삭제 시 두 곳(본 §4.3 + `loop_state.py`)만 갱신하며 `.claude/agents`·`.claude/skills` 내 prompt 파일에는 사본을 두지 않는다.

### 4.4 loop_state.json v3 schema (5 핵심 필드)

`stage` / `inner_phase` / `sub_phase` / `slug` / `stage_version`. `iteration` 필드·autonomous 참조는 완전히 제거됨. v1/v2 상태는 `loop_state.py migrate_to_v3()`가 첫 read 시 in-place 변환 + 백업.

### 4.5 중단 조건

- `qa` B-2 3사이클 연속 통과 Evidence 0개
- `experiments` E-2 2회 연속 verifier 실패
- `experiments` E-3 또는 `analyze` F-2 codex-reviewer `reject` 2회
- 리소스 한계(유료 API / 외부 LLM·LLDM 수정)
- 사용자 명시 개입 ("멈춰", "pause", "check")

---

## 5. Directory Structure

전체 디렉토리·파일 배치는 `docs/harness-layout.md` 참조.

---

## 6. 핵심 규칙

### RAG Stack
- **Embedding**: BAAI/bge-m3 (sentence-transformers)
- **Store**: ChromaDB PersistentClient at `papers/vector_db/chroma`
- **Chunking**: 섹션 단위 + 수식/표 블록 보존. chunk_size ~1200 tokens.
- **증분 갱신**: `manifest.json`에 파일 경로 → SHA256 저장. rag-curator가 변경된 것만 upsert.
- **쿼리 인터페이스**: `python3 .claude/skills/paper-rag/scripts/query.py "<question>" --k 5`

### Paper Sources
- **arXiv**: `arxiv` Python 패키지로 쿼리 (키워드 + 카테고리 + 날짜)
- **OpenReview**: `openreview-py`로 venue ID 기반 논문 목록
- 두 소스는 정규화된 제목 + arXiv ID로 dedup

### Adaptive Summary Template
모든 논문 요약 파일은 **논문별 adaptive outline**을 가진다 (상세는 `paper-summarize` 스킬). 고정 6-part 템플릿은 폐기됨 (2026-04-16).

**공통 구조**:
- Marp frontmatter (`marp: true`, PPT 호환 유지)
- 최상단 `<!-- PLANNING: ... -->` 주석 블록 (planning-first 검증용 — **SECTIONS + IMAGE_SOURCES 서브블록 모두** 가진다)
- H1 lead 슬라이드 (title, authors, venue, links)

**Planning-first 워크플로우**: 본문 작성 전에 PLANNING 블록을 먼저 설계한다. PLANNING은 (1) SECTIONS 서브블록에서 모든 섹션 번호·제목·이미지 배치(`[Figure N]` 또는 `[no image]`)를 upfront로 결정, (2) IMAGE_SOURCES 서브블록에서 SECTIONS에 등장한 각 figure의 경로와 한 줄 용도를 기록한다. 이후 본문은 PLANNING 그대로 구현하며 도중 재배치 금지.

**필수 앵커 4개 (제목 변형 허용, 순서 고정)**:
1. **TL;DR** — H1 lead 직후 첫 콘텐츠 슬라이드, `> ` blockquote 한두 문장
2. **Method** — 핵심 idea + 수식 verbatim + pseudocode/figure 참조
3. **Result** — 수치 표는 반드시 Markdown 표 (이미지 스크린샷 금지)
4. **Critical Reading** — 논문의 부족한 부분 3~5 bullet (full-text 기반)

**앵커 사이 자유 섹션** — 논문 흐름에 맞게 0개 이상: Motivation / Observation / Experiments Setup / Analysis / Discussion / Conclusion 또는 narrative 한국어 H2 ("왜 이 문제가 어려운가", "핵심 아이디어는 무엇인가").

**이미지 규칙**:
- **섹션당 이미지 ≤1장**. Method / Motivation / Observation / Analysis 계열에 주로 배치.
- Result / TL;DR / Critical Reading / Lead는 기본 `[no image]` — 결과 수치는 figure가 있어도 별도 Markdown 표로 옮긴다.
- 사용 가능한 figure는 digest frontmatter의 `figures:` YAML 리스트(`{label, path, section_hint, reason}`)에만 존재하는 것들이며, 파일명 규칙은 `.figure_cache/<slug>__fig<N>.png`.
- digest `figures: []`(빈 리스트)이면 PLANNING의 모든 섹션을 `[no image]`로 두고 이미지 삽입 생략.

**Keywords (RAG용)**: 선택 — 쓸 때만 말미에 abstract 기반 10~15개.

**문체**: 한영 code-switching + 음슴체(~임, ~함, ~됨). 한국어 문장 + 영어 technical term. 어색한 완역 금지. 상세는 `paper-summarize` 스킬 "문체 규칙" 참조.

### Working Norms
- 새 코드는 configurable path + CLI arg — 머신별 경로 하드코딩 금지
- 모든 에이전트는 `model: opus`
- 서브프로젝트가 git repo인지 확인 후 git 액션 제안
- 실험 디렉토리에서 공격 방식·타겟·데이터셋·seed·커맨드 복구 가능해야 함

### Response Style
- 간결·기술적. 파일 경로/명령 정확히 명시.

---

## 7. 에이전트 팀 구성

14 에이전트 (연구 루프 12 + codex-reviewer + harness-engineer) + phase 매핑 표는 `docs/harness-layout.md` 참조. 상세 워크플로우는 `orchestrate` 스킬.

---

*모든 날짜는 한국 시간(KST) 기준.*

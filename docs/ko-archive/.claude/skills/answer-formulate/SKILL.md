---
name: answer-formulate
description: "사용자 연구 질문에 대한 근거 기반 직접 답변 formulate. 새 연구 주제·가설 생성 금지. hybrid_query로 RAG/KG 근거 수집 → Direct Answer + Evidence Chain (3-7개, grounding/confidence/verifiability/verification_sketch) 생성. answer-formulator 전용. 트리거: '답변 정리', '근거 생성', '연구 질문 답변', 'evidence chain', 'answer formulation'."
---

# Answer Formulate Skill

사용자가 cycle 시작 시 준 **연구 질문**에 대해, 논문 RAG/KG 근거를 바탕으로 **직접 답변 + 근거 체인**을 작성하는 절차. 새 연구 아이디어·가설 생성은 **금지**한다.

## 목적 대비 (Scope)

| 하는 것 | 하지 않는 것 |
|---|---|
| 사용자 질문에 직접 답변 | 새 연구 주제 제안 |
| 근거 3~7개, 각 citation 링크 | Novelty 점수·duplicate 체크 (divergent critique) |
| 각 근거에 실험 검증 스케치 | Hypothesis 변형·확장 |
| 질문이 커버 못한 Open Sub-Question 기록 | Divergent ideation / 브레인스토밍 |

> **새 연구 주제 생성 금지**: 질문이 "X는 왜 Y인가"라면 답은 "Y인 이유는 A, B, C 근거 때문"이어야 하고, "X의 다른 변형을 연구해보자" 같은 후보 3-5개 생성은 하지 않는다.

## 입력

- `loop_state.json`의 `current_slug`와 orchestrator가 보관한 **seed_question** (사용자 원문)
- RAG/KG 쿼리 인터페이스

## 산출물 템플릿

`research/answers/YYYY-MM-DD_<slug>.md`:

```markdown
---
date: 2026-04-15
seed_question: "<사용자 원 질문 verbatim>"
slug: <slug>
stage_version: 1
---

# Answer — {slug}

## User Question

> <사용자 원 질문 재인용 (verbatim, 인용 블록)>

## Direct Answer

<한 문단. 모호 표현 금지. 구체 수치·조건 포함. "A 상황에서는 X가 Y% 일어나고, B 상황에서는 Z 조건이 추가로 필요" 형식으로.>

## Evidence Chain

### E1: <claim 한 문장>

- **grounding**: [paper:<id> §Section] "<원문 인용 구문>" / KG: `claim:<id>`
- **confidence**: 4/5 (근거: 3개 논문이 독립적으로 동의 — paper:<a>, paper:<b>, paper:<c>)
- **verifiability**: 4/5 (직접 측정 가능한 metric 존재)
- **verification_sketch**: `<dataset>`에 `<method>` 적용 후 `<metric>` 측정. evidence가 참이면 metric ∈ [X, Y], 반박되면 metric < Z.

### E2: <claim>

...

### E3: ...

## Open Sub-Questions

Direct Answer가 커버하지 못하는 하위 질문 (다음 iteration의 seed 후보):
- Q1: ...
- Q2: ...

## Self-Check

- [ ] 사용자 질문 원문 verbatim 인용 (User Question 섹션)
- [ ] Direct Answer 한 문단 + 구체 수치·조건
- [ ] Evidence 3~7개
- [ ] 각 근거에 grounding (paper/claim id + 원문 문구) + confidence + verifiability + verification_sketch 4요소 모두
- [ ] Verifiability 0인 근거점 없음 (있으면 폐기)
- [ ] hybrid_query 실행 결과 본문에 기록
- [ ] **Divergent 후보 생성 없음** (새 연구 주제 제안 self-review)
- [ ] `YYYY-MM-DD_<slug>.kg.json` 작성 (Answer + Evidence 노드 + GROUNDED_IN 엣지)
```

## 작성 원칙

1. **Grounding 의무**: 모든 Evidence는 RAG chunk id 또는 KG `Paper|Claim` id로 링크. 무근거 주장 금지. grounding을 쓸 수 없으면 그 Evidence는 폐기.
2. **hybrid_query 필수**: 작성 시작 전 반드시 실행.
   ```bash
   python3 .claude/skills/paper-kg/scripts/hybrid_query.py "<seed_question>" --k 10
   ```
   - `rag.chunks`로 원문 근거 문장 확보
   - `kg.matched_nodes`로 기존 Paper/Claim/Method id 파악
   - 두 결과의 교집합이 Evidence의 grounding 원천이 된다.
3. **Confidence calibration**:
   - 5: 3+ 독립 논문이 동일 결론, 통계적·실험적 지지
   - 4: 2-3 논문 동의, 일부 조건부
   - 3: 단일 강한 논문 + 이론적 설명
   - 2: 단일 약한 근거 or 간접 추론
   - 1: 추측에 가까움
   - 0: **Evidence로 채택 불가 — 폐기**
4. **Verifiability 강제**: 각 Evidence에 `verification_sketch`를 반드시 작성. metric·dataset·방법을 구체적으로. verifiability 0이면 Evidence 폐기 (C-1이 검증 실험을 짤 수 없음).
5. **Direct Answer는 한 문단**: 여러 문단으로 발산하지 않는다. 질문에 대한 최단 답변.
6. **Evidence 3~7개**: 3 미만이면 답변 근거 부족으로 critic이 거절. 7 초과면 답변이 여러 질문에 걸쳐진 것 — Open Sub-Questions로 분리.

## 실패 모드

- RAG/KG 결과 빈약: 키워드 확장(동의어, 상위/하위 개념) 후 재쿼리. 여전히 빈약하면 paper-hunter 재dispatch 요청.
- 모든 Evidence가 verifiability 0: 질문 자체가 경험적 검증 범위 밖 — orchestrator에 보고, 질문 재정의 요청.
- Evidence가 서로 모순: 모순을 Direct Answer에 명시 ("A 조건에서는 X, B 조건에서는 Y") 후 Evidence 병기.
- 무의식적으로 새 연구 주제 제안이 섞임: **즉시 삭제**. Self-Check의 "Divergent 후보 없음" 체크에서 걸러낸다.

## 체크리스트

- [ ] hybrid_query 실행, `rag.chunks` + `kg.matched_nodes` 기록
- [ ] User Question 섹션 (verbatim 인용)
- [ ] Direct Answer 한 문단 + 구체성
- [ ] Evidence 3~7개, 각각 4요소 (grounding/confidence/verifiability/verification_sketch)
- [ ] Open Sub-Questions
- [ ] Self-Check 전 항목 통과
- [ ] `YYYY-MM-DD_<slug>.kg.json` 작성 (KG Emission 참조)

---

## KG Emission (byproduct)

`research/answers/YYYY-MM-DD_<slug>.md`와 같은 경로에 `YYYY-MM-DD_<slug>.kg.json`을 작성한다. 이 스킬이 소유하는 노드 타입:

| 타입 | prefix | 필수 필드 |
|---|---|---|
| `Answer` | `answer:` | seed_question, direct_answer, slug, stage_version, n_evidence_points |
| `Evidence` | `evidence:` | claim, confidence (0-5), verifiability (0-5), parent_answer_id |

**엣지**:
- `Answer --ADDRESSES--> Question` (Question 노드는 `loop_state.py start`가 방출 — orchestrator 몫)
- `Answer --CONTAINS--> Evidence` (근거점마다)
- `Evidence --GROUNDED_IN--> Paper` (RAG로 찾은 seed 논문 각각, ≥1개)
- `Evidence --GROUNDED_IN--> Claim` (KG의 기존 Claim 노드를 참조하면)

ID 예시:
- `answer:diffusion-late-step#local`
- `evidence:diffusion-late-step--e1` (parent_answer_id = answer:diffusion-late-step#local)

Provenance: `author_agent: "answer-formulator"`, `source_sha`는 `.md`의 SHA256.

## Alias Check Protocol

`Answer`·`Evidence` 자체는 이 스킬에만 존재하므로 alias는 **수행하지 않는다**. `GROUNDED_IN`이 가리키는 `Paper|Claim`은 **반드시 DB에 이미 존재하는 id만** 사용한다 (dangling 방지). 매치 없으면 paper-summarizer가 먼저 해당 Paper/Claim을 등록하도록 요청하고, 본 `.kg.json`에서는 그 엣지를 **보류**(meta에 `pending_paper: "<title>"` 기록).

## Hybrid Query

답변 작성 단계에서 **필수로** 호출:

```bash
python3 .claude/skills/paper-kg/scripts/hybrid_query.py "<seed_question>" --k 10
```

- `rag.chunks`로 관련 원문 문단을 읽고 Direct Answer의 문장 단위 grounding에 사용
- `kg.matched_nodes`로 이미 등록된 Paper/Claim/Method 노드 파악하여 `GROUNDED_IN` 엣지 src/dst id 확정
- Evidence의 confidence 점수는 matched_nodes 중 **독립 Paper 수**를 기준으로 calibrate

반대 근거(counter-evidence) 탐색도 이 단계에서 선제적으로 한 번 수행:
```bash
python3 .claude/skills/paper-kg/scripts/hybrid_query.py "<direct_answer negation>" --k 5
```
- 강한 반박 근거 발견 시 Direct Answer를 그 조건을 포함하도록 수정 ("A 조건에서는 X, B 조건에서는 Y").

## Schema Enforcement

모든 `.kg.json`은 `paper-kg/schema.py`의 `KGFile` 모델을 통과해야 한다. `Evidence --GROUNDED_IN--> Paper`의 dst는 DB에 이미 존재해야 하며, dangling이면 파일 전체가 reject된다. 상세는 `.claude/skills/paper-kg/SKILL.md`.

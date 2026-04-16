---
name: critique
description: "답변(Answer)의 근거 체인 독립 비판. 4축(Grounding Validity / Support Strength / Counter-Evidence / Verifiability) 0~5 점수, 각 Evidence가 Grounding≥3 AND Support≥3 AND Verifiability≥3 통과. 탈락 시 answer-formulator에 수정 피드백. critic 전용. 트리거: '답변 비판', 'evidence 검증', 'grounding 검토', '근거 강도 평가'."
---

# Critique Skill

`research/answers/YYYY-MM-DD_<slug>.md`의 **Direct Answer + Evidence Chain**을 독립 비판한다. 더 이상 Novelty를 채점하지 않는다 — 질문 답변이 근거 위에 서 있는지만 평가.

## 입력

- `research/answers/YYYY-MM-DD_<slug>.md` (answer-formulator 산출)
- RAG/KG 쿼리 인터페이스

## 4축 비판 프레임 (신규)

| 축 | 의미 | 0~5 의미 |
|---|---|---|
| **Grounding Validity** | Evidence의 citation이 실제 그 claim을 뒷받침하는가? paper 인용이 out-of-context이거나 반대 의미면 감점 | 5=정확 인용, 3=인용 맞지만 section mismatch, 0=out-of-context/반대 |
| **Support Strength** | Evidence가 Direct Answer를 논리적으로 뒷받침하는가? Non-sequitur, 누락된 연결고리 체크 | 5=필수·충분, 3=보강·약간 우회, 0=non-sequitur |
| **Counter-Evidence** | `hybrid_query("<counter claim>")` 로 반박 논문 검색. 발견 시 감점 (낮을수록 위험) | 5=반박 없음, 3=미미한 조건부 반박, 0=강력한 반박 |
| **Verifiability** | Evidence가 E-1에서 실제 실험으로 검증 가능한가? verification_sketch가 구체 metric/dataset을 명시하는가? | 5=즉시 실험 가능, 3=일부 모호, 0=경험 검증 불가 |

## 통과 기준

- **Per-Evidence**: `Grounding ≥ 3 AND Support ≥ 3 AND Verifiability ≥ 3`
- `Counter-Evidence ≤ 2`인 Evidence는 **"약함"** 태그 후 통과시키되 C-1에서 **우선 검증** 대상으로 표시
- **Answer-level**: 통과한 Evidence 수 `≥ 3`. 2 이하면 Answer 전체 FAIL → B-1 재호출

## 산출물 템플릿

`research/critiques/<slug>.md`:

```markdown
---
critic_of: research/answers/YYYY-MM-DD_<slug>.md
date: 2026-04-15
stage_version: 1
---

# Critique — {slug}

## Evidence Scoring Table

| Evidence | Grounding | Support | Counter-Evidence | Verifiability | Pass? |
|---|---|---|---|---|---|
| E1 | 5 | 4 | 4 | 5 | YES |
| E2 | 3 | 2 | 3 | 4 | NO (Support) |
| E3 | 4 | 5 | 1 | 4 | YES (weak — counter!) |

## Per-Evidence Analysis

### E1 (PASS)

**Grounding Validity 5**: paper:<id> §3.2의 "X increases when Y" 인용 정확.
**Support Strength 4**: Direct Answer의 "A 조건에서 X 발생" 주장을 직접 뒷받침. 단, "조건 C"는 별도 보강 필요.
**Counter-Evidence 4**: `hybrid_query("X decreases when Y")` 결과 paper:<z>의 축소 효과 보고 있으나 다른 setting. 경미.
**Verifiability 5**: verification_sketch가 구체 metric (accuracy@k) + dataset (HumanEval) 명시.

---

### E2 (FAIL — Support)

**Grounding Validity 3**: 인용은 맞지만 paper 원문은 일반 tendency를 말하며 특정 수치 Y%는 언급 없음.
**Support Strength 2**: Direct Answer의 핵심 claim과 논리적 연결이 약함. non-sequitur 위험.
**Counter-Evidence 3**: 직접 반박은 없음.
**Verifiability 4**: 검증은 가능.

**Fix suggestion**: Direct Answer의 어떤 하위 주장을 E2가 뒷받침하는지 명시적으로 재작성 OR 더 직접적 인용을 가진 paper 재탐색.

---

### E3 (PASS — weak, counter flagged)

**Counter-Evidence 1**: `hybrid_query` 결과 paper:<w>가 반대 방향 결과 보고 (n=500, p<0.01). 강력한 반박.
→ C-1은 이 Evidence를 **우선 검증** 대상으로 PLAN에 표시해야 함.

---

## Counter-Evidence Review

`hybrid_query` 결과 찾은 반박 논문:

| Evidence | Counter Paper | Impact | Action |
|---|---|---|---|
| E3 | paper:<w> (ACL 2024) | 반대 효과 유의 (p<0.01) | C-1에서 E3 우선 검증 |
| — | paper:<q> | Direct Answer와 무관, 다른 도메인 | 영향 없음 |

## Answer Revision Suggestions

Direct Answer 수정 제안:
- E2의 뒷받침이 약하므로 Direct Answer의 "Y%" 수치는 paper:<id> §3.2가 실제 보고한 "Y%±δ" 범위로 수정 필요
- E3의 counter-evidence를 조건부로 반영: "A 조건에서는 X, 다만 B setting에서는 반대 경향 (paper:<w>)"

## Pass/Fail Decision

- Evidence pass: E1, E3 (weak)
- Evidence fail: E2
- Answer-level: **PASS** (2+ evidence통과) — C-1 진행 가능
- 조건: E2는 answer-formulator 재작업 후 재비판

## Feedback to answer-formulator

**E2**:
- paper:<id>의 §3.2 원문을 다시 확인. "Y%" 수치가 실제로 보고되었는지 검증.
- 대안: 같은 claim을 paper:<a> §4의 직접 수치로 재grounding.
- Grounding Validity 3→5 + Support 2→4 로 끌어올릴 것.
```

## 작성 원칙

1. **answer-formulator의 self-check를 읽지 않음**: 독립 검증 편향 차단
2. **hybrid_query 의무**: Counter-Evidence 축은 반드시 `python3 .claude/skills/paper-kg/scripts/hybrid_query.py` 결과를 기반으로 채점. 그냥 "없음"이라고 쓰지 않는다.
3. **구체 피드백**: "unclear"가 아니라 "paper:<id> §X의 인용이 원문과 다름" 형식.
4. **Novelty·선행연구 중복 체크 금지**: 이 루프는 발명이 아니라 근거 기반 답변이다.
5. **Grounding out-of-context 탐색**: paper 원문 인용을 실제 RAG로 확인 (grep 한 번). 위조된 인용은 Grounding 0.

## 실패 모드

- Evidence 전부 fail: answer-formulator 사이클 재진입 (최대 3회)
- Counter-Evidence 축 채점 모호: 보수적으로 낮게(≤2) 처리해 C-1에서 우선 검증
- RAG/KG 검색 실패: 수동 키워드 매칭으로 대체 + Known 표시

## 체크리스트

- [ ] Evidence Scoring Table 모든 Evidence
- [ ] 각 Evidence에 4축 비판 전부 수행
- [ ] hybrid_query 결과 기록 (특히 Counter-Evidence)
- [ ] Counter-Evidence Review 테이블
- [ ] Answer Revision Suggestions
- [ ] Pass/Fail Decision (per-Evidence + Answer-level)
- [ ] 탈락 Evidence에 구체 피드백
- [ ] 같은 디렉토리에 `<slug>.kg.json` 작성 (KG Emission 참조)

---

## KG Emission (byproduct)

`research/critiques/<slug>.md`와 같은 경로에 `<slug>.kg.json`을 작성한다. 이 스킬이 소유하는 노드 타입:

| 타입 | prefix | 필수 필드 |
|---|---|---|
| `Critique` | `critique:` | target_answer_id, per_evidence_scores (dict: Evidence id → 4축), answer_pass (bool), summary |

**엣지**:
- `Critique --REVIEWS--> Answer`
- `Critique --CITES--> Paper` (grounding 검증·counter 탐색에 사용한 논문)
- `Critique --CONTRADICTS--> Claim` (counter-evidence 단계에서 발견한 반박 논문의 claim)
- `Critique --FLAGS_WEAK--> Evidence` (통과했지만 Counter-Evidence ≤ 2인 Evidence)

ID 예시: `critique:diffusion-late-step#local`

Provenance: `author_agent: "critic"`.

## Hybrid Query

**Counter-Evidence 축 채점 시 반드시** 호출:

```bash
# 각 Evidence의 claim을 반대로 뒤집은 쿼리
python3 .claude/skills/paper-kg/scripts/hybrid_query.py "<negated claim>" --k 10
```

- `kg.matched_nodes`의 Paper 노드가 반대 결과 보고하면 점수 감점
- `rag.chunks`로 구체 문맥 확인 후 critique 본문에 인용
- 결과 top-k Paper id를 `CITES` + 필요 시 `CONTRADICTS` 엣지로 기록

Grounding Validity 축 채점 시에도 호출 (인용 진위 확인):

```bash
python3 .claude/skills/paper-kg/scripts/hybrid_query.py "<exact quoted phrase>" --k 3
```

- 인용 문구가 실제 paper에 존재하는지 chunk 단위로 확인. 없으면 Grounding 0.

## Schema Enforcement

`Critique` 노드의 `target_answer_id`는 DB에 이미 존재해야 하며, 그렇지 않으면 dangling으로 reject된다. answer-formulator 산출의 `.kg.json`이 먼저 ingest되어야 함. `FLAGS_WEAK --> Evidence` dst도 DB에 있어야 함 (Answer의 CONTAINS 엣지로 이미 등록됨). 상세는 `.claude/skills/paper-kg/SKILL.md`.

(이 스킬은 `Method|Dataset|Model|Metric` 신규 노드를 만들지 않으므로 **Alias Check 비적용**.)

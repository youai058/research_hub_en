---
name: results-analyze
description: "Evidence verification outcome 분석. 각 Experiment 결과를 CONFIRMED/REFUTED/INCONCLUSIVE/IMPL_BUG 중 하나로 판정 (PLAN의 Expected Under/If Wrong 범위와 비교). Evidence별 판정 요약 → Direct Answer revision seed, 4-way 실패 분류, PNG + 자기완결 HTML. results-analyst 전용. 트리거: 'evidence 검증 결과', 'diagnosis', 'verification outcome', '답변 수정 제안', 'HTML 리포트'."
---

# Results Analyze Skill

실험 결과를 **Evidence verification outcome** 관점에서 해석한다. 핵심 질문은 "각 Evidence가 실험으로 **확인되었는가, 반박되었는가**? 근거 위에 선 Direct Answer는 여전히 유효한가?"

## 입력

- `results_<slug>/` 원시 결과 (PLAN에 정의된 경로 규약 따름)
- `research/plans/<slug>/PLAN.md`
- `research/answers/YYYY-MM-DD_<slug>.md`
- (선택) `experiments/<slug>/IMPL_MAP.md`

## Evidence Verification Outcome (primary classification)

각 Experiment E<i>의 결과를 PLAN의 Expected Under / If Wrong 범위와 비교하여 **4개 중 하나**로 판정한다:

| 판정 | 기준 | 후속 처리 |
|---|---|---|
| **CONFIRMED** | metric ∈ Expected Under range, 통계적 유의 | Evidence confidence +1 (상향). Direct Answer 유지. |
| **REFUTED** | metric ∈ Expected If Wrong range (or 반대 방향 유의) | Evidence 폐기. Direct Answer에서 해당 근거 제거하고 revision 제안. |
| **INCONCLUSIVE** | 중간 지대, CI가 두 범위를 모두 포함 | 추가 실험 권고 (N 증가 or ablation). Evidence 보존, 상태 "pending". |
| **IMPL_BUG** | 코드 문제 (smoke test 회귀, NaN, 저장 실패) | E-1 복귀 (implementer 재dispatch). 판정 자체 무효. |

**판정 의무**: 각 Experiment × Evidence 쌍마다 위 4개 중 정확히 하나를 부여. `decide_verdict()` 코드 출력과 수동 검토 결과가 일치하는지 cross-check.

diagnosis는 다음을 답한다:
1. 몇 개 Evidence가 CONFIRMED / REFUTED / INCONCLUSIVE인가?
2. Direct Answer는 그대로 유효한가? (전부 CONFIRMED → 유효, 핵심 Evidence REFUTED → revision 필요)
3. 다음 iteration의 answer-formulator에게 넘길 revision seed는 무엇인가?

## 4-Way 실패 분류 (secondary — REFUTED 발생 시 원인 분해)

결과가 hypothesis를 지지하지 않을 때 원인을 하나(또는 복수)로 분류. 다음 행동은 sub-phase 단위로 지정한다 (loop_state.py advance --force 필요).

| 분류 | 정의 | 진단 방법 | 다음 행동 |
|---|---|---|---|
| **claim wrong** | Evidence 자체가 실세계와 불일치. 구현·세팅 모두 정상. | 여러 seed·ablation 일관되게 If Wrong range | B-1 복귀 (answer-formulator 재호출, Direct Answer revision — 해당 Evidence 제거 또는 조건 추가) |
| **impl bug** | 구현 오류. 코드가 PLAN과 다름. | smoke test 재검, 로그 비정상 | E-1 복귀 (code-implementer 재구현) |
| **setup error** | baseline·hyperparameter·metric이 부적절. | baseline 수치가 선행논문과 괴리 | C-1 복귀 (experiment-planner PLAN 수정) |
| **data issue** | 데이터 편향·스플릿 오류·누수. | train/val 중복, 클래스 불균형 | A-1 복귀 (데이터 재수집) 또는 C-1 복귀 (스플릿 변경) |

**증거 기반 분류 의무**: 각 분류에 대해 구체적 증거(로그 라인, 수치, 코드 스니펫)를 제시.

## diagnosis.md 템플릿

`research/diagnoses/<slug>.md`:

```markdown
---
slug: <slug>
answer: research/answers/YYYY-MM-DD_<slug>.md
plan: research/plans/<slug>/PLAN.md
results: results_<slug>/
iteration: 3
date: 2026-04-15
---

# Diagnosis — {slug}

## TL;DR

**Direct Answer status**: {fully supported / partially supported / needs revision / fully refuted}

**Verification summary**: E1 CONFIRMED, E2 REFUTED, E3 INCONCLUSIVE → answer-formulator가 E2를 제거하고 E3 조건을 더 좁힌 새 Direct Answer를 작성해야 함.

**Next action**: {B-1 (Answer revision) / E-1 (impl fix) / C-1 (PLAN fix) / A-1 (새 iteration) / done}

---

## User Question (for reference)

> <answer의 seed_question 재인용>

## Current Direct Answer

<answer-formulator의 Direct Answer 재인용>

---

## Evidence Verification Outcomes

| Evidence | Experiment | Metric value (mean ± CI) | Expected Under | Expected If Wrong | Verdict |
|---|---|---|---|---|---|
| evidence:<slug>--e1 | E1 | 0.82 ± 0.03 | [0.75, 0.95] | < 0.55 | **CONFIRMED** |
| evidence:<slug>--e2 | E2 | 0.15 ± 0.06 | [0.10, 0.30] | N/A (primary metric) | **CONFIRMED** |
| evidence:<slug>--e3 | E3 | 0.51 ± 0.08 | [0.65, 0.90] | < 0.50 | **INCONCLUSIVE** |

## Statistical Detail

- Seeds: 3 runs per condition
- Test: paired t-test (C1 vs C2)
- p-value: 0.42 (not significant for C1), 0.003 (significant for C2)
- Effect size (Cohen's d): C1=0.15, C2=0.82

## Failure Classification (if any)

### C1 gap → claim wrong (probability 0.7)

**Evidence**:
- 모든 3 seed에서 일관되게 null에 가까움 (log: results_<slug>/seed*/metrics.json)
- Ablation A2에서도 method A vs B 차이 없음
- Impl은 verifier 통과, baseline 수치는 [Paper X]와 일치 (±0.5%)

**Alternative hypothesis**: setup error (probability 0.2)
- baseline B가 논문의 optimal 설정보다 약간 약할 수 있음

**Alternative hypothesis**: data issue (probability 0.1)
- 클래스 분포 확인 완료, 정상

## Re-Experiment Triggers

- **If claim wrong (primary)**: B-1로 복귀 (`loop_state.py advance --to B-1 --force`). C1을 폐기하고 C2만 유지, C2의 후속 질문 탐색.
- **If setup error (alt)**: baseline B의 하이퍼파라미터를 [Paper X] §4.2 값으로 재실행. 1시간 추가.

## Visualizations

- `results_<slug>/plots/accuracy_comparison.png`: bar plot, 3 methods × 3 seeds
- `results_<slug>/plots/learning_curves.png`: train/val loss
- `research/diagnoses/<slug>.html`: 자기완결 리포트

## Findings to Accumulate (RAG에 추가할 인사이트)

- **Negative result**: Method A는 이 task에서 유의미한 개선 없음 (effect size 0.15)
- **Positive result**: Method C는 baseline 대비 유의미한 개선 (p=0.003, d=0.82)
- 후속 연구에 참고할 가치 있음

## Next Loop Entry

- `loop_state.json.history` 추가:
  ```json
  {"iteration": 3, "outcome": "claim wrong (C1) / claim supported (C2)", "next": "B-1"}
  ```
```

## 시각화 규약

### PNG (matplotlib)

- 분석용 raw PNG는 `results_<slug>/plots/`에 저장
- 파일명: `{metric}_{comparison}.png`
- 해상도: `dpi=150`
- 스타일: `seaborn-v0_8` 또는 기본, 일관되게

### HTML (자기완결)

- `research/diagnoses/<slug>.html`
- 규약:
  - 단일 `.html` 파일로 완결
  - CSS/JS는 inline (외부 CDN 금지)
  - 이미지는 base64로 embed
  - 인터랙티브 요소 있다면 plotly inline bundle
- 템플릿:
  ```html
  <!DOCTYPE html>
  <html>
  <head>
    <style>body {font-family: sans-serif; max-width: 900px; margin: 2em auto;}</style>
  </head>
  <body>
    <h1>Diagnosis — {slug}</h1>
    <p><b>Claim support</b>: ...</p>
    <h2>Accuracy Comparison</h2>
    <img src="data:image/png;base64,{b64}" />
    <h2>Finding</h2>
    ...
  </body>
  </html>
  ```

## 작성 원칙

1. **Claim support 결론 의무**: supported/weakly/rejected/refuted 중 하나 명시
2. **증거 기반 분류**: "느낌"이 아니라 로그·수치 인용
3. **복수 가설 병기**: 원인이 불확실하면 확률과 함께 여러 가설 제시
4. **Next loop entry 필수**: 다음 행동과 진입 Phase를 반드시 제안
5. **Findings 축적**: 개별 실험 결과가 아니라 **후속 연구에 쓸 인사이트** 추출

## 실패 모드

- 결과 파일 손상: log에서 부분 복구 + Known/Unknown에 명시
- statistical test 불가 (샘플 1개): effect size만 보고 + 추가 seed 권장
- HTML 렌더 실패: PNG는 별도 파일로, HTML은 다음 실행에서 재시도
- claim 모호: answer-formulator 원문(`research/answers/<slug>.md`) 재독 후 재해석

## 체크리스트

- [ ] TL;DR (support 결론 + next action)
- [ ] Claim vs Result 테이블
- [ ] Statistical detail (test, p, effect size)
- [ ] Failure classification with 증거 (if any)
- [ ] Re-experiment triggers
- [ ] PNG 플롯 생성
- [ ] 자기완결 HTML 리포트
- [ ] Findings to Accumulate
- [ ] loop_state.json 업데이트 제안
- [ ] 같은 디렉토리에 `<slug>.kg.json` 작성 (KG Emission 참조)

---

## KG Emission (byproduct)

`research/diagnoses/<slug>.md`와 같은 경로에 `<slug>.kg.json`을 작성한다. 이 스킬이 소유하는 노드 타입:

| 타입 | prefix | 필수 필드 |
|---|---|---|
| `Result` | `result:` | experiment_id, evidence_id, metric_id, value (원문 수치), ci (optional), seeds[], verdict (CONFIRMED/REFUTED/INCONCLUSIVE/IMPL_BUG) |
| `Diagnosis` | `diagnosis:` | slug, answer_status (fully supported / partially supported / needs revision / fully refuted), n_confirmed, n_refuted, n_inconclusive, next_action |

**엣지 (필수)**:
- `Experiment --PRODUCES--> Result`
- `Result --EVIDENCED_BY--> Evidence` (meta.polarity ∈ {support, contradict, mixed})
  - support: verdict == CONFIRMED
  - contradict: verdict == REFUTED
  - mixed: verdict == INCONCLUSIVE
- `Diagnosis --ABOUT--> Experiment` (각 실험마다)
- `Diagnosis --CONCERNS--> Answer` (대상 Answer)
- `Diagnosis --SUGGESTS_NEXT--> Answer` (다음 iteration에서 answer-formulator가 만들 예정의 Answer id를 placeholder로 예약 — 또는 생략)

ID 예시: `result:late-step-generation-gap--c1-seed0`, `diagnosis:late-step-generation-gap#local`

Provenance: `author_agent: "results-analyst"`.

## Polarity 결정 원칙

**EVIDENCED_BY의 `polarity`는 필수**. 결정 규칙:

1. 결과의 effect size가 PLAN의 prediction 방향과 같고 통계적 유의 (p<0.05) → `support`
2. effect size가 prediction 방향과 반대거나, null (CI가 0 포함) → `contradict`
3. 일부 condition/seed에서만 지지 → `mixed` (meta에 상세 기록)

curator가 `polarity` 누락 시 파일 전체를 reject한다. 애매하면 `mixed`로 기록하고 diagnosis.md 본문에 불확실성 명시.

## Alias Check Protocol

신규 `Metric` 노드를 만들 일이 있다면 lookup 필수 (보통 experiment-planner가 이미 등록했음). 이 스킬에서는 대개 **기존 id 재사용만** 수행.

## Hybrid Query

**Findings 축적 단계**에서 유사 선행연구와 비교할 때:

```bash
python3 .claude/skills/paper-kg/scripts/hybrid_query.py "<metric> <method> negative result" --k 5
```

- `kg.matched_nodes`로 같은 Method/Dataset에 대한 기존 Result 노드 파악
- 현재 결과와 수치 비교 후 diagnosis.md에 "선행 논문 X는 Y%, 본 실험은 Z%" 형식으로 인용

## Schema Enforcement

`Result --EVIDENCED_BY--> Evidence`은 dst가 DB의 기존 `Evidence` id여야 한다 (answer-formulator가 등록). Evidence가 없으면 dangling reject. Hypothesis 노드는 루프에서 제거되었으므로 대체 불가. 상세는 `.claude/skills/paper-kg/SKILL.md`.

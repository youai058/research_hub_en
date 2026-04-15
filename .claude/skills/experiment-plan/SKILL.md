---
name: experiment-plan
description: "Evidence verification 실험 계획. 통과한 각 Evidence point를 경험적으로 검증하는 실험을 1:1로 설계 (PLAN ↔ Evidence 매핑). IV/DV/baseline/ablation + Expected result under evidence / if evidence wrong 사전 명시. experiment-planner 전용. 트리거: 'evidence 검증 실험', 'PLAN.md 작성', 'verification plan'."
---

# Experiment Plan Skill

통과한 Answer의 각 **Evidence point**를 **경험적으로 검증하는 실험**을 설계한다. PLAN.md의 각 cell은 "새 가설 테스트"가 아니라 **Evidence verification**이다.

## 입력

- `research/answers/YYYY-MM-DD_<slug>.md` (answer-formulator 산출)
- `research/critiques/<slug>.md` (critic의 per-Evidence 점수 + weak flag + revision suggestions)
- RAG/KG 참조 (관련 논문의 실험 세팅)

## PLAN.md 구조 원칙

- **각 실험 cell = 정확히 하나의 Evidence point**에 매핑. 1:1 추적.
- IV/DV 설계는 "새로움" 기준 아니라 **"evidence 검증 충실도"** 기준.
- **Expected result를 사전 명시**: evidence가 참이면 예상 값, 반박되면 예상 값. post-hoc 해석 방지.
- critic이 `FLAGS_WEAK`로 표시한 Evidence는 **우선 검증** 순서로 배치.

## PLAN.md 템플릿

`research/plans/<slug>/PLAN.md`:

```markdown
---
plan_for: research/answers/YYYY-MM-DD_<slug>.md
critique: research/critiques/<slug>.md
date: 2026-04-15
iteration: 1
estimated_runtime: "2 hours on 1x A100"
---

# Evidence Verification Plan — {slug}

## Direct Answer (for reference)

<answer-formulator가 쓴 Direct Answer 재인용>

## Evidence Verification Map

| Exp | Evidence id | Claim | Priority | Status |
|---|---|---|---|---|
| E1 | evidence:<slug>--e1 | ... | normal | planned |
| E2 | evidence:<slug>--e2 | ... | **weak (counter flagged)** | planned — priority |
| E3 | evidence:<slug>--e3 | ... | normal | planned |

---

## Experiment E1: Verify Evidence Point 1

**Evidence (from answer)**: "<E1의 원문 claim>"
**Claim being verified**: <E1 claim 한 문장>
**Verification logic**:
- If experiment result confirms → Evidence E1 confidence +1 (upgrade), Direct Answer 유지
- If experiment result refutes → Evidence E1 폐기, Direct Answer 수정 필요 (E1을 뺀 축소 or 조건 추가)

### Variables

| Type | Name | Values | Justification |
|---|---|---|---|
| IV | <factor> | {A, B, C} | E1의 claim이 factor의 함수로 표현됨 |
| DV (verification metric) | <metric> | scalar | E1 → metric 의 직접 매핑 |
| Control | seed | {0, 1, 2} | reproducibility |

### Baseline

| # | Baseline | Source Paper | Why |
|---|---|---|---|
| 1 | BaselineA | [Paper:<id>] | E1이 인용한 논문의 셋업 재현 |
| 2 | Null model | — | Evidence가 거짓일 때의 예상 분포 |

### Expected Results

- **Under evidence (E1 참)**: `<metric> ∈ [X_low, X_high]` (e.g., accuracy ≥ 0.75)
- **If evidence wrong**: `<metric> < X_null` (e.g., accuracy ≤ 0.55, 즉 baseline과 차이 없음)
- **Inconclusive zone**: `X_null < metric < X_low`
- Statistical test: paired t-test / Wilcoxon / bootstrap CI, α=0.05, power=0.8
- **Power analysis**: minimum N = ... (effect size d=..., α, power)

### Ablations (verification-specific)

- A1: IV 제거 → null model로 회귀 확인
- A2: 다른 dataset 반복 → evidence 일반성 확인

### Resources

- GPU: 1× A100, Estimated runtime: <fill after dry-run>
- Disk: ~2GB

### Implementation Checklist

- [ ] Data loader for `<dataset>`
- [ ] Model wrapper implementing `<method>`
- [ ] `<metric>` computation (returns scalar 0-1)
- [ ] Expected-range assertion script (outputs CONFIRMED / REFUTED / INCONCLUSIVE)
- [ ] Run with 3 seeds

---

## Experiment E2: Verify Evidence Point 2 (**priority — weak**)

critic이 Counter-Evidence로 flag함. 먼저 실행.

**Evidence**: "..."
**Claim being verified**: ...
**Verification logic**: ...

### Variables ...

### Baseline ...

### Expected Results

- 일반 E와 동일 포맷 + **counter paper의 결과 지점**도 명시:
  - `<metric> at counter-paper's setting` (실제로 재현되는지)

...

---

## Experiment E3: ...

...

---

## Resources (Total)

- GPU hours: 3× <per-exp estimate> = <sum>
- Disk: ~10GB

> weak-priority Experiment를 먼저 실행해서 근거 붕괴 가능성을 앞당겨 판단. 유료 API 호출·외부 LLM·LLDM 경로 의존 발견 시 orchestrator에 사전 보고.

## Reproducibility

- [ ] Seed 고정 (3개 반복) per Experiment
- [ ] 데이터 스플릿 해시 기록
- [ ] 하이퍼파라미터 YAML 보존
- [ ] 실행 커맨드 `run.sh`에 저장
- [ ] 결과 경로 규약: `results_<slug>/E<i>/seed{N}/metrics.json`

## Success Criteria

- 각 Experiment가 `CONFIRMED` / `REFUTED` / `INCONCLUSIVE` 판정을 줄 수 있는 정량 기준을 가짐
- Reproducibility 체크리스트 100%
- F-1 results-analyst가 Evidence 단위로 해석 가능한 포맷

## Open Questions / Known Risks

- E2의 counter paper의 hyperparameter 공개 여부 불확실
- dataset X 라이선스 확인 필요
```

## 작성 원칙

1. **PLAN ↔ Evidence 1:1**: 하나의 Experiment가 여러 Evidence를 뭉뚱그리면 F-1에서 책임 소재 불명. 반드시 1:1.
2. **Expected Under / If Wrong 의무**: post-hoc 해석 방지. 사전에 "이러면 confirmed, 이러면 refuted"를 수치로 고정.
3. **Weak-flag 우선**: critic이 Counter-Evidence로 flag한 Evidence는 PLAN 순서에서 먼저. 붕괴하면 이후 실험이 무의미해질 수 있음.
4. **RAG 참조 의무**: baseline·metric·hyperparameter는 rag_query로 원 논문 setting 확인.
5. **통계력**: power analysis 없이 "충분"이라 쓰면 반려.
6. **리소스 추정 보수적**: 실제 runtime의 1.5배.
7. **run.sh 의무**: 수동 커맨드 아닌 재현 가능 스크립트.

## 실패 모드

- Evidence의 verification_sketch가 너무 모호 → answer-formulator에 verification_sketch 보강 요청 (B-1로 backward)
- Expected range 산출 근거 부족 → 선행 논문의 reported number를 RAG로 찾아 기준점 설정
- 유료 API / 외부 LLM·LLDM 의존 필요 → orchestrator 보고
- baseline 재현 불가 (코드 없음) → 최소 구현 대체 + IMPL_MAP에 명시

## 체크리스트

- [ ] Evidence Verification Map 테이블 (모든 Evidence 커버)
- [ ] 각 Experiment에 Evidence id + verification logic 명시
- [ ] IV/DV/control 테이블
- [ ] Expected Under / If Wrong 수치 명시 (사전)
- [ ] Baselines 2개 이상 (RAG 참조)
- [ ] Power analysis
- [ ] Ablations (verification-specific)
- [ ] Resources 추정
- [ ] Reproducibility 체크리스트
- [ ] Implementation Checklist per Experiment
- [ ] run.sh 포함 계획
- [ ] weak-flag Evidence 우선 배치
- [ ] 같은 디렉토리에 `PLAN.kg.json` 작성 (KG Emission)

---

## KG Emission (byproduct)

`research/plans/<slug>/PLAN.md`와 같은 디렉토리에 `PLAN.kg.json`을 작성한다.

| 타입 | prefix | 필수 필드 |
|---|---|---|
| `Plan` | `plan:` | slug, answer_id, n_experiments, baselines[], metrics[] |
| `Experiment` (shell — code-implementer가 채움) | `experiment:` | slug, plan_id, evidence_id, expected_under, expected_if_wrong |

> 주: `Experiment` 노드의 실제 생성은 E-1 code-implementer의 책임. 본 스킬은 Plan 노드만 방출하고, 각 Experiment slot은 meta.pending_experiments에 evidence_id 리스트로 예약만 기록.

**엣지**:
- `Plan --VERIFIES--> Answer`
- `Plan --USES_DATASET--> Dataset`
- `Plan --USES_MODEL--> Model`
- `Plan --USES_METRIC--> Metric`
- `Plan --COMPARES_WITH--> Method` (baseline 각각)

Provenance: `author_agent: "experiment-planner"`.

## Alias Check Protocol

`Dataset|Model|Metric|Method` (baselines 포함)를 가리키는 엣지를 만들 때 lookup:

```bash
python3 .claude/skills/paper-kg/scripts/query.py lookup --type Dataset --name-fuzzy "AdvBench"
```

매치 id 재사용. 매치 없으면 paper-summarizer가 먼저 등록하도록 두고 해당 엣지 보류.

## Hybrid Query

Baseline·Metric 선정 + Expected range 산출 시 **필수**:

```bash
python3 .claude/skills/paper-kg/scripts/hybrid_query.py "<evidence claim> baselines" --k 10
```

- `kg.matched_nodes`의 Paper → Method 경로로 실제 쓰인 baseline·metric 식별
- `rag.chunks`로 하이퍼파라미터·reported numbers 원문 인용 → Expected range 기준점

## Schema Enforcement

`Plan --VERIFIES--> Answer`의 Answer id는 DB에 존재해야 한다. answer-formulator가 먼저 `.kg.json` ingest되어야 함. Dangling 시 파일 reject. 상세는 `.claude/skills/paper-kg/SKILL.md`.

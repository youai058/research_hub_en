---
name: implementation-verify
description: "구현 incremental QA. PLAN.md↔IMPL_MAP.md 경계면 교차 비교(IV/DV/metric shape), smoke test, edge case, 실패 시 implementer 피드백. implementation-verifier 전용. 트리거: '구현 검증', 'QA', 'smoke test', 'boundary check'."
---

# Implementation Verify Skill

**경계면 교차 비교 + 실행 증명** 기반 QA. 존재 확인을 넘어 shape 일치와 실제 동작을 확인한다.

## 입력

- `research/plans/<slug>/PLAN.md`
- `experiments/<slug>/IMPL_MAP.md`
- code-implementer가 SendMessage로 전달한 **변경 파일 목록**

## 4단계 검증

### 1. Mapping Completeness

- PLAN.md의 모든 `[ ]` 항목이 IMPL_MAP.md에 존재하는가?
- IMPL_MAP의 모든 매핑이 실제 파일·함수·라인을 가리키는가?
- 누락 → **실패**: "PLAN §3.2 'Ablation A1' not mapped in IMPL_MAP"

### 2. Boundary Crossing Check (Evidence-aware)

PLAN의 IV/DV/metric과 실제 코드 타입을 교차 비교한다. **존재가 아니라 shape**이 핵심. 추가로 **Evidence verification 충실도**를 확인한다.

예:
- PLAN: "DV = accuracy (scalar, 0-100)"
- IMPL: `def compute_accuracy(preds, labels) -> float`
- 통과: float 스칼라 맞음

반례:
- PLAN: "DV = latency (ms, per-sample)"
- IMPL: `def compute_latency(batch) -> float  # batch avg`
- 실패: "PLAN expects per-sample but IMPL returns batch average"

**Evidence verification boundary (신규, 필수)**:
- PLAN §E<i>의 `verification metric`과 IMPL_MAP의 `Verification metric` 컬럼이 일치하는가?
- 각 Experiment가 **정확히 하나의** Evidence id를 가리키는가? (IMPL_MAP의 Evidence ↔ Experiment 1:1 확인)
- `decide_verdict()` 함수가 PLAN의 `Expected Under / If Wrong` 범위와 동일 수치로 CONFIRMED/REFUTED/INCONCLUSIVE를 결정하는가?
  - PLAN: Expected Under [0.75, 0.95], If Wrong < 0.55
  - IMPL: `if metric >= 0.75: return "CONFIRMED"; elif metric < 0.55: return "REFUTED"; else: return "INCONCLUSIVE"`
  - 수치가 어긋나면 실패 (F-1에서 잘못된 판정)

### 3. Smoke Test (실제 실행 증명)

- Minimal sample 1개로 해당 모듈 호출
- 기대 출력 shape·range 검증
- 예외 없이 통과해야 함

```python
# 예시
from experiments.slug.code.data.loader import load_dataset, split
ds = load_dataset(debug=True, max_samples=4)
tr, va, te = split(ds, ratios=(0.5, 0.25, 0.25))
assert len(tr) == 2 and len(va) == 1 and len(te) == 1
```

- dry-run 금지: 실제로 데이터 흐름 확인
- synthetic sample로 충분. 전체 데이터셋 로드 금지(시간 낭비)

### 4. Edge Case 탐색

최소 3개 엣지 케이스 시도:
- 빈 입력 (empty list, zero rows)
- 단일 샘플 (batch_size=1)
- 최대 길이 / 큰 값
- NaN/None/빈 문자열
- Seed 동일성 (같은 seed → 같은 출력)

## 실패 시 피드백 포맷

SendMessage(code-implementer):

```
[FAIL] Module X verification

1. Mapping: PASS
2. Boundary crossing:
   - FAIL: function foo at code/models/wrapper.py:42
     - PLAN §2.1 expects input shape (B, N, D)
     - IMPL signature: foo(x: Tensor[N, D])  # missing batch dim
   - Fix suggestion: add batch dimension or wrap with vmap
3. Smoke test: SKIPPED (boundary fail)
4. Edge case: SKIPPED

Please fix boundary issue and re-request verification.
```

**구체성 의무**: "function exists but wrong shape"처럼 막연한 표현 금지. 파일·라인·PLAN 섹션 3개를 모두 인용.

## 통과 시

```
[PASS] Module X verification

1. Mapping: all PLAN §2 items covered
2. Boundary crossing: all shapes match
3. Smoke test: 4 samples processed, output shape (4, 10) as expected
4. Edge case: empty/single/nan all handled gracefully

PLAN checkboxes §2.1-2.3 → [x]. Ready for Module Y.
```

## 환경 이슈 처리

- Import 에러 → `experiments/<slug>/code/__init__.py` 존재 확인, venv 활성 확인
- 데이터셋 path 에러 → config의 경로 오타 또는 절대/상대 혼동 지적
- CUDA OOM → `CUDA_VISIBLE_DEVICES=""` 또는 `device='cpu'`로 smoke test 시도

## Incremental 타이밍

- 모든 모듈 완성 후 1회 일괄 QA → **금지**
- 각 모듈 완성 직후 즉시 QA → **필수**
- 실패 시 해당 모듈만 수정 후 재QA. 인접 모듈은 영향 없으면 재검증 skip.

## 실패 모드

- venv 손상: 복구 스크립트 또는 사용자 안내
- PLAN 자체 모호: experiment-planner에 명확화 요청
- 2회 연속 실패: orchestrator에 보고, 루프 중단 트리거

## 체크리스트

- [ ] IMPL_MAP 존재 확인
- [ ] Mapping Completeness
- [ ] Boundary Crossing Check (shape 비교)
- [ ] Smoke test 실행 (실제 데이터 흐름)
- [ ] Edge case 3개 이상
- [ ] Pass/Fail 결정 + 구체 피드백
- [ ] (통과 시) PLAN 체크박스 `[x]` 갱신 승인

---
name: code-implement
description: "PLAN.md 기반 실험 코드 구현. 외부 논문 repo 최소 침습 통합, experiments/<slug>/code/ 배치, IMPL_MAP.md PLAN↔코드 매핑, configurable path·라이선스·convention 강제. code-implementer 전용. 트리거: '코드 구현', '외부 repo 통합', '실험 모듈 작성'."
---

# Code Implement Skill

PLAN.md의 각 체크박스를 **실행 가능한 코드**로 변환하는 절차. implementation-verifier와 짝을 이루어 incremental QA.

## 입력

- `research/plans/<slug>/PLAN.md`
- 외부 논문 repo URL들 (PLAN 또는 RAG에서 식별)

## 출력 구조

```
experiments/<slug>/
├── code/
│   ├── data/              데이터 로더, 전처리
│   ├── models/            모델 래퍼, 메서드 구현
│   ├── training/          학습 루프
│   ├── eval/              metric, 통계 테스트
│   ├── ablations/         ablation runner들
│   └── utils/             공용 헬퍼
├── configs/
│   └── default.yaml
├── run.sh
└── IMPL_MAP.md
```

## 외부 Repo 탐색 절차

1. **Read README first**: 목적, 의존성, 진입점 파악
2. **Find the entry point**: `main.py`, `train.py`, `run_*.py`
3. **Trace dependencies**: import 그래프로 핵심 모듈 식별
4. **License check**: MIT/Apache → 코드 차용 가능 (주석 의무), GPL → 피하거나 참조만
5. **Minimal extraction**: 필요한 함수만 가져와 어댑터로 감쌈. 전체 repo 복사 금지.

## 최소 침습 통합 원칙

1. **어댑터 패턴**: 외부 함수를 직접 호출하지 않고 얇은 wrapper로 감쌈
   ```python
   # experiments/<slug>/code/models/external_adapter.py
   """Adapter for [Paper X] method.
   Source: https://github.com/.../paper-x (MIT License)
   Only func_Y is used.
   """
   from external_lib import func_Y

   def call_method_A(x, config):
       return func_Y(x, **_map_config(config))
   ```

2. **Config-driven**: 경로·하이퍼파라미터를 `configs/default.yaml`로 외부화
3. **CLI-friendly**: `run.sh`에서 `--method A --seed 0 --output results_<slug>/seed0/` 형식
4. **Naming preservation**: 외부 코드의 명명을 억지로 바꾸지 않음 (단, local 변수는 본 프로젝트 스타일)

## IMPL_MAP.md 템플릿 (3-way mapping)

`experiments/<slug>/IMPL_MAP.md`. **Evidence ↔ Experiment ↔ Code** 3-way 추적:

```markdown
# Implementation Map — {slug}

PLAN.md의 각 Experiment cell을 실제 코드로 매핑한다. 각 Experiment는 정확히 하나의 Evidence를 검증한다.

## Evidence ↔ Experiment ↔ Code (전체 매핑)

| Evidence id | Experiment | PLAN §  | Code entry | Verification metric | Expected range |
|---|---|---|---|---|---|
| evidence:<slug>--e1 | E1 | PLAN §E1 | `code/experiments/e1.py::run()` | accuracy@k | [0.75, 0.95] |
| evidence:<slug>--e2 | E2 | PLAN §E2 | `code/experiments/e2.py::run()` | bootstrap CI | [0.10, 0.30] |
| evidence:<slug>--e3 | E3 | PLAN §E3 | `code/experiments/e3.py::run()` | paired-diff | [0.02, 0.08] |

## Experiment E1: Verify Evidence evidence:<slug>--e1

PLAN §E1의 각 체크박스:

| PLAN item | File | Function | Line |
|---|---|---|---|
| Load {dataset} | `code/data/loader.py` | `load_dataset()` | 12 |
| Model wrapper | `code/models/wrapper.py` | `MethodA` | 34 |
| Metric computation | `code/eval/metrics.py` | `accuracy_at_k()` | 18 |
| Expected-range check | `code/experiments/e1.py` | `decide_verdict()` | 55 |

> `decide_verdict()`는 `CONFIRMED / REFUTED / INCONCLUSIVE` 중 하나를 반환. PLAN의 Expected Under / If Wrong 범위와 비교.

## Experiment E2: Verify Evidence evidence:<slug>--e2
...

## External Dependencies

| Package | Version | Source | License |
|---|---|---|---|
| transformers | 4.40.0 | pip | Apache-2.0 |
| paper-x-lib | commit abc123 | GitHub | MIT |
```

> 3-way 의무: 이 테이블에서 Evidence id가 빠지면 F-1 results-analyst가 CONFIRMED/REFUTED 판정을 evidence 단위로 낼 수 없다. **필수**.

## run.sh 템플릿

```bash
#!/usr/bin/env bash
set -euo pipefail

SLUG="$(basename "$(dirname "$0")")"
OUT_ROOT="/home/irteam/sw/research_hub/results_${SLUG}"
mkdir -p "$OUT_ROOT"

METHODS=("A" "B" "C")
SEEDS=(0 1 2)

for method in "${METHODS[@]}"; do
  for seed in "${SEEDS[@]}"; do
    OUT="${OUT_ROOT}/method${method}_seed${seed}"
    mkdir -p "$OUT"
    python3 code/training/main.py \
      --config configs/default.yaml \
      --method "$method" \
      --seed "$seed" \
      --output "$OUT" \
      2>&1 | tee "$OUT/log.txt"
  done
done

echo "done: $OUT_ROOT"
```

## Incremental 작업 단위

1. **모듈 단위 commit**: 각 모듈 완성 → verifier 호출 → 통과 → 다음
2. **verifier 메시지 포맷**:
   ```
   SendMessage(verifier,
     "Module 1 (Data loader) complete.
      Files: code/data/loader.py
      IMPL_MAP: §Module 1
      PLAN items: 3 checkboxes
      Ready for verification.")
   ```
3. **통과 전에 다음 모듈 시작 금지**

## 실패 모드

- 외부 repo 접근 실패: 대체 구현 또는 minimal stub + IMPL_MAP에 "external missing" 플래그
- 의존성 충돌: 기존 `LLDM` conda env에 추가 설치 전에 사용자 확인. 필요 시 venv 분리.
- verifier 재실패 2회: orchestrator에 보고, 해당 모듈 rollback 후 재설계
- PLAN 모호: experiment-planner에 명확화 요청

## 체크리스트

- [ ] PLAN.md 전체 검토, 모듈 경계 파악
- [ ] 외부 repo URL들 확인, 라이선스 체크
- [ ] `experiments/<slug>/code/` 디렉토리 구조 생성
- [ ] configs/default.yaml 초안
- [ ] 모듈 1 구현 → verifier → 통과 → 모듈 2...
- [ ] IMPL_MAP.md 갱신 (모든 PLAN 체크박스 커버)
- [ ] run.sh 작성 및 smoke test
- [ ] PLAN.md의 `[ ]`를 `[x]`로 전환
- [ ] `experiments/<slug>/IMPL_MAP.kg.json` 작성 (KG Emission 참조)

---

## KG Emission (byproduct)

`experiments/<slug>/IMPL_MAP.md`와 같은 디렉토리에 `IMPL_MAP.kg.json`을 작성한다. 이 스킬이 **실험 노드의 유일한 소유자**이다:

| 타입 | prefix | 필수 필드 |
|---|---|---|
| `Experiment` | `experiment:` | slug, plan_id, evidence_id, expected_under, expected_if_wrong, run_sh_path, output_dir, commit_hash (있으면), seeds[] |

**엣지**:
- `Experiment --IMPLEMENTS--> Plan`
- `Experiment --VERIFIES--> Evidence` (**필수** — 3-way 추적의 핵심)
- `Experiment --USES_DATASET--> Dataset` (DB 기존 id)
- `Experiment --USES_MODEL--> Model`
- `Experiment --USES_METHOD--> Method` (PLAN의 baseline 포함)

ID 예시: `experiment:late-step-generation-gap#local`

Provenance: `author_agent: "code-implementer"`.

> ⚠️ 이 노드를 만들지 않으면 results-analyst가 결과를 Plan에 매핑할 수 없어 전체 그래프에 gap이 생긴다. **필수**.

## Alias Check Protocol

`USES_DATASET|USES_MODEL|USES_METHOD` 엣지의 dst는 반드시 lookup으로 기존 id를 찾는다:

```bash
python3 .claude/skills/paper-kg/scripts/query.py lookup --type Model --name-fuzzy "LLaMA-2-7B"
```

매치 없음 → Plan 단계로 되돌아가 (experiment-planner가 해당 노드의 alias를 확정했는지 확인). 여기서 새 Model/Dataset/Method 노드를 만들지 않는다.

## Hybrid Query

외부 repo 탐색 시 참조:

```bash
python3 .claude/skills/paper-kg/scripts/hybrid_query.py "<method> implementation" --k 5
```

- `kg.matched_nodes`의 Paper → 원 논문 repo 링크 확인
- `rag.chunks`의 § Setup/§ Methodology 문단에서 하이퍼파라미터 원문 추출
- 라이선스·commit hash 메타를 `Experiment` 노드의 provenance에 반영

## Schema Enforcement

`Experiment --IMPLEMENTS--> Plan`에서 Plan id는 DB에 존재해야 한다. experiment-planner의 `PLAN.kg.json`이 먼저 ingest되지 않았으면 orchestrator가 재dispatch 요청. 상세는 `.claude/skills/paper-kg/SKILL.md`.

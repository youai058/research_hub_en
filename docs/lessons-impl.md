---
domain: impl
updated: 2026-04-15
covers: [code-implementer, implementation-verifier]
---

# Lessons — Implementation (implement / verify)

code-implementer, implementation-verifier가 작업 시작 전에 이 파일을 Read한다. append-only.

Phase C-1 도메인: 외부 repo 통합, IMPL_MAP, boundary crossing, smoke test, edge cases.

## How to add

`/research-lesson impl "<rule title>"`

---

<!-- append entries below this line -->

## 2026-04-15 — IMPL_MAP.md 필수
- **Rule**: code-implementer는 experiments/<slug>/IMPL_MAP.md를 먼저 생성하고, PLAN.md의 각 체크리스트 항목을 실제 파일 경로·함수·CLI 플래그에 1:1로 매핑한 뒤에 구현을 시작한다
- **Why**: 매핑 없이 구현하면 verifier가 PLAN↔코드 boundary crossing을 검증할 수 없고, 실패 원인 분류에서 impl/setup 경계가 흐려진다
- **When to apply**: Phase C-1 시작 시 — IMPL_MAP.md 누락은 hard stop

## 2026-04-15 — 외부 repo는 최소 침습 통합
- **Rule**: 외부 논문 구현체는 experiments/<slug>/code/ 하위에 서브디렉토리로 clone하고, 원본 파일을 직접 수정하지 말고 wrapper/patch 파일을 별도로 둔다
- **Why**: 원본 수정은 upstream 업데이트 대응과 reproducibility를 동시에 망가뜨린다
- **When to apply**: 외부 repo 첫 통합 시 — 필요한 수정은 patches/*.diff 또는 overrides/*.py로 격리

## 2026-04-15 — 머신별 경로 하드코딩 금지
- **Rule**: 새 코드는 /home/irteam/... 같은 절대 경로를 하드코딩하지 않고 --root, --data-dir 같은 CLI 인자로 주입받는다
- **Why**: 하네스가 /home1/irteam/와 /home/irteam/ 두 심볼릭 경로를 오가며, 하드코딩은 다른 머신 이식을 막는다
- **When to apply**: 모든 experiments/<slug>/code/ 신규 스크립트 작성 시

## 2026-04-15 — Smoke test 먼저, 풀 실행은 나중에
- **Rule**: implementation-verifier는 풀 데이터셋 실행 전 1 batch + 1 step smoke test로 IV/DV shape·metric 경계를 먼저 검증한다
- **Why**: 8시간짜리 학습 끝에 shape mismatch가 드러나면 GPU·시간 낭비가 크다
- **When to apply**: Phase C-1 말미, analyst에게 넘기기 전 gate

<!-- seeded 2026-04-15 -->

## 2026-04-15 — force-commit hook은 global step counter로 모든 block을 덮어야 한다
- **Rule**: force-commit 훅은 global abs_step에 트리거되고, fire 시점에 gen 영역 전체(모든 block)의 still-masked 포지션을 한 번에 덮어쓴 뒤 스케줄러 루프를 short-circuit한다
- **Why**: block-local로 구현하면 fire 시점에 current/prior block만 허용되는데 거기는 이미 committed라 no-op이 되어 smoke test가 baseline과 bit-exact 결과를 낸다. 2026-04-15 diffusion-llm-step iter1에서 실제로 발생
- **When to apply**: masked-diffusion LM sampler에 intervention hook을 넣을 때 — baseline과 결과가 동일하면 즉시 의심하고 touched-positions 수로 검증하라

## 2026-04-15 — 배치 드라이버는 nohup+disown+heartbeat+sentinel 4종 세트 필수
- **Rule**: 장시간(>2분) 배치 드라이버는 `nohup ./driver.sh > logs/driver.log 2>&1 & disown`로 띄우고, 드라이버 내부에 (a) 셀당 touch된 `.heartbeat` (b) 완료 sentinel `batch.done` (c) 실패 목록 `batch_failed.txt` (d) 셀 진입 전 `metrics.json` 존재 체크(skip) 네 가지를 모두 포함해야 한다. `set -e` 금지; 셀 하나 실패가 배치 전체를 죽이면 안 된다.
- **Why**: 2026-04-15 diffusion-llm-step iter1 wave2에서 `nohup`·`disown` 없이 부모 bash만 백그라운드로 돌렸더니 Claude-Code 세션 리프 때 드라이버가 SIGHUP로 함께 죽어 seed0 직후 seed1 8/50에서 중단됐다. 또한 드라이버에 CSV append 로직이 없어 seed0 완료 결과조차 `results.csv`에 누락됐다.
- **When to apply**: `experiments/*/code/run_wave_*.sh` 같은 모든 배치 드라이버 작성·런치 시 — 그리고 드라이버 안에는 cell-단위 결과를 공용 CSV/JSON aggregator에 **inline append** 하는 단계를 반드시 포함한다 (셀 실행 후 별도 aggregator pass를 기대하지 말 것).

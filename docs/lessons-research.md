---
domain: research
updated: 2026-04-15
covers: [answer-formulator, critic, experiment-planner]
---

# Lessons — Research (answer-formulate / critique / experiment-plan)

answer-formulator, critic, experiment-planner가 작업 시작 전에 이 파일을 Read한다. append-only — 기존 엔트리 편집 금지, 신규만 append.

Phase B-1/B-2/C-1 도메인: Direct Answer + Evidence Chain 작성, 근거 4축 비판, Evidence verification 실험 계획. (2026-04-15 이전 엔트리는 divergent ideation 프레임 기준이므로 과거 라벨 그대로 보존.)

## How to add

`/research-lesson research "<rule title>"`

---

<!-- append entries below this line -->

## 2026-04-15 — answer-formulator↔critic 독립성 유지
- **Rule**: critic은 answer-formulator의 산출물만 읽고 동일 세션 프롬프트·프리셋을 공유하지 않는다 — 별도 agent thread에서 활성화한다
- **Why**: 같은 컨텍스트에서 생성과 비판을 섞으면 "자기 방어 편향"으로 약점을 축소하게 되어 Evidence 4축 점수가 부풀려진다
- **When to apply**: Phase B-2에서 critic 활성 시 — answers/<slug>.md를 독립 입력으로 받아 4축(Grounding Validity / Support Strength / Counter-Evidence / Verifiability) 평가

## 2026-04-15 — codex 교차 검증 통과 기준
- **Rule**: 각 Evidence가 Grounding≥3 AND Support≥3 AND Verifiability≥3 AND codex-review 통과 네 조건을 모두 만족할 때 Answer를 C-1 planner로 넘긴다
- **Why**: 내부 critic 점수만으로는 echo chamber를 벗어나지 못했고, codex는 독립 moderator 역할을 한다
- **When to apply**: Phase B-2 종료 전 — 어느 한 조건이라도 실패 시 answer-formulator로 재작업 요청

## 2026-04-15 — PLAN.md는 IV/DV/control을 명시해야 한다
- **Rule**: experiment-planner가 작성하는 PLAN.md는 Evidence 매핑·IV·DV·control·baseline·metric·ablation·resource·Expected Under/If Wrong 섹션을 필수로 포함한다
- **Why**: IV/DV가 빠진 PLAN은 code-implementer가 해석을 추측으로 채우게 되어 결과 해석 단계에서 Evidence verdict(CONFIRMED/REFUTED/INCONCLUSIVE/IMPL_BUG)를 결정할 수 없다
- **When to apply**: Phase C-1 산출물 gate — 빠진 섹션 발견 시 즉시 반려

## 2026-04-15 — Evidence grounding first, then Direct Answer
- **Rule**: answer-formulator는 먼저 hybrid_query로 RAG chunk + KG matched Paper/Claim을 수집하고, 그 결과를 citation과 함께 answers/<slug>.md에 기록한 뒤에만 Direct Answer 문단과 Evidence Chain을 작성한다
- **Why**: 근거 수집 없이 작성된 Answer는 fabrication 위험이 크고, critic의 Grounding Validity 축에서 0점 맞아 재작업 비용이 커진다
- **When to apply**: Phase B-1 시작 시 — hybrid_query.py 실행 로그와 top-k chunk/node를 answers 파일 상단에 붙인다

<!-- seeded 2026-04-15 -->

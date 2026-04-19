---
domain: analysis
updated: 2026-04-15
covers: [results-analyst]
---

# Lessons — Analysis (results)

results-analyst가 작업 시작 전에 이 파일을 Read한다. append-only.

Phase C-2 도메인: claim-result gap 해석, 4-way 실패 분류, 통계 검정, HTML 리포트.

## How to add

`/research-lesson analysis "<rule title>"`

---

<!-- append entries below this line -->

## 2026-04-15 — 4-way 실패 분류 강제
- **Rule**: results-analyst는 실패한 모든 실험 행에 대해 claim / impl / setup / data 중 하나로 원인을 분류하고 diagnoses/<slug>.md에 근거와 함께 기록한다
- **Why**: 분류 없이는 다음 루프의 answer-formulator가 Evidence를 재작성할지 폐기할지 판단할 수 없어 동일 실패가 반복된다
- **When to apply**: Phase C-2 마지막 — 한 실패라도 unclassified 상태면 gate 차단

## 2026-04-15 — 자기완결 HTML 리포트
- **Rule**: HTML 리포트는 외부 CSS/JS를 참조하지 않고 인라인 <style>·<script>, 이미지는 base64 data URL로 내장한다
- **Why**: 공유 시 상대경로가 깨지고, 아카이브 후 수개월 뒤에도 동일하게 렌더되어야 diagnosis가 재현 가능하다
- **When to apply**: results-analyst가 results_<slug>/report.html 생성 시

## 2026-04-15 — Claim-result gap 테이블 필수
- **Rule**: 모든 분석 리포트는 "저자 주장 vs 우리 결과" 테이블을 포함하며, 각 행에 metric, claimed value, observed value, delta, 4-way 분류를 적는다
- **Why**: gap을 표 형식으로 시각화하지 않으면 서술 중 일부 metric이 암묵적으로 누락된다
- **When to apply**: Phase C-2 리포트 렌더링 단계 — 테이블 누락 리포트는 반려

## 2026-04-15 — PNG + HTML 이중 산출물
- **Rule**: 주요 비교 플롯은 PNG(개별 공유용)와 HTML 리포트 내 base64 내장(통합 뷰)을 모두 생성한다
- **Why**: PNG만 있으면 내러티브가 흩어지고, HTML만 있으면 슬랙·논문에 바로 붙이기 힘들다
- **When to apply**: analysis 스크립트의 출력 단계 표준 컨벤션

<!-- seeded 2026-04-15 -->

## 2026-04-15 — force-rule 차원은 step-index와 독립적 confound
- **Rule**: force-commit ablation을 보고할 때 force_rule (argmax / sampled / prophet-thresh) 차원을 별도 축으로 분리해서 보고하라. 동일 t*에서 rule에 따라 결과가 정반대일 수 있다
- **Why**: diffusion-llm-step iter1 GSM8K n=50에서 t*=0.5T, argmax는 -24pt 드롭, prophet@0.9는 +2pt. PLAN H1의 '≤2pt drop' 예측은 prophet-style에만 적용되며 argmax는 별도 mechanism
- **When to apply**: force-commit 또는 early-commit 계열 ablation 리포트 작성 시 — rule을 표 축으로 드러내지 않으면 mechanism 결론이 뒤집힌다

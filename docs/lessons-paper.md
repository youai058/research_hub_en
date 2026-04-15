---
domain: paper
updated: 2026-04-15
covers: [paper-hunter, paper-summarizer, rag-curator]
---

# Lessons — Paper (hunt / summarize / RAG)

paper-hunter, paper-summarizer, rag-curator가 작업 시작 전에 이 파일을 Read한다. append-only.

Phase A-1 도메인: arXiv/OpenReview 수집, PDF 파싱, Marp 요약, ChromaDB 인덱싱.

## How to add

`/research-lesson paper "<rule title>"`

---

<!-- append entries below this line -->

## 2026-04-14 — KG bootstrap with sibling .kg.json
- **Rule**: 모든 prose-writing agent는 결과 .md 옆에 같은 이름의 .kg.json을 함께 작성한다
- **Why**: KG는 LLM 추론 없이 에이전트가 적은 그대로만 반영하기에, byproduct 파일이 단일 진실이다
- **When to apply**: paper-summarizer / answer-formulator / critic / experiment-planner / code-implementer / results-analyst 모든 산출물 생성 후

## 2026-04-14 — Listing vs summarization: full-text 요구 수준 분리
- **Rule**: paper-hunter(리스팅)는 abstract·API 메타만으로 판단·분류·dedup·raw.md 생성하고, PDF 전문은 venue_class 분류 불가 / near-duplicate 의심 / relevance 애매 중 하나일 때에만 첫 2–3페이지를 optional하게 fetch한다. paper-summarizer(요약)는 여전히 full-text PDF를 pymupdf로 파싱해야 하며 abstract-only 요약은 `papers/_rejected/`로 격리한다.
- **Why**: 리스팅은 수백 건 훑는 고처리량 단계라 전문 파싱을 강제하면 rate limit·파싱 실패로 drop이 늘고, 요약은 저자 주장과 증거를 분리해야 하므로 전문 독해 없이는 Critical Reading 품질이 보장되지 않는다. 두 단계의 요구 수준을 혼동하면 리스팅이 느려지거나 요약이 얕아진다.
- **When to apply**: paper-hunter가 abstract만으로 판단이 서면 그대로 raw.md에 기록하고, 위 3가지 애매함 신호 중 하나가 뜰 때에만 pdf_cache에 첫 몇 페이지를 받아 판단을 보조한다. paper-summarizer는 raw.md를 입력으로 받더라도 항상 PDF 전문을 새로 파싱한다.

## 2026-04-15 — paper-rag must skip _fixture/ and underscore dirs
- **Rule**: paper-rag index.py는 papers/ 하위 `_fixture`, `rag`, `kg`, 그리고 밑줄(`_`)로 시작하는 디렉토리를 무조건 skip한다
- **Why**: KG 스모크 테스트용 `papers/_fixture/kg-*/paper.md`가 RAG 청크로 잘못 인덱싱되어 query.py 결과에 `bad_0_0` 같은 테스트 문서가 섞였다
- **When to apply**: 새 인덱서 경로 추가나 fixture 디렉토리 생성 시 — 컨벤션은 `_`-prefix = "indexing/ingest 대상 아님"

## 2026-04-15 — Venue routing: drop 금지, etc/로 라우팅
- **Rule**: whitelist 11 venue에 없더라도 논문을 drop하지 말고 `papers/etc/<Year>/<slug>.md`로 라우팅하며 frontmatter에 `venue`(원문)·`venue_class: "etc"`를 기록한다
- **Why**: ACL Findings·workshop·arXiv preprint·저널이 relevance 필터링 대상에서 빠지면 gap mining 품질이 떨어진다
- **When to apply**: paper-hunter의 venue 분류 단계 — 분류 불가 시 etc로 폴백, 절대 drop 금지

## 2026-04-15 — Full-text PDF 강제 (paper-summarizer)
- **Rule**: paper-summarizer는 abstract-only로 5-part 요약을 생성해선 안 되며, 반드시 pymupdf로 full-text PDF를 파싱해 Critical Reading 섹션까지 작성한다
- **Why**: abstract만으로는 저자 주장과 실제 증거 gap을 포착할 수 없어 answer-formulator가 잘못된 전제 위에 Evidence를 세운다
- **When to apply**: Phase A-1 paper-summarizer 활성 시 — PDF 파싱 실패 시 요약 보류하고 `papers/_rejected/`로 격리

## 2026-04-15 — paper-hunter 키워드는 분야 canonical 용어로 넓게 (recall-first)
- **Rule**: 사용자 narrow topic(예: "LLDM denoising step 순서")을 그대로 `--keywords`로 넣지 말고, 축(모델족/문제/방법)을 분야 canonical 용어(예: `"LLDM" "large language diffusion"`)로 치환해 2-3개 축까지만 유지한다. narrow term은 paper-triage `--topic`에만 남긴다
- **Why**: hunter는 recall을, triage는 precision을 맡는 2단계 구조다. hunter가 narrow term으로 miss하면 triage에 도달할 후보 자체가 사라져 복구 불가. arXiv 쿼리는 metadata 검색이라 긴 문장·좁은 방법명은 0건 리콜이 흔하다
- **When to apply**: orchestrator가 A-1 진입 시 topic → `--keywords` 변환을 수행. paper-hunter 호출 전 키워드가 문장형이거나 narrow method 이름이면 중단하고 분야 용어로 재구성. 규칙·예시 테이블은 `paper-hunt` 스킬 "키워드 전략" 섹션

## 2026-04-15 — paper-hunt 키워드는 title ∪ abstract 양쪽 매칭
- **Rule**: paper-hunter는 모든 source(arxiv/anthology/openreview)에서 키워드 매칭을 title과 abstract 양쪽에 걸쳐 수행한다. arxiv 쿼리는 `(ti:"kw" OR abs:"kw")`, anthology는 listing 단계에서 title pre-filter 없이 detail fetch 후 title+abstract 문자열에 매치, openreview는 venueid 전체 dump이므로 자동으로 양쪽 포함.
- **Why**: 이전 arxiv `abs:"kw"` 단독·anthology title-only pre-filter 방식은 키워드가 한쪽에만 등장하는 논문을 구조적으로 누락했다. recall 담당인 paper-hunter가 이런 miss를 내면 하류 triage에 도달조차 못하므로 복구 불가.
- **When to apply**: paper-hunt 코드 수정 시 이 규칙을 유지할 것. anthology에서 detail fetch가 비싸지만 `--max-per-venue-year` cap이 도달 즉시 짧아지는 안전장치가 있으므로 title pre-filter를 다시 넣지 않는다.

---
domain: paper
updated: 2026-04-16
covers: [paper-hunter, paper-summarizer, rag-curator]
---
<!-- Latest appends: 2026-04-16 planning-first multi-figure paper-summarizer -->


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

## 2026-04-15 — paper-rag must skip _fixture/ and underscore dirs
- **Rule**: paper-rag index.py는 papers/ 하위 `_fixture`, `rag`, `kg`, 그리고 밑줄(`_`)로 시작하는 디렉토리를 무조건 skip한다
- **Why**: KG 스모크 테스트용 `papers/_fixture/kg-*/paper.md`가 RAG 청크로 잘못 인덱싱되어 query.py 결과에 `bad_0_0` 같은 테스트 문서가 섞였다
- **When to apply**: 새 인덱서 경로 추가나 fixture 디렉토리 생성 시 — 컨벤션은 `_`-prefix = "indexing/ingest 대상 아님"

## 2026-04-15 — Venue routing: drop 금지, etc/로 라우팅
- **Rule**: whitelist 11 venue에 없더라도 논문을 drop하지 말고 `papers/marp-summary/etc/<Year>/<slug>.md`로 라우팅하며 frontmatter에 `venue`(원문)·`venue_class: "etc"`를 기록한다
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

## 2026-04-16 — paper-summarizer는 PDF를 안 읽는다 — Gemini digest 2-stage 파이프라인 전제
- **Rule**: paper-summarizer 에이전트의 Claude-side 비용을 'Claude가 PDF 전문을 읽는다'로 추정하지 말 것. 실제 파이프라인은 Stage 1(Gemini CLI gemini-3-pro-preview 1M 컨텍스트가 PDF → 2-5k word dense Markdown digest 생성, papers/digest/<V>/<Y>/<slug>.digest.md 캐시) → Stage 2(Claude가 digest + raw.md 메타만 읽고 5-part Marp + Critical Reading + Known/Unknown + .kg.json 작성). Claude 편당 비용은 digest ~3k 토큰 + raw.md 메타 읽기 + Marp 템플릿 채우기 + Critical Reading 추론 ≈ 30-60초. 따라서 176편 규모도 2h 남짓에 가능하며, 오산으로 템플릿 배치 스크립트(a3_batch_summarize.py 같은)로 우회하는 건 abstract-only/heuristic 요약을 정상 venue 디렉토리에 쌓는 결과가 되어 하류 QA stage evidence chain을 오염시킨다.
- **Why**: 2026-04-16 diffusion-LLM 코퍼스 수집 중 orchestrator가 paper-summarizer를 'per-paper Claude ~3분 PDF 읽기'로 잘못 모델링해 176편 × 3분 = 8.75h라 불가능하다고 판단, 템플릿 배치 Python 드라이버 작성을 시도했다가 사용자 denial로 halt. 실제는 digest가 이미 Gemini가 만들어놓은 텍스트라 Claude는 PDF를 직접 안 읽고 digest만 소비한다. skill 문서(.claude/skills/paper-summarize/SKILL.md §17-52)와 agent 문서(.claude/agents/paper-summarizer.md §24-27)에 명시되어 있었으나 orchestrator가 이를 무시하고 time budget을 잘못 산정. 배치 템플릿으로 우회하면 Critical Reading 섹션이 digest의 'Limitations stated by authors'로 degrade돼 저자 claim/실제 증거 분리가 사라지고, 이후 QA answer-formulator가 잘못된 근거 체인을 작성하게 된다.
- **When to apply**: A-3 paper-summarizer dispatch 전 orchestrator는 항상 (1) digest 캐시 존재율 확인(`papers/digest/` 하위 카운트) (2) 남은 digest 생성은 별도 백그라운드 bash로 처리 (3) Claude 분량은 '편당 30-60초 × 편수'로 산정 (4) 한 agent turn에 한계가 있으면 paper-summarizer를 accepted 리스트를 분할한 병렬 dispatch로 N개 동시 기동 (5) Gemini OOM 편은 skill의 pymupdf fallback 경로가 자동 처리하므로 배치 드라이버로 heuristic 템플릿을 쌓지 말 것. paper-summarize skill §60-67 fallback 경로만 사용 허용. 새로운 Gemini heap 이슈(NODE_OPTIONS) 조정은 scripts/gemini_digest.py 레벨에서만 한다.

## 2026-04-16 — papers/ 디렉토리 type-segregated 구조 전환
- **Rule**: papers/ 하위 파일은 용도별 4개 최상위 디렉토리로 분리 저장된다: `metadata/<V>/<Y>/<slug>.raw.md` (수집 메타), `digest/<V>/<Y>/<slug>.digest.md` (Gemini dense digest + `.pdf_cache/`), `marp-summary/<V>/<Y>/<slug>.md` (6-part Marp 요약 + `.figure_cache/`), `vector_db/` (ChromaDB, KG sqlite, manifest, kg-staging). 이전 flat 구조(`papers/<Venue>/<Year>/`에 모든 파일 혼재)는 폐기됨.
- **Why**: raw metadata, binary PDF cache, generated digest, final Marp summary, vector DB가 같은 <Venue>/<Year>/ 아래 혼재하면 (1) glob 패턴이 타입 구분 없이 전부 매칭 (2) .gitignore 세분화 불가 (3) RAG 인덱서가 digest를 잘못 인덱싱하는 사고 발생. 용도별 분리로 각 에이전트가 자기 산출물 디렉토리만 스캔.
- **When to apply**: 새 저장 경로나 파일 타입 추가 시 반드시 이 4-way 분리를 유지할 것. gemini_digest.py는 raw.md 경로에서 `metadata`를 찾아 papers_root를 역산하므로 metadata/ 계층을 변경하면 깨짐.

## 2026-04-16 — paper-summarizer adaptive outline-first 템플릿 (고정 6-part 폐기)
- **Rule**: paper-summarizer는 고정 6-part 템플릿(Summary&Contribution/Motivation/Observation/Method/Setup/Result)을 더 이상 사용하지 않는다. 대신 **논문마다 outline을 먼저 설계**하고 필수 앵커 4개(TL;DR blockquote → Method → Result → Critical Reading)만 순서 고정, 그 사이 자유 섹션(Motivation/Observation/Setup/Analysis/Conclusion 또는 narrative 한국어 H2)은 논문 흐름에 맞게 선택한다. 파일 최상단에 `<!-- OUTLINE: ... -->` HTML 주석으로 outline을 명시하고 이후 도중 재배치 금지. TL;DR은 H1 lead 직후 `> ` blockquote 한두 문장으로 고정. 결과표는 반드시 Markdown 표(이미지 스크린샷/figure 대체 금지). Key Figure는 Method 또는 Observation 섹션 안쪽/직후의 의미 있는 자리에 배치 (title 직후 고정 X). Keywords는 선택(쓸 때만 말미). Marp frontmatter는 유지(PPT 호환). PROMPT_VERSION은 v4→v5 bump으로 기존 digest 캐시 전면 무효화.
- **Why**: 사용자가 2026-04-16에 수기 작성한 Notion 스타일 요약 6편(ExportBlock-615b3bec.../예시 ...md)을 reference로 제시하며 기존 6-part Marp 출력이 "양식이 별로야"라고 rejected. 분석 결과 사용자의 스타일은 (1) TL;DR blockquote 오프닝 (2) 논문마다 다른 section 구조 — classical(Intro/Method/Setup&Result/Analyse/Conclusion) 또는 narrative(한국어 H3 질문형) (3) 수치는 본문 bullet에 녹이고 결과표는 Markdown 표 (4) 저자 claim과 실제 증거 gap을 본문 흐름 속에 자연스럽게, Critical Reading은 별도 bullet 섹션 (5) Key Figure는 서술 맥락 안에 배치. 고정 6-part는 narrative flow와 수기 스타일의 논리 흐름을 깨고, 논문마다 딱 맞지 않는 섹션(예: Observation 없는 논문)에 "(해당 없음)" placeholder를 남김. adaptive template으로 전환해 읽기 자료 품질을 높이고, 필수 앵커 4개만 유지해 RAG 청킹 일관성과 answer-formulator의 근거 추출 안정성을 동시에 확보.
- **When to apply**: (1) paper-summarizer가 digest 읽은 뒤 본문 작성 전에 반드시 OUTLINE 주석을 먼저 작성. (2) 앵커 4개(TL;DR/Method/Result/Critical Reading) 누락 시 실패로 간주. (3) 결과 수치를 figure/이미지로만 제시하고 Markdown 표로 재현하지 않으면 재작성. (4) gemini_digest.py PROMPT_VERSION 변경 시 반드시 SKILL.md · paper-summarizer.md · research_hub/CLAUDE.md §6 3곳 모두 동기 유지. (5) harness-validate의 skill/agent frontmatter 검증은 description에 "6-part" 토큰 잔존 여부를 수동 확인. (6) 기존 marp-summary/ 디렉토리의 6-part 포맷 파일은 재요약 전까지 legacy로 유지 (RAG 청킹은 H2 기반이라 호환됨).

## 2026-04-16 — paper-summarizer planning-first multi-figure (OUTLINE → PLANNING)
- **Rule**: `<!-- OUTLINE: ... -->` 블록을 `<!-- PLANNING: ... -->` 블록으로 전환한다. PLANNING은 두 서브섹션을 모두 가진다 — (1) **SECTIONS**: 모든 섹션 번호·제목·이미지 배치를 upfront로 결정하며, 각 섹션은 `[Figure N]`(이미지 있음) 또는 `[no image]`(또는 `[no image — <사유>]`) 태그를 가진다. (2) **IMAGE_SOURCES**: SECTIONS에 등장한 각 figure의 `.figure_cache/<slug>__fig<N>.png` 경로 + 한 줄 용도. digest frontmatter의 `figures:` YAML 리스트(`{label, path, section_hint, reason}` 항목 최대 4개)에 존재하는 figure만 참조 가능. 섹션당 이미지 ≤1장, Method/Motivation/Observation/Analysis 계열에 주로 배치, Result/TL;DR/Critical Reading/Lead는 기본 `[no image]`. digest `figures: []`이면 전 섹션 `[no image]`. gemini_digest.py는 PROMPT_VERSION v5→v6 bump으로 DIGEST_PROMPT 말미가 `KEY_FIGURE` 단일 블록에서 `CANDIDATE: Figure N | Section: <hint> | Reason: <한 문장>` 형식의 최대 4개 candidate로 전환됐고, figure PNG 파일명은 `<slug>.png`에서 `<slug>__fig<N>.png`로 변경됨.
- **Why**: 2026-04-16에 사용자가 "각 논문마다 처음에 섹션 구조와 섹션별로 들어갈 이미지를 planning으로 정하고 정리하도록 해줘"를 요청. 기존 adaptive OUTLINE은 섹션 구조만 planning하고 이미지는 단일 Key Figure를 Method/Observation에 고정 배치했는데, 실제 논문에서는 Method 도식 + Motivation 관찰 figure처럼 2장 이상이 서로 다른 섹션에 들어가야 읽기 흐름이 자연스러운 경우가 많았다. 특히 paper-summarizer가 본문을 쓰는 도중에 "여기에 figure 하나 더 필요한데?"라며 되돌아가 재배치하면 outline 일관성이 깨지고 token도 낭비됨. upfront PLANNING으로 섹션과 이미지를 동시에 결정하면 (1) 본문 작성 단계에서 배치 판단 부하 제거 (2) figure 없는 섹션은 `[no image]`로 명시해 "figure 억지로 찾아 넣기" 방지 (3) multi-figure 논문(diagram + table + bar chart)의 풍성한 시각 설명을 섹션 흐름에 맞게 자연스럽게 편성 (4) outline-first 검증(`<!-- PLANNING:`)이 여전히 기계 점검 가능.
- **When to apply**: (1) paper-summarizer가 digest 읽은 뒤 본문 작성 전에 반드시 PLANNING 블록(SECTIONS + IMAGE_SOURCES 서브블록 **둘 다**) 작성. 한쪽 누락 시 실패로 간주. (2) SECTIONS에서 `[Figure N]` 태그가 붙은 섹션 수와 IMAGE_SOURCES 항목 수가 일치해야 함 (미스매치 시 재작성). (3) digest `figures:` 리스트에 없는 figure를 IMAGE_SOURCES에 등장시키면 실패. (4) 섹션당 이미지 ≤1장 규칙 위반 시 재작성. (5) digest `figures: []`인 논문은 PLANNING 모든 섹션을 `[no image]`로 두고 이미지 삽입 생략 — Critical Reading에 "figure 없음" 플래그 금지. (6) PROMPT_VERSION bump(v5→v6)으로 기존 digest 캐시는 전부 재생성돼야 하며 gemini_digest.py · SKILL.md · paper-summarizer.md · research_hub/CLAUDE.md §6 4곳 동기화 필수. (7) 기존 marp-summary/ 디렉토리의 OUTLINE 포맷 파일은 재요약 전까지 legacy로 유지 (RAG 청킹은 H2 기반이라 호환됨).

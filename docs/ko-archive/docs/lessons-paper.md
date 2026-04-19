---
domain: paper
updated: 2026-04-19
covers: [paper-hunter, paper-summarizer, rag-curator]
---
<!-- Latest appends: 2026-04-17 gemini_digest OpenReview UA + Node heap + CANDIDATE regex + figure-crop 3-stage -->
<!-- 2026-04-19: bodies compressed (dedup / point-to-SSOT) — all rules preserved, narrative prose trimmed -->


# Lessons — Paper (hunt / summarize / RAG)

paper-hunter, paper-summarizer, rag-curator가 작업 시작 전에 이 파일을 Read한다. append-only. 압축은 허용 (rule/artifact 보존 전제).

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
- **Rule**: whitelist venue (CLAUDE.md §1의 6 venue + `--include-arxiv` 플래그 시 추가 소스)에 없더라도 drop 금지. `papers/marp-summary/etc/<Year>/<slug>.md`로 라우팅하고 frontmatter에 `venue`(원문)·`venue_class: "etc"` 기록.
- **Why**: ACL Findings·workshop·arXiv preprint·저널이 relevance 필터링 대상에서 빠지면 gap mining 품질 하락.
- **When to apply**: paper-hunter venue 분류 단계 — 분류 불가 시 etc로 폴백, drop 금지.

## 2026-04-15 — Full-text PDF 강제 (paper-summarizer)
- **Rule**: paper-summarizer는 abstract-only로 요약 생성 금지. 반드시 pymupdf로 full-text PDF 파싱해 Critical Reading까지 작성.
- **Why**: abstract만으론 저자 주장과 실제 증거 gap을 포착 못 해 answer-formulator가 잘못된 전제 위에 Evidence 구축.
- **When to apply**: Phase A-1 paper-summarizer 활성 시. PDF 파싱 실패 시 요약 보류 + `papers/_rejected/`로 격리.

## 2026-04-15 — paper-hunter 키워드는 분야 canonical 용어로 넓게 (recall-first)
- **Rule**: 사용자 narrow topic을 그대로 `--keywords`로 넣지 말고, 축(모델족/문제/방법)을 분야 canonical 용어로 치환해 **최대 2개** 축까지. narrow term은 paper-triage `--topic`에만 남긴다. 상세 규칙·예시는 `paper-hunt` 스킬 "키워드 전략" 섹션.
- **Why**: hunter=recall / triage=precision 2단계. hunter가 narrow term으로 miss하면 triage 도달 후보 자체가 사라져 복구 불가. arXiv 쿼리는 metadata 검색이라 긴 문장·좁은 방법명은 0건 리콜 흔함.
- **When to apply**: 호출자가 A-1 진입 시 topic → `--keywords` 변환 수행. 키워드가 문장형이거나 narrow method 이름이면 중단하고 분야 용어로 재구성.

## 2026-04-15 — paper-hunt 키워드는 title ∪ abstract 양쪽 매칭
- **Rule**: 모든 source(arxiv/anthology/openreview)에서 키워드 매칭을 title과 abstract 양쪽에 수행. arxiv: `(ti:"kw" OR abs:"kw")`, anthology: listing 단계에서 title pre-filter 없이 detail fetch 후 title+abstract 매칭, openreview: venueid 전체 dump이므로 자동 양쪽 포함.
- **Why**: 이전 arxiv `abs:"kw"` 단독·anthology title-only pre-filter 방식은 키워드가 한쪽에만 등장하는 논문을 구조적 누락. recall 담당 hunter가 miss하면 하류 triage 도달 불가.
- **When to apply**: paper-hunt 코드 수정 시 유지. anthology detail fetch 비용은 `--max-per-venue-year` cap이 안전장치. title pre-filter 재도입 금지.

## 2026-04-16 — paper-summarizer는 PDF를 안 읽는다 — 2-stage Gemini digest 파이프라인
- **Rule**: paper-summarizer Claude-side 비용을 '편당 PDF 전문 읽기'로 모델링 금지. 실제는 Stage 1(Gemini CLI `gemini-3-pro-preview` 1M ctx가 PDF → 2-5k word dense Markdown digest, `papers/digest/<V>/<Y>/<slug>.digest.md` 캐시) → Stage 2(Claude가 digest + raw.md 메타만 소비). 편당 Claude 비용 ≈ 30-60초. 176편도 2h 남짓 가능. 템플릿 배치 스크립트로 우회(a3_batch_summarize.py 등) 금지 — abstract-only/heuristic 요약이 정상 venue 디렉토리에 섞이면 하류 QA evidence chain 오염.
- **Why**: 2026-04-16 diffusion-LLM corpus 수집 중 per-paper Claude ~3분으로 오산해 176편 × 3분 = 8.75h 불가능 판단 → 배치 템플릿 우회 시도 → 사용자 halt. skill 문서(§17-52)·agent 문서(§24-27)에 명시되어 있었으나 무시. 우회 시 Critical Reading이 digest의 "Limitations stated by authors"로 degrade.
- **When to apply**: A-3 dispatch 전: (1) digest 캐시 존재율 확인(`papers/digest/` 카운트) (2) 미존재 digest는 백그라운드 bash로 별도 생성 (3) Claude 분량 = 편당 30-60초 × 편수로 산정 (4) turn 한계 시 accepted 분할 병렬 dispatch (5) Gemini OOM 편은 skill §60-67 pymupdf fallback만 사용, 배치 heuristic 금지. NODE_OPTIONS 조정은 gemini_digest.py 레벨.

## 2026-04-16 — papers/ 디렉토리 type-segregated 구조
- **Rule**: papers/ 하위 4-way 분리: `metadata/<V>/<Y>/<slug>.raw.md` (수집 메타), `digest/<V>/<Y>/<slug>.digest.md` (Gemini digest + `.pdf_cache/`), `marp-summary/<V>/<Y>/<slug>.md` (요약 + `.figure_cache/`), `vector_db/` (Chroma·KG·manifest·kg-staging). SSOT: `docs/harness-layout.md`. 이전 flat `papers/<V>/<Y>/` 혼재 폐기.
- **Why**: raw/PDF/digest/Marp/DB 혼재 시 (1) glob 패턴이 타입 구분 못 함 (2) .gitignore 세분화 불가 (3) RAG 인덱서가 digest 오인덱싱 사고 발생.
- **When to apply**: 새 저장 경로 추가 시 4-way 분리 유지. gemini_digest.py는 raw.md 경로에서 `metadata`를 찾아 papers_root 역산하므로 metadata/ 계층 변경 시 깨짐.

## 2026-04-16 — paper-summarizer adaptive outline-first (고정 6-part 폐기) — [SUPERSEDED by 2026-04-16 PLANNING 아래]
- **Rule**: 고정 6-part 템플릿(Summary/Motivation/Observation/Method/Setup/Result)은 폐기. **active 잔존 규칙**: TL;DR = H1 lead 직후 `> ` blockquote 한두 문장, 결과표는 반드시 Markdown 표(figure/스크린샷 대체 금지), Keywords는 선택(쓸 때만 말미), Marp frontmatter 유지. SSOT: CLAUDE.md §6. 구 PROMPT_VERSION v4→v5 bump (이미 v6까지 진행됨 — 아래 entry 참조).
- **Why**: 사용자 Notion-style reference 6편 기준 narrative flow 존중 필요. 6-part 고정은 "(해당 없음)" placeholder 남기고 읽기 품질 훼손.
- **When to apply**: OUTLINE 관련 상세는 **SUPERSEDED** — 아래 "PLANNING" entry 사용. 본 entry는 TL;DR/Markdown 표/Keywords 규칙만 여전히 유효 (CLAUDE.md §6과 동일).

## 2026-04-16 — paper-summarizer planning-first multi-figure (PLANNING block)
- **Rule**: 본문 작성 전 `<!-- PLANNING: ... -->` 블록 필수. 두 서브섹션 모두 요구: **SECTIONS** (섹션 번호·제목·`[Figure N]` 또는 `[no image]` 태그 upfront), **IMAGE_SOURCES** (각 figure의 `.figure_cache/<slug>__fig<N>.png` 경로 + 한 줄 용도). 섹션당 이미지 ≤1장. Method/Motivation/Observation/Analysis에 주로 배치, Result/TL;DR/Critical Reading/Lead는 기본 `[no image]`. digest `figures: []`이면 전 섹션 `[no image]`. 파일명: `<slug>__fig<N>.png`. PROMPT_VERSION v5→v6 (CANDIDATE 포맷). SSOT: CLAUDE.md §6, paper-summarize SKILL.md.
- **Why**: Method 도식 + Motivation 관찰 figure 등 multi-figure 논문에서 single Key Figure 고정 배치가 흐름 훼손. 본문 작성 중 재배치 시 outline 일관성·token 낭비.
- **When to apply**: (1) PLANNING 두 서브블록 누락 시 실패 (2) `[Figure N]` 태그 수 = IMAGE_SOURCES 항목 수 (미스매치 재작성) (3) digest `figures:` 리스트 외 figure 참조 시 실패 (4) 섹션당 ≤1장 위반 재작성 (5) digest `figures: []`이면 Critical Reading에 "figure 없음" 플래그 금지 (6) PROMPT_VERSION bump 시 gemini_digest.py · SKILL.md · paper-summarizer.md · CLAUDE.md §6 4곳 동기.

## 2026-04-17 — raw.md `authors:` is a JSON-array string, not CSV
- **Rule**: raw.md frontmatter `authors:`는 hunt.py가 `json.dumps(authors)`로 방출한 JSON-array 리터럴(예: `authors: ["Smith, John", "Doe, Jane"]`). consumer는 JSON array 먼저 파싱, 실패 시에만 CSV fallback. 단순 `.split(",")` 금지.
- **Why**: `_parse_frontmatter`가 line-wise scalar parser라 `[` 값을 verbatim string 반환. naive `,` split 시 multi-author 논문마다 4개 corrupt author로 깨지고 kg_skeleton.py가 이를 Author 노드로 승격해 KG 오염. 2026-04-17 commit 59e0e7a 리뷰에서 Critical bug 발견.
- **When to apply**: (1) gemini_digest.py `_write_digest`의 authors 파싱 — JSON-first → CSV fallback (2) kg_skeleton.py `_build_skeleton`은 digest frontmatter (이미 정규화된 YAML list) 기준 (3) hunt.py 출력 포맷 변경 시 모든 consumer 동시 업데이트. raw.md frontmatter SSOT = hunt.py.

## 2026-04-17 — OpenReview PDF fetch는 browser User-Agent 필수
- **Rule**: `scripts/gemini_digest.py`의 PDF fetch는 OpenReview(`openreview.net/pdf?id=...`) 도메인에 대해 브라우저 UA(`Mozilla/5.0 ... Chrome/...`) 송신. 다른 도메인(arXiv)은 현행 UA OK.
- **Why**: 2026-04-17 Hierarchy Decoding (ICLR 2026, OpenReview-only) 요약 중 nginx 403. OpenReview는 bot UA 차단 정책 → ICLR/NeurIPS 등 OpenReview 호스팅 논문에서 재발 확실. arXiv는 동일 문제 없음.
- **When to apply**: gemini_digest.py에 도메인별 UA 분기 + OpenReview 기본값 browser UA. `--pdf-cache` 선행 seed 성공 시 fetch skip.

## 2026-04-17 — Gemini CLI는 63k+ char PDF에서 Node heap OOM, NODE_OPTIONS 선제 주입
- **Rule**: `scripts/gemini_digest.py` Gemini CLI 스폰 시 `NODE_OPTIONS=--max-old-space-size=8192` (또는 12288) 기본 주입. 기존 `NODE_OPTIONS` 있으면 덮어쓰지 말고 append.
- **Why**: KLASS (83k char)·Hierarchy Decoding (63k char) 모두 Node.js v8 기본 heap(~4GB) 초과 OOM. 60k+ char 논문은 diffusion-LLM corpus 기준 흔함 — 재발 확실.
- **When to apply**: gemini_digest.py subprocess/os.environ 세팅 지점 수정. 사용자 override 우선. 개별 에이전트 프롬프트에는 이 규칙 복사 금지 — gemini_digest.py 한 곳만.

## 2026-04-17 — DIGEST `CANDIDATE:` 파서는 `Reason:` 리터럴 prefix를 강제하지 말 것
- **Rule**: `CANDIDATE: Figure N | Section: <hint> | <reason>` 포맷. `Reason:` 리터럴 prefix는 **optional**. `| ` 구분자 split으로 충분. 대안 정규식: `^CANDIDATE:\s*(?P<label>Figure \d+)\s*\|\s*Section:\s*(?P<section>[^|]+)\s*\|\s*(?:Reason:\s*)?(?P<reason>.+)$`.
- **Why**: 2026-04-17 Hierarchy Decoding 요약 중 Gemini가 `Reason:` 없이 출력 → 기존 regex가 candidate 3개 drop, `figures: []`. prompt를 빡빡하게 강제하는 것보다 파서를 관대하게 만드는 게 LLM 출력 variance에 강건.
- **When to apply**: gemini_digest.py CANDIDATE 라인 파싱 완화. 수정 후 두 variant(`Reason:` 있음/없음) 모두 figures 리스트에 들어가는지 스모크 테스트.

## 2026-04-17 — Figure crop은 prior-caption 상한 + 텍스트-overlap reject + closest-cluster 3단계
- **Rule**: `_extract_figure_png` "above caption" crop: (1) 같은 페이지 직전 `Figure M:`/`Table M:` 캡션 bottom을 상한(+`FIGURE_PRIOR_CAPTION_PAD` 6pt 여백) (2) `_refine_figure_region`에서 raster/drawing bbox를 `FIGURE_CLUSTER_VGAP_PT` 18pt 간격으로 수직 클러스터링 (3) cluster text-block 겹침 > `FIGURE_CLUSTER_TEXT_OVERLAP_REJECT` 0.55면 reject (4) 생존 cluster 중 y1 최대 선택. **union-all 방식 금지**.
- **Why**: 2026-04-17 Prophet 논문에서 Figure 3이 Figure 2 전체+캡션까지 합쳐짐, Figure 5는 본문+표 포함. 원인: `above` region이 page_top부터 시작(→ Fig 2/3 union), 페이지 전체 drawing 무차별 union(→ 450개 drawing hull). prior-caption 상한으로 Fig 3, cluster text-overlap reject로 Fig 5 해결. Fig 1/2 regression 없음.
- **When to apply**: gemini_digest.py figure extraction 수정 시 Prophet PDF(`papers/digest/etc/2026/.pdf_cache/diffusion-language-models-know-the-answer-before-decoding.pdf`) Fig 1/2/3/5 4장 스모크 재추출 — Fig 3은 다이어그램만, Fig 5는 histogram 하나만. `_refine_figure_region` 로그에 `clusters=N`, `text_overlap=0.NN`, `survivors=N` 3필드 유지. corner case 시 상수 조정보다 필터 추가 선호.

## 2026-04-17 — paper-triage는 dense-retrieval pre-filter 뒤에서만 rubric scoring
- **Rule**: A-2 paper-triage는 전체 corpus abstract JSON을 Claude에 넘기지 않는다. A-1.5 `abstract-indexer`가 유지하는 ChromaDB `abstracts` collection에서 `retrieve.py`가 cosine top-K(기본 K≤300, threshold 0.5) 좁힌 candidate set에서만 rubric 0-5 scoring. `triage_context.exclude`는 hard veto(substring match), `signal_methods`는 cosine +0.05 boost + `signal_hit: true` hint.
- **Why**: 1,491개 raw.md → 2.65 MB abstract JSON → Opus 입력 ~660K 토큰. Opus가 Lucene 역할로 토큰 비용이 corpus 크기에 선형 증가. OpenReview·Semantic Scholar·Elicit 모두 2-stage retrieval 패턴. repo는 rag-curator가 bge-m3+Chroma 보유했으나 triage가 재사용 안 하고 있었음.
- **When to apply**: paper-triage SKILL.md·agent 수정 시 `collect_abstracts.py`를 Step 2 default로 되돌리지 말 것. retrieve.py 선 호출. 새 corpus로 triage 실패 시 A-1.5 manifest 확인. Ad-hoc 호출에서 collection 비어 있으면 exit 5 — abstract-indexer 수동 실행.

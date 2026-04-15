---
name: paper-summarize
description: "논문 전문(full-text PDF) 5-part 비판적 Marp 요약. pymupdf 파싱 강제(abstract-only 금지), 5섹션(Claims/Experiments/Methodology/Setup/Results) + Critical Reading + Known/Unknown, Marp frontmatter, 수식·수치 원문 인용. paper-summarizer 전용. 트리거: '논문 요약', 'Marp 슬라이드', 'paper summary'."
---

# Paper Summarize Skill

논문을 **비판적**이고 **간결**하게 5-part 구조로 요약하는 절차와 템플릿.

## 입력

- `papers/<V>/<Y>/<slug>.raw.md` (paper-hunter 산출) — 이 파일은 **abstract-level 메타데이터**다. paper-hunt 스킬은 리스팅 단계에서 abstract·API 메타로만 판단하며, raw.md 본문의 `## Abstract` 섹션에는 abstract만 들어 있다.
- 본 요약 단계는 raw.md만으로는 부족하므로 **반드시 PDF 전문을 다운로드·pymupdf로 파싱**해야 한다. abstract-only 요약은 금지.

## 전문(full-text) 읽기 프로토콜 — 2-Stage (필수)

이 스킬은 **Claude가 PDF 전문을 직접 읽지 않는다**. Stage 1에서 Gemini CLI(gemini-3-pro-preview, 1M+ 컨텍스트)가 PDF를 읽고 dense digest를 생성하고, Stage 2에서 Claude paper-summarizer agent가 그 digest + raw.md 메타만을 근거로 5-part Marp + KG를 작성한다. pymupdf 직접 파싱은 **fallback 경로에서만** 허용된다.

### Stage 1 — Gemini digest 생성 (bash)

```bash
python3 .claude/skills/paper-summarize/scripts/gemini_digest.py <raw_md_path>
# 성공 시 stdout 마지막 줄 = 절대경로 papers/<V>/<Y>/.gemini_digest/<slug>.digest.md
# 실패 시 non-zero exit code (2: raw.md, 3: PDF, 4: pymupdf, 5: gemini CLI)
```

스크립트가 내부적으로 수행하는 일:

1. **raw.md frontmatter 파싱** → `pdf_url` / `arxiv_id` / `anthology_id` / `cvf_url` / `slug` / `venue_class` / `venue` / `year`.
2. **PDF 확보** (4-way fallback, 기존 우선순위 유지):
   1. raw.md frontmatter의 `pdf_url` (arXiv/OpenReview/CVF/Anthology)
   2. `arxiv_id`로 `https://arxiv.org/pdf/{id}.pdf`
   3. `anthology_id`로 `https://aclanthology.org/{id}.pdf`
   4. `cvf_url` 직접
   - 저장 경로: `papers/<V>/<Y>/.pdf_cache/<slug>.pdf` (gitignore 대상). 이미 있으면 재사용, `--force`로 무효화.
3. **pymupdf 전문 파싱** + `len(full_text) > 3000` 체크.
4. **Gemini 호출**: `gemini -m gemini-3-pro-preview -p "<digest_prompt v1>" -o text` 에 full_text를 stdin으로 전달. 타임아웃 600s. 출력은 장문 Markdown digest (2–5k words, 수식·수치 verbatim).
5. **digest 파일 작성**: `papers/<V>/<Y>/.gemini_digest/<slug>.digest.md` (gitignore 대상). frontmatter에 `source_raw`, `source_pdf_sha256`, `generated_at` (KST), `model: gemini-3-pro-preview`, `prompt_version: v2`, 그리고 key figure 3필드(`key_figure_label`, `key_figure_reason`, `key_figure_path`) 기록. digest 캐시는 `source_pdf_sha256` **AND** `prompt_version`이 둘 다 일치해야 유효하다 — PROMPT_VERSION이 bump되면 PDF sha가 같아도 재생성된다. `--force`는 캐시를 전면 무효화.
6. **Key figure 선정 + 추출** (v2부터):
   - Gemini가 디gest 말미에 `KEY_FIGURE: Figure N` + `KEY_FIGURE_REASON: <한 문장>` 블록(또는 `KEY_FIGURE: NONE`)을 출력하도록 프롬프트가 강제한다. 테이블은 선택 대상이 아니다.
   - `gemini_digest.py`가 이 블록을 정규식으로 파싱해 `N`을 추출하고, pymupdf로 해당 번호의 캡션(`^(Figure|Fig\.?)\s*N[:\.\s]`)을 찾아 캡션 **위쪽** 영역을 crop한다. 위가 비어있으면 아래쪽 → 그래도 실패하면 페이지 전체. 내부의 image block/`page.get_drawings()` union으로 bbox를 축소하되, 축소된 높이가 페이지 높이의 10% 미만이면 원본 영역 유지.
   - `fitz.Matrix(3, 3)` (≈216 DPI)로 clip 렌더 → `papers/<V>/<Y>/.figure_cache/<slug>.png` (gitignore 대상).
   - sanity: PNG 파일이 10KB 미만이면 실패로 간주하고 삭제 → `key_figure_path: null`.
   - **figure 추출 실패는 fatal이 아니다**. digest는 그대로 성공 exit 0으로 쓰고, `key_figure_path`만 `null`로 기록한다. 다운스트림(agent)는 path가 null이면 Key Figure 슬라이드를 **생략**한다.

### Stage 2 — Claude summarizer (agent)

1. `raw_md_path`와 `digest_path`를 Read 도구로 읽는다. **pymupdf 직접 호출 금지** (fallback 제외).
2. digest의 `Claims (verbatim)` / `Methodology` / `Results` / `Ablations` / `Limitations` 섹션을 5-part Marp 템플릿에 매핑한다.
3. 수식·수치는 digest에 이미 verbatim으로 들어 있으므로 그대로 복사한다. paraphrase 금지는 유지.
4. Critical Reading / Known / Unknown은 digest에 없으므로 Claude가 작성한다 (digest의 "Limitations stated by authors" ≠ Critical Reading).
5. **Key Figure 임베딩**: digest frontmatter의 `key_figure_path`를 확인한다.
   - non-null이면 title 슬라이드 **바로 다음**(즉 `## 1. 주요 주장 (Claims)` 바로 앞)에 `## Key Figure — {key_figure_label}` 슬라이드를 **1장** 삽입한다. 포맷은 아래 Marp 템플릿의 Key Figure 블록을 그대로 사용.
   - `key_figure_path`는 raw.md 디렉토리 기준 상대경로로 기록되어 있으며, 최종 `<slug>.md`도 같은 디렉토리에 저장되므로 **경로 변환 없이 그대로** 이미지 src로 쓴다 (예: `./.figure_cache/<slug>.png`).
   - `null`이면 Key Figure 슬라이드 전체를 **생략**한다 (빈 슬라이드 만들지 마). 이는 실패 모드가 아니라 정상 경로이므로 Unknown/Critical Reading에 실패 플래그를 추가하지 않는다.
6. 저장 경로 라우팅은 기존 그대로: `venue_class` 필드 기반. `<slug>.kg.json`도 같은 디렉토리에 emit.

### Fallback (Gemini digest 실패 시)

Stage 1 스크립트가 non-zero로 끝나거나 digest가 비어있으면 **abstract-only가 아니라** 기존 pymupdf 경로로 진행한다:

1. Claude가 직접 `import fitz` + `papers/<V>/<Y>/.pdf_cache/<slug>.pdf`를 로드해 full_text 구성.
2. 섹션 분할 (`Introduction`, `Method/Approach`, `Experiments`, `Results`, `Ablation`, `Conclusion`, `Appendix`) → 5-part 근거로 사용.
3. 긴 논문(>80쪽)은 메인 → ablation 부록 → 기타 부록 순서로 점진 요약.
4. 출력 파일 frontmatter에 `digest_source: fallback-pymupdf`와 실패 이유(exit code + stderr 요약)를 반드시 기록.

PDF 확보 자체가 불가능한 경우에만 요약 중단 + `papers/_rejected/`로 격리 (기존 규칙). **Abstract-only 축소 요약은 정상 출력이 아니며**, 쓸 경우 Known/Unknown에 `full-text 미확인` 플래그 + Critical Reading skip.

## 출력 템플릿 (Marp)

```markdown
---
marp: true
theme: default
paginate: true
title: "{paper title}"
---

<!-- _class: lead -->

# {paper title}

**{authors}** — {venue} {year}

[arXiv]({url}) · [PDF]({pdf_url})

---

<!--
  Key Figure 슬라이드 — digest frontmatter의 `key_figure_path`가 non-null일 때만 삽입.
  `key_figure_path`는 raw.md 디렉토리 기준 상대경로이고 최종 <slug>.md도 같은 디렉토리에
  저장되므로 그대로 쓰면 된다. `key_figure_path`가 null이면 이 블록 전체를 생략할 것
  (빈 슬라이드 만들지 말 것).
-->

## Key Figure — {key_figure_label}

![w:650](./{key_figure_path})

{key_figure_reason}

---

## 1. 주요 주장 (Claims)

- {claim 1: one-liner}
- {claim 2}
- {claim 3}

> 저자가 명시적으로 말한 것만 여기에. 해석은 Critical Reading으로.

---

## 2. 뒷받침 실험 (Experiments)

| # | Claim | 실험 | 데이터셋 |
|---|---|---|---|
| 1 | claim 1 | exp-A | DS1 |
| 2 | claim 2 | exp-B | DS2 |

---

## 3. 방법론 (Methodology)

- 핵심 아이디어 한 문장
- 수식 (원문 그대로):

$$
\text{loss} = -\sum_i \log p(y_i | x_i)
$$

- 알고리즘 의사코드 또는 그림 참조

---

## 4. 실험 세팅 (Setup)

| 항목 | 값 |
|---|---|
| 모델 | ... |
| 데이터셋 | ... |
| Baselines | ... |
| Hyperparameters | lr=..., batch=..., steps=... |
| 평가 지표 | ... |
| Seed / 반복 | ... |
| 하드웨어 | ... |

---

## 5. 실험 결과 (Results)

- 주요 수치 (원문 그대로, 반올림 금지):
  - Claim 1: X 대비 Y (+Z%)
- 통계적 유의성 보고 여부
- Ablation 핵심 발견

---

## Critical Reading

**저자 주장 vs 실제 증거**:
- 저자는 "general improvement"라 주장하지만 실험은 DS1에서만.
- claim 3의 증거가 부록에만 있고 main text에 수치 없음.

**약점**:
- baseline 선택 편향 (구 버전 사용)
- seed 1개만 실행

---

## Known / Unknown

**Known**:
- 코드 공개 여부: {yes/no/partial}
- 재현 난이도: {easy/medium/hard}

**Unknown**:
- 다른 데이터셋 일반화 여부
- 큰 모델 스케일링 여부
- 수식 (eq. 3)의 유도 생략됨

---

## 관련 키워드 (RAG용)

`keyword1`, `keyword2`, `keyword3`, ...
```

## 비판적 추출 원칙

1. **저자 주장과 증거 분리**: Claims 섹션에는 저자가 쓴 문장만. 검증은 Critical Reading에.
2. **수식·수치 원문 인용**: paraphrase 금지. 반올림·단위 변환 금지.
3. **슬라이드 수 ~15개 목표**: 각 섹션 2~3 슬라이드. 과도한 상세 금지.
4. **Unknown은 반드시 채움**: 논문이 명시하지 않은 것(ablation 누락, 한계 미언급, 데이터 편향 등).
5. **키워드 추출**: 말미에 RAG 검색에 유용한 키워드 10~15개 리스트.

## 파일명·경로

- 입력: `papers/<V>/<Y>/<slug>.raw.md`
- 출력: `papers/<V>/<Y>/<slug>.md` (raw 파일은 보존, 새 파일 생성)
- 파일 길이: 200~500줄 목표, 초과 시 요약 축소

## 실패 모드

- **PDF 없음 / 404**: 다운로드 경로 4종(arxiv/openreview/anthology/cvf)을 전부 시도한 뒤에도 실패하면 요약을 **중단하고** orchestrator에 reject 리턴. abstract-only 요약은 해당 venue 디렉토리에 저장하지 말고 `papers/_rejected/<slug>.raw.md`로 격리 후 이유를 기록.
- **파싱 깨진 수식**: 해당 수식을 raw text로 code block에 보존 + Unknown에 플래그
- **너무 긴 논문 (80페이지+)**: 메인 → ablation 부록 → 기타 부록 순서로 섹션 단위 요약 후 통합. 부록 생략 시 "Appendix X.Y는 요약 생략" 명시.
- **저자 주장이 명확하지 않음**: Claims 섹션에 "저자 주장 추출 불확실" 플래그

## 체크리스트

- [ ] `gemini_digest.py` 실행 성공 → `.gemini_digest/<slug>.digest.md` 존재, 또는 실패 시 fallback 플래그(`digest_source: fallback-pymupdf`) 기록
- [ ] PDF 다운로드 성공 + (digest 경로) Gemini digest 생성 / (fallback 경로) pymupdf 파싱 성공 (`len(full_text) > 3000`)
- [ ] Introduction/Method/Experiments/Results/Appendix 중 최소 4개 섹션 본문 내용이 digest 또는 pymupdf 경로로 확보됨
- [ ] Marp frontmatter `marp: true`
- [ ] 5개 필수 섹션 모두 존재
- [ ] Critical Reading + Known/Unknown 포함 (full-text 기반일 때만 Critical Reading 허용)
- [ ] 수식·수치 원문 인용
- [ ] 슬라이드 ~15개, 500줄 이내
- [ ] 키워드 리스트 말미 포함
- [ ] key figure가 있으면 Marp에 임베딩 (없으면 스킵) — digest frontmatter `key_figure_path`가 non-null이면 title 슬라이드 직후에 `## Key Figure — {label}` 슬라이드 1장 삽입, null이면 생략
- [ ] 같은 디렉토리에 `<slug>.kg.json` 동시 작성 (아래 KG Emission 참조)
- [ ] 저장 경로: 원본 raw.md의 `venue_class` 필드를 그대로 따라 라우팅 (paper-hunt가 이미 결정해 놓은 값)
  - `whitelist` → `papers/<NeurIPS|AAAI|ICLR|ICML|ACL|EMNLP>/<Year>/`
  - `etc`       → `papers/etc/<Year>/` (평탄 구조, 하위 venue 디렉토리 없음)
  - 두 경로 모두 **정상 출력**이며 `etc`가 품질 열등을 의미하지 않는다 — 요약 기준은 동일하다.
- [ ] 금지 경로 확인: `papers/arXiv/`, `papers/OpenReview/`, `papers/preprint/`, `papers/workshop/`, `papers/findings/` 등 소스/속성 디렉토리에 저장하지 않았는지 (해당 논문은 전부 `papers/etc/<Year>/`로)

---

## KG Emission (byproduct)

요약 `.md`와 **같은 디렉토리**에 `<slug>.kg.json`을 반드시 작성한다. 이 스킬이 소유하는 노드 타입:

| 타입 | prefix | 필수 필드 |
|---|---|---|
| `Paper` | `paper:` | title, authors[], venue, year, url |
| `Author` | `author:` | name |
| `Venue` | `venue:` | name, year |
| `Claim` | `claim:` | text (저자 원문 인용), paper id |
| `Method` | `method:` | name |
| `Dataset` | `dataset:` | name |
| `Model` | `model:` | name |
| `Metric` | `metric:` | name |
| `Result` | `result:` | metric, value (원문 수치 그대로) |

**엣지**:
- `Paper --AUTHORED_BY--> Author`
- `Paper --PUBLISHED_IN--> Venue`
- `Paper --MAKES_CLAIM--> Claim`
- `Paper --USES_METHOD--> Method`
- `Paper --USES_DATASET--> Dataset`
- `Paper --USES_MODEL--> Model`
- `Paper --REPORTS_RESULT--> Result`
- `Result --EVIDENCED_BY--> Claim` (meta.polarity ∈ {support, contradict, mixed}; 필수)

ID 예시: `paper:greedy-coordinate-gradient-2023#local`, `claim:greedy-coordinate-gradient-2023--c1`

Provenance는 `KGFile` 루트에 `{source_file, source_sha, extracted_at, author_agent: "paper-summarizer"}`로 기입.

## Alias Check Protocol

**`Method | Dataset | Model | Metric`** 신규 노드 emit 전 반드시 alias lookup:

```bash
python3 .claude/skills/paper-kg/scripts/query.py lookup \
  --type Method --name-fuzzy "Greedy Coordinate Gradient"
```

- 매치 score ≥85: 기존 id 재사용 (새 노드 생성 금지)
- score <85: 새 id 생성 + `alias_check: {queried_name, matches: [...], decision: "new"}` 필드를 노드에 기록
- 부트스트랩 (DB `nodes < 50`): alias_check 누락 허용 (curator가 softening). 단, 3회차 이후는 반드시 작성

## Hybrid Query (참조)

요약 중 "이 논문의 이전 버전이 있는가?", "같은 dataset을 쓰는 논문" 등을 확인할 때:

```bash
python3 .claude/skills/paper-kg/scripts/hybrid_query.py "GCG variant papers" --k 5
```

리턴 JSON의 `kg.matched_nodes`와 `rag.chunks`를 교차 확인 후 alias/중복을 결정.

## Schema Enforcement

모든 `.kg.json`은 `paper-kg/scripts/schema.py`의 `KGFile` Pydantic 모델을 통과해야 한다. 검증·upsert는 kg-curator가 수행하며, 실패 시 `papers/kg/rejected.jsonl`에 기록되어 orchestrator가 재dispatch한다. 상세 규칙은 `.claude/skills/paper-kg/SKILL.md` 참조.

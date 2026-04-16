---
name: paper-summarize
description: "논문 전문(full-text PDF) adaptive Marp 요약. 2-stage 파이프라인(Gemini digest → Claude summary), pymupdf 파싱 강제(abstract-only 금지), 논문마다 PLANNING 블록 먼저 작성 (섹션 구조 + 섹션별 이미지 배치를 upfront로 결정)하고 필수 앵커 4개(TL;DR / Method / Result / Critical Reading)만 유지, 그 사이 섹션은 논문 흐름에 맞게 자유. 수식·수치 verbatim, 결과표는 Markdown 표. Marp frontmatter 유지. paper-summarizer 전용. 트리거: '논문 요약', 'Marp 슬라이드', 'paper summary'."
---

# Paper Summarize Skill

논문을 **비판적**이고 **간결**하게, 각 논문의 논리 흐름에 맞춘 adaptive 구조로 요약하는 절차와 템플릿.

## 입력

- `papers/metadata/<V>/<Y>/<slug>.raw.md` (paper-hunter 산출) — 이 파일은 **abstract-level 메타데이터**다. paper-hunt 스킬은 리스팅 단계에서 abstract·API 메타로만 판단하며, raw.md 본문의 `## Abstract` 섹션에는 abstract만 들어 있다.
- 본 요약 단계는 raw.md만으로는 부족하므로 **반드시 PDF 전문을 다운로드·pymupdf로 파싱**해야 한다. abstract-only 요약은 금지.

## 전문(full-text) 읽기 프로토콜 — 2-Stage (필수)

이 스킬은 **Claude가 PDF 전문을 직접 읽지 않는다**. Stage 1에서 Gemini CLI(gemini-3-pro-preview, 1M+ 컨텍스트)가 PDF를 읽고 dense digest를 생성하고, Stage 2에서 Claude paper-summarizer agent가 그 digest + raw.md 메타만을 근거로 adaptive Marp 요약 (PLANNING-first, 4 앵커) + KG를 작성한다. pymupdf 직접 파싱은 **fallback 경로에서만** 허용된다.

### Stage 1 — Gemini digest 생성 (bash)

```bash
python3 .claude/skills/paper-summarize/scripts/gemini_digest.py <raw_md_path>
# 성공 시 stdout 마지막 줄 = 절대경로 papers/digest/<V>/<Y>/<slug>.digest.md
# 실패 시 non-zero exit code (2: raw.md, 3: PDF, 4: pymupdf, 5: gemini CLI)
```

스크립트가 내부적으로 수행하는 일:

1. **raw.md frontmatter 파싱** → `pdf_url` / `arxiv_id` / `anthology_id` / `cvf_url` / `slug` / `venue_class` / `venue` / `year`.
2. **PDF 확보** (4-way fallback, 기존 우선순위 유지):
   1. raw.md frontmatter의 `pdf_url` (arXiv/OpenReview/CVF/Anthology)
   2. `arxiv_id`로 `https://arxiv.org/pdf/{id}.pdf`
   3. `anthology_id`로 `https://aclanthology.org/{id}.pdf`
   4. `cvf_url` 직접
   - 저장 경로: `papers/digest/<V>/<Y>/.pdf_cache/<slug>.pdf` (gitignore 대상). 이미 있으면 재사용, `--force`로 무효화.
3. **pymupdf 전문 파싱** + `len(full_text) > 3000` 체크.
4. **Gemini 호출**: `gemini -m gemini-3-pro-preview -p "<digest_prompt v1>" -o text` 에 full_text를 stdin으로 전달. 타임아웃 600s. 출력은 장문 Markdown digest (2–5k words, 수식·수치 verbatim).
5. **digest 파일 작성**: `papers/digest/<V>/<Y>/<slug>.digest.md` (gitignore 대상). frontmatter에 `source_raw`, `source_pdf_sha256`, `generated_at` (KST), `model: gemini-3-pro-preview`, `prompt_version: v6`, 그리고 **figure list**(`figures:` YAML 배열, 각 항목 `{label, path, section_hint, reason}`) + backward-compat 단축 필드(`key_figure_label`, `key_figure_reason`, `key_figure_path` = figures[0]) 기록. digest 캐시는 `source_pdf_sha256` **AND** `prompt_version`이 둘 다 일치해야 유효하다 — PROMPT_VERSION이 bump되면 PDF sha가 같아도 재생성된다. `--force`는 캐시를 전면 무효화.
6. **Figure candidates 선정 + 추출** (v6부터):
   - Gemini가 digest 말미에 `CANDIDATE: Figure N | Section: <hint> | Reason: <한 문장>` 라인을 **1-4개** (priority 순서, 가장 정보량 많은 figure가 첫 줄) 출력하도록 프롬프트가 강제한다. 테이블은 선택 대상이 아니다. 그림이 없는 논문은 `CANDIDATES: NONE — <reason>` 한 줄.
   - `section_hint` token: `Method|Motivation|Observation|Setup|Result|Analysis|Discussion` 중 하나 — 다운스트림 agent가 섹션별 이미지 배치를 PLANNING에서 결정할 때 힌트로 사용한다.
   - `gemini_digest.py`가 각 candidate에 대해 pymupdf 캡션 검색(`^(Figure|Fig\.?)\s*N[:\.\s]`)으로 위치를 찾고 캡션 위 → 아래 → 전체 페이지 순서로 crop, image block·`page.get_drawings()` union으로 bbox 축소(높이 10% 미만이면 원본 영역 유지).
   - `fitz.Matrix(3, 3)` (≈216 DPI)로 clip 렌더 → `papers/marp-summary/<V>/<Y>/.figure_cache/<slug>__fig<N>.png` (gitignore 대상). **파일명 스킴은 `<slug>__fig<N>.png`** — figure 번호를 그대로 보존해 다운스트림 PLANNING이 참조하기 쉽게 한다.
   - sanity: PNG <10KB면 실패로 간주하고 삭제 → 해당 figure만 list에서 누락.
   - **figure 추출 실패는 fatal이 아니다**. digest는 exit 0으로 쓰고, 성공한 figure만 `figures:` list에 담긴다. 전부 실패하면 `figures: []`. 다운스트림(agent)은 사용 가능한 figure만 PLANNING에 배치한다.

### Stage 2 — Claude summarizer (agent, **planning-first**)

논문마다 섹션 구조가 다르고 figure 위치·용도도 다르므로 **PLANNING 블록(섹션 구조 + 섹션별 이미지 배치)을 먼저 결정한 뒤 본문을 채운다**. 고정 6-part 템플릿에 억지로 맞추지 않는다. 섹션 순서·제목·이미지 배치는 PLANNING이 정해지면 그대로 유지 — 도중에 재배치 금지.

**Step 2a — digest 읽기**
1. `raw_md_path`와 `digest_path`를 Read 도구로 읽는다. **pymupdf 직접 호출 금지** (fallback 제외).
2. digest의 `## Author Framing` 블록, 각 섹션 제목, `# Figures and Tables index`, frontmatter의 `figures:` 리스트를 스캔해 (a) 논문 구조 (b) 사용 가능한 이미지 후보를 파악한다.

**Step 2b — PLANNING 블록 설계 (필수, 본문 작성 전)**

파일 최상단에 HTML 주석으로 PLANNING 블록을 먼저 적는다 (최종 .md에도 남긴다 — 유지보수·검증용). **섹션 구조와 섹션별 이미지 배치를 함께 결정**한다. 아래 형식을 엄격히 따른다:

```markdown
<!--
PLANNING:
  SECTIONS:
    1. Lead                                    [no image]
    2. TL;DR (anchor)                          [no image]
    3. Background — 왜 이 문제가 어려운가       [no image]
    4. 핵심 관찰 — attention sink shift         [Figure 2]
    5. Method (anchor) — PAD attack 구조        [Figure 3]
    6. Experiments Setup                       [no image — baseline table]
    7. Result (anchor)                         [no image — Markdown tables]
    8. Analysis — sink-shift score 상관관계    [Figure 5]
    9. Critical Reading (anchor)               [no image]
  IMAGE_SOURCES:
    - Figure 2: .figure_cache/<slug>__fig2.png — DLM step별 attention sink 시각화
    - Figure 3: .figure_cache/<slug>__fig3.png — PAD attack pipeline overview
    - Figure 5: .figure_cache/<slug>__fig5.png — sink-shift score vs ASR
-->
```

규칙:
- **SECTIONS**: 모든 섹션 번호·제목·이미지 결정을 한 블록에 담는다. 이미지가 들어가는 섹션은 `[Figure N]`, 안 들어가면 `[no image]` 또는 `[no image — <이유 한 마디>]`.
- **IMAGE_SOURCES**: SECTIONS에 나온 모든 figure의 실제 path와 한 줄 용도. digest frontmatter `figures:` 리스트에 존재하는 figure만 허용 (없으면 추출 실패 또는 Gemini가 추천하지 않은 것 — PLANNING에 넣지 말 것).
- 필수 앵커 4개(TL;DR / Method / Result / Critical Reading)는 반드시 SECTIONS에 포함. 제목 변형 허용, 순서 고정.
- 자유 섹션 0개 이상: Background / Motivation / Observation / Experiments Setup / Analysis / Discussion / Conclusion 또는 narrative 한국어 H2.
- 이미지는 **Method / Motivation / Observation / Analysis** 계열 섹션에 주로 배치. Result 섹션은 수치 표를 쓰므로 **기본적으로 no image**.
- TL;DR / Critical Reading / Experiments Setup / Lead / Conclusion은 **기본 no image** (baseline 표·글만으로 충분).
- 한 섹션에 2장 이상은 금지 (시각적 혼잡). 여러 figure가 적합하면 섹션을 쪼개거나 한 figure만 선택.
- digest `figures:`에 한 장도 없으면 모든 섹션 `[no image]`.

**필수 앵커 섹션 4개** (제목 변형 허용, 순서는 아래대로):
1. **TL;DR** — H1 lead 직후 첫 콘텐츠 슬라이드. `> ` blockquote로 한두 문장 요약.
2. **Method** — 핵심 idea + 수식 verbatim + pseudocode/figure.
3. **Result** (또는 "Experiments Result", "실험 결과") — 수치 표는 반드시 Markdown 표.
4. **Critical Reading** — 논문의 부족한 부분 3~5 bullet.

**PLANNING 예시 두 가지 outline**:
- *classical*: Lead → TL;DR → Motivation → Method(Figure) → Setup → Result → Critical Reading
- *narrative*: Lead → TL;DR → "왜 이 문제가 어려운가" → "핵심 아이디어"(Figure) → "어떻게 통하는가"(Figure) → Result → Critical Reading

**Step 2c — 본문 채우기 (PLANNING에 정확히 맞춰)**
1. SECTIONS의 순서·제목·이미지 배치를 **그대로 구현**한다. 섹션을 추가·삭제·재배치 금지.
2. 각 섹션에 digest 내용을 매핑한다. 수식·수치는 digest에 이미 verbatim이므로 그대로 복사 (paraphrase 금지).
3. **결과표는 Markdown 표로 작성한다 — 이미지 스크린샷 금지**. digest에 Markdown 표가 있으면 그대로, 있으나 지저분하면 정리하되 값은 절대 건드리지 말 것.
4. **Critical Reading**은 digest에 없으므로 Claude가 작성한다 (full-text 기반 추론 — 실험 scope 한계, baseline 편향, reproducibility 등 3~5 bullet).
5. **Keywords (RAG용)**는 선택 사항. 쓸 때는 최말미에 `` `kw1`, `kw2`, ... `` 형태로 raw.md abstract 기반 10~15개.

**Step 2d — 이미지 임베딩 (PLANNING IMAGE_SOURCES 그대로)**

PLANNING의 각 `[Figure N]` 태그가 달린 섹션에, IMAGE_SOURCES에 명시된 경로를 그대로 써서 이미지를 한 장 삽입한다:
- 포맷: 해당 섹션 내부에 `![w:650](./.figure_cache/<slug>__fig<N>.png)` + 한 줄 캡션(IMAGE_SOURCES의 설명 또는 digest `figures[i].reason`).
- 경로는 raw.md 디렉토리 기준 상대경로(`.figure_cache/<slug>__fig<N>.png`) — 최종 `<slug>.md`도 같은 디렉토리이므로 **경로 변환 없이 그대로**.
- 이미지 한 장당 전용 슬라이드 만들 필요 없음 — 섹션 안쪽 흐름에 섞어도 OK. 맥락이 중요.
- 결과 수치는 **절대 figure로 대체하지 않는다**. 성능 비교 bar chart가 figures에 있어도 그 figure는 PLANNING에서 `[no image]`로 두고 별도 Markdown 표로 수치를 옮긴다 (Gemini prompt가 이미 result-bar-chart는 배제하도록 강제하지만 최종 판단은 agent).
- digest `figures: []` (빈 리스트)이면 PLANNING의 모든 섹션을 `[no image]`로 두고 이미지 삽입 생략. 실패 모드 아님 — Critical Reading에 "figure 없음" 플래그 추가 금지.

**Step 2e — 저장 경로 라우팅**
`venue_class` 필드 기반. `<slug>.kg.json`도 같은 디렉토리에 emit.

### Fallback (Gemini digest 실패 시)

Stage 1 스크립트가 non-zero로 끝나거나 digest가 비어있으면 **abstract-only가 아니라** 기존 pymupdf 경로로 진행한다:

1. Claude가 직접 `import fitz` + `papers/digest/<V>/<Y>/.pdf_cache/<slug>.pdf`를 로드해 full_text 구성.
2. 섹션 분할 (`Introduction`, `Method/Approach`, `Experiments`, `Results`, `Ablation`, `Conclusion`, `Appendix`) → adaptive Marp 요약의 PLANNING 근거로 사용.
3. 긴 논문(>80쪽)은 메인 → ablation 부록 → 기타 부록 순서로 점진 요약.
4. 출력 파일 frontmatter에 `digest_source: fallback-pymupdf`와 실패 이유(exit code + stderr 요약)를 반드시 기록.

PDF 확보 자체가 불가능한 경우에만 요약 중단 + `papers/_rejected/`로 격리 (기존 규칙). **Abstract-only 축소 요약은 정상 출력이 아니며**, 정상 venue 디렉토리에 저장 금지.

## 출력 템플릿 (Marp, adaptive)

**Marp frontmatter는 고정**이고, 본문 섹션 구성은 논문마다 다르다. 아래는 *classical outline* 예시다 (narrative outline도 동일 앵커만 지키면 OK).

```markdown
---
marp: true
theme: default
paginate: true
title: "{paper title}"
---

<!--
PLANNING:
  SECTIONS:
    1. Lead                            [no image]
    2. TL;DR (anchor)                  [no image]
    3. Motivation                      [no image]
    4. Method (anchor)                 [Figure 2]
    5. Experiments Setup               [no image — baseline table]
    6. Result (anchor)                 [no image — Markdown tables]
    7. Analysis                        [Figure 5]
    8. Critical Reading (anchor)       [no image]
  IMAGE_SOURCES:
    - Figure 2: .figure_cache/{slug}__fig2.png — core method diagram
    - Figure 5: .figure_cache/{slug}__fig5.png — schedule invariance plot
-->

<!-- _class: lead -->

# {paper title}

**{authors}** — {venue} {year}

[arXiv]({url}) · [PDF]({pdf_url})

---

## TL;DR

> {한두 문장 — 논문이 뭘 보여줬고 왜 중요한지. 음슴체 유지. 예: "LLaDA-style discrete DLM에서 attention sink가 ARM과 달리 denoising step마다 shift한다는 걸 empirical하게 보여줌. 이는 DLM-specific prompt injection defense가 필요함을 시사함."}

---

## Motivation  <!-- 자유 섹션, 논문에 해당 flow 있을 때만 -->

- **Problem**: {풀려는 problem}
- **기존 approach**: {prior work 방식}
- **Limitation**: {기존 한계 → 이 연구를 motivate}

---

## Method  <!-- 필수 앵커. 제목 변형 OK ("Approach", "우리가 제안하는 것") -->

- 핵심 idea 한 문장
- 수식 (digest verbatim):

$$
\mathcal{L} = -\sum_i \log p(y_i | x_i)
$$

- algorithm pseudocode 또는 figure 참조

<!-- PLANNING에서 이 섹션에 [Figure 2] 지정 → IMAGE_SOURCES 경로 그대로 -->
![w:650](./.figure_cache/{slug}__fig2.png)

*{figures[i].reason 한 줄 캡션}*

---

## Experiments Setup  <!-- 자유 섹션 -->

| Method | Architecture | Key HP | Training | 비고 |
|---|---|---|---|---|
| **Proposed** | ... | lr=…, batch=…, steps=… | from scratch / finetune | ... |
| **Baseline A** | ... | ... | ... | 공정 비교 여부 / 논문 수치 인용 |

> 규칙: 각 비교 방법론 개별 행, HP 누락 시 "(논문 미기재)".

---

## Result  <!-- 필수 앵커. 수치 표는 반드시 Markdown 표 (이미지 금지) -->

| Benchmark | Baseline | Proposed | Δ |
|---|---|---|---|
| LM1B PPL ↓ | 20.86 | ≤23.00 | +2.14 |
| OWT PPL ↓ | 17.54 | ≤23.21 | +5.67 |

- ablation 핵심 finding (digest verbatim 수치 유지, 반올림 금지)
- statistical significance 보고 여부

---

## Analysis  <!-- 자유 섹션, 논문에 해당 flow 있을 때만 -->

- 저자의 관찰·해석
- 보조 실험 (hyperparameter sweep, ablation detail 등)

---

## Critical Reading  <!-- 필수 앵커 -->

**논문의 부족한 부분**:
- {약점 1: 예) experiment가 특정 dataset에만 한정됨}
- {약점 2: 예) baseline이 outdated version임}
- {약점 3: 예) main claim과 OWT 결과 간 32% gap을 "match or exceed"로 표현}

---

## Keywords (RAG용, optional)  <!-- 말미에 두고 생략 가능 -->

`keyword1`, `keyword2`, `keyword3`, ...
```

### Narrative outline 예시 (같은 앵커 4개만 지키면 한국어 H2 자유)

```markdown
## TL;DR
> ...

## 왜 이 문제가 어려운가
- ...

## 핵심 아이디어 — PAD가 하는 것
$$ ... $$

## Method  <!-- 앵커 제목은 그대로 유지해도 되고 "PAD 어떻게 동작하는가?"로 바꿔도 됨 -->
- ...

## 실험 결과가 말하는 것
| ... | ... | ... |

## Critical Reading
- ...
```

### 슬라이드 분리 규칙

- 모든 H2 앞에 `---` 슬라이드 구분자.
- 한 슬라이드 안에 bullet >7개면 "## Method (cont.)" 같은 이어보기 슬라이드로 split.
- 전체 ~12–18 슬라이드 목표 (논문 복잡도에 따라 가변).

## 문체 규칙 (Code-switching + 음슴체)

**한영 혼용 음슴체**: researcher가 랩 노트·커뮤니티에서 쓰는 자연스러운 한영 혼용 + 음슴체(~임, ~함, ~됨, ~없음) 말투를 사용한다.
- **종결어미는 음슴체**: "~한다/~했다" 대신 "~함/~했음/~임/~됨/~있음/~없음" 사용.
  - 예: "DLM의 attention sink가 ARM과 달리 denoising step마다 dynamically shift함" (O)
  - 예: "DLM의 attention sink가 ARM과 달리 denoising step마다 dynamically shift한다" (X)
- **기본 문장은 한국어**, technical term·proper noun·method name·metric name은 영어 그대로 유지.
  - 예: "기존 ARM은 BOS token에 attention이 고정되는데, DLM은 step마다 sink position이 바뀜" (O)
  - 예: "확산 언어 모델의 주의 집중 싱크가 자기회귀 모델과 달리..." (X — 어색한 번역 금지)
- **번역하지 않는 것**: model name, method name, dataset name, metric name, loss function, architecture 용어 (transformer, attention, embedding 등), 약어 (LLM, DLM, ARM, BLEU, PPL 등).
- **한국어로 쓰는 것**: 접속사, 조사, 일반 동사/형용사, 문장 구조 ("~를 제안함", "~에 비해 ~% 향상됨", "~라는 한계가 있음").
- Section header는 영어 그대로 유지 (Marp 템플릿 고정).

## 비판적 추출 원칙

1. **Planning-first**: 본문을 쓰기 전에 PLANNING 주석 블록을 먼저 작성한다. 섹션 구조 + 섹션별 이미지 배치(SECTIONS + IMAGE_SOURCES)를 **한 번에** 결정하고, 정해지면 그대로 채운다 — 도중에 섹션 순서·이미지 배치를 재배치하지 않는다. 이미지 배치는 digest `figures:` 리스트에 실제로 존재하는 figure만 허용.
2. **TL;DR은 blockquote 한두 문장**: H1 lead 직후 첫 콘텐츠 슬라이드로 고정. 논문이 뭘 보여줬고 왜 중요한지. paraphrase OK (요약이므로).
3. **수식·수치 원문 인용**: digest verbatim 그대로. paraphrase 금지, 반올림·단위 변환 금지. 결과표는 Markdown 표로 재현 (이미지 스크린샷 금지).
4. **슬라이드 수 ~12–18 목표**: 각 section 1–3 슬라이드. 과도한 상세 금지. 논문 복잡도에 따라 가변.
5. **Critical Reading은 논문의 부족한 부분**: experiment scope 한계, baseline 선택 편향, reproducibility issue, 저자 주장과 실제 증거 gap 등. 3–5 bullet.
6. **이미지는 맥락 있는 자리에**: Method / Motivation / Observation / Analysis 계열 섹션 안쪽에 배치. title 슬라이드 직후·Result 섹션·Critical Reading에 고정 삽입하지 않는다. 한 섹션당 최대 1장.
7. **Keywords는 선택**: 쓸 때만 최말미. abstract 본문에서 핵심 용어 10~15개. 저자 메타데이터나 Gemini 생성 키워드 금지.

## 파일명·경로

- 입력: `papers/metadata/<V>/<Y>/<slug>.raw.md`
- 출력: `papers/marp-summary/<V>/<Y>/<slug>.md` (raw 파일은 보존, 새 파일 생성)
- 파일 길이: 200~500줄 목표, 초과 시 요약 축소

## 실패 모드

- **PDF 없음 / 404**: 다운로드 경로 4종(arxiv/openreview/anthology/cvf)을 전부 시도한 뒤에도 실패하면 요약을 **중단하고** orchestrator에 reject 리턴. abstract-only 요약은 해당 venue 디렉토리에 저장하지 말고 `papers/_rejected/<slug>.raw.md`로 격리 후 이유를 기록.
- **파싱 깨진 수식**: 해당 수식을 raw text로 code block에 보존 + Unknown에 플래그
- **너무 긴 논문 (80페이지+)**: 메인 → ablation 부록 → 기타 부록 순서로 섹션 단위 요약 후 통합. 부록 생략 시 "Appendix X.Y는 요약 생략" 명시.
- **저자 주장이 명확하지 않음**: Claims 섹션에 "저자 주장 추출 불확실" 플래그

## 체크리스트

- [ ] `gemini_digest.py` 실행 성공 → `papers/digest/<V>/<Y>/<slug>.digest.md` 존재, 또는 실패 시 fallback 플래그(`digest_source: fallback-pymupdf`) 기록
- [ ] PDF 다운로드 성공 + (digest 경로) Gemini digest 생성 / (fallback 경로) pymupdf 파싱 성공 (`len(full_text) > 3000`)
- [ ] Introduction/Method/Experiments/Results/Appendix 중 최소 4개 섹션 본문 내용이 digest 또는 pymupdf 경로로 확보됨
- [ ] Marp frontmatter `marp: true` (PPT 호환 유지)
- [ ] 최상단에 `PLANNING` HTML 주석 블록 존재 (planning-first 검증용). SECTIONS + IMAGE_SOURCES 두 서브블록 모두 존재
- [ ] **4개 필수 앵커 모두 존재**: TL;DR / Method / Result / Critical Reading (제목 변형 허용)
- [ ] TL;DR이 H1 lead 직후 첫 콘텐츠 슬라이드에 `> ` blockquote로 존재
- [ ] 수식·수치 원문 인용 (digest verbatim)
- [ ] 결과표는 **Markdown 표**로 작성 (이미지 스크린샷 금지)
- [ ] 슬라이드 ~12–18개, 600줄 이내
- [ ] PLANNING의 `[Figure N]` 태그가 달린 각 섹션에 해당 이미지가 정확히 1장 삽입됨 (PLANNING과 본문 동기화 검증). 경로는 IMAGE_SOURCES의 값 그대로. digest `figures: []`면 모든 섹션 `[no image]`
- [ ] 한 섹션당 이미지 ≤1장. Result / TL;DR / Critical Reading / Lead 섹션은 `[no image]`
- [ ] Critical Reading 포함 — 논문의 부족한 부분 3–5 bullet (full-text 기반일 때만 허용)
- [ ] Keywords (RAG용)는 **선택** — 쓸 때만 말미, abstract 본문 기반 10~15개
- [ ] 같은 디렉토리에 `<slug>.kg.json` 동시 작성 (아래 KG Emission 참조)
- [ ] 저장 경로: 원본 raw.md의 `venue_class` 필드를 그대로 따라 라우팅 (paper-hunt가 이미 결정해 놓은 값)
  - `whitelist` → `papers/marp-summary/<NeurIPS|AAAI|ICLR|ICML|ACL|EMNLP>/<Year>/`
  - `etc`       → `papers/marp-summary/etc/<Year>/` (평탄 구조, 하위 venue 디렉토리 없음)
  - 두 경로 모두 **정상 출력**이며 `etc`가 품질 열등을 의미하지 않는다 — 요약 기준은 동일하다.
- [ ] 금지 경로 확인: `papers/arXiv/`, `papers/OpenReview/`, `papers/preprint/`, `papers/workshop/`, `papers/findings/` 등 소스/속성 디렉토리에 저장하지 않았는지 (해당 논문은 전부 `papers/marp-summary/etc/<Year>/`로)

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

모든 `.kg.json`은 `paper-kg/scripts/schema.py`의 `KGFile` Pydantic 모델을 통과해야 한다. 검증·upsert는 kg-curator가 수행하며, 실패 시 `papers/vector_db/rejected.jsonl`에 기록되어 orchestrator가 재dispatch한다. 상세 규칙은 `.claude/skills/paper-kg/SKILL.md` 참조.

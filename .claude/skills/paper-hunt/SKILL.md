---
name: paper-hunt
description: "논문 수집. 기본은 6 whitelist venue(NeurIPS·AAAI·ICLR·ICML·ACL·EMNLP) 전용. OpenReview/ACL Anthology 스캔 + dedup + manifest cursor. workshop/Findings/arXiv preprint는 `--include-arxiv` 플래그 opt-in 시 `papers/etc/<Year>/`로 수집. 트리거: '논문 수집', 'arxiv 검색', 'OpenReview', 'venue 스캔', 'paper hunt'."
---

# Paper Hunt Skill

논문 리스팅 단일 통합 플로우. seed/follow-up 구분 없음.

## 입력 / 출력

- **입력**: 키워드, source 선택(openreview/anthology/arxiv), 연도 버킷(`--years`), venue 지정 방식 (`--venues` 명시 / `--venues-whitelist-all` 6개 전체), arXiv opt-in(`--include-arxiv`), 상한 (`--max-per-query` / `--max-per-venue-year`), `--date-from`(backward compat)
- **출력**: `papers/<Venue>/<Year>/<slug>.raw.md` (whitelist). `--include-arxiv` 있을 때만 `papers/etc/<Year>/<slug>.raw.md` (etc)도 생성. `papers/rag/manifest.json` cursor 갱신, year-bucket별 카운트 로그 + grand total (whitelist/etc/per-venue-year breakdown)

### 주요 CLI 플래그

| 플래그 | 기본값 | 의미 |
|---|---|---|
| `--years Y1 Y2 ...` | `[today.year, -1, -2]` (KST) | scan-priority 순서로 year 버킷 순회. 입력 순서 존중. **newest-first 권장**. |
| `--venues-whitelist-all` | False | 6 whitelist venue 전체를 target에 추가 (`--venues`와 합집합). OpenReview 지원 venue(ICLR/NeurIPS/ICML)는 자동으로 `<Venue>.cc/<year>/Conference` venueid로 확장. 나머지(AAAI/ACL/EMNLP)는 anthology/arXiv comment source로 커버된다. |
| `--include-arxiv` | False | **opt-in**. True일 때만 arXiv 키워드 소스를 돌리고 openreview/anthology의 `venue_class == "etc"` 결과를 keep. False면 arXiv 소스는 자동 스킵되고 etc 분류는 drop. |
| `--sources` | `openreview anthology arxiv` | year bucket 안에서 **이 순서 고정**으로 호출된다. `--include-arxiv`가 없으면 `arxiv`는 런타임에 자동 제거. |
| `--max-per-venue-year N` | 200 | (canonical venue, year) 조합당 상한. 글로벌 dedup과 독립적으로 동작. |
| `--max-per-query N` | 100 | arXiv 키워드 쿼리 1회당 상한. (year × keyword별 독립 호출) |
| `--date-from YYYY-MM-DD` | None | **`--years` 있으면 무시**. backward compat. |

## 키워드 전략

hunter는 **recall 담당**, narrow 관련도 판단은 하류 triage(`--topic`)에 위임 (hunter=recall / triage=precision 경계).

- 사용자가 준 topic에서 **분야(field)를 추출해 canonical 용어로 변환**한 것을 키워드로 쓴다. 주제 문장·narrow 방법명을 그대로 쓰지 않는다.
- 축 2-3개로 분해하고, 잘 확립된 분야는 canonical 용어 1개 + synonym 정도로 충분.
- **생소·신생 분야**(표기 아직 표준화 안 됨)는 축약형·풀이·어순 변형을 여러 개 병기해 recall 확보.
- 분야 추출과 canonical 변환은 Claude가 topic을 보고 직접 판단한다.
- **키워드 매칭 범위: title ∪ abstract** (모든 source). arXiv는 `(ti:"kw" OR abs:"kw")` 쿼리, anthology는 listing 단계에서 title pre-filter 없이 detail fetch 후 `title + abstract` 문자열에서 매치, openreview는 venueid 전체 dump이므로 이 규칙과 무관. 이전 arxiv `abs:` 단독·anthology title pre-filter 방식은 abstract-only 또는 title-only hit을 누락했다.

---

## 핵심 규칙 (inline — references로 옮기지 않는다)

- **6 whitelist venue**: `NeurIPS`, `AAAI`, `ICLR`, `ICML`, `ACL`, `EMNLP` (대문자 casing 고정). whitelist 밖 venue는 `classify_route()`가 `etc` 라벨로 분류한다 (venue label은 원문 보존).
- **venue_class ∈ {whitelist, etc}**: 모든 논문은 `classify_route()`를 거쳐 이 둘 중 하나로 라벨링된다.
- **`etc` 라우팅은 `--include-arxiv` opt-in**: 기본 실행(플래그 없음)에서는 `etc` 분류 결과를 hunt.py가 drop하고 arXiv 소스를 아예 돌리지 않는다. `--include-arxiv`가 있을 때만 `whitelist` → `papers/<Venue>/<Year>/`, `etc` → `papers/etc/<Year>/`로 두 경로 모두 기록된다.
- **3개년 버킷, newest-first 순회**: 기본 scan 순서는 `[today.year, -1, -2]`. 루프는 `year → source → venue` (outer → inner). per-year source 순서는 `openreview → anthology → arxiv`로 **고정**. 사용자가 `--years`로 연도 순서를 주면 그 순서 그대로 존중 (내부 재정렬 금지).
- **전역 dedup은 year 경계를 넘어 유지**: `SeenKeys`는 manifest에서 1회만 초기화되고 모든 year 버킷을 관통한다. 2026 버킷에서 본 arxiv_id/openreview_id/정규화 제목은 2025/2024 버킷에서 재처리되지 않는다. 연도 진입 시 테이블 리셋 금지.
- **금지 디렉토리 (신규 생성 금지)**: `papers/arXiv/`, `papers/OpenReview/`, `papers/preprint/`, `papers/workshop/`, `papers/findings/` — 이런 논문은 전부 `papers/etc/<Year>/`로 모은다.
- **Full-text 정책 분리 (listing vs summarization)**:
  - 이 스킬(paper-hunt, 리스팅)은 **abstract + API 메타만** 사용해 판단·분류·dedup·`raw.md` 생성.
  - 전문 PDF 파싱 + 5-part 요약은 **paper-summarize** 스킬의 책임 (`len(full_text) > 3000` 등 full-text 프로토콜 강제).
  - **Optional full-text fetch**: (1) venue_class 분류 불가, (2) near-duplicate 의심, (3) relevance 애매 중 하나일 때만 `pymupdf`로 PDF 첫 2–3페이지만 읽어 판단 보조. `raw.md` 본문에는 여전히 abstract만 저장.
- **frontmatter**: `venue`는 원문, `venue_class: "whitelist" | "etc"`, 그 외 id/url/published/categories/keywords/hunter_fetched.
- **Findings of ACL/EMNLP (및 NAACL main·Findings 전체)**: 메인 proceedings 6-venue whitelist에 포함되지 않으므로 `venue_class: "etc"`. `--include-arxiv` 있을 때만 `papers/etc/<Year>/`에 `venue: "ACL Findings"` 같은 원문 라벨로 기록된다. 없으면 drop.

## 정식 진입점 (scripts/)

| 스크립트 | 역할 |
|---|---|
| `scripts/classify_route.py` | `classify_route(result)` 순수 함수 + `WHITELIST`·`VENUE_PAT`·`CANONICAL`. 3개 소스가 전부 이 함수를 거쳐 `venue_class` 결정. |
| `scripts/hunt.py` | CLI. OpenReview + Anthology + arXiv 통합, dedup, `raw.md` emit, manifest cursor. abstract만 사용. |

**호출 예**:

(1) 자동 3년 버킷 (권장 기본값, 6-venue whitelist 전용):
```bash
python3 /home/irteam/sw/research_hub/.claude/skills/paper-hunt/scripts/hunt.py \
    --venues-whitelist-all \
    --keywords "diffusion language model" "LLaDA" \
    --max-per-venue-year 200
```
→ `--years` 생략 시 KST 기준 `[today.year, today.year-1, today.year-2]`. whitelist 6개 venue(OpenReview ICLR/NeurIPS/ICML + Anthology ACL/EMNLP + arXiv comment AAAI)만 newest-first로 훑는다. arXiv 키워드 소스는 자동 스킵.

(2) arXiv opt-in (사용자가 `--include-arxiv` 요청 시):
```bash
python3 /home/irteam/sw/research_hub/.claude/skills/paper-hunt/scripts/hunt.py \
    --years 2026 2025 2024 \
    --venues-whitelist-all \
    --keywords "masked diffusion" "discrete diffusion" \
    --include-arxiv \
    --max-per-query 100 \
    --max-per-venue-year 200
```
→ 동일하게 `year → source → venue` 순서. per-year source 순서는 `openreview → anthology → arxiv` 고정. arXiv는 각 year의 `submittedDate:[YYYY01010000 TO YYYY12312359]` 윈도우로 쿼리. openreview/anthology의 `etc` 분류도 keep되어 `papers/etc/<Year>/`에 저장.

CLI 플래그·내부 플로우 상세는 `scripts/RUNBOOK.md` 참조.

## 상세 참고

- **Source API 호출 템플릿 (openreview/anthology/arxiv) · canonical casing 표 · dedup 휴리스틱 상세 · raw.md full template**: `references/sources.md`
- **CLI 플래그 · 내부 플로우 · 실패 복구 · 환경 설정**: `scripts/RUNBOOK.md`

## 실패 처리

- API 429: 30s 대기 후 1회 재시도, 두 번째 429는 venue skip
- 인증 실패 (OpenReview): env 안내 후 venue skip (public-only fallback 시도)
- 네트워크: 지수 백오프 3회
- Optional fetch 실패: 리스팅 중단하지 않음, abstract fallback, 필요 시 `venue_class: "etc"` 라우팅

## 체크리스트 (축약)

- [ ] cursor 로드, API credential 확인
- [ ] Primary source(whitelist 6) 기본. `--include-arxiv` 있을 때만 추가 source(arxiv keyword / reference chasing / non-whitelist venue) 동일 실행에서 스캔.
- [ ] **year bucket newest-first 순회** (`[today.year, -1, -2]` 기본 / 사용자 `--years` 순서 존중)
- [ ] per-year source 순서는 `openreview → anthology → arxiv` 고정
- [ ] 리스팅은 abstract·메타 기반. 전문 파싱은 paper-summarize.
- [ ] Optional full-text fetch는 분류불가/near-dup/애매 시만 (PDF 2–3p)
- [ ] 각 결과 `classify_route()` → `whitelist`/`etc` 라벨
- [ ] dedup (정규화 제목 + arxiv_id + anthology_id + openreview_id)
- [ ] **전역 dedup 테이블이 year 경계를 넘어 유지됨** (버킷 진입 시 reset 금지)
- [ ] `--max-per-venue-year` cap 준수 — per (canonical venue, year) 카운트
- [ ] 저장 경로:
  - whitelist → `papers/{NeurIPS|AAAI|ICLR|ICML|ACL|EMNLP}/<Year>/`
  - etc → `papers/etc/<Year>/` (평탄) — whitelist 외 venue 포함
- [ ] 금지 디렉토리 미생성 확인: `papers/arXiv/`, `papers/OpenReview/`, `papers/preprint/`, `papers/workshop/`, `papers/findings/`
- [ ] manifest 갱신, 카운트 리포트(whitelist/etc/실패)

# paper-hunt scripts — RUNBOOK

## 기본 호출 (자동 3년 버킷, newest-first, 6-venue whitelist 전용)

```bash
python3 /home/irteam/sw/research_hub/.claude/skills/paper-hunt/scripts/hunt.py \
    --venues-whitelist-all \
    --keywords "diffusion language model" "LLaDA" \
    --max-per-venue-year 200
```

`--years`를 생략하면 KST 기준 `[today.year, today.year-1, today.year-2]`가 기본이며,
6-venue whitelist 전체(OpenReview ICLR/NeurIPS/ICML + Anthology ACL/EMNLP + arXiv
comment AAAI)가 newest-first로 스윕된다. **`--include-arxiv`가 없으므로 arXiv 키워드
소스는 자동 스킵되고 `venue_class == "etc"` 결과(NAACL·IJCAI·Findings·워크숍·preprint)는
drop된다.**

## arXiv opt-in 호출 (`--include-arxiv`)

```bash
python3 /home/irteam/sw/research_hub/.claude/skills/paper-hunt/scripts/hunt.py \
    --years 2026 2025 2024 \
    --venues-whitelist-all \
    --keywords "masked diffusion" "discrete diffusion" \
    --include-arxiv \
    --max-per-query 100 \
    --max-per-venue-year 200
```

`--include-arxiv`가 붙으면 (a) arXiv 키워드 쿼리 소스가 per-year window로 돌아가고
(b) OpenReview/Anthology가 뱉은 `venue_class == "etc"` 결과도 keep되어 `papers/etc/<Year>/`로
저장된다. 입력 순서가 곧 scan 우선순위다. `--years 2024 2025 2026`으로 주면 oldest-first로
돌아간다 (내부 정렬 없음).

## CLI 플래그

| 플래그 | 기본 | 설명 |
|---|---|---|
| `--venues` | `[]` | 명시적 OpenReview venueid 리스트. 예: `ICLR.cc/2026/Conference`. `--venues-whitelist-all`과 합집합. |
| `--venues-whitelist-all` | False | 6 whitelist venue 전부를 target에 추가. OpenReview 지원 venue(ICLR/NeurIPS/ICML)는 각 year에 대해 `<Venue>.cc/<year>/Conference`로 자동 확장. 나머지(AAAI/ACL/EMNLP)는 OpenReview에서 silent skip되고 anthology/arxiv comment source로 커버된다. |
| `--include-arxiv` | False | **opt-in**. True일 때만 (a) arXiv 키워드 쿼리 소스를 실제로 호출하고 (b) OpenReview/Anthology에서 `venue_class == "etc"`로 분류된 결과를 keep한다. False면 arXiv 소스는 `--sources`에 있어도 런타임에 자동 제거되고 etc 분류는 drop. |
| `--keywords` | `[]` | 키워드 쿼리 (공백 분리 리스트). arXiv·Anthology 검색에 사용. |
| `--years Y1 Y2 …` | `[today.year, -1, -2]` (KST) | scan-priority 순서로 year 버킷 순회. **입력 순서 존중 (내부 정렬 금지)**. newest-first 권장. |
| `--date-from YYYY-MM-DD` | None | arXiv 날짜 lower bound. **`--years`가 있으면 무시**. backward compat용. |
| `--sources` | `openreview anthology arxiv` | 3개 소스 중 부분집합 선택. per-year 호출 순서는 항상 `openreview → anthology → arxiv`로 **고정**. `--include-arxiv`가 없으면 `arxiv`가 리스트에 있어도 런타임에 자동 제거된다. |
| `--max-per-query` | 100 | arXiv 키워드 1개 × 1개 year 당 상한. |
| `--max-per-venue-year` | 200 | (canonical venue, year) 조합당 상한. 모든 source 합산. cap 도달 시 해당 venue-year 추가 emit 중단. |
| `--manifest` | `papers/rag/manifest.json` | manifest 경로 override (미구현 자리). |
| `--dry-run` | False | manifest 갱신 skip. 로그만 찍음. |

## 내부 플로우 (year → source → venue)

1. `--years` 해석: 없으면 default `[today.year, -1, -2]` (KST).
2. `build_openreview_venueids(years, explicit_venues)` — whitelist-all이면 ICLR/NeurIPS/ICML × years로 venueid 확장. 나머지 whitelist venue(AAAI/ACL/EMNLP)와 non-whitelist venue는 OpenReview에선 실체 없음 (silent skip).
3. `--include-arxiv` 해석: False면 모듈 레벨 `_ALLOW_ETC = False`로 고정되고, `args.sources`에서 `arxiv`가 자동 제거된다(stderr 1줄 알림). True면 `_ALLOW_ETC = True`로 arXiv 소스와 etc emit 모두 활성화.
4. manifest 로드 → `SeenKeys` 1회만 초기화 → 모든 year 버킷 공유.
5. 각 year에 대해 **이 순서 고정**:
   a. **openreview**: 해당 year에 속한 venueid만 필터해서 `hunt_openreview_year()`. 404/nonexistent venueid는 stderr 1줄 + silent skip. whitelist 라벨이 먼저 박힌다. `classify_route()` 결과가 `etc`이고 `_ALLOW_ETC == False`이면 drop.
   b. **anthology**: `hunt_anthology_year()`. `aclanthology.org/events/<event>-<year>/` 리스팅 → title ∪ abstract keyword match → main proceedings(ACL/EMNLP)는 whitelist, NAACL·Findings·workshops는 etc. `_ALLOW_ETC == False`이면 etc는 drop.
   c. **arxiv** (keyword 있을 때 + `--include-arxiv` 있을 때만): `hunt_arxiv_year()`. `(ti:"<kw>" OR abs:"<kw>") AND submittedDate:[YYYY01010000 TO YYYY12312359]`. 각 결과에 `classify_route()` → 이미 seen이면 dedup drop → `--max-per-venue-year` cap 체크 → emit.
   d. 버킷 종료 시 `[year YYYY] whitelist=N, etc=M, bucket_total=T` 로그 출력.
6. `all_emitted` 파일을 manifest에 등록 (sha256 + mtime + normalized_title).
7. grand summary JSON 출력: `{ emitted, whitelist, etc, years, per_venue_year, manifest }`.

**중요**:
- `SeenKeys`는 year 경계를 넘어 전역으로 유지된다 — 2026 버킷에서 본 arxiv_id/openreview_id/정규화 제목은 2025/2024 버킷에서 재처리되지 않는다.
- `per_venue_year_counts`도 전역이다 (예: arXiv comment로 ICLR 2026 라벨을 받은 논문이 2026 버킷과 2025 버킷 양쪽에서 발견돼도 cap은 하나의 `("ICLR", 2026)` 버킷에 대해 적용된다).
- emit 경로는 **항상 `classify_route()`의 최종 venue·year에 따른다**. scan 당시의 bucket year가 아니다.

## 실패 처리

- API 429: `time.sleep(30)` 후 1회 재시도, 두 번째 429는 해당 venue skip
- 인증 실패 (OpenReview): `OPENREVIEW_USERNAME/PASSWORD` 환경변수 안내 후 venue skip
- 존재하지 않는 venueid (404 / NotFoundError): stderr 1줄 info 후 다음 venueid로
- 네트워크 끊김: 지수 백오프 3회

## 환경 설정

```bash
# 필요 패키지 (conda LLDM env)
pip install arxiv openreview-py pymupdf

# OpenReview credentials (선택)
export OPENREVIEW_USERNAME='...'
export OPENREVIEW_PASSWORD='...'  # /home/irteam/sw/.env에 보관
```

## Optional full-text fetch

- `pymupdf`로 PDF 첫 2–3페이지만 읽는 것까지만 허용.
- 트리거 조건(venue_class 분류 불가 / near-duplicate 의심 / relevance 애매) 중 하나 만족 시만.
- `raw.md` 본문에는 abstract만 유지. fetch 결과는 분류·dedup·routing 판단용.
- Cache: `papers/<V>/<Y>/.pdf_cache/<slug>.pdf`

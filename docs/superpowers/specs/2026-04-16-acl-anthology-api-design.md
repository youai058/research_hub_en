# ACL Anthology API Integration Design

**Date**: 2026-04-16
**Status**: Approved
**Approach**: #2 — Lazy singleton + venue expansion

## Problem

`hunt.py`의 ACL Anthology 소스(`hunt_anthology_year()`)가 HTML 스크래핑으로 동작한다.
논문 1편당 HTTP 요청 2회(listing page + detail page) + `time.sleep(0.3)`이 필요하며,
HTML 구조 변경 시 깨진다. `_anth_fetch_listing()`, `_anth_fetch_detail()` 등
~170줄의 brittle 파싱 코드를 유지해야 한다.

## Solution

`acl-anthology` Python 패키지(`pip install acl-anthology-py`)로 교체한다.
패키지는 `acl-org/acl-anthology` GitHub repo를 shallow clone해 로컬 XML 데이터를
파싱하며, HTTP 요청 없이 title/authors/abstract/PDF URL을 즉시 접근 가능하다.

## Design

### 1. Initialization & Dependency Injection

- `main()`에서 `"anthology" in args.sources`일 때 `Anthology.from_repo()` 1회 호출
- 첫 실행 시 shallow clone (~210MB), 이후 `git pull`만
- 초기화 실패 시 `args.sources`에서 `"anthology"` 제거 → 나머지 source 정상 동작
- `hunt_anthology_year()` 시그니처에 `anthology` 파라미터 추가

```python
anthology_obj = None
if "anthology" in args.sources:
    try:
        from acl_anthology import Anthology
        anthology_obj = Anthology.from_repo()
    except Exception as e:
        print(f"[anthology] skip — init failed: {e}", file=sys.stderr)
        args.sources = [s for s in args.sources if s != "anthology"]
```

### 2. Core Logic Replacement

`hunt_anthology_year()` 내부를 패키지 API 호출로 교체:

```python
def hunt_anthology_year(
    root, year, keywords, max_per_venue_year,
    seen, manifest, per_venue_year_counts,
    anthology,  # Anthology object
):
    for canon, event in ANTHOLOGY_WHITELIST_EVENTS.items():
        coll = anthology.collections.get(f"{year}.{event}")
        if coll is None:
            continue
        for vol in coll.volumes():
            for paper in vol.papers():
                if paper.is_frontmatter:
                    continue
                # dedup → classify_route → keyword filter → write_raw
```

Key differences vs current:
- **HTTP 0회**: 로컬 데이터 직접 접근
- **abstract 즉시 접근**: detail 페이지 fetch 불필요
- **`time.sleep(0.3)` 제거**: 네트워크 요청 없음
- **volume 단위 순회**: `vol.papers()`가 long/short/main 구분
- **presentation_type 정렬 없음**: OpenReview는 oral/spotlight/poster 정렬이 있지만 ACL Anthology에는 해당 메타데이터가 없으므로 volume 순서(long→short→demos) 그대로 사용

### 3. Venue Expansion

```python
ANTHOLOGY_WHITELIST_EVENTS = {
    "ACL": "acl",
    "EMNLP": "emnlp",
    "NAACL": "naacl",  # 추가 — classify_route가 etc로 라우팅
}
```

NAACL은 `classify_route()`가 `etc`로 분류. `--include-arxiv` 없으면 자동 drop.

### 4. Deletions (~170 lines)

| Item | Lines | Reason |
|---|---|---|
| `_ANTH_ID_RE` | ~5 | HTML 파싱용 regex |
| `_anth_fetch_listing()` | ~50 | HTML listing parser |
| `_anth_fetch_detail()` | ~30 | HTML detail parser |
| `_anth_venue_label()` | ~20 | anthology_id → label mapper |
| `_try_bs()` | ~5 | BeautifulSoup helper (anthology only) |
| `_http_get()` | ~55 | HTTP helper (anthology only) |

### 5. Document Updates

- `sources.md` — ACL Anthology 섹션을 패키지 기반으로 교체
- `SKILL.md` — HTML scraping 언급 제거

## Unchanged Components

- `classify_route.py` — 변경 없음
- `_Shim` class — 그대로 사용
- `write_raw()` — 그대로 사용
- `SeenKeys` — 그대로 사용
- `_kw_match()` — 그대로 사용
- `hunt_openreview_year()` — 변경 없음
- `hunt_arxiv_year()` — 변경 없음
- `main()` loop structure — anthology 초기화 + 인자 전달만 추가

## Testing

- `hunt.py --sources anthology --keywords "diffusion" --years 2025 --dry-run`
  → ACL/EMNLP 2025 논문 중 "diffusion" 키워드 매칭 확인
- dedup: 기존 manifest에 있는 논문이 중복 emit 안 되는지 확인
- classify_route: ACL main → whitelist, NAACL/Findings → etc 라우팅 확인
- `--include-arxiv` 없을 때 etc 결과 drop 확인

## Dependencies

- `pip install acl-anthology-py` (LLDM conda env)
- `git` CLI (시스템에 이미 설치됨)
- Disk: ~210MB for shallow clone at `~/.local/share/acl-anthology/git/`

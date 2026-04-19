# Paper Hunt — Source Details & Canonical Casing

## Primary venue sources (whitelist 6개)

| Category | Venue | 소스 (우선순위) | Identifier / 검증 방식 |
|---|---|---|---|
| AI | NeurIPS | OpenReview → arXiv | `NeurIPS.cc/YYYY/Conference` / arXiv comment "NeurIPS YYYY" |
| AI | AAAI | arXiv → AAAI proceedings | arXiv cs.AI + comment "AAAI YYYY"; `aaai.org/ojs` DOI |
| AI | ICLR | OpenReview → arXiv | `ICLR.cc/YYYY/Conference` / arXiv comment "ICLR YYYY" |
| AI | ICML | OpenReview(2024+) → PMLR → arXiv | `ICML.cc/YYYY/Conference` / PMLR vXYZ / arXiv comment "ICML YYYY" |
| NLP | ACL | ACL Anthology → arXiv | `aclanthology.org/YYYY.acl-*` / arXiv comment "ACL YYYY" |
| NLP | EMNLP | ACL Anthology → arXiv | `aclanthology.org/YYYY.emnlp-*` / arXiv comment "EMNLP YYYY" |

**Canonical casing** (엄격히 고정, whitelist 6개): `NeurIPS`, `AAAI`, `ICLR`, `ICML`, `ACL`, `EMNLP`. `CANONICAL` 딕셔너리는 non-whitelist이되 자주 등장하는 venue(`IJCAI`, `NAACL`)의 라벨도 보존용으로 가지고 있다 — 이들은 `venue_class: "etc"`로 라우팅되며 `--include-arxiv` opt-in에서만 저장된다.

`Findings of ACL/EMNLP/NAACL` 및 NAACL·IJCAI 메인 proceedings, 워크숍, arXiv preprint, 저널 논문은 전부 `venue_class: "etc"`다. **기본 실행(flag 없음)에서는 drop**된다. `/research-papers <topic> --include-arxiv`처럼 opt-in 플래그가 들어온 경우에만 `classify_route()`의 fallback 경로를 타고 `papers/metadata/etc/<Year>/`에 `venue`는 원문 라벨(예: "ACL Findings", "NAACL 2024") 그대로 기록된다.

## arXiv 쿼리 템플릿 (opt-in: `--include-arxiv`)

```python
import sys
sys.path.insert(0, "/home/irteam/sw/research_hub/.claude/skills/paper-hunt/scripts")
from classify_route import classify_route, WHITELIST, VENUE_PAT, CANONICAL
```

- Unified flow: 3 sources(OpenReview / ACL Anthology / arXiv)만 사용. per-year 호출 순서는 `openreview → anthology → arxiv`로 **고정** — OR/Anthology가 whitelist 라벨을 먼저 박은 뒤 arXiv 재발견분은 dedup drop된다.
- **Runtime gate**: `--include-arxiv`가 없으면 `main()`이 `args.sources`에서 `arxiv`를 제거해 이 소스 자체가 실행되지 않는다 (`SKILL.md` L21-22와 동기). 즉 이 섹션의 쿼리 템플릿은 opt-in 경로에서만 돈다.
- Rate limit: 3초/요청 (arxiv 라이브러리 자동 처리)
- Pagination: `max_results` + cursor로 `last_entry_id` 저장
- 내부 구현: `arxiv.Search(...)` + `arxiv.Client(page_size=20, delay_seconds=3)`

## OpenReview 쿼리 템플릿 (accepted only)

```python
import openreview
client = openreview.api.OpenReviewClient(
    baseurl='https://api2.openreview.net',
    username=os.environ.get('OPENREVIEW_USERNAME'),
    password=os.environ.get('OPENREVIEW_PASSWORD'),
)
# ICLR/NeurIPS/ICML: 반드시 "Accepted" decision 필터
notes = client.get_all_notes(
    content={'venueid': 'ICLR.cc/2026/Conference'},  # accepted 논문만
)
for n in notes:
    # n.content['title']['value'], n.content['abstract']['value']
    # n.content['authors']['value'], n.content.get('pdf', {}).get('value')
    ...
```

- `api2.openreview.net`은 2024+ venue용. 과거 venue는 `api.openreview.net`.
- **Submission invitation이 아닌 accepted venueid**를 쓴다. Submission은 reject/withdraw 포함이라 venue로 인정 불가.
- 인증 실패 시 public-only 모드: `OpenReviewClient(baseurl=..., username=None)` 시도.

## ACL Anthology 쿼리 (acl-anthology 패키지)

```python
from acl_anthology import Anthology
anthology = Anthology.from_repo()  # shallow clone on first run, git pull after

coll = anthology.collections.get("2025.acl")  # "{year}.{event}"
for vol in coll.volumes():
    for paper in vol.papers():
        if paper.is_frontmatter:
            continue
        title = str(paper.title)
        abstract = str(paper.abstract) if paper.abstract else ""
        authors = [f"{a.name.first} {a.name.last}" for a in paper.authors]
        pdf_url = f"https://aclanthology.org/{paper.full_id}.pdf"
```

- `Anthology.from_repo()` → shallow clone (~210MB) of `acl-org/acl-anthology` GitHub repo. 이후 호출은 `git pull`만.
- Rate limit 없음 (로컬 데이터).
- ACL/EMNLP main proceedings(`.acl-long`, `.acl-short`, `.emnlp-main` 등)는 whitelist → `papers/metadata/<ACL|EMNLP>/<Year>/`로 라우팅.
- NAACL은 `ANTHOLOGY_WHITELIST_EVENTS`에 포함되어 스캔되지만 `classify_route()`가 `etc`로 분류. `--include-arxiv` opt-in 시만 저장.

## Dedup 규칙 (상세)

1. **정규화 제목**: 소문자화 + 구두점 제거 + 공백 단일화
2. **키**: `normalized_title` OR `arxiv_id` OR `openreview_id` OR `anthology_id`
3. 기존 manifest에 키 존재 → skip
4. 같은 논문이 arXiv+OpenReview 양쪽에 있으면 OpenReview 버전 우선(peer-reviewed)
5. Near-duplicate 휴리스틱: 제목 Levenshtein 90%+ AND 저자 top-1 일치 → merge

## Incremental Cursor

`papers/vector_db/manifest.json`에 venue별 cursor 저장:

```json
{
  "cursors": {
    "arxiv:cs.CL:jailbreak": {"last_date": "2026-04-10"},
    "openreview:ICLR.cc/2026": {"last_note_id": "xxx"}
  },
  "files": {
    "papers/metadata/ICLR/2026/attack-lldm.raw.md": {"sha256": "...", "mtime": 1234567890}
  }
}
```

각 실행은 cursor 이후만 조회. 실행 후 cursor 갱신.

## raw.md 출력 포맷 (full template)

```markdown
---
title: "Paper Title"
authors: ["A. Author", "B. Author"]
venue: "ICLR"          # whitelist 6개 중 하나 OR 원문 학술지/워크숍 이름(NAACL/IJCAI/ACL Findings 등 포함) OR "arXiv"
year: 2026             # 게재 연도 (etc 모드에서는 arxiv published.year)
venue_class: "whitelist"  # "whitelist" | "etc"
arxiv_id: "2601.12345"
openreview_id: "xyzABC"
anthology_id: "2025.acl-long.123"  # ACL/EMNLP/NAACL 전용
pdf_url: "https://arxiv.org/pdf/2601.12345"
published: "2026-04-10"
categories: ["cs.CL", "cs.LG"]
keywords: ["diffusion", "jailbreak"]
venue_source: "openreview"   # openreview|anthology|arxiv-comment|arxiv-only
hunter_fetched: "2026-04-14T15:00:00+09:00"
---

# {title}

## Abstract
{abstract 전문}

## Metadata
- venue / year / authors / URLs (위 frontmatter 그대로 bullet로 중복)
```

- 파일명: `{slug}.raw.md` where `slug = re.sub(r'[^a-z0-9]+', '-', title.lower())[:60]`
- 경로 분기:
  - `venue_class == "whitelist"` → `papers/metadata/<Venue>/<Year>/<slug>.raw.md`
  - `venue_class == "etc"` → `papers/metadata/etc/<Year>/<slug>.raw.md`

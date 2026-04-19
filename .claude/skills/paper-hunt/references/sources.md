# Paper Hunt — Source Details & Canonical Casing

## Primary venue sources (6 whitelist)

| Category | Venue | Source (priority) | Identifier / verification |
|---|---|---|---|
| AI | NeurIPS | OpenReview → arXiv | `NeurIPS.cc/YYYY/Conference` / arXiv comment "NeurIPS YYYY" |
| AI | AAAI | arXiv → AAAI proceedings | arXiv cs.AI + comment "AAAI YYYY"; `aaai.org/ojs` DOI |
| AI | ICLR | OpenReview → arXiv | `ICLR.cc/YYYY/Conference` / arXiv comment "ICLR YYYY" |
| AI | ICML | OpenReview(2024+) → PMLR → arXiv | `ICML.cc/YYYY/Conference` / PMLR vXYZ / arXiv comment "ICML YYYY" |
| NLP | ACL | ACL Anthology → arXiv | `aclanthology.org/YYYY.acl-*` / arXiv comment "ACL YYYY" |
| NLP | EMNLP | ACL Anthology → arXiv | `aclanthology.org/YYYY.emnlp-*` / arXiv comment "EMNLP YYYY" |

**Canonical casing** (strictly fixed, 6 whitelist): `NeurIPS`, `AAAI`, `ICLR`, `ICML`, `ACL`, `EMNLP`. The `CANONICAL` dictionary also carries label preservations for non-whitelist venues that appear frequently (`IJCAI`, `NAACL`) — those route as `venue_class: "etc"` and are saved only under `--include-arxiv` opt-in.

`Findings of ACL/EMNLP/NAACL`, plus NAACL / IJCAI main proceedings, workshops, arXiv preprints, and journal papers, are all `venue_class: "etc"`. **In the default run (no flag) they are dropped**. Only when an opt-in flag like `/research-papers <topic> --include-arxiv` is given, `classify_route()`'s fallback path routes them into `papers/metadata/etc/<Year>/` with the original label preserved in `venue` (e.g. "ACL Findings", "NAACL 2024").

## arXiv query template (opt-in: `--include-arxiv`)

```python
import sys
sys.path.insert(0, "/home/irteam/sw/research_hub/.claude/skills/paper-hunt/scripts")
from classify_route import classify_route, WHITELIST, VENUE_PAT, CANONICAL
```

- Unified flow: only 3 sources (OpenReview / ACL Anthology / arXiv). The per-year call order is **fixed** at `openreview → anthology → arxiv` — OR/Anthology stamp whitelist labels first, then arXiv re-discoveries are dedup-dropped.
- **Runtime gate**: without `--include-arxiv`, `main()` removes `arxiv` from `args.sources` so this source never runs (synced with `SKILL.md` L21-22). That is, the query template in this section only runs on the opt-in path.
- Rate limit: 3s per request (handled automatically by the arxiv library)
- Pagination: `max_results` + cursor, save `last_entry_id`
- Internal: `arxiv.Search(...)` + `arxiv.Client(page_size=20, delay_seconds=3)`

## OpenReview query template (accepted only)

```python
import openreview
client = openreview.api.OpenReviewClient(
    baseurl='https://api2.openreview.net',
    username=os.environ.get('OPENREVIEW_USERNAME'),
    password=os.environ.get('OPENREVIEW_PASSWORD'),
)
# ICLR/NeurIPS/ICML: always filter by "Accepted" decision
notes = client.get_all_notes(
    content={'venueid': 'ICLR.cc/2026/Conference'},  # accepted papers only
)
for n in notes:
    # n.content['title']['value'], n.content['abstract']['value']
    # n.content['authors']['value'], n.content.get('pdf', {}).get('value')
    ...
```

- `api2.openreview.net` is for 2024+ venues. Older venues use `api.openreview.net`.
- Use **the accepted venueid, not the Submission invitation**. Submission includes reject/withdraw, so it cannot be accepted as a venue.
- On auth failure, try public-only mode: `OpenReviewClient(baseurl=..., username=None)`.

## ACL Anthology query (acl-anthology package)

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

- `Anthology.from_repo()` → shallow clone (~210MB) of the `acl-org/acl-anthology` GitHub repo. Subsequent calls only `git pull`.
- No rate limit (local data).
- ACL/EMNLP main proceedings (`.acl-long`, `.acl-short`, `.emnlp-main`, etc.) are whitelist → routed to `papers/metadata/<ACL|EMNLP>/<Year>/`.
- NAACL is in `ANTHOLOGY_WHITELIST_EVENTS` and scanned, but `classify_route()` classifies it `etc`. Saved only under `--include-arxiv` opt-in.

## Dedup rules (detailed)

1. **Normalized title**: lowercase + punctuation stripped + whitespace collapsed
2. **Key**: `normalized_title` OR `arxiv_id` OR `openreview_id` OR `anthology_id`
3. If key exists in manifest → skip
4. If the same paper exists on both arXiv and OpenReview, prefer the OpenReview version (peer-reviewed)
5. Near-duplicate heuristic: title Levenshtein 90%+ AND top-1 author match → merge

## Incremental Cursor

`papers/vector_db/manifest.json` stores per-venue cursors:

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

Each run queries only entries past the cursor. After the run, update the cursor.

## raw.md output format (full template)

```markdown
---
title: "Paper Title"
authors: ["A. Author", "B. Author"]
venue: "ICLR"          # one of the 6 whitelist OR original journal/workshop name (incl. NAACL / IJCAI / ACL Findings) OR "arXiv"
year: 2026             # publication year (in etc mode, arxiv published.year)
venue_class: "whitelist"  # "whitelist" | "etc"
arxiv_id: "2601.12345"
openreview_id: "xyzABC"
anthology_id: "2025.acl-long.123"  # ACL/EMNLP/NAACL only
pdf_url: "https://arxiv.org/pdf/2601.12345"
published: "2026-04-10"
categories: ["cs.CL", "cs.LG"]
keywords: ["diffusion", "jailbreak"]
venue_source: "openreview"   # openreview|anthology|arxiv-comment|arxiv-only
hunter_fetched: "2026-04-14T15:00:00+09:00"
---

# {title}

## Abstract
{full abstract}

## Metadata
- venue / year / authors / URLs (duplicated as bullets from the frontmatter above)
```

- Filename: `{slug}.raw.md` where `slug = re.sub(r'[^a-z0-9]+', '-', title.lower())[:60]`
- Path branching:
  - `venue_class == "whitelist"` → `papers/metadata/<Venue>/<Year>/<slug>.raw.md`
  - `venue_class == "etc"` → `papers/metadata/etc/<Year>/<slug>.raw.md`

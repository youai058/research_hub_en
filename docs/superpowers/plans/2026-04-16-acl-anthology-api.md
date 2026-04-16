# ACL Anthology API Integration — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace HTML scraping in `hunt.py`'s ACL Anthology source with the `acl-anthology` Python package for faster, more reliable paper collection.

**Architecture:** Lazy-init `Anthology.from_repo()` once in `main()`, inject into `hunt_anthology_year()`. Delete ~170 lines of HTML helpers. Add NAACL to venue map.

**Tech Stack:** `acl-anthology-py` (Python package), existing `classify_route.py`, `write_raw()`.

**Spec:** `docs/superpowers/specs/2026-04-16-acl-anthology-api-design.md`

---

### Task 1: Install dependency

**Files:**
- None (conda env change only)

- [ ] **Step 1: Install acl-anthology-py**

```bash
conda run -n LLDM pip install acl-anthology-py
```

- [ ] **Step 2: Verify import works**

```bash
conda run -n LLDM python3 -c "from acl_anthology import Anthology; print('OK')"
```

Expected: `OK`

- [ ] **Step 3: Verify `from_repo()` works (first-time clone)**

```bash
conda run -n LLDM python3 -c "
from acl_anthology import Anthology
a = Anthology.from_repo()
c = a.collections.get('2024.acl')
print(f'2024.acl: {sum(1 for v in c.volumes() for p in v.papers() if not p.is_frontmatter)} papers')
"
```

Expected: `2024.acl: <N> papers` (should be ~1600+)

- [ ] **Step 4: Commit** (nothing to commit — env-only change, no tracked files)

---

### Task 2: Add NAACL to venue map and rewrite `hunt_anthology_year()`

**Files:**
- Modify: `.claude/skills/paper-hunt/scripts/hunt.py:91-94` (ANTHOLOGY_WHITELIST_EVENTS)
- Modify: `.claude/skills/paper-hunt/scripts/hunt.py:654-876` (delete HTML helpers + rewrite `hunt_anthology_year()`)
- Modify: `.claude/skills/paper-hunt/scripts/hunt.py:549-621` (delete `_http_get`, `_UA`, `_try_bs`)

- [ ] **Step 1: Add NAACL to `ANTHOLOGY_WHITELIST_EVENTS`**

Change lines 91-94:

```python
# ACL Anthology event slugs for whitelist NLP venues.
ANTHOLOGY_WHITELIST_EVENTS = {
    "ACL": "acl",
    "EMNLP": "emnlp",
    "NAACL": "naacl",
}
```

- [ ] **Step 2: Delete the HTML-only helpers**

Delete these blocks entirely (lines 549-665):

- `_UA` constant (line 554)
- `_http_get()` function (lines 557-612)
- `_try_bs()` function (lines 615-621)
- `_ANTH_ID_RE` regex (lines 662-665)
- `_anth_fetch_listing()` function (lines 668-727)
- `_anth_fetch_detail()` function (lines 730-762)
- `_anth_venue_label()` function (lines 765-783)
- The `# ---- ACL Anthology` section comment (lines 654-661)

Keep `_kw_match()` (lines 624-629) and `_Shim` (lines 632-651) — these are shared.

- [ ] **Step 3: Rewrite `hunt_anthology_year()`**

Replace the old function (lines 786-876) with:

```python
def hunt_anthology_year(
    root: Path,
    year: int,
    keywords: list[str],
    max_per_venue_year: int,
    seen: SeenKeys,
    manifest: dict,
    per_venue_year_counts: dict[tuple[str, int], int],
    anthology,
) -> list[Path]:
    """ACL Anthology scanner for a single year bucket.

    Uses the `acl-anthology` package (local XML data) instead of HTTP
    scraping.  Iterates collections → volumes → papers for each event
    in ANTHOLOGY_WHITELIST_EVENTS.
    """
    emitted: list[Path] = []
    for _canon, event in ANTHOLOGY_WHITELIST_EVENTS.items():
        coll_id = f"{year}.{event}"
        coll = anthology.collections.get(coll_id)
        if coll is None:
            print(f"[anthology][{year}] collection {coll_id} not found", file=sys.stderr)
            continue

        paper_count = 0
        for vol in coll.volumes():
            for paper in vol.papers():
                if paper.is_frontmatter:
                    continue
                paper_count += 1
                title = str(paper.title)
                anthology_id = paper.full_id

                if seen.seen(title=title, anthology_id=anthology_id):
                    continue

                shim = _Shim(anthology_id=anthology_id, published_year=year)
                venue, v_year, vclass = classify_route(shim)
                if vclass == "etc" and not _ALLOW_ETC:
                    continue

                cap_key = (venue, v_year)
                if per_venue_year_counts.get(cap_key, 0) >= max_per_venue_year:
                    continue

                abstract = str(paper.abstract) if paper.abstract else ""
                if keywords and not _kw_match(title + " " + abstract, keywords):
                    continue

                authors = [
                    f"{a.name.first} {a.name.last}".strip()
                    for a in (paper.authors or [])
                ]
                pdf_url = f"https://aclanthology.org/{anthology_id}.pdf"

                path = write_raw(
                    root,
                    venue=venue,
                    year=v_year,
                    venue_class=vclass,
                    title=title,
                    authors=authors,
                    abstract=abstract or "(abstract unavailable)",
                    pdf_url=pdf_url,
                    anthology_id=anthology_id,
                    published=str(v_year),
                    venue_source="anthology",
                )
                seen.add(title=title, anthology_id=anthology_id)
                per_venue_year_counts[cap_key] = per_venue_year_counts.get(cap_key, 0) + 1
                emitted.append(path)
                print(f"  + [{venue} {v_year} :: {vclass}] {title[:80]}", flush=True)

        print(f"[anthology][{year}] {event}-{year}: {paper_count} papers scanned", flush=True)
        manifest.setdefault("cursors", {})[f"anthology:{event}:{year}"] = {
            "last_run": now_kst(),
            "year": year,
        }
    return emitted
```

- [ ] **Step 4: Verify syntax**

```bash
conda run -n LLDM python3 -c "
import sys; sys.path.insert(0, '.claude/skills/paper-hunt/scripts')
import hunt
print('import OK')
"
```

Expected: `import OK`

- [ ] **Step 5: Commit**

```bash
git add .claude/skills/paper-hunt/scripts/hunt.py
git commit -m "refactor(hunt): replace ACL Anthology HTML scraping with acl-anthology package

Delete ~170 lines of HTML helpers (_http_get, _try_bs, _anth_fetch_listing,
_anth_fetch_detail, _anth_venue_label, _ANTH_ID_RE). Add NAACL to
ANTHOLOGY_WHITELIST_EVENTS. hunt_anthology_year() now iterates local XML
data via Anthology.from_repo() — zero HTTP requests."
```

---

### Task 3: Wire up `Anthology` init in `main()` and update call site

**Files:**
- Modify: `.claude/skills/paper-hunt/scripts/hunt.py` — `main()` function

- [ ] **Step 1: Add lazy anthology init in `main()` before the year loop**

Insert after the `per_venue_year_counts` line (around current line 979) and before `all_emitted`:

```python
    # Lazy-init ACL Anthology package (local XML data, no HTTP).
    anthology_obj = None
    if "anthology" in args.sources:
        try:
            from acl_anthology import Anthology  # type: ignore
            anthology_obj = Anthology.from_repo()
            print("[anthology] init OK (local XML data)", file=sys.stderr)
        except Exception as e:
            print(f"[anthology] skip — init failed: {e}", file=sys.stderr)
            args.sources = [s for s in args.sources if s != "anthology"]
```

- [ ] **Step 2: Update the `hunt_anthology_year()` call site to pass `anthology_obj`**

Change the anthology call block in the year loop (around current line 1004-1008):

```python
        if "anthology" in args.sources and anthology_obj is not None:
            all_emitted += hunt_anthology_year(
                root, year, args.keywords, args.max_per_venue_year,
                seen, manifest, per_venue_year_counts,
                anthology_obj,
            )
```

- [ ] **Step 3: Verify syntax again**

```bash
conda run -n LLDM python3 -c "
import sys; sys.path.insert(0, '.claude/skills/paper-hunt/scripts')
import hunt
print('import OK')
"
```

Expected: `import OK`

- [ ] **Step 4: Commit**

```bash
git add .claude/skills/paper-hunt/scripts/hunt.py
git commit -m "feat(hunt): wire Anthology init in main() and pass to hunt_anthology_year"
```

---

### Task 4: Smoke test — dry run with real data

**Files:**
- None (test only)

- [ ] **Step 1: Run anthology-only dry run with keyword filter**

```bash
cd /home1/irteam/sw/research_hub && \
conda run -n LLDM python3 .claude/skills/paper-hunt/scripts/hunt.py \
    --sources anthology \
    --keywords "diffusion" \
    --years 2024 \
    --max-per-venue-year 5 \
    --dry-run
```

Expected: JSON output with `"emitted": <N>` where N > 0. Papers should be from ACL/EMNLP 2024 with "diffusion" in title or abstract.

- [ ] **Step 2: Verify NAACL scanning (with --include-arxiv for etc)**

```bash
cd /home1/irteam/sw/research_hub && \
conda run -n LLDM python3 .claude/skills/paper-hunt/scripts/hunt.py \
    --sources anthology \
    --keywords "language model" \
    --years 2024 \
    --include-arxiv \
    --max-per-venue-year 3 \
    --dry-run
```

Expected: NAACL results should appear with `venue_class: "etc"`. ACL/EMNLP main results should appear with `venue_class: "whitelist"`.

- [ ] **Step 3: Verify dedup — run the same command twice, second should emit 0**

```bash
cd /home1/irteam/sw/research_hub && \
conda run -n LLDM python3 .claude/skills/paper-hunt/scripts/hunt.py \
    --sources anthology \
    --keywords "diffusion" \
    --years 2024 \
    --max-per-venue-year 5

# Second run — all papers already in manifest
conda run -n LLDM python3 .claude/skills/paper-hunt/scripts/hunt.py \
    --sources anthology \
    --keywords "diffusion" \
    --years 2024 \
    --max-per-venue-year 5
```

Expected: Second run output shows `"emitted": 0`.

- [ ] **Step 4: Verify full pipeline (all sources together)**

```bash
cd /home1/irteam/sw/research_hub && \
conda run -n LLDM python3 .claude/skills/paper-hunt/scripts/hunt.py \
    --venues-whitelist-all \
    --keywords "diffusion language model" \
    --years 2025 \
    --max-per-venue-year 3 \
    --dry-run
```

Expected: OpenReview (ICLR/NeurIPS/ICML) + Anthology (ACL/EMNLP/NAACL) all scan without errors.

---

### Task 5: Update documentation

**Files:**
- Modify: `.claude/skills/paper-hunt/references/sources.md`
- Modify: `.claude/skills/paper-hunt/SKILL.md`

- [ ] **Step 1: Update `sources.md` — ACL Anthology section**

Replace the "ACL Anthology 쿼리 템플릿" section (around lines 55-65) with:

```markdown
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
```

- [ ] **Step 2: Update `SKILL.md` — remove HTML scraping references**

In the `## 실패 처리` section, remove or update the line about "API 429: 30s 대기 후 1회 재시도" since anthology no longer uses HTTP. The 429 handling still applies to OpenReview/arXiv, so keep it but clarify scope:

```markdown
## 실패 처리

- API 429 (OpenReview/arXiv): 30s 대기 후 1회 재시도, 두 번째 429는 venue skip
- Anthology init 실패: `acl-anthology` 패키지 import 또는 `from_repo()` 실패 시 anthology source skip
- 인증 실패 (OpenReview): env 안내 후 venue skip (public-only fallback 시도)
- 네트워크 (arXiv): 지수 백오프 3회
- Optional fetch 실패: 리스팅 중단하지 않음, abstract fallback, 필요 시 `venue_class: "etc"` 라우팅
```

- [ ] **Step 3: Commit**

```bash
git add .claude/skills/paper-hunt/references/sources.md .claude/skills/paper-hunt/SKILL.md
git commit -m "docs(paper-hunt): update sources.md and SKILL.md for acl-anthology package"
```

---

### Task 6: Final commit and cleanup verification

**Files:**
- None

- [ ] **Step 1: Verify no leftover references to deleted functions**

```bash
cd /home1/irteam/sw/research_hub && \
grep -rn "_anth_fetch\|_try_bs\|_http_get\|_ANTH_ID_RE\|_anth_venue_label\|BeautifulSoup" \
    .claude/skills/paper-hunt/scripts/hunt.py
```

Expected: zero matches.

- [ ] **Step 2: Verify `_kw_match` and `_Shim` still present**

```bash
grep -n "_kw_match\|class _Shim" .claude/skills/paper-hunt/scripts/hunt.py
```

Expected: both found.

- [ ] **Step 3: Count lines removed**

```bash
git diff --stat HEAD~3..HEAD -- .claude/skills/paper-hunt/scripts/hunt.py
```

Expected: significant net deletion (target: ~170 lines removed, ~60 added = ~110 net reduction).

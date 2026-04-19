# paper-hunt scripts — RUNBOOK

## Default invocation (auto 3-year buckets, newest-first, 6-venue whitelist only)

```bash
python3 /home/irteam/sw/research_hub/.claude/skills/paper-hunt/scripts/hunt.py \
    --venues-whitelist-all \
    --keywords "diffusion language model" "LLaDA" \
    --max-per-venue-year 200
```

If `--years` is omitted, the default is KST `[today.year, today.year-1, today.year-2]`,
sweeping the entire 6-venue whitelist (OpenReview ICLR/NeurIPS/ICML + Anthology ACL/EMNLP + arXiv
comment AAAI) newest-first. **Without `--include-arxiv`, the arXiv keyword source is auto-skipped and
`venue_class == "etc"` results (NAACL / IJCAI / Findings / workshops / preprints) are dropped.**

## arXiv opt-in invocation (`--include-arxiv`)

```bash
python3 /home/irteam/sw/research_hub/.claude/skills/paper-hunt/scripts/hunt.py \
    --years 2026 2025 2024 \
    --venues-whitelist-all \
    --keywords "masked diffusion" "discrete diffusion" \
    --include-arxiv \
    --max-per-query 100 \
    --max-per-venue-year 200
```

With `--include-arxiv`, (a) the arXiv keyword query source runs per-year windows and (b) `venue_class == "etc"`
results from OpenReview / Anthology are kept and saved under `papers/metadata/etc/<Year>/`.
The input order is the scan priority. Passing `--years 2024 2025 2026` runs oldest-first
(no internal re-sort).

## CLI flags

| Flag | Default | Meaning |
|---|---|---|
| `--venues` | `[]` | Explicit OpenReview venueid list. Example: `ICLR.cc/2026/Conference`. Union with `--venues-whitelist-all`. |
| `--venues-whitelist-all` | False | Add all 6 whitelist venues to targets. OpenReview-supported venues (ICLR/NeurIPS/ICML) are auto-expanded per year to `<Venue>.cc/<year>/Conference`. The rest (AAAI/ACL/EMNLP) are silently skipped on OpenReview and covered via anthology / arxiv-comment sources. |
| `--include-arxiv` | False | **Opt-in**. Only when True does (a) the arXiv keyword query source actually run and (b) `venue_class == "etc"` results from OpenReview/Anthology get kept. When False, even if `arxiv` is in `--sources` it is auto-removed at runtime and etc results are dropped. |
| `--keywords` | `[]` | Keyword queries (whitespace-separated list). Used by arXiv / Anthology search. |
| `--years Y1 Y2 …` | `[today.year, -1, -2]` (KST) | Iterate year buckets in scan-priority order. **Respect input order (no internal re-sort)**. Newest-first recommended. |
| `--date-from YYYY-MM-DD` | None | arXiv date lower bound. **Ignored if `--years` is present**. For backward compatibility. |
| `--sources` | `openreview anthology arxiv` | Subset of the 3 sources. The per-year call order is always **fixed** at `openreview → anthology → arxiv`. Without `--include-arxiv`, `arxiv` is auto-removed at runtime even if listed. |
| `--max-per-query` | 100 | Cap per (one arXiv keyword × one year). |
| `--max-per-venue-year` | 200 | Cap per (canonical venue, year) combo. Sums across all sources. At cap, stop emitting for that venue-year. |
| `--manifest` | `papers/vector_db/manifest.json` | manifest path override (stub slot, not yet implemented). |
| `--dry-run` | False | Skip manifest update; log only. |

## Internal flow (year → source → venue)

1. Resolve `--years`: if absent, default to `[today.year, -1, -2]` (KST).
2. `build_openreview_venueids(years, explicit_venues)` — whitelist-all expands ICLR/NeurIPS/ICML × years into venueids. Other whitelist venues (AAAI/ACL/EMNLP) and non-whitelist venues have no OpenReview presence (silent skip).
3. Resolve `--include-arxiv`: if False, module-level `_ALLOW_ETC = False` is pinned and `arxiv` is auto-removed from `args.sources` (stderr one-line notice). If True, `_ALLOW_ETC = True` and both the arXiv source and etc emission are enabled.
4. Load manifest → initialize `SeenKeys` **exactly once** → shared across every year bucket.
5. For each year, **order fixed**:
   a. **openreview**: filter venueids belonging to that year, then `hunt_openreview_year()`. 404 / nonexistent venueids → stderr one-line + silent skip. Whitelist labels are stamped first. If `classify_route()` returns `etc` and `_ALLOW_ETC == False`, drop.
   b. **anthology**: `hunt_anthology_year()`. Listing `aclanthology.org/events/<event>-<year>/` → title ∪ abstract keyword match → main proceedings (ACL/EMNLP) are whitelist; NAACL, Findings, workshops are etc. If `_ALLOW_ETC == False`, drop etc.
   c. **arxiv** (only when keywords present AND `--include-arxiv` set): `hunt_arxiv_year()`. `(ti:"<kw>" OR abs:"<kw>") AND submittedDate:[YYYY01010000 TO YYYY12312359]`. For each result, run `classify_route()` → dedup-drop if already seen → check `--max-per-venue-year` cap → emit.
   d. At bucket end, log `[year YYYY] whitelist=N, etc=M, bucket_total=T`.
6. Register every `all_emitted` file into the manifest (sha256 + mtime + normalized_title).
7. Print the grand summary JSON: `{ emitted, whitelist, etc, years, per_venue_year, manifest }`.

**Important**:
- `SeenKeys` persists across year boundaries — an arxiv_id / openreview_id / normalized title seen in the 2026 bucket is not reprocessed in 2025 / 2024.
- `per_venue_year_counts` is also global (e.g. if a paper labeled ICLR 2026 via arXiv comment is found in both the 2026 and 2025 buckets, the cap applies once to the single `("ICLR", 2026)` bucket).
- Emit paths **always follow the final venue · year from `classify_route()`**, not the bucket year at scan time.

## Failure handling

- API 429: `time.sleep(30)` and retry once; a second 429 skips the venue
- OpenReview auth failure: guide to `OPENREVIEW_USERNAME/PASSWORD` env vars and skip the venue
- Nonexistent venueid (404 / NotFoundError): one-line stderr info and move to the next venueid
- Network drop: exponential backoff, 3 retries

## Environment setup

```bash
# Required packages (conda LLDM env)
pip install arxiv openreview-py pymupdf

# OpenReview credentials (optional)
export OPENREVIEW_USERNAME='...'
export OPENREVIEW_PASSWORD='...'  # stored in /home/irteam/sw/.env
```

## Optional full-text fetch

- Only reading the first 2–3 PDF pages via `pymupdf` is allowed.
- Run only when one of the trigger conditions holds: venue_class unclassifiable / near-duplicate suspected / relevance ambiguous.
- `raw.md` body still keeps only the abstract. The fetch result is used for classification / dedup / routing decisions.
- Cache: `papers/digest/<V>/<Y>/.pdf_cache/<slug>.pdf`

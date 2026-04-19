---
name: paper-hunt
description: "Paper collection. Default targets the 6 whitelist venues (NeurIPS / AAAI / ICLR / ICML / ACL / EMNLP) only. OpenReview / ACL Anthology scans + dedup + manifest cursor. Workshop / Findings / arXiv preprints are collected to `papers/metadata/etc/<Year>/` only when the `--include-arxiv` flag opts in. Triggers: 'paper collection', 'arxiv search', 'OpenReview', 'venue scan', 'paper hunt'."
---

# Paper Hunt Skill

Single integrated flow for paper listing. No seed / follow-up distinction.

## Input / Output

- **Input (CLI)**: keywords, source selection (openreview / anthology / arxiv), year buckets (`--years`), venue specification (`--venues` explicit / `--venues-whitelist-all` for all 6), arXiv opt-in (`--include-arxiv`), limits (`--max-per-query` / `--max-per-venue-year`), `--date-from` (backward compat).
- **Upstream contract (applies to the `papers` stage only)**: these CLI flags map 1:1 with the 3 fields the orchestrator reads from `research/topics/<slug>.topic.json` and injects into paper-hunter's Phase A prompt. This skill does not read topic.json directly; paper-hunter takes the prompt context and unfolds it into flags when calling `hunt.py`.
  - `refined_topic` → Goal sentence (not a CLI parameter; cited in PLAN.md)
  - `keyword_groups` (`[[a1, a2, ...], [b1, ...]]`, ≤ 2 groups) → the set of `--keywords` arguments. In-group variants are spread as individual arguments.
  - `scope.venues` → `--venues-whitelist-all` or `--venues` list; `scope.years` → `--years` (empty array → default 3-year window); `scope.include_arxiv` → presence/absence of `--include-arxiv`
  - Fallback: if topic.json is missing (legacy CLI path), paper-hunter takes a raw topic string and expands it into 3 forms (abbrev / full name / word-order variant). If topic.json exists but `topic_spec.py validate` fails, the orchestrator should already have aborted Phase A, so this path does not execute.
- **Output**: `papers/metadata/<Venue>/<Year>/<slug>.raw.md` (whitelist). With `--include-arxiv`, also `papers/metadata/etc/<Year>/<slug>.raw.md` (etc). Updates `papers/vector_db/manifest.json` cursor; logs per-year-bucket counts + grand total (whitelist / etc / per-venue-year breakdown).

### Key CLI flags

| Flag | Default | Meaning |
|---|---|---|
| `--years Y1 Y2 ...` | `[today.year, -1, -2]` (KST) | Iterate year buckets in scan-priority order. Respects input order. **Newest-first recommended.** |
| `--venues-whitelist-all` | False | Add all 6 whitelist venues to targets (union with `--venues`). OpenReview-supported venues (ICLR/NeurIPS/ICML) auto-expand to `<Venue>.cc/<year>/Conference` venueids; the rest (AAAI/ACL/EMNLP) are covered via anthology / arXiv comment sources. |
| `--include-arxiv` | False | **Opt-in**. Only when True does the arXiv keyword source run, and `venue_class == "etc"` results from openreview/anthology are kept. When False, arXiv source is auto-skipped and etc classification is dropped. |
| `--sources` | `openreview anthology arxiv` | Invoked in **this fixed order** inside a year bucket. Without `--include-arxiv`, `arxiv` is auto-removed at runtime. |
| `--max-per-venue-year N` | 200 | Cap per (canonical venue, year) combination. Operates independently of global dedup. |
| `--max-per-query N` | 100 | Cap per single arXiv keyword query. (Called independently per year × keyword.) |
| `--date-from YYYY-MM-DD` | None | **Ignored if `--years` is given**. Backward compat. |

## Keyword strategy

The hunter handles **recall**; narrow relevance judgment is delegated to downstream triage (`--topic`) (hunter = recall / triage = precision boundary).

- Extract the **field** from the user's topic and convert to **canonical terms** to use as keywords. Do not use the topic sentence or narrow method name verbatim.
- Decompose into **at most 2 axes**. For well-established fields, one canonical term + a synonym is usually enough.
- For **new / emerging fields** (no standardized notation yet), list multiple variants (abbrev / expansion / word-order) to secure recall.
- Field extraction and canonicalization are judged by Claude directly from the topic.
- **Keyword match scope: title ∪ abstract** (all sources). arXiv uses `(ti:"kw" OR abs:"kw")`; for anthology, listing does not pre-filter on title — fetch detail, then match on `title + abstract`; openreview dumps the whole venueid so this rule does not apply. The older arxiv `abs:`-only / anthology title-pre-filter approach missed abstract-only or title-only hits.

---

## Core rules (inline — do not move to references)

- **6 whitelist venues**: `NeurIPS`, `AAAI`, `ICLR`, `ICML`, `ACL`, `EMNLP` (uppercase casing fixed). Non-whitelist venues are labeled `etc` by `classify_route()` (the venue label preserves the original).
- **venue_class ∈ {whitelist, etc}**: every paper passes through `classify_route()` and is labeled as one of the two.
- **`etc` routing requires `--include-arxiv` opt-in**: in default runs (no flag), hunt.py drops `etc` results and does not run the arXiv source at all. Only with `--include-arxiv` are both paths written: `whitelist` → `papers/metadata/<Venue>/<Year>/`, `etc` → `papers/metadata/etc/<Year>/`.
- **3-year buckets, newest-first**: default scan order `[today.year, -1, -2]`. The loop is `year → source → venue` (outer → inner). The per-year source order is **fixed** at `openreview → anthology → arxiv`. If the user passes year order via `--years`, respect that order exactly (no internal reordering).
- **Global dedup persists across year boundaries**: `SeenKeys` initializes once from the manifest and carries through all year buckets. arxiv_id / openreview_id / normalized title seen in the 2026 bucket are not reprocessed in 2025 / 2024. Do not reset the table on year entry.
- **Forbidden directories (must not be created)**: `papers/arXiv/`, `papers/OpenReview/`, `papers/preprint/`, `papers/workshop/`, `papers/findings/` — every such paper goes under `papers/metadata/etc/<Year>/`.
- **Full-text policy separation (listing vs. summarization)**:
  - This skill (paper-hunt, listing) uses **abstract + API metadata only** to judge, classify, dedup, and produce `raw.md`.
  - Full-text PDF parsing + adaptive Marp summarization are **paper-summarize**'s responsibility (enforcing `len(full_text) > 3000` and other full-text protocols).
  - **Optional full-text fetch**: only when (1) venue_class cannot be classified, (2) near-duplicate is suspected, or (3) relevance is ambiguous — read the PDF's first 2–3 pages via `pymupdf` as a decision aid. `raw.md` body still stores abstract only.
- **frontmatter**: `venue` is verbatim; `venue_class: "whitelist" | "etc"`; plus id/url/published/categories/keywords/hunter_fetched.
- **Findings of ACL/EMNLP (and NAACL main + Findings)**: not part of the main 6-venue whitelist → `venue_class: "etc"`. With `--include-arxiv`, recorded under `papers/metadata/etc/<Year>/` using the original label (e.g. `venue: "ACL Findings"`). Without the flag, dropped.

## Canonical entry points (scripts/)

| Script | Role |
|---|---|
| `scripts/classify_route.py` | Pure function `classify_route(result)` + `WHITELIST` · `VENUE_PAT` · `CANONICAL`. All 3 sources go through it to set `venue_class`. |
| `scripts/hunt.py` | CLI. Integrates OpenReview + Anthology + arXiv, dedup, `raw.md` emission, manifest cursor. Uses abstract only. |

**Invocation examples**:

(1) Auto 3-year buckets (recommended default, whitelist-only):
```bash
python3 /home/irteam/sw/research_hub/.claude/skills/paper-hunt/scripts/hunt.py \
    --venues-whitelist-all \
    --keywords "diffusion language model" "LLaDA" \
    --max-per-venue-year 200
```
→ Without `--years`, defaults to KST `[today.year, today.year-1, today.year-2]`. Scans the 6 whitelist venues (OpenReview ICLR/NeurIPS/ICML + Anthology ACL/EMNLP + arXiv comment AAAI) newest-first. The arXiv keyword source is auto-skipped.

(2) arXiv opt-in (when the user requests `--include-arxiv`):
```bash
python3 /home/irteam/sw/research_hub/.claude/skills/paper-hunt/scripts/hunt.py \
    --years 2026 2025 2024 \
    --venues-whitelist-all \
    --keywords "masked diffusion" "discrete diffusion" \
    --include-arxiv \
    --max-per-query 100 \
    --max-per-venue-year 200
```
→ Same `year → source → venue` order. Per-year source order fixed: `openreview → anthology → arxiv`. arXiv queries each year with `submittedDate:[YYYY01010000 TO YYYY12312359]`. `etc` classifications from openreview/anthology are kept under `papers/metadata/etc/<Year>/`.

For CLI flag / internal flow details see `scripts/RUNBOOK.md`.

## Detailed references

- **Source API call templates (openreview / anthology / arxiv) · canonical casing table · dedup heuristic details · full `raw.md` template**: `references/sources.md`
- **CLI flags · internal flow · failure recovery · environment setup**: `scripts/RUNBOOK.md`

## Failure handling

- API 429 (OpenReview / arXiv): wait 30 s, retry once; a second 429 skips that venue
- Anthology init failure: if `acl-anthology` import or `from_repo()` fails, skip the anthology source
- Auth failure (OpenReview): guide env; skip venue (attempt public-only fallback)
- Network (arXiv): exponential backoff, 3 retries
- Optional fetch failure: do not abort listing; fall back to abstract; route as `venue_class: "etc"` if necessary

## Checklist (abbreviated)

- [ ] Cursor loaded; API credentials verified
- [ ] Primary source (whitelist 6) by default. Additional sources (arxiv keyword / reference chasing / non-whitelist venue) scanned in the same run only if `--include-arxiv` is set.
- [ ] **Year buckets iterated newest-first** (`[today.year, -1, -2]` default / respect user `--years` order)
- [ ] Per-year source order fixed: `openreview → anthology → arxiv`
- [ ] Listing uses abstract + metadata. Full-text parsing is paper-summarize's job.
- [ ] Optional full-text fetch only on classify-failure / near-dup / ambiguity (PDF 2–3p)
- [ ] Each result labeled via `classify_route()` → `whitelist` / `etc`
- [ ] Dedup (normalized title + arxiv_id + anthology_id + openreview_id)
- [ ] **Global dedup table carries across year boundaries** (no reset at bucket entry)
- [ ] `--max-per-venue-year` cap enforced — per (canonical venue, year) count
- [ ] Output paths:
  - whitelist → `papers/metadata/{NeurIPS|AAAI|ICLR|ICML|ACL|EMNLP}/<Year>/`
  - etc → `papers/metadata/etc/<Year>/` (flat) — includes any non-whitelist venue
- [ ] Verify forbidden directories not created: `papers/arXiv/`, `papers/OpenReview/`, `papers/preprint/`, `papers/workshop/`, `papers/findings/`
- [ ] Manifest updated; count report (whitelist / etc / failures)

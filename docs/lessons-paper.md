---
domain: paper
updated: 2026-04-19
covers: [paper-hunter, paper-summarizer, rag-curator]
---
<!-- Latest appends: 2026-04-17 gemini_digest OpenReview UA + Node heap + CANDIDATE regex + figure-crop 3-stage -->
<!-- 2026-04-19: bodies compressed (dedup / point-to-SSOT) — all rules preserved, narrative prose trimmed -->


# Lessons — Paper (hunt / summarize / RAG)

paper-hunter, paper-summarizer, and rag-curator MUST Read this file before starting work. Append-only. Compression is allowed (provided rules and artifacts are preserved).

Phase A-1 domain: arXiv/OpenReview collection, PDF parsing, Marp summarization, ChromaDB indexing.

## How to add

`/research-lesson paper "<rule title>"`

---

<!-- append entries below this line -->

## 2026-04-14 — KG bootstrap with sibling .kg.json
- **Rule**: every prose-writing agent writes a sibling `.kg.json` with the same base name next to its output `.md`
- **Why**: the KG reflects exactly what agents write, with no LLM inference, so the byproduct file is the single source of truth
- **When to apply**: after every artifact produced by paper-summarizer / answer-formulator / critic / experiment-planner / code-implementer / results-analyst

## 2026-04-15 — paper-rag must skip _fixture/ and underscore dirs
- **Rule**: `paper-rag index.py` unconditionally skips `_fixture`, `rag`, `kg` under `papers/`, and any directory starting with underscore (`_`)
- **Why**: KG smoke-test fixtures at `papers/_fixture/kg-*/paper.md` were incorrectly indexed as RAG chunks, contaminating `query.py` results with test docs like `bad_0_0`
- **When to apply**: when adding a new indexer path or creating a fixture directory — convention is `_`-prefix = "not an indexing/ingest target"

## 2026-04-15 — Venue routing: no drop, route to etc/
- **Rule**: if a paper is outside the whitelist venues (the 6 venues in CLAUDE.md §1 + extra sources when `--include-arxiv` is set), do NOT drop. Route to `papers/marp-summary/etc/<Year>/<slug>.md` and record `venue` (original) + `venue_class: "etc"` in the frontmatter.
- **Why**: dropping ACL Findings / workshops / arXiv preprints / journals from relevance filtering degrades gap-mining quality.
- **When to apply**: at the paper-hunter venue classification step — on classification failure, fall back to etc; never drop.

## 2026-04-15 — Full-text PDF required (paper-summarizer)
- **Rule**: paper-summarizer must NOT generate an abstract-only summary. It MUST parse the full-text PDF via pymupdf and write through the Critical Reading section.
- **Why**: abstract-only cannot catch the gap between author claims and actual evidence; answer-formulator would then build Evidence on a false premise.
- **When to apply**: when paper-summarizer is active at Phase A-1. On PDF parse failure, withhold the summary and quarantine to `papers/_rejected/`.

## 2026-04-15 — paper-hunter keywords use field-canonical terms, broad (recall-first)
- **Rule**: do NOT feed the user's narrow topic directly as `--keywords`. Replace each axis (model family / problem / method) with the field-canonical term, **up to 2 axes maximum**. Keep the narrow term only in paper-triage `--topic`. See the `paper-hunt` skill "keyword strategy" section for details and examples.
- **Why**: hunter = recall / triage = precision, 2-stage. If the hunter misses with a narrow term, the candidate set never reaches triage and there is no recovery. arXiv queries are metadata search, so long sentences or narrow method names often return 0 recall.
- **When to apply**: the caller performs the `topic → --keywords` conversion when entering A-1. If the keyword is a sentence or a narrow method name, stop and rephrase in field-canonical terms.

## 2026-04-15 — paper-hunt keywords match BOTH title and abstract
- **Rule**: for every source (arxiv / anthology / openreview), match keywords against both title and abstract. arxiv: `(ti:"kw" OR abs:"kw")`; anthology: do NOT pre-filter by title at the listing step — fetch detail and match title+abstract; openreview: the full `venueid` dump already contains both.
- **Why**: the old arxiv `abs:"kw"` alone + anthology title-only pre-filter structurally missed papers where the keyword appears in only one side. If the recall-owning hunter misses, downstream triage never sees it.
- **When to apply**: maintain when modifying paper-hunt code. The anthology detail fetch cost is bounded by `--max-per-venue-year`. Do NOT reintroduce title pre-filter.

## 2026-04-16 — paper-summarizer does NOT read the PDF — 2-stage Gemini digest pipeline
- **Rule**: do NOT model paper-summarizer Claude-side cost as "reading the full PDF per paper". Actually: Stage 1 (Gemini CLI `gemini-3-pro-preview` 1M ctx takes PDF → 2-5k word dense Markdown digest, cached at `papers/digest/<V>/<Y>/<slug>.digest.md`) → Stage 2 (Claude consumes digest + raw.md metadata only). Per-paper Claude cost ≈ 30-60s. 176 papers is doable in ~2h. Do NOT bypass via template batch scripts (e.g. `a3_batch_summarize.py`) — abstract-only / heuristic summaries mixed into the regular venue directories contaminate downstream QA evidence chains.
- **Why**: during 2026-04-16 diffusion-LLM corpus collection, per-paper Claude cost was mis-estimated as ~3min, leading to "176 × 3min = 8.75h, impossible" → batch-template bypass attempt → user halt. The rule is documented in skill §17-52 and agent §24-27, but was ignored. The bypass degrades Critical Reading to "Limitations stated by authors" from the digest.
- **When to apply**: before A-3 dispatch: (1) check digest cache coverage (count `papers/digest/`) (2) missing digests → separately generate via background bash (3) estimate Claude budget as 30-60s × N papers (4) if turn-limited, split the accepted set and dispatch in parallel (5) for Gemini-OOM papers, use only the pymupdf fallback in skill §60-67, no batch heuristics. `NODE_OPTIONS` tuning belongs at the `gemini_digest.py` level.

## 2026-04-16 — papers/ directory type-segregated structure
- **Rule**: 4-way split under `papers/`: `metadata/<V>/<Y>/<slug>.raw.md` (collected metadata), `digest/<V>/<Y>/<slug>.digest.md` (Gemini digest + `.pdf_cache/`), `marp-summary/<V>/<Y>/<slug>.md` (summary + `.figure_cache/`), `vector_db/` (Chroma / KG / manifest / kg-staging). SSOT: `docs/harness-layout.md`. The old flat `papers/<V>/<Y>/` mix is deprecated.
- **Why**: mixing raw / PDF / digest / Marp / DB causes (1) glob patterns cannot distinguish types (2) fine-grained `.gitignore` becomes impossible (3) the RAG indexer mis-indexes digests.
- **When to apply**: when adding a new storage path, maintain the 4-way split. `gemini_digest.py` locates `papers_root` by searching `metadata` upward from the raw.md path, so changes to the `metadata/` layout will break it.

## 2026-04-16 — paper-summarizer adaptive outline-first (fixed 6-part deprecated) — [SUPERSEDED by 2026-04-16 PLANNING below]
- **Rule**: the fixed 6-part template (Summary/Motivation/Observation/Method/Setup/Result) is deprecated. **Active remaining rules**: TL;DR = a one-or-two-sentence `> ` blockquote right after the H1 lead; result tables MUST be Markdown tables (no figure/screenshot replacement); Keywords are optional (only at the end if included); preserve the Marp frontmatter. SSOT: CLAUDE.md §6. Old PROMPT_VERSION bump v4→v5 (already advanced to v6 — see entry below).
- **Why**: based on user-supplied Notion-style reference summaries (6 exemplars), narrative flow must be respected. A fixed 6-part template leaves "(not applicable)" placeholders that degrade readability.
- **When to apply**: outline details are **SUPERSEDED** — use the "PLANNING" entry below. This entry is still valid only for the TL;DR / Markdown tables / Keywords rules (identical to CLAUDE.md §6).

## 2026-04-16 — paper-summarizer planning-first multi-figure (PLANNING block)
- **Rule**: a `<!-- PLANNING: ... -->` block is required before the body. Both subblocks are mandatory: **SECTIONS** (section number, title, and `[Figure N]` or `[no image]` tag upfront), **IMAGE_SOURCES** (each figure's `.figure_cache/<slug>__fig<N>.png` path + one-line purpose). ≤1 image per section. Place mainly at Method/Motivation/Observation/Analysis; Result/TL;DR/Critical Reading/Lead default to `[no image]`. If digest `figures: []`, all sections are `[no image]`. Filename convention: `<slug>__fig<N>.png`. PROMPT_VERSION bump v5→v6 (CANDIDATE format). SSOT: CLAUDE.md §6, paper-summarize SKILL.md.
- **Why**: papers with a Method schematic + Motivation observation figure suffer flow damage when a single Key Figure is placed in a fixed slot. Mid-body rearrangement breaks outline consistency and wastes tokens.
- **When to apply**: (1) missing either PLANNING subblock = fail (2) `[Figure N]` tag count must equal IMAGE_SOURCES item count (mismatch = rewrite) (3) referencing a figure outside the digest `figures:` list = fail (4) >1 image per section = rewrite (5) if digest `figures: []`, do NOT flag "no figures" in Critical Reading (6) on PROMPT_VERSION bump, sync all 4 locations: `gemini_digest.py` · SKILL.md · paper-summarizer.md · CLAUDE.md §6.

## 2026-04-17 — raw.md `authors:` is a JSON-array string, not CSV
- **Rule**: the `authors:` frontmatter in raw.md is a JSON-array literal emitted by hunt.py via `json.dumps(authors)` (e.g. `authors: ["Smith, John", "Doe, Jane"]`). Consumers parse as JSON array first and fall back to CSV only on failure. Do NOT `.split(",")` directly.
- **Why**: `_parse_frontmatter` is a line-wise scalar parser and returns the `[` value as a verbatim string. Naive `,` split corrupts multi-author papers into 4 broken author fragments, which `kg_skeleton.py` then promotes to Author nodes, polluting the KG. Found as a Critical bug in the 2026-04-17 commit 59e0e7a review.
- **When to apply**: (1) in `gemini_digest.py _write_digest`, parse authors as JSON-first → CSV fallback (2) `kg_skeleton.py _build_skeleton` uses digest frontmatter (already normalized YAML list) as its source (3) any change to the hunt.py output format must update all consumers simultaneously. raw.md frontmatter SSOT = hunt.py.

## 2026-04-17 — OpenReview PDF fetch requires a browser User-Agent
- **Rule**: in `scripts/gemini_digest.py`, PDF fetches against the OpenReview domain (`openreview.net/pdf?id=...`) must send a browser UA (`Mozilla/5.0 ... Chrome/...`). Other domains (arXiv) are fine with the existing UA.
- **Why**: during the 2026-04-17 Hierarchy Decoding (ICLR 2026, OpenReview-only) summary, nginx returned 403. OpenReview has a bot-UA blocking policy — this is guaranteed to recur for OpenReview-hosted papers (ICLR / NeurIPS etc.). arXiv has no equivalent issue.
- **When to apply**: add per-domain UA branching in `gemini_digest.py` with OpenReview defaulting to the browser UA. Skip fetch if `--pdf-cache` seeding succeeded earlier.

## 2026-04-17 — Gemini CLI OOMs on 63k+ char PDFs; inject NODE_OPTIONS preemptively
- **Rule**: when `scripts/gemini_digest.py` spawns the Gemini CLI, inject `NODE_OPTIONS=--max-old-space-size=8192` (or 12288) by default. If `NODE_OPTIONS` is already set, do NOT overwrite — append.
- **Why**: KLASS (83k chars) and Hierarchy Decoding (63k chars) both exceeded the Node.js v8 default heap (~4GB) and OOMed. 60k+ char papers are common in the diffusion-LLM corpus — recurrence guaranteed.
- **When to apply**: modify the subprocess / `os.environ` setup in `gemini_digest.py`. User overrides take precedence. Do NOT copy this rule into individual agent prompts — only `gemini_digest.py`.

## 2026-04-17 — DIGEST `CANDIDATE:` parser must NOT require `Reason:` literal prefix
- **Rule**: format is `CANDIDATE: Figure N | Section: <hint> | <reason>`. The `Reason:` literal prefix is **optional**. Splitting on `| ` is sufficient. Alternative regex: `^CANDIDATE:\s*(?P<label>Figure \d+)\s*\|\s*Section:\s*(?P<section>[^|]+)\s*\|\s*(?:Reason:\s*)?(?P<reason>.+)$`.
- **Why**: during the 2026-04-17 Hierarchy Decoding summary, Gemini emitted the candidates without `Reason:` → the existing regex dropped all 3 candidates and produced `figures: []`. Loosening the parser is more robust to LLM output variance than tightening the prompt.
- **When to apply**: relax CANDIDATE-line parsing in `gemini_digest.py`. After the change, smoke-test that both variants (with / without `Reason:`) populate the `figures` list.

## 2026-04-17 — Figure crop uses prior-caption upper bound + text-overlap reject + closest-cluster, 3 stages
- **Rule**: `_extract_figure_png` "above caption" crop: (1) upper bound = bottom of the immediately-prior `Figure M:` / `Table M:` caption on the same page (+`FIGURE_PRIOR_CAPTION_PAD` 6pt margin) (2) `_refine_figure_region` vertically clusters raster/drawing bboxes with a `FIGURE_CLUSTER_VGAP_PT` 18pt gap (3) reject any cluster whose text-block overlap exceeds `FIGURE_CLUSTER_TEXT_OVERLAP_REJECT` 0.55 (4) among surviving clusters, pick the one with the largest y1. **Do NOT use union-all.**
- **Why**: on the 2026-04-17 Prophet paper, Figure 3 merged all of Figure 2 + its caption, and Figure 5 included body text and a table. Cause: the `above` region started from `page_top` (→ Fig 2/3 union) and the drawing union was indiscriminate over the whole page (→ 450-drawing hull). Prior-caption upper bound fixed Fig 3; cluster text-overlap reject fixed Fig 5. No regression on Fig 1/2.
- **When to apply**: when modifying figure extraction in `gemini_digest.py`, smoke-re-extract Fig 1/2/3/5 from the Prophet PDF (`papers/digest/etc/2026/.pdf_cache/diffusion-language-models-know-the-answer-before-decoding.pdf`) — Fig 3 must contain only the diagram, Fig 5 only the histogram. Keep the 3 fields (`clusters=N`, `text_overlap=0.NN`, `survivors=N`) in the `_refine_figure_region` log. For corner cases, prefer adding a filter over tuning constants.

## 2026-04-17 — paper-triage does rubric scoring ONLY after dense-retrieval pre-filter
- **Rule**: A-2 paper-triage does NOT pass the full corpus abstract JSON to Claude. From the ChromaDB `abstracts` collection maintained by A-1.5 `abstract-indexer`, `retrieve.py` narrows via cosine top-K (default K ≤ 300, threshold 0.5), and rubric 0-5 scoring runs ONLY on the candidate set. `triage_context.exclude` is a hard veto (substring match), `signal_methods` is cosine +0.05 boost + `signal_hit: true` hint.
- **Why**: 1,491 raw.md → 2.65 MB abstract JSON → ~660K Opus input tokens. Using Opus as a Lucene substitute makes token cost scale linearly with corpus size. OpenReview / Semantic Scholar / Elicit all use 2-stage retrieval. The repo already had bge-m3 + Chroma via rag-curator, but triage wasn't reusing it.
- **When to apply**: when modifying paper-triage SKILL.md / agent, do NOT revert `collect_abstracts.py` to the Step-2 default. Call `retrieve.py` first. If triage fails on a new corpus, check the A-1.5 manifest. For ad-hoc calls where the collection is empty, exit 5 — run abstract-indexer manually.

---
name: paper-summarize
description: "Full-text PDF adaptive Marp summary. 2-stage pipeline (Gemini digest → Claude summary), pymupdf parsing mandatory (abstract-only forbidden), per-paper PLANNING block first (section structure + per-section image placement decided upfront) with only 4 required anchors (TL;DR / Method / Result / Critical Reading); free sections between them follow the paper's flow. Equations / numbers verbatim, result tables as Markdown tables. Marp frontmatter preserved. paper-summarizer only. Triggers: 'paper summary', 'Marp slides', 'paper summary'."
---

# Paper Summarize Skill

Procedure and template for summarizing a paper **critically** and **concisely** with an adaptive structure tuned to each paper's logical flow.

## Input

- `papers/metadata/<V>/<Y>/<slug>.raw.md` (paper-hunter output) — this file is **abstract-level metadata**. The paper-hunt skill decides based on abstract + API metadata at listing time, and the `## Abstract` section of raw.md contains only the abstract.
- This summarization stage cannot rely on raw.md alone, so it **must download the full PDF and parse via pymupdf**. Abstract-only summaries are forbidden.

## Full-text reading protocol — 2-Stage (required)

This skill **does not have Claude read the PDF directly**. In Stage 1 the Gemini CLI (gemini-3-pro-preview, 1M+ context) reads the PDF and produces a dense digest; in Stage 2 the Claude paper-summarizer agent writes the adaptive Marp summary (PLANNING-first, 4 anchors) + KG based on that digest + raw.md metadata only. Direct pymupdf parsing is allowed **on the fallback path only**.

### Stage 1 — Generate Gemini digest (bash)

```bash
python3 .claude/skills/paper-summarize/scripts/gemini_digest.py <raw_md_path>
# On success, last stdout line = absolute path papers/digest/<V>/<Y>/<slug>.digest.md
# On failure, non-zero exit code (2: raw.md, 3: PDF, 4: pymupdf, 5: gemini CLI)
```

What the script does internally:

1. **Parse raw.md frontmatter** → `pdf_url` / `arxiv_id` / `anthology_id` / `cvf_url` / `slug` / `venue_class` / `venue` / `year`.
2. **Acquire PDF** (4-way fallback, order preserved):
   1. `pdf_url` from raw.md frontmatter (arXiv/OpenReview/CVF/Anthology)
   2. `https://arxiv.org/pdf/{id}.pdf` from `arxiv_id`
   3. `https://aclanthology.org/{id}.pdf` from `anthology_id`
   4. `cvf_url` directly
   - Save path: `papers/digest/<V>/<Y>/.pdf_cache/<slug>.pdf` (gitignored). Reused if present; `--force` invalidates.
3. **pymupdf full-text parse** + `len(full_text) > 3000` check.
4. **Gemini call**: `gemini -m gemini-3-pro-preview -p "<digest_prompt v1>" -o text` with full_text on stdin. Timeout 600s. Output is a long Markdown digest (2–5k words, equations and numbers verbatim).
5. **Write digest file**: `papers/digest/<V>/<Y>/<slug>.digest.md` (gitignored). Frontmatter records `source_raw`, `source_pdf_sha256`, `generated_at` (KST), `model: gemini-3-pro-preview`, `prompt_version: v6`, plus a **figure list** (`figures:` YAML array; each entry `{label, path, section_hint, reason}`) and backward-compat shortcut fields (`key_figure_label`, `key_figure_reason`, `key_figure_path` = figures[0]). The digest cache is valid only when **both** `source_pdf_sha256` AND `prompt_version` match — if PROMPT_VERSION is bumped the digest is regenerated even when the PDF sha is unchanged. `--force` fully invalidates the cache.
6. **Figure candidate selection + extraction** (since v6):
   - The prompt forces Gemini to emit **1–4** trailing lines `CANDIDATE: Figure N | Section: <hint> | Reason: <one sentence>` (priority order, most informative figure first). Tables are not candidates. Papers with no figures emit a single `CANDIDATES: NONE — <reason>` line.
   - `section_hint` token: one of `Method|Motivation|Observation|Setup|Result|Analysis|Discussion` — the downstream agent uses this hint when deciding per-section image placement in PLANNING.
   - `gemini_digest.py` locates each candidate via pymupdf caption search (`^(Figure|Fig\.?)\s*N[:\.\s]`), crops above-caption → below-caption → whole-page, and shrinks the bbox via union of image blocks + `page.get_drawings()` (keeps the original region if crop height < 10%).
   - Renders the clip at `fitz.Matrix(3, 3)` (≈216 DPI) → `papers/marp-summary/<V>/<Y>/.figure_cache/<slug>__fig<N>.png` (gitignored). **Filename scheme is `<slug>__fig<N>.png`** — preserving the figure number so downstream PLANNING can reference it easily.
   - Sanity: if the PNG is <10 KB treat it as a failure and delete → only that figure is dropped from the list.
   - **Figure extraction failure is not fatal**. The digest is still written with exit 0; only successfully extracted figures land in the `figures:` list. If all fail, `figures: []`. The downstream agent places only available figures into PLANNING.

### Stage 2 — Claude summarizer (agent, **planning-first**)

Section structure, figure placement, and figure purpose differ per paper, so **decide the PLANNING block (section structure + per-section image placement) first, then fill the body**. Do not force papers into a fixed 6-part template. Once PLANNING fixes the section order / titles / image placement, keep it — do not rearrange mid-flight.

**Step 2.0 — Agent-level cache re-check (idempotency guard)**

Before running any summarization work, verify that this paper was not already summarized in a concurrent run. The main-session cache_gate.py filtered the batch, but a race is possible (two `/research-papers` runs on the same slug).

```bash
python3 /home/irteam/sw/research_hub/.claude/skills/paper-summarize/scripts/cache_gate.py \
    --paths "<this_paper_raw_md>" \
    --out /tmp/cache_gate_recheck_<slug>.json
```

Parse the JSON. If `hits` contains this paper's path, skip the remaining steps for this paper and go to the next one in `batch_paths`. Log `[summarizer] cache re-check: <slug> already fresh — skipping`.

This step is cheap (~100ms per paper) and guards against wasted work when two main sessions race.

**Step 2a — Read the digest**
1. Read `raw_md_path` and `digest_path` with the Read tool. **Do not call pymupdf directly** (fallback path only).
2. Scan the digest's `## Author Framing` block, each section heading, `# Figures and Tables index`, and frontmatter `figures:` list to identify (a) the paper structure and (b) available image candidates.

**Step 2b — Design the PLANNING block (required, before body)**

Place the PLANNING block at the very top of the file as an HTML comment (also keep it in the final .md for maintenance / verification). **Decide section structure and per-section image placement together**. Strictly follow the format below:

```markdown
<!--
PLANNING:
  SECTIONS:
    1. Lead                                    [no image]
    2. TL;DR (anchor)                          [no image]
    3. Background — why is this problem hard   [no image]
    4. Key observation — attention sink shift  [Figure 2]
    5. Method (anchor) — PAD attack structure  [Figure 3]
    6. Experiments Setup                       [no image — baseline table]
    7. Result (anchor)                         [no image — Markdown tables]
    8. Analysis — sink-shift score correlation [Figure 5]
    9. Critical Reading (anchor)               [no image]
  IMAGE_SOURCES:
    - Figure 2: .figure_cache/<slug>__fig2.png — DLM attention sink visualization across steps
    - Figure 3: .figure_cache/<slug>__fig3.png — PAD attack pipeline overview
    - Figure 5: .figure_cache/<slug>__fig5.png — sink-shift score vs ASR
-->
```

Rules:
- **SECTIONS**: every section number, title, and image decision lives in this single block. Tag each section `[Figure N]` if an image goes in, `[no image]` or `[no image — <one-word reason>]` otherwise.
- **IMAGE_SOURCES**: actual path and one-line purpose for every figure referenced in SECTIONS. Only figures present in the digest's frontmatter `figures:` list are allowed (if absent: either extraction failed or Gemini did not recommend it — do not add to PLANNING).
- The 4 required anchors (TL;DR / Method / Result / Critical Reading) must appear in SECTIONS. Title variants allowed, order fixed.
- 0 or more free sections: Background / Motivation / Observation / Experiments Setup / Analysis / Discussion / Conclusion, or narrative H2 headings in the summary's writing language.
- Images go mostly into **Method / Motivation / Observation / Analysis** family sections. Result sections use numeric tables, so they are **by default no image**.
- TL;DR / Critical Reading / Experiments Setup / Lead / Conclusion are **by default no image** (baseline table / prose is enough).
- More than one image per section is forbidden (visual clutter). If multiple figures fit, split the section or pick one.
- If the digest has no figures at all, mark every section `[no image]`.

**4 required anchor sections** (title variants allowed, order as below):
1. **TL;DR** — first content slide right after the H1 lead. A `> ` blockquote of one or two sentences.
2. **Method** — core idea + equation verbatim + pseudocode / figure reference.
3. **Result** (or "Experiments Result", "실험 결과") — numeric tables MUST be Markdown tables.
4. **Critical Reading** — 3–5 bullets on the paper's weaknesses.

**Two PLANNING outline examples**:
- *classical*: Lead → TL;DR → Motivation → Method(Figure) → Setup → Result → Critical Reading
- *narrative*: Lead → TL;DR → "왜 이 문제가 어려운가" → "핵심 아이디어"(Figure) → "어떻게 통하는가"(Figure) → Result → Critical Reading

**Step 2c — Fill the body (exactly matching PLANNING)**
1. Implement SECTIONS' order, titles, and image placement **as-is**. Do not add / remove / rearrange.
2. Map digest content into each section. Equations and numbers are already verbatim in the digest — copy them as-is (no paraphrase).
3. **Result tables go in as Markdown tables — no screenshot images**. If the digest has Markdown tables, reuse; if messy, tidy structure but never touch values.
4. **Critical Reading** is not in the digest, so Claude writes it (inferred from the full text — experiment scope limits, baseline bias, reproducibility, etc., 3–5 bullets).
5. **Keywords (for RAG)** is optional. When included, put it at the very end as `` `kw1`, `kw2`, ... `` with 10–15 abstract-based terms.

**Step 2d — Embed images (PLANNING IMAGE_SOURCES as-is)**

For each PLANNING section tagged `[Figure N]`, insert exactly one image using the path from IMAGE_SOURCES:
- Format: inside that section, `![w:650](./.figure_cache/<slug>__fig<N>.png)` + a one-line caption (from IMAGE_SOURCES description or digest `figures[i].reason`).
- Path is relative to the raw.md directory (`.figure_cache/<slug>__fig<N>.png`) — the final `<slug>.md` lives in the same directory, so **use the path as-is without conversion**.
- No need for a dedicated slide per image — mixing inside the section flow is fine. Context matters.
- **Never substitute a figure for result numbers**. Even if a performance-bar-chart exists in figures, mark that section `[no image]` in PLANNING and transcribe the numbers into a Markdown table (the Gemini prompt already excludes result-bar-charts, but the final call is the agent's).
- If digest `figures: []` (empty list), mark every PLANNING section `[no image]` and skip image insertion. Not a failure mode — do not add a "no figure" flag to Critical Reading.

**Step 2e — Save path routing**
Based on the `venue_class` field. `<slug>.kg.json` is emitted to the same directory.

**Step 2f — Invoke kg_skeleton.py and patch Claim/Result on top**

Before writing `<slug>.kg.json`, generate the deterministic skeleton:

```bash
python3 /home/irteam/sw/research_hub/.claude/skills/paper-summarize/scripts/kg_skeleton.py \
    --digest <papers/digest/<V>/<Y>/<slug>.digest.md> \
    --slug <slug> \
    --out <papers/digest/<V>/<Y>/<slug>.kg.skeleton.json>
```

Capture the exit code:
- `0` — skeleton written successfully. Read the file, preserve every existing node + edge, then **append only**:
  - `Claim` nodes (one per distinct empirical claim the paper makes)
  - `Result` nodes (one per reported metric × method × dataset cell)
  - `MAKES_CLAIM` edges from `paper:<slug>` to each new `claim:<slug>#N`
  - `REPORTS_RESULT` edges from `paper:<slug>` to each new `result:<slug>#N`
  - `EVIDENCED_BY` edges from each supporting result back to the claim it evidences (i.e. `src=result:<slug>#M`, `dst=claim:<slug>#N`; must include `meta.polarity ∈ {support, contradict, mixed}`)

  Write the merged structure to `<slug>.kg.json` (not `.kg.skeleton.json`). Set `kg_skeleton_used: true` in the Marp frontmatter.

- `1`, `2`, or `3` (non-zero) — skeleton step failed. Fall back to authoring the full KG file from scratch (Paper/Author/Venue/Method/.../Claim/Result). Set `kg_skeleton_used: false` in the Marp frontmatter. This is the pre-v7 behavior; no correctness regression.

**Invariant**: the skeleton file itself is a build artefact in `papers/digest/<V>/<Y>/`. It is not versioned, not an agent deliverable, and can be deleted at any time without breaking anything (next run regenerates it).

### Fallback (when the Gemini digest fails)

If the Stage 1 script exits non-zero or the digest is empty, proceed via the pre-existing pymupdf path — **not** abstract-only:

1. Claude directly `import fitz` + loads `papers/digest/<V>/<Y>/.pdf_cache/<slug>.pdf` to build full_text.
2. Section split (`Introduction`, `Method/Approach`, `Experiments`, `Results`, `Ablation`, `Conclusion`, `Appendix`) → used as PLANNING basis for the adaptive Marp summary.
3. For long papers (>80 pages), summarize incrementally in order Main → Ablation appendix → other appendices.
4. The output file frontmatter MUST record `digest_source: fallback-pymupdf` and the failure reason (exit code + stderr summary).

Only when even the PDF cannot be acquired do we stop summarization + quarantine to `papers/_rejected/` (existing rule). **Abstract-only shrunken summaries are not valid output** and must not be saved to a regular venue directory.

## Output template (Marp, adaptive)

**Marp frontmatter is fixed**, body section composition is per-paper. The example below is a *classical outline* (a narrative outline is fine too as long as the 4 anchors are preserved).

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

> {one or two sentences — what the paper shows and why it matters. Maintain 음슴체. Example: "LLaDA-style discrete DLM에서 attention sink가 ARM과 달리 denoising step마다 shift한다는 걸 empirical하게 보여줌. 이는 DLM-specific prompt injection defense가 필요함을 시사함."}

---

## Motivation  <!-- Free section, only when the paper has this flow -->

- **Problem**: {problem to solve}
- **기존 approach**: {prior work approach}
- **Limitation**: {limitation that motivates this work}

---

## Method  <!-- Required anchor. Title variants OK ("Approach", "우리가 제안하는 것") -->

- Core idea in one sentence
- Equations (digest verbatim):

$$
\mathcal{L} = -\sum_i \log p(y_i | x_i)
$$

- algorithm pseudocode or figure reference

<!-- PLANNING marked this section [Figure 2] → IMAGE_SOURCES path as-is -->
![w:650](./.figure_cache/{slug}__fig2.png)

*{one-line caption from figures[i].reason}*

---

## Experiments Setup  <!-- Free section -->

| Method | Architecture | Key HP | Training | Notes |
|---|---|---|---|---|
| **Proposed** | ... | lr=…, batch=…, steps=… | from scratch / finetune | ... |
| **Baseline A** | ... | ... | ... | fairness / paper-cited numbers |

> Rule: one row per compared method; when HP missing, "(not reported)".

---

## Result  <!-- Required anchor. Numeric tables MUST be Markdown tables (no image) -->

| Benchmark | Baseline | Proposed | Δ |
|---|---|---|---|
| LM1B PPL ↓ | 20.86 | ≤23.00 | +2.14 |
| OWT PPL ↓ | 17.54 | ≤23.21 | +5.67 |

- key ablation finding (digest verbatim numbers preserved, no rounding)
- statistical significance reported?

---

## Analysis  <!-- Free section, only when the paper has this flow -->

- Authors' observations / interpretations
- Auxiliary experiments (hyperparameter sweep, ablation detail, etc.)

---

## Critical Reading  <!-- Required anchor -->

**논문의 부족한 부분**:
- {Weakness 1: e.g., experiments limited to specific dataset}
- {Weakness 2: e.g., baseline is outdated version}
- {Weakness 3: e.g., 32% gap with main claim on OWT framed as "match or exceed"}

---

## Keywords (for RAG, optional)  <!-- At the end, may be omitted -->

`keyword1`, `keyword2`, `keyword3`, ...
```

### Narrative outline example (free Korean H2 as long as the 4 anchors hold)

```markdown
## TL;DR
> ...

## 왜 이 문제가 어려운가
- ...

## 핵심 아이디어 — PAD가 하는 것
$$ ... $$

## Method  <!-- Anchor title can stay "Method" or become "PAD 어떻게 동작하는가?" -->
- ...

## 실험 결과가 말하는 것
| ... | ... | ... |

## Critical Reading
- ...
```

### Slide split rules

- `---` slide separator before every H2.
- If a slide has >7 bullets, split into a follow-up like "## Method (cont.)".
- Target total ~12–18 slides (varies with paper complexity).

## Writing style (Code-switching + 음슴체)

**Korean–English code-switching in 음슴체 register**: use the natural code-switched 음슴체(~임, ~함, ~됨, ~없음) voice that researchers write in lab notes / community posts.
- **Sentence endings in 음슴체**: use "~함/~했음/~임/~됨/~있음/~없음" instead of "~한다/~했다".
  - OK: "DLM의 attention sink가 ARM과 달리 denoising step마다 dynamically shift함"
  - NG: "DLM의 attention sink가 ARM과 달리 denoising step마다 dynamically shift한다"
- **Base sentence in Korean**, keep technical terms / proper nouns / method names / metric names in English as-is.
  - OK: "기존 ARM은 BOS token에 attention이 고정되는데, DLM은 step마다 sink position이 바뀜"
  - NG: "확산 언어 모델의 주의 집중 싱크가 자기회귀 모델과 달리..." (awkward translation forbidden)
- **Do not translate**: model name, method name, dataset name, metric name, loss function, architecture terms (transformer, attention, embedding, etc.), abbreviations (LLM, DLM, ARM, BLEU, PPL, etc.).
- **Write in Korean**: conjunctions, particles, general verbs/adjectives, sentence structure ("~를 제안함", "~에 비해 ~% 향상됨", "~라는 한계가 있음").
- Section headers stay in English (Marp template fixed).

## Critical-extraction principles

1. **Planning-first**: write the PLANNING comment block before the body. Decide section structure + per-section image placement (SECTIONS + IMAGE_SOURCES) **in one go** and then fill as decided — do not rearrange section order or image placement mid-flight. Image placement is allowed only for figures actually in the digest `figures:` list.
2. **TL;DR is a one-or-two-sentence blockquote**: fixed as the first content slide right after the H1 lead. What the paper shows and why it matters. Paraphrase OK (it's a summary).
3. **Equations and numbers quoted verbatim**: as-is from the digest. No paraphrase, no rounding, no unit conversion. Reproduce result tables as Markdown tables (no screenshot images).
4. **Target ~12–18 slides**: 1–3 slides per section. Avoid over-detail. Scale with paper complexity.
5. **Critical Reading = the paper's weaknesses**: experiment scope limits, baseline selection bias, reproducibility issues, gaps between author claims and actual evidence, etc. 3–5 bullets.
6. **Images go in context**: inside Method / Motivation / Observation / Analysis family sections. Do not fix-insert right after the title slide, inside Result, or inside Critical Reading. Max 1 per section.
7. **Keywords optional**: only when used, at the very end. 10–15 key terms from the abstract body. No author metadata or Gemini-generated keywords.

## Filename / path

- Input: `papers/metadata/<V>/<Y>/<slug>.raw.md`
- Output: `papers/marp-summary/<V>/<Y>/<slug>.md` (raw preserved, new file created)
- File length: target 200–500 lines; shrink summary if over.

## Failure modes

- **PDF missing / 404**: after all 4 download paths (arxiv/openreview/anthology/cvf) fail, **abort** summarization and return reject to the orchestrator. Do not save an abstract-only summary to the venue directory; quarantine to `papers/_rejected/<slug>.raw.md` with the reason recorded.
- **Broken equation parse**: preserve that equation as raw text in a code block + flag it under Unknown.
- **Very long paper (80+ pages)**: summarize per section in order Main → Ablation appendix → other appendices, then merge. If an appendix is skipped, state "Appendix X.Y summary omitted".
- **Author claim unclear**: add a "author claim extraction uncertain" flag to the Claims section.

## Checklist

- [ ] `gemini_digest.py` ran successfully → `papers/digest/<V>/<Y>/<slug>.digest.md` exists, or on failure the fallback flag (`digest_source: fallback-pymupdf`) is recorded
- [ ] PDF download succeeded + (digest path) Gemini digest generated / (fallback path) pymupdf parse succeeded (`len(full_text) > 3000`)
- [ ] Content for at least 4 of Introduction/Method/Experiments/Results/Appendix obtained via digest or pymupdf path
- [ ] Marp frontmatter `marp: true` (PPT compatibility)
- [ ] Top-of-file `PLANNING` HTML comment block exists (planning-first verification). Both SECTIONS + IMAGE_SOURCES subblocks present
- [ ] **All 4 required anchors present**: TL;DR / Method / Result / Critical Reading (title variants allowed)
- [ ] TL;DR exists as a `> ` blockquote on the first content slide right after the H1 lead
- [ ] Equations / numbers quoted verbatim (digest verbatim)
- [ ] Result tables written as **Markdown tables** (no screenshot images)
- [ ] ~12–18 slides, within 600 lines
- [ ] Each PLANNING `[Figure N]`-tagged section has exactly one image inserted (PLANNING ↔ body sync check). Paths exactly match IMAGE_SOURCES. If digest `figures: []`, every section is `[no image]`
- [ ] ≤1 image per section. Result / TL;DR / Critical Reading / Lead sections are `[no image]`
- [ ] Critical Reading included — 3–5 bullets on the paper's weaknesses (only when full-text based)
- [ ] Keywords (for RAG) **optional** — when used, at the end, 10–15 terms based on the abstract body
- [ ] `<slug>.kg.json` written in the same directory (see KG Emission below)
- [ ] Save path: route per the original raw.md's `venue_class` value (pre-decided by paper-hunt)
  - `whitelist` → `papers/marp-summary/<NeurIPS|AAAI|ICLR|ICML|ACL|EMNLP>/<Year>/`
  - `etc`       → `papers/marp-summary/etc/<Year>/` (flat, no sub-venue directory)
  - Both paths are **valid output**; `etc` does not imply lower quality — the summarization bar is identical.
- [ ] Forbidden-path check: did not save under `papers/arXiv/`, `papers/OpenReview/`, `papers/preprint/`, `papers/workshop/`, `papers/findings/`, etc. (those all go to `papers/marp-summary/etc/<Year>/`)
- [ ] Frontmatter `source_digest_sha256` matches `sha256(<slug>.digest.md)` byte-for-byte
- [ ] Frontmatter `prompt_version` equals digest's `prompt_version` (both should be `v7` for new summaries)
- [ ] Looped over every entry in `batch_paths` — none silently skipped except via Step 2.0 cache re-check

---

## KG Emission (byproduct)

Write `<slug>.kg.json` in the **same directory** as the summary `.md`. Node types owned by this skill:

| Type | Prefix | Required fields |
|---|---|---|
| `Paper` | `paper:` | title, authors[], venue, year, url |
| `Author` | `author:` | name |
| `Venue` | `venue:` | name, year |
| `Claim` | `claim:` | text (author's original wording), paper id |
| `Method` | `method:` | name |
| `Dataset` | `dataset:` | name |
| `Model` | `model:` | name |
| `Metric` | `metric:` | name |
| `Result` | `result:` | metric, value (original number as-is) |

**Edges**:
- `Paper --AUTHORED_BY--> Author`
- `Paper --PUBLISHED_IN--> Venue`
- `Paper --MAKES_CLAIM--> Claim`
- `Paper --USES_METHOD--> Method`
- `Paper --USES_DATASET--> Dataset`
- `Paper --USES_MODEL--> Model`
- `Paper --REPORTS_RESULT--> Result`
- `Result --EVIDENCED_BY--> Claim` (meta.polarity ∈ {support, contradict, mixed}; required)

Example IDs: `paper:greedy-coordinate-gradient-2023#local`, `claim:greedy-coordinate-gradient-2023--c1`

Provenance lives on the `KGFile` root as `{source_file, source_sha, extracted_at, author_agent: "paper-summarizer"}`.

## Alias Check Protocol

Before emitting a new **`Method | Dataset | Model | Metric`** node, alias lookup is mandatory:

```bash
python3 .claude/skills/paper-kg/scripts/query.py lookup \
  --type Method --name-fuzzy "Greedy Coordinate Gradient"
```

- Match score ≥85: reuse existing id (do not create a new node)
- Score <85: create new id + record `alias_check: {queried_name, matches: [...], decision: "new"}` on the node
- Bootstrap (DB `nodes < 50`): missing alias_check tolerated (curator softens). From the 3rd run onward it is mandatory.

## Hybrid Query (reference)

While summarizing, to check things like "is there a prior version of this paper?" or "papers that use the same dataset":

```bash
python3 .claude/skills/paper-kg/scripts/hybrid_query.py "GCG variant papers" --k 5
```

Cross-check `kg.matched_nodes` and `rag.chunks` in the returned JSON before deciding alias / duplicate.

## Schema Enforcement

Every `.kg.json` must pass the `KGFile` Pydantic model in `paper-kg/scripts/schema.py`. Validation and upsert are handled by kg-curator; failures are logged to `papers/vector_db/rejected.jsonl` and re-dispatched by the orchestrator. For details see `.claude/skills/paper-kg/SKILL.md`.

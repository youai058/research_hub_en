---
name: paper-triage
description: Paper relevance filtering. Claude scores each raw.md abstract 0–5 against the topic (LLM-native, no external API). Scores are runtime only — raw.md frontmatter is untouched, each run is independent. Narrows the summarizer input queue to reduce wasted Gemini digests. Side effect: appends topic history to research/topics/<slug>.md. Triggers 'paper triage', 'relevance triage', 'relevance filter', 'abstract scoring'.
---

# Paper Triage Skill

Scores the `raw.md` pool collected by paper-hunter against the current research topic and narrows it down to the subset passed on to `paper-summarize`. Scores are **runtime only**. Raw.md files are untouched, and each run is independent. This is the orchestrator's Phase A-2 (paper-triage) step, between A-1 (paper-hunter) and A-3 (paper-summarizer).

## Philosophy

- **Claude-native**: no external judge (Gemini/OpenAI) calls. The agent reads abstracts directly and scores via its own reasoning.
- **Stateless**: no triage_status field, no manifest, no hash.
- **Non-destructive**: raw.md is not touched.
- **Summarizer-agnostic**: the summarizer has no gate — it processes whatever path it is dispatched with. Filtering is the orchestrator's responsibility.
- **Log-but-don't-load**: `--topic "..."` is canonical per run. History is appended separately to `research/topics/<slug>.md`. Reuse via `--topic-from <slug>`.

## Invocation examples

```bash
# 1) Dense-retrieval pre-filter (1491 → ≤300)
python3 .claude/skills/paper-triage/scripts/retrieve.py \
    --topic-spec research/topics/<slug>.topic.json \
    > /tmp/triage_candidates.json

# 2) Agent reads /tmp/triage_candidates.json, scores each with rubric 0-5
#    → emit accepted paths (≥ threshold 3.0) to stdout, one per line
#    → topic_log.py append updates research/topics/<slug>.md
```

Precondition: `abstracts` ChromaDB collection populated by A-1.5 `abstract-indexer`.

## Workflow (agent responsibilities)

### Step 1 — Fix the topic

Priority (exactly one of):
1. `--topic-spec <path>` given → `topic.json` path. Must pass `topic_spec.py validate <path>`. Extract `refined_topic` + `triage_context` as the canonical topic (this mode **takes precedence** over the flat-string mode).
2. `--topic-from <slug>` given → load text via `python3 topic_log.py load <slug>`.
3. `--topic "<string>"` given → use as-is.
4. None of the above → exit 2.

`--topic-spec` and `--topic`/`--topic-from` are **mutually exclusive**.

The agent computes the slug alongside the topic text:

```bash
# --topic-spec mode:
python3 .claude/skills/topic-refine/scripts/topic_spec.py get <path> refined_topic
# slug is parsed from the spec filename:
slug=$(basename <path> .topic.json)

# --topic or --topic-from mode:
python3 .claude/skills/paper-triage/scripts/topic_log.py slug --topic "<string>"
# → example: lldm-late-step-<8hex>
```

### Step 2 — Dense-retrieval pre-filter

The agent calls `retrieve.py` to pull topic-relevant candidates from the ChromaDB `abstracts` collection. The full corpus is not bundled as JSON.

```bash
python3 .claude/skills/paper-triage/scripts/retrieve.py \
    --topic-spec <path-to-topic.json> \
    --k-cap 300 \
    --cosine-threshold 0.5
```

stdout JSON array: `[{path, slug, title, abstract, venue, year, venue_class, published, categories, cos_score, signal_hit}, ...]`

Filter details:
- If any `triage_context.exclude` term appears (substring) in title+abstract (lowercased) → **hard veto** (drop)
- If any `triage_context.signal_methods` entry matches, add a cosine **+0.05 boost** (`signal_hit: true`)
- Only emit hits with final `cosine >= --cosine-threshold`
- `--k-cap` ceiling (default 300)

The agent reads this stdout JSON and passes it into Step 3 scoring. `collect_abstracts.py` is no longer on the default path; it is retained only for ad-hoc use.

**Precondition**: the `abstracts` collection must be populated. Because A-1.5 abstract-indexer runs immediately before, the `/research-papers` path is always covered. In ad-hoc invocations, if the collection is empty, retrieve.py emits exit 5 + a "run A-1.5 first" hint.

### Step 3 — Claude-native scoring

The agent iterates the JSON array and assigns **each entry** a 0–5 score against the topic plus a one-line reason. **Process every input — no skipping, no hallucination**.

**Rubric** (apply strictly):

- **5** — Directly overlaps the topic's core contribution. Methods, datasets, and experimental setup all match.
- **4** — Directly connected to the methods / datasets / models the topic uses. A core reference.
- **3** — Same subfield, indirect relation. Useful background.
- **2** — Peripheral. Reference-worthy but not core.
- **1** — Unrelated topic. Surface keyword overlap only.
- **0** — Off-topic / noise. Overlaps with out-of-scope.

Scoring criteria:
- **Read the entire abstract**. Do not decide from title / venue alone.
- When in doubt, err **lower**. If the direction differs from the topic and only keywords overlap, cap at 2.
- If the topic text explicitly lists an "out of scope" item, papers matching it are immediately 0–1.

**`--topic-spec` mode extra rules** (when structured `triage_context` is given):

- `core_question`: primary judgment is whether you can say "yes, this paper answers it". Yes → ≥3, No → ≤2.
- `include`: each entry is a positive signal. A match sets baseline 3.
- `exclude`: each entry is a hard veto. On match **force 0–1**. If the abstract shows grounds for exclusion, other include signals are ignored. Choice of 0 vs 1 follows the original rubric (0 = noise/off-topic, 1 = surface keyword overlap only).
- `signal_methods`: method name mentioned in the abstract gives **+1 bonus** (null and void if core_question fails). Stackable with the `include` baseline 3; final score clamped at 5.

In `--topic` / `--topic-from` mode (string topic) apply only the rubric; the structured rules above are ignored.

**`signal_hit` hint**: the `signal_hit: true` tag set by retrieve.py is an **advisory**, not an automatic bonus. Rubric judgment is done by the agent after reading the full abstract. If `signal_hit: true` but off-topic, score low as usual.

### Step 4 — Filtering

- `--threshold F` (default **3.0**): accept only entries with score ≥ F. 3.0 is the default gate that passes the rubric's "same subfield, indirect relation" tier and above.
- `--top-n N`: top N by descending score (mutually exclusive with threshold)
- On ties, newer `published` wins.

### Step 5 — Output

Default format `paths`: one accepted path (project-relative) per line to stdout.
```
papers/metadata/etc/2026/foo.raw.md
papers/metadata/etc/2026/bar.raw.md
```

`--format json`: `[{path, score, reason}]` (for orchestrator parsing).
`--format table`: sorted table for human review (with stats on stderr).

### Step 6 — Append history

After finalizing the result, the agent runs:
```bash
python3 .claude/skills/paper-triage/scripts/topic_log.py append \
    --slug <slug> --topic "<string>" \
    --stats-json '{"scanned":N,"accepted":M,"threshold":3.0,"accepted_slugs":["slug1",...]}'
```
→ Creates `research/topics/<slug>.md` or appends a `## Runs` bullet to an existing file. If `--no-save-topic` is set, skip this step.

### Step 7 — Return to orchestrator

The orchestrator captures the list of accepted paths on stdout and passes each to `paper-summarize`. Scores are discarded at this boundary.

## Topic file format (`research/topics/<slug>.md`)

```markdown
---
slug: lldm-late-step-abcd1234
created_at: 2026-04-15T15:30:00+09:00
last_run_at: 2026-04-15T15:30:00+09:00
run_count: 1
---

# Topic
<raw topic text as-is>

## Runs
- 2026-04-15T15:30:00+09:00 — scanned 130, accepted 18 (threshold 3.0) [foo, bar, ...]
```

Append-only: if the file exists, update `last_run_at` / `run_count` and add a bullet under `## Runs`. If the user deletes it manually, the next run creates it anew with `run_count=1`.

## Checklist

- [ ] Exactly one of `--topic-spec` / `--topic` / `--topic-from`
- [ ] For `--topic-spec`, `topic_spec.py validate` passes upfront
- [ ] `retrieve.py` exits 0 with JSON parsed successfully
- [ ] `abstracts` collection is non-empty (not exit 5)
- [ ] Every input paper scored (zero omissions)
- [ ] Threshold / top-n filter applied; ties broken by newest `published`
- [ ] Every output path maps to a real file
- [ ] raw.md **untouched** (scores are not written to frontmatter)
- [ ] `topic_log.py append` called (unless `--no-save-topic`)
- [ ] Timestamps in KST ISO8601

## Failure handling

- Two or more of `--topic-spec` / `--topic` / `--topic-from` at once, or none of them → exit 2
- `--topic-spec` path fails `topic_spec.py validate` → exit 2 (propagate spec error)
- `collect_abstracts.py` failure → propagate error, abort triage
- JSON parse failure → report as a script bug, abort
- Length mismatch during scoring → wrong behavior, rerun required
- `topic_log.py append` failure is **not fatal** → warn only; accepted paths still emitted normally

## Lessons

Before starting, Read `docs/lessons.md` + `docs/lessons-paper.md`.

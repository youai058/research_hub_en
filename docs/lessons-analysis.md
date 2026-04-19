---
domain: analysis
updated: 2026-04-15
covers: [results-analyst]
---

# Lessons — Analysis (results)

results-analyst MUST Read this file before starting work. Append-only.

Phase C-2 domain: claim-result gap interpretation, 4-way failure classification, statistical tests, HTML reports.

## How to add

`/research-lesson analysis "<rule title>"`

---

<!-- append entries below this line -->

## 2026-04-15 — 4-way failure classification required
- **Rule**: for every failed experiment row, results-analyst classifies the cause as one of claim / impl / setup / data and records the classification with evidence in `diagnoses/<slug>.md`
- **Why**: without classification, the next loop's answer-formulator cannot decide whether to rewrite or discard an Evidence, and the same failure repeats
- **When to apply**: at the end of Phase C-2 — if even one failure is unclassified, block at the gate

## 2026-04-15 — Self-contained HTML report
- **Rule**: the HTML report must NOT reference external CSS/JS; use inline `<style>` / `<script>` and embed images as base64 data URLs
- **Why**: relative paths break when shared, and the report must render identically months later after archiving for the diagnosis to be reproducible
- **When to apply**: when results-analyst generates `results_<slug>/report.html`

## 2026-04-15 — Claim-result gap table required
- **Rule**: every analysis report must include an "author claim vs our result" table, with columns: metric, claimed value, observed value, delta, 4-way classification
- **Why**: without visualizing the gap as a table, some metrics get implicitly dropped in narrative text
- **When to apply**: at the Phase C-2 report rendering step — reject any report that lacks this table

## 2026-04-15 — PNG + HTML dual output
- **Rule**: key comparison plots generate BOTH a PNG (for individual sharing) and a base64-embedded copy inside the HTML report (for the integrated view)
- **Why**: PNG only scatters the narrative; HTML only makes it hard to drop into Slack or a paper
- **When to apply**: as the standard convention for analysis-script output steps

<!-- seeded 2026-04-15 -->

## 2026-04-15 — The force-rule dimension is a confound independent of step-index
- **Rule**: when reporting force-commit ablations, separate the `force_rule` dimension (argmax / sampled / prophet-thresh) onto its own axis. Results can be opposite at the same `t*` depending on the rule.
- **Why**: at diffusion-llm-step iter1 GSM8K n=50, `t*=0.5T` with argmax was −24pt drop while prophet@0.9 was +2pt. The PLAN H1 prediction "≤2pt drop" applies only to the prophet-style rule; argmax is a separate mechanism.
- **When to apply**: when writing any force-commit or early-commit ablation report — if the rule is not surfaced as a table axis, the mechanism conclusion flips.

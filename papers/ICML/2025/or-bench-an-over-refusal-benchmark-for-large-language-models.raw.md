---
title: "OR-Bench: An Over-Refusal Benchmark for Large Language Models"
authors: ["Justin Cui", "Wei-Lin Chiang", "Ion Stoica", "Cho-Jui Hsieh"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "CdFnEu0JZV"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/6635c4038a6f3169ac9d29e8e0eaa0aad64bf06c.pdf"
published: "2025"
categories: []
keywords: ["safety", "llm", "over-refusal"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:23+09:00"
---

# OR-Bench: An Over-Refusal Benchmark for Large Language Models

## Abstract
Large Language Models (LLMs) require careful safety alignment to prevent malicious outputs. While significant research focuses on mitigating harmful content generation, 
the enhanced safety often come with the side effect of over-refusal, where LLMs may reject innocuous prompts and become less helpful.
Although the issue of over-refusal has been empirically observed, a systematic measurement is challenging 
due to the difficulty of crafting prompts that can elicit the over-refusal behaviors of LLMs.
This study proposes a novel method for automatically generating large-scale over-refusal datasets. Leveraging this technique, we introduce OR-Bench, the first large-scale over-refusal benchmark. OR-Bench comprises 80,000 over-refusal prompts across 10 common rejection categories, a subset of around 1,000 hard prompts that are challenging even for state-of-the-art LLMs, and an additional 600 toxic prompts to prevent indiscriminate responses.
We then conduct a comprehensive study to measure the over-refusal of 32 popular LLMs across 8 model families. Our datasets are publicly available at https://huggingface.co/bench-llms and our codebase is open-sourced at https://github.com/justincui03/or-bench.
 We hope this benchmark can help the community develop better safety aligned models.

## Metadata
- venue: ICML
- year: 2025
- authors: Justin Cui, Wei-Lin Chiang, Ion Stoica, Cho-Jui Hsieh
- arxiv_id: 
- openreview_id: CdFnEu0JZV
- anthology_id: 
- pdf_url: https://openreview.net/pdf/6635c4038a6f3169ac9d29e8e0eaa0aad64bf06c.pdf
- published: 2025
- keywords: safety, llm, over-refusal

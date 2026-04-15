---
title: "Thinking Out of Order: When Output Order Stops Reflecting Reasoning Order in Diffusion Language Models"
authors: ["Longxuan Yu", "Yu Fu", "Shaorong Zhang", "Hui Liu", "Mukund Varma T", "Greg Ver Steeg", "Yue Dong"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2601.22035"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2601.22035v1"
published: "2026-01-29"
categories: ["cs.CL", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:21+09:00"
---

# Thinking Out of Order: When Output Order Stops Reflecting Reasoning Order in Diffusion Language Models

## Abstract
Autoregressive (AR) language models enforce a fixed left-to-right generation order, creating a fundamental limitation when the required output structure conflicts with natural reasoning (e.g., producing answers before explanations due to presentation or schema constraints). In such cases, AR models must commit to answers before generating intermediate reasoning, and this rigid constraint forces premature commitment. Masked diffusion language models (MDLMs), which iteratively refine all tokens in parallel, offer a way to decouple computation order from output structure. We validate this capability on GSM8K, Math500, and ReasonOrderQA, a benchmark we introduce with controlled difficulty and order-level evaluation. When prompts request answers before reasoning, AR models exhibit large accuracy gaps compared to standard chain-of-thought ordering (up to 67% relative drop), while MDLMs remain stable ($\leq$14% relative drop), a property we term "order robustness". Using ReasonOrderQA, we present evidence that MDLMs achieve order robustness by stabilizing simpler tokens (e.g., reasoning steps) earlier in the diffusion process than complex ones (e.g., final answers), enabling reasoning tokens to stabilize before answer commitment. Finally, we identify failure conditions where this advantage weakens, outlining the limits required for order robustness.

## Metadata
- venue: arXiv
- year: 2026
- authors: Longxuan Yu, Yu Fu, Shaorong Zhang, Hui Liu, Mukund Varma T, Greg Ver Steeg, Yue Dong
- arxiv_id: 2601.22035
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2601.22035v1
- published: 2026-01-29

---
title: "Locally Coherent Parallel Decoding in Diffusion Language Models"
authors: ["Michael Hersche", "Nicolas Menet", "Ronan Tanios", "Abbas Rahimi"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.20216"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.20216v1"
published: "2026-03-03"
categories: ["cs.CL", "cs.AI", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:13:58+09:00"
---

# Locally Coherent Parallel Decoding in Diffusion Language Models

## Abstract
Diffusion language models (DLMs) have emerged as a promising alternative to autoregressive (AR) models, offering sub-linear generation latency and bidirectional capabilities that are particularly appealing for code generation and editing. Achieving sub-linear latency in discrete DLMs requires predicting multiple tokens in parallel. However, standard DLMs sample tokens independently from conditional marginal distributions, failing to capture the joint dependencies among concurrently generated tokens. As a result, they often lead to syntactic inconsistencies and break multi-token structures. In this work, we introduce CoDiLA (Coherent Diffusion with Local Autoregression), a method that reconciles parallel sampling with local dependency modeling. Rather than forcing the DLM to resolve fine-grained syntax, CoDiLA delegates local decoding to a small, auxiliary AR model operating on the diffusion latents. This design allows for parallel block generation while ensuring sequential validity within each block and maintaining core DLM capabilities, including bidirectional modeling across blocks. We demonstrate that using a highly compact auxiliary AR model (e.g., 0.6B parameters) effectively eliminates coherence artifacts, establishing a new Pareto frontier for accuracy and speed in code generation benchmarks.

## Metadata
- venue: arXiv
- year: 2026
- authors: Michael Hersche, Nicolas Menet, Ronan Tanios, Abbas Rahimi
- arxiv_id: 2603.20216
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.20216v1
- published: 2026-03-03

---
title: "Physics of Language Models: Part 3.3, Knowledge Capacity Scaling Laws"
authors: ["Zeyuan Allen-Zhu", "Yuanzhi Li"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "FxNNiUgtfa"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/7a9985d2cec78e1746e3dc81372bed15021471b0.pdf"
published: "2025"
categories: []
keywords: ["scaling laws", "knowledge capacity", "language models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:16+09:00"
---

# Physics of Language Models: Part 3.3, Knowledge Capacity Scaling Laws

## Abstract
Scaling laws describe the relationship between the size of language models and their capabilities. Unlike prior studies that evaluate a model's capability via loss or benchmarks, we estimate information-theoretically the number of knowledge \emph{bits} a model stores. We focus on factual knowledge represented as tuples, such as (USA, capital, Washington D.C.) from a Wikipedia page. Through multiple controlled datasets, we establish that language models can and only can store \emph{2 bits of knowledge per parameter, even when quantized to int8}, and such knowledge can be flexibly extracted for downstream applications. 

More broadly, we present 12 results on how (1) training duration, (2) model architecture, (3) quantization, (4) sparsity constraints such as MoE, and (5) data signal-to-noise ratio affect a model's knowledge storage capacity.

## Metadata
- venue: ICLR
- year: 2025
- authors: Zeyuan Allen-Zhu, Yuanzhi Li
- arxiv_id: 
- openreview_id: FxNNiUgtfa
- anthology_id: 
- pdf_url: https://openreview.net/pdf/7a9985d2cec78e1746e3dc81372bed15021471b0.pdf
- published: 2025
- keywords: scaling laws, knowledge capacity, language models

---
title: "Attention Sinks and Compression Valleys in LLMs are Two Sides of the Same Coin"
authors: ["Enrique Queipo-de-Llano", "Alvaro Arroyo", "Federico Barbero", "Xiaowen Dong", "Michael M. Bronstein", "Yann LeCun", "Ravid Shwartz-Ziv"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "c5TFhCJ6fs"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b5b6b7454024147aa3702d4c6eb23569cbddf34f.pdf"
published: "2026"
categories: []
keywords: ["attention sinks", "compression valleys", "deep trasformer-based LLMs"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:51+09:00"
---

# Attention Sinks and Compression Valleys in LLMs are Two Sides of the Same Coin

## Abstract
Attention sinks and compression valleys have attracted significant attention as two puzzling phenomena in large language models, but have been studied in isolation. In this work, we present a surprising connection between attention sinks and compression valleys, tracing both to the formation of massive activations in the residual stream. We prove theoretically that massive activations necessarily produce representational compression and establish bounds on the resulting entropy reduction. Through experiments across several models (410M--120B parameters), we confirm that when the beginning-of-sequence token develops extreme activation norms in the middle layers, both compression valleys and attention sinks emerge simultaneously. Targeted ablation validates our theoretical predictions. This unified view motivates us to propose the Mix-Compress-Refine theory of information flow, as an attempt to explain how LLMs organize their computation in depth by controlling attention and representational compression via massive activations. Specifically, we posit that Transformer-based LLMs process tokens in three distinct phases: (1) broad mixing in the early layers, (2) compressed computation with limited mixing in the middle layers, and (3) selective refinement in the late layers. Our framework helps explain why embedding tasks perform best at intermediate layers, whereas generation tasks benefit from full-depth processing, clarifying differences in task-dependent representations.

## Metadata
- venue: ICLR
- year: 2026
- authors: Enrique Queipo-de-Llano, Alvaro Arroyo, Federico Barbero, Xiaowen Dong, Michael M. Bronstein, Yann LeCun, Ravid Shwartz-Ziv
- arxiv_id: 
- openreview_id: c5TFhCJ6fs
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b5b6b7454024147aa3702d4c6eb23569cbddf34f.pdf
- published: 2026
- keywords: attention sinks, compression valleys, deep trasformer-based LLMs

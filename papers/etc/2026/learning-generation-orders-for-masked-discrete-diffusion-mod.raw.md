---
title: "Learning Generation Orders for Masked Discrete Diffusion Models via Variational Inference"
authors: ["David Fox", "Sam Bowyer", "Song Liu", "Laurence Aitchison", "Raul Santos-Rodriguez", "Mengyue Yang"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.23968"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.23968v1"
published: "2026-02-27"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:28+09:00"
---

# Learning Generation Orders for Masked Discrete Diffusion Models via Variational Inference

## Abstract
Masked discrete diffusion models (MDMs) are a promising new approach to generative modelling, offering the ability for parallel token generation and therefore greater efficiency than autoregressive counterparts. However, achieving an optimal balance between parallel generation and sample quality remains an open problem. Current approaches primarily address this issue through fixed, heuristic parallel sampling methods. There exist some recent learning based approaches to this problem, but its formulation from the perspective of variational inference remains underexplored. In this work, we propose a variational inference framework for learning parallel generation orders for MDMs. As part of our method, we propose a parameterisation for the approximate posterior of generation orders which facilitates parallelism and efficient sampling during training. Using this method, we conduct preliminary experiments on the GSM8K dataset, where our method performs competitively against heuristic sampling strategies in the regime of highly parallel generation. For example, our method achieves 33.1\% accuracy with an average of only only 4 generation steps, compared to 23.7-29.0\% accuracy achieved by standard competitor methods in the same number of steps. We believe further experiments and analysis of the method will yield valuable insights into the problem of parallel generation with MDMs.

## Metadata
- venue: arXiv
- year: 2026
- authors: David Fox, Sam Bowyer, Song Liu, Laurence Aitchison, Raul Santos-Rodriguez, Mengyue Yang
- arxiv_id: 2602.23968
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.23968v1
- published: 2026-02-27

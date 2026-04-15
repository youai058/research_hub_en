---
title: "On Powerful Ways to Generate: Autoregression, Diffusion, and Beyond"
authors: ["Chenxiao Yang", "Cai Zhou", "David Wipf", "Zhiyuan Li"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.06190"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.06190v2"
published: "2025-10-07"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:10+09:00"
---

# On Powerful Ways to Generate: Autoregression, Diffusion, and Beyond

## Abstract
Diffusion language models have recently emerged as a competitive alternative to autoregressive language models. Beyond next-token generation, they are more efficient and flexible by enabling parallel and any-order token generation. However, despite empirical successes, their computational power and fundamental limitations remain poorly understood. In this paper, we formally study whether non-autoregressive generation in Masked Diffusion Models (MDM) enables solving problems beyond the reach of Auto-Regressive Models (ARM). Our results show that MDM with sufficiently large context length is computationally universal with decoding steps matching the optimal parallel time complexity in PRAM. However, when controlling for other factors, MDM's flexibility to generate in any-order does not expand what ARM can already solve. To address this, we propose a new form of generation called any-process generation, which extends MDM with capabilities to remask, insert and delete tokens, allowing self-correction, length-variable editing, and adaptive parallelism. Theoretically and empirically, we demonstrate these capabilities enable scalability to significantly harder reasoning problems that are otherwise intractable for ARM and vanilla MDM. Additionally, they prove essential for generation tasks where objects naturally evolve through non-sequential processes, crucial for extending current LLMs beyond natural language to domains such as coding and science.

## Metadata
- venue: arXiv
- year: 2025
- authors: Chenxiao Yang, Cai Zhou, David Wipf, Zhiyuan Li
- arxiv_id: 2510.06190
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.06190v2
- published: 2025-10-07

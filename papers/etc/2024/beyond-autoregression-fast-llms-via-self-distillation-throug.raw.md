---
title: "Beyond Autoregression: Fast LLMs via Self-Distillation Through Time"
authors: ["Justin Deschenaux", "Caglar Gulcehre"]
venue: "arXiv"
year: 2024
venue_class: "etc"
arxiv_id: "2410.21035"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2410.21035v2"
published: "2024-10-28"
categories: ["cs.LG", "cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:20:02+09:00"
---

# Beyond Autoregression: Fast LLMs via Self-Distillation Through Time

## Abstract
Autoregressive (AR) Large Language Models (LLMs) have demonstrated significant success across numerous tasks. However, the AR modeling paradigm presents certain limitations; for instance, contemporary autoregressive LLMs are trained to generate one token at a time, which can result in noticeable latency. Recent advances have indicated that search and repeated sampling can enhance performance in various applications, such as theorem proving, code generation, and alignment, by utilizing greater computational resources during inference. In this study, we demonstrate that diffusion language models are capable of generating at least 32 tokens simultaneously, while exceeding the performance of AR models in text quality and on the LAMBADA natural language understanding benchmark. This outcome is achieved through a novel distillation method for discrete diffusion models, which reduces the number of inference steps by a factor of 32-64. Practically, at the 1.3B parameters scale, diffusion models, even without caching, can generate tokens at a rate that is up to 8 times faster than AR models employing KV-caching, and we anticipate further improvements with the inclusion of caching. Moreover, we demonstrate the efficacy of our approach for diffusion language models with up to 860M parameters.

## Metadata
- venue: arXiv
- year: 2024
- authors: Justin Deschenaux, Caglar Gulcehre
- arxiv_id: 2410.21035
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2410.21035v2
- published: 2024-10-28

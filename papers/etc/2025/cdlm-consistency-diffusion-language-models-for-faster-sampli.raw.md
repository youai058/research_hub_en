---
title: "CDLM: Consistency Diffusion Language Models For Faster Sampling"
authors: ["Minseo Kim", "Chenfeng Xu", "Coleman Hooper", "Harman Singh", "Ben Athiwaratkun", "Ce Zhang", "Kurt Keutzer", "Amir Gholami"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2511.19269"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2511.19269v2"
published: "2025-11-24"
categories: ["cs.LG", "cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:06+09:00"
---

# CDLM: Consistency Diffusion Language Models For Faster Sampling

## Abstract
Diffusion Language Models (DLMs) offer a promising parallel generation paradigm but suffer from slow inference due to numerous refinement steps and the inability to use standard KV caching. We introduce CDLM (Consistency Diffusion Language Models), a training-based acceleration method that simultaneously tackles both bottlenecks. CDLM integrates consistency modeling to drastically reduce the number of required sampling steps by enabling multi-token finalization. Furthermore, we enforce a block-wise causal attention mask during fine-tuning, making the model fully compatible with KV caching. Experiments show CDLM achieves 3.6x-14.5x lower latency while maintaining competitive accuracy on math and coding tasks. The full training and evaluation code is available at https://github.com/SqueezeAILab/CDLM.

## Metadata
- venue: arXiv
- year: 2025
- authors: Minseo Kim, Chenfeng Xu, Coleman Hooper, Harman Singh, Ben Athiwaratkun, Ce Zhang, Kurt Keutzer, Amir Gholami
- arxiv_id: 2511.19269
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2511.19269v2
- published: 2025-11-24

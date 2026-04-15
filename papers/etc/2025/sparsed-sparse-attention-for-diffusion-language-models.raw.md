---
title: "SparseD: Sparse Attention for Diffusion Language Models"
authors: ["Zeqing Wang", "Gongfan Fang", "Xinyin Ma", "Xingyi Yang", "Xinchao Wang"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2509.24014"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2509.24014v1"
published: "2025-09-28"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:14+09:00"
---

# SparseD: Sparse Attention for Diffusion Language Models

## Abstract
While diffusion language models (DLMs) offer a promising alternative to autoregressive models (ARs), existing open-source DLMs suffer from high inference latency. This bottleneck is mainly due to the attention's quadratic complexity with respect to context length in computing all query-key pairs. Intuitively, to reduce this complexity, a natural strategy is to restrict attention to sparse patterns that retain only the most relevant connections. Such approaches are well-established in ARs, where attention follows fixed and clearly defined sparse patterns. However, in DLMs, we observe distinct sparsity behaviors: (1) attention patterns vary across heads, (2) attention patterns in each head remain highly similar across denoising steps, and (3) early denoising steps are critical for generation. These findings render sparse attention methods designed for ARs largely incompatible with DLMs, as they fail to capture head-specific structures and risk degrading generation when applied in early denoising steps. To address these challenges, we propose SparseD, a novel sparse attention method for DLMs. Leveraging the observations, SparseD only requires pre-computing head-specific sparse patterns one time, and reuses them across all steps. This prevents recomputing sparse patterns at each denoising step. Meanwhile, SparseD uses full attention in the early steps, then switches to sparse attention later to maintain generation quality. Together, these establish SparseD as a practical and efficient solution for deploying DLMs in long-context applications. Experimental results demonstrate that SparseD achieves lossless acceleration, delivering up to $1.50\times$ speedup over FlashAttention at a 64k context length with 1,024 denoising steps.

## Metadata
- venue: arXiv
- year: 2025
- authors: Zeqing Wang, Gongfan Fang, Xinyin Ma, Xingyi Yang, Xinchao Wang
- arxiv_id: 2509.24014
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2509.24014v1
- published: 2025-09-28

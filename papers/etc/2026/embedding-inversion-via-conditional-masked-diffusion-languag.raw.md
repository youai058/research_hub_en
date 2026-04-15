---
title: "Embedding Inversion via Conditional Masked Diffusion Language Models"
authors: ["Han Xiao"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.11047"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.11047v3"
published: "2026-02-11"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:05+09:00"
---

# Embedding Inversion via Conditional Masked Diffusion Language Models

## Abstract
We frame embedding inversion as conditional masked diffusion, recovering all tokens in parallel through iterative denoising rather than sequential autoregressive generation. A masked diffusion language model is conditioned on the target embedding via adaptive layer normalization, requiring only 8 forward passes with no access to the target encoder at inference time. On 32-token sequences across three embedding models, the method achieves token recovery through parallel denoising without requiring encoder access, iterative correction, or architecture-specific alignment. Source code and live demo are available at https://github.com/jina-ai/embedding-inversion-demo.

## Metadata
- venue: arXiv
- year: 2026
- authors: Han Xiao
- arxiv_id: 2602.11047
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.11047v3
- published: 2026-02-11

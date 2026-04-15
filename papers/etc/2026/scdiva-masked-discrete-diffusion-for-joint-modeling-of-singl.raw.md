---
title: "ScDiVa: Masked Discrete Diffusion for Joint Modeling of Single-Cell Identity and Expression"
authors: ["Mingxuan Wang", "Cheng Chen", "Gaoyang Jiang", "Zijia Ren", "Chuangxin Zhao", "Lu Shi", "Yanbiao Ma"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.03477"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.03477v1"
published: "2026-02-03"
categories: ["cs.LG", "cs.AI", "q-bio.GN"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:36+09:00"
---

# ScDiVa: Masked Discrete Diffusion for Joint Modeling of Single-Cell Identity and Expression

## Abstract
Single-cell RNA-seq profiles are high-dimensional, sparse, and unordered, causing autoregressive generation to impose an artificial ordering bias and suffer from error accumulation. To address this, we propose scDiVa, a masked discrete diffusion foundation model that aligns generation with the dropout-like corruption process by defining a continuous-time forward masking mechanism in token space. ScDiVa features a bidirectional denoiser that jointly models discrete gene identities and continuous values, utilizing entropy-normalized serialization and a latent anchor token to maximize information efficiency and preserve global cell identity. The model is trained via depth-invariant time sampling and a dual denoising objective to simulate varying sparsity levels while ensuring precise recovery of both identity and magnitude. Pre-trained on 59 million cells, scDiVa achieves strong transfer performance across major benchmarks, including batch integration, cell type annotation, and perturbation response prediction. These results suggest that masked discrete diffusion serves as a biologically coherent and effective alternative to autoregression.

## Metadata
- venue: arXiv
- year: 2026
- authors: Mingxuan Wang, Cheng Chen, Gaoyang Jiang, Zijia Ren, Chuangxin Zhao, Lu Shi, Yanbiao Ma
- arxiv_id: 2602.03477
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.03477v1
- published: 2026-02-03

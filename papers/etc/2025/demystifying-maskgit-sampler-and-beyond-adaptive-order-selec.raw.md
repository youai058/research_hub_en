---
title: "Demystifying MaskGIT Sampler and Beyond: Adaptive Order Selection in Masked Diffusion"
authors: ["Satoshi Hayakawa", "Yuhta Takida", "Masaaki Imaizumi", "Hiromi Wakaki", "Yuki Mitsufuji"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.04525"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.04525v2"
published: "2025-10-06"
categories: ["cs.LG", "math.PR", "stat.ML"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:26+09:00"
---

# Demystifying MaskGIT Sampler and Beyond: Adaptive Order Selection in Masked Diffusion

## Abstract
Masked diffusion models have shown promising performance in generating high-quality samples in a wide range of domains, but accelerating their sampling process remains relatively underexplored. To investigate efficient samplers for masked diffusion, this paper theoretically analyzes the MaskGIT sampler for image modeling, revealing its implicit temperature sampling mechanism. Through this analysis, we introduce the "moment sampler," an asymptotically equivalent but more tractable and interpretable alternative to MaskGIT, which employs a "choose-then-sample" approach by selecting unmasking positions before sampling tokens. In addition, we improve the efficiency of choose-then-sample algorithms through two key innovations: a partial caching technique for transformers that approximates longer sampling trajectories without proportional computational cost, and a hybrid approach formalizing the exploration-exploitation trade-off in adaptive unmasking. Experiments in image and text domains demonstrate our theory as well as the efficiency of our proposed methods, advancing both theoretical understanding and practical implementation of masked diffusion samplers.

## Metadata
- venue: arXiv
- year: 2025
- authors: Satoshi Hayakawa, Yuhta Takida, Masaaki Imaizumi, Hiromi Wakaki, Yuki Mitsufuji
- arxiv_id: 2510.04525
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.04525v2
- published: 2025-10-06

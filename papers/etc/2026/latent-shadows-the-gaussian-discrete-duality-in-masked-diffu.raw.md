---
title: "Latent Shadows: The Gaussian-Discrete Duality in Masked Diffusion"
authors: ["Guinan Chen", "Xunpeng Huang", "Ying Sun", "Shijin Wang", "Yanyong Zhang", "Chao Wang"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.00792"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.00792v1"
published: "2026-01-31"
categories: ["cs.LG", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:17+09:00"
---

# Latent Shadows: The Gaussian-Discrete Duality in Masked Diffusion

## Abstract
Masked discrete diffusion is a dominant paradigm for high-quality language modeling where tokens are iteratively corrupted to a mask state, yet its inference efficiency is bottlenecked by the lack of deterministic sampling tools. While diffusion duality enables deterministic distillation for uniform models, these approaches generally underperform masked models and rely on complex integral operators. Conversely, in the masked domain, prior methods typically assume the absence of deterministic trajectories, forcing a reliance on stochastic distillation. To bridge this gap, we establish explicit Masked Diffusion Duality, proving that the masked process arises as the projection of a continuous Gaussian process via a novel maximum-value index preservation mechanism. Furthermore, we introduce Masked Consistency Distillation (MCD), a principled framework that leverages this duality to analytically construct the deterministic coupled trajectories required for consistency distillation, bypassing numerical ODE solvers. This result strictly improves upon prior stochastic distillation methods, achieving a 16$\times$ inference speedup without compromising generation quality. Our findings not only provide a solid theoretical foundation connecting masked and continuous diffusion, but also unlock the full potential of consistency distillation for high-performance discrete generation. Our code is available at https://anonymous.4open.science/r/MCD-70FD.

## Metadata
- venue: arXiv
- year: 2026
- authors: Guinan Chen, Xunpeng Huang, Ying Sun, Shijin Wang, Yanyong Zhang, Chao Wang
- arxiv_id: 2602.00792
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.00792v1
- published: 2026-01-31

---
title: "TABES: Trajectory-Aware Backward-on-Entropy Steering for Masked Diffusion Models"
authors: ["Shreshth Saini", "Avinab Saha", "Balu Adsumilli", "Neil Birkbeck", "Yilin Wang", "Alan C. Bovik"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.00250"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.00250v2"
published: "2026-01-30"
categories: ["cs.LG", "cs.AI", "cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:17+09:00"
---

# TABES: Trajectory-Aware Backward-on-Entropy Steering for Masked Diffusion Models

## Abstract
Masked Diffusion Models (MDMs) have emerged as a promising non-autoregressive paradigm for generative tasks, offering parallel decoding and bidirectional context utilization. However, current sampling methods rely on simple confidence-based heuristics that ignore the long-term impact of local decisions, leading to trajectory lock-in where early hallucinations cascade into global incoherence. While search-based methods mitigate this, they incur prohibitive computational costs ($O(K)$ forward passes per step). In this work, we propose Backward-on-Entropy (BoE) Steering, a gradient-guided inference framework that approximates infinite-horizon lookahead via a single backward pass. We formally derive the Token Influence Score (TIS) from a first-order expansion of the trajectory cost functional, proving that the gradient of future entropy with respect to input embeddings serves as an optimal control signal for minimizing uncertainty. To ensure scalability, we introduce \texttt{ActiveQueryAttention}, a sparse adjoint primitive that exploits the structure of the masking objective to reduce backward pass complexity. BoE achieves a superior Pareto frontier for inference-time scaling compared to existing unmasking methods, demonstrating that gradient-guided steering offers a mathematically principled and efficient path to robust non-autoregressive generation. We will release the code.

## Metadata
- venue: arXiv
- year: 2026
- authors: Shreshth Saini, Avinab Saha, Balu Adsumilli, Neil Birkbeck, Yilin Wang, Alan C. Bovik
- arxiv_id: 2602.00250
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.00250v2
- published: 2026-01-30

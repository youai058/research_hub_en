---
title: "$\\textit{Jump Your Steps}$: Optimizing Sampling Schedule of Discrete Diffusion Models"
authors: ["Yong-Hyun Park", "Chieh-Hsin Lai", "Satoshi Hayakawa", "Yuhta Takida", "Yuki Mitsufuji"]
venue: "arXiv"
year: 2024
venue_class: "etc"
arxiv_id: "2410.07761"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2410.07761v1"
published: "2024-10-10"
categories: ["cs.LG", "cs.AI", "cs.CL", "cs.CV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:20:09+09:00"
---

# $\textit{Jump Your Steps}$: Optimizing Sampling Schedule of Discrete Diffusion Models

## Abstract
Diffusion models have seen notable success in continuous domains, leading to the development of discrete diffusion models (DDMs) for discrete variables. Despite recent advances, DDMs face the challenge of slow sampling speeds. While parallel sampling methods like $τ$-leaping accelerate this process, they introduce $\textit{Compounding Decoding Error}$ (CDE), where discrepancies arise between the true distribution and the approximation from parallel token generation, leading to degraded sample quality. In this work, we present $\textit{Jump Your Steps}$ (JYS), a novel approach that optimizes the allocation of discrete sampling timesteps by minimizing CDE without extra computational cost. More precisely, we derive a practical upper bound on CDE and propose an efficient algorithm for searching for the optimal sampling schedule. Extensive experiments across image, music, and text generation show that JYS significantly improves sampling quality, establishing it as a versatile framework for enhancing DDM performance for fast sampling.

## Metadata
- venue: arXiv
- year: 2024
- authors: Yong-Hyun Park, Chieh-Hsin Lai, Satoshi Hayakawa, Yuhta Takida, Yuki Mitsufuji
- arxiv_id: 2410.07761
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2410.07761v1
- published: 2024-10-10

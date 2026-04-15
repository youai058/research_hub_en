---
title: "Improving Classifier-Free Guidance in Masked Diffusion: Low-Dim Theoretical Insights with High-Dim Impact"
authors: ["Kevin Rojas", "Ye He", "Chieh-Hsin Lai", "Yuhta Takida", "Yuki Mitsufuji", "Molei Tao"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2507.08965"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2507.08965v2"
published: "2025-07-11"
categories: ["cs.LG", "cs.AI", "stat.ML"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:29+09:00"
---

# Improving Classifier-Free Guidance in Masked Diffusion: Low-Dim Theoretical Insights with High-Dim Impact

## Abstract
Classifier-Free Guidance (CFG) is a widely used technique for conditional generation and improving sample quality in continuous diffusion models, and its extensions to discrete diffusion has recently started to be investigated. In order to improve the algorithms in a principled way, this paper starts by analyzing the exact effect of CFG in the context of a low-dimensional masked diffusion model, with a special emphasis on the guidance schedule. Our analysis shows that high guidance early in sampling (when inputs are heavily masked) harms generation quality, while late-stage guidance improves it. These findings provide a theoretical explanation for empirical observations in recent studies on guidance schedules. The analysis also reveals an imperfection of the current CFG implementations. These implementations can unintentionally cause imbalanced transitions, such as unmasking too rapidly during the early stages of generation, which degrades the quality of the resulting samples. To address this, we draw insight from the analysis and propose a novel classifier-free guidance mechanism. Intuitively, our method smooths the transport between the data distribution and the initial (masked) distribution, resulting in improved sample quality. Remarkably, our method is achievable via a simple one-line code change. Experiments on conditional image and text generation empirically confirm the efficacy of our method.

## Metadata
- venue: arXiv
- year: 2025
- authors: Kevin Rojas, Ye He, Chieh-Hsin Lai, Yuhta Takida, Yuki Mitsufuji, Molei Tao
- arxiv_id: 2507.08965
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2507.08965v2
- published: 2025-07-11

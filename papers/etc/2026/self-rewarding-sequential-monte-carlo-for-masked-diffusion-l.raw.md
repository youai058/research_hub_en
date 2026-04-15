---
title: "Self-Rewarding Sequential Monte Carlo for Masked Diffusion Language Models"
authors: ["Ziwei Luo", "Ziqi Jin", "Lei Wang", "Lidong Bing", "Thomas B. Schön"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.01849"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.01849v1"
published: "2026-02-02"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:05+09:00"
---

# Self-Rewarding Sequential Monte Carlo for Masked Diffusion Language Models

## Abstract
This work presents self-rewarding sequential Monte Carlo (SMC), an inference-time scaling algorithm enabling effective sampling of masked diffusion language models (MDLMs). Our algorithm stems from the observation that most existing MDLMs rely on a confidence-based sampling strategy, where only tokens with the highest prediction confidence are preserved at each step. This restricts the generation to a noise-sensitive, greedy decoding paradigm, resulting in an inevitable collapse in the diversity of possible paths. We address this problem by launching multiple interacting diffusion processes in parallel, referred to as particles, for trajectory exploration. Importantly, we introduce the trajectory-level confidence as a self-rewarding signal for assigning particle importance weights. During sampling, particles are iteratively weighted and resampled to systematically steer generation towards globally confident, high-quality samples. Our self-rewarding SMC is verified on various masked diffusion language models and benchmarks, achieving significant improvement without extra training or reward guidance, while effectively converting parallel inference capacity into improved sampling quality. Our code is available at https://github.com/Algolzw/self-rewarding-smc.

## Metadata
- venue: arXiv
- year: 2026
- authors: Ziwei Luo, Ziqi Jin, Lei Wang, Lidong Bing, Thomas B. Schön
- arxiv_id: 2602.01849
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.01849v1
- published: 2026-02-02

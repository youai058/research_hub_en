---
title: "Advancing Reasoning in Diffusion Language Models with Denoising Process Rewards"
authors: ["Shaoan Xie", "Lingjing Kong", "Xiangchen Song", "Xinshuai Dong", "Guangyi Chen", "Eric P. Xing", "Kun Zhang"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.01544"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.01544v2"
published: "2025-10-02"
categories: ["cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:10+09:00"
---

# Advancing Reasoning in Diffusion Language Models with Denoising Process Rewards

## Abstract
Diffusion-based large language models offer a non-autoregressive alternative for text generation, but enabling them to perform complex reasoning remains challenging. Reinforcement learning has recently emerged as an effective post-training strategy for improving their performance; however, existing methods rely primarily on outcome-based rewards, which provide no direct supervision over the denoising process and often result in poorly structured reasoning that is difficult to interpret and inconsistently supports the final prediction. To address this limitation, we introduce \emph{denoising process reward}, a process-level reinforcement signal defined over the denoising trajectory of diffusion language models. This reward is obtained by estimating the contribution of intermediate denoising intervals to the final task outcome, encouraging the model to favor reasoning trajectories that consistently guide generation toward correct predictions. We further propose an efficient stochastic estimator that reuses standard training rollouts, enabling practical process-level supervision at scale. Experiments on challenging reasoning benchmarks demonstrate that our approach yields consistent improvements in reasoning stability, interpretability, and overall task performance.

## Metadata
- venue: arXiv
- year: 2025
- authors: Shaoan Xie, Lingjing Kong, Xiangchen Song, Xinshuai Dong, Guangyi Chen, Eric P. Xing, Kun Zhang
- arxiv_id: 2510.01544
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.01544v2
- published: 2025-10-02

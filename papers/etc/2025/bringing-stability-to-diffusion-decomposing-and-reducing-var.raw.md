---
title: "Bringing Stability to Diffusion: Decomposing and Reducing Variance of Training Masked Diffusion Models"
authors: ["Mengni Jia", "Mengyu Zhou", "Yihao Liu", "Xiaoxi Jiang", "Guanjun Jiang"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2511.18159"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2511.18159v1"
published: "2025-11-22"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:19+09:00"
---

# Bringing Stability to Diffusion: Decomposing and Reducing Variance of Training Masked Diffusion Models

## Abstract
Masked diffusion models (MDMs) are a promising alternative to autoregressive models (ARMs), but they suffer from inherently much higher training variance. High variance leads to noisier gradient estimates and unstable optimization, so even equally strong pretrained MDMs and ARMs that are competitive at initialization often diverge after task-specific training, with MDMs falling far behind. There has been no theoretical explanation or systematic solution. We derive the first decomposition of MDM training variance into three sources: (A) masking pattern noise, (B) masking rate noise, and (C) data noise, while ARMs are only affected by (C). This explains the fundamental training gap. Building on this foundation, we design six variance-reduction methods, including two core methods: (1) P-POTS, a Pareto-optimal t sampler that minimizes training variance by sampling harder t values more often with appropriately smaller update steps, and (2) MIRROR, which uses negatively correlated samples to reduce (A). Experiments show that compared to standard MDM training, our methods improve accuracy by 7-8% on complex reasoning tasks, while simultaneously reducing run-to-run variability to near ARM levels, substantially narrowing the gap with strong ARM baselines; in most settings, even the best baseline runs remain below the worst run of our method.

## Metadata
- venue: arXiv
- year: 2025
- authors: Mengni Jia, Mengyu Zhou, Yihao Liu, Xiaoxi Jiang, Guanjun Jiang
- arxiv_id: 2511.18159
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2511.18159v1
- published: 2025-11-22

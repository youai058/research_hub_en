---
title: "Effective Test-Time Scaling of Discrete Diffusion through Iterative Refinement"
authors: ["Sanghyun Lee", "Sunwoo Kim", "Seungryong Kim", "Jongho Park", "Dongmin Park"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2511.05562"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2511.05562v1"
published: "2025-11-04"
categories: ["cs.LG", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:37+09:00"
---

# Effective Test-Time Scaling of Discrete Diffusion through Iterative Refinement

## Abstract
Test-time scaling through reward-guided generation remains largely unexplored for discrete diffusion models despite its potential as a promising alternative. In this work, we introduce Iterative Reward-Guided Refinement (IterRef), a novel test-time scaling method tailored to discrete diffusion that leverages reward-guided noising-denoising transitions to progressively refine misaligned intermediate states. We formalize this process within a Multiple-Try Metropolis (MTM) framework, proving convergence to the reward-aligned distribution. Unlike prior methods that assume the current state is already aligned with the reward distribution and only guide the subsequent transition, our approach explicitly refines each state in situ, progressively steering it toward the optimal intermediate distribution. Across both text and image domains, we evaluate IterRef on diverse discrete diffusion models and observe consistent improvements in reward-guided generation quality. In particular, IterRef achieves striking gains under low compute budgets, far surpassing prior state-of-the-art baselines.

## Metadata
- venue: arXiv
- year: 2025
- authors: Sanghyun Lee, Sunwoo Kim, Seungryong Kim, Jongho Park, Dongmin Park
- arxiv_id: 2511.05562
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2511.05562v1
- published: 2025-11-04

---
title: "Parallel Sampling from Masked Diffusion Models via Conditional Independence Testing"
authors: ["Iskander Azangulov", "Teodora Pandeva", "Niranjani Prasad", "Javier Zazo", "Sushrut Karmalkar"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.21961"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.21961v1"
published: "2025-10-24"
categories: ["cs.LG", "cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:22+09:00"
---

# Parallel Sampling from Masked Diffusion Models via Conditional Independence Testing

## Abstract
Masked diffusion models (MDMs) offer a compelling alternative to autoregressive models (ARMs) for discrete text generation because they enable parallel token sampling, rather than sequential, left-to-right generation. This means potentially much faster inference. However, effective parallel sampling faces two competing requirements: (i) simultaneously updated tokens must be conditionally independent, and (ii) updates should prioritise high-confidence predictions. These goals conflict because high-confidence predictions often cluster and depend on each other, opportunities for parallel updates.
  We present PUNT, a model-agnostic sampler that reconciles this trade-off. Our method identifies token dependencies and removes lower-confidence tokens from conflicting groups. This produces sets of indices for unmasking that satisfy both independence and confidence criteria. Our approach ensures improved parallel unmasking through approximate conditional independence testing.
  Our experiments show that PUNT delivers a superior trade-off between accuracy and compute when compared to other strong training-free baselines, especially for generation of longer sequences. On the IFEval benchmark, it achieves up to 16\% higher accuracy over baseline methods, including sequential generation (one-by-one). These gains hold across different values of hyperparameters, mitigating the need for brittle hyperparameter tuning. Moreover, we observe that PUNT induces an emergent hierarchical generation strategy, where the model first establishes high-level paragraph structure before local refinement, suggesting a planning-like generation process that contributes to strong alignment performance.

## Metadata
- venue: arXiv
- year: 2025
- authors: Iskander Azangulov, Teodora Pandeva, Niranjani Prasad, Javier Zazo, Sushrut Karmalkar
- arxiv_id: 2510.21961
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.21961v1
- published: 2025-10-24

---
title: "Masked Diffusion Captioning for Visual Feature Learning"
authors: ["Chao Feng", "Zihao Wei", "Andrew Owens"]
venue: "EMNLP"
year: 2025
venue_class: "whitelist"
arxiv_id: "2510.26799"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.26799v1"
published: "2025-10-30"
categories: ["cs.CV"]
keywords: []
venue_source: "arxiv-comment"
hunter_fetched: "2026-04-15T05:17:06+09:00"
---

# Masked Diffusion Captioning for Visual Feature Learning

## Abstract
We learn visual features by captioning images with an image-conditioned masked diffusion language model, a formulation we call masked diffusion captioning (MDC). During training, text tokens in each image-caption pair are masked at a randomly chosen ratio, and a decoder conditioned on visual features is trained to reconstruct the original text. After training, the learned visual features can be applied to downstream vision tasks. Unlike autoregressive captioning, the strength of the visual learning signal in MDC does not depend on each token's position in the sequence, reducing the need for auxiliary objectives. Linear probing experiments across a variety of academic-scale models and datasets show that the learned visual features are competitive with those produced by autoregressive and contrastive approaches.

## Metadata
- venue: EMNLP
- year: 2025
- authors: Chao Feng, Zihao Wei, Andrew Owens
- arxiv_id: 2510.26799
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.26799v1
- published: 2025-10-30

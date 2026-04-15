---
title: "Stop Training for the Worst: Progressive Unmasking Accelerates Masked Diffusion Training"
authors: ["Jaeyeon Kim", "Jonathan Geuter", "David Alvarez-Melis", "Sham Kakade", "Sitan Chen"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.10314"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.10314v1"
published: "2026-02-10"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:17+09:00"
---

# Stop Training for the Worst: Progressive Unmasking Accelerates Masked Diffusion Training

## Abstract
Masked Diffusion Models (MDMs) have emerged as a promising approach for generative modeling in discrete spaces. By generating sequences in any order and allowing for parallel decoding, they enable fast inference and strong performance on non-causal tasks. However, this flexibility comes with a training complexity trade-off: MDMs train on an exponentially large set of masking patterns, which is not only computationally expensive, but also creates a train--test mismatch between the random masks used in training and the highly structured masks induced by inference-time unmasking. In this work, we propose Progressive UnMAsking (PUMA), a simple modification of the forward masking process that aligns training-time and inference-time masking patterns, thereby focusing optimization on inference-aligned masks and speeding up training. Empirically, PUMA speeds up pretraining at the 125M scale by $\approx 2.5\times$ and offers complementary advantages on top of common recipes like autoregressive initialization. We open-source our codebase at https://github.com/JaeyeonKim01/PUMA.

## Metadata
- venue: arXiv
- year: 2026
- authors: Jaeyeon Kim, Jonathan Geuter, David Alvarez-Melis, Sham Kakade, Sitan Chen
- arxiv_id: 2602.10314
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.10314v1
- published: 2026-02-10

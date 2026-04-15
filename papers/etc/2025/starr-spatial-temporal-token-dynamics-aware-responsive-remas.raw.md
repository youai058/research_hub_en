---
title: "STaRR: Spatial-Temporal Token-Dynamics-Aware Responsive Remasking for Diffusion Language Models"
authors: ["Xinhao Sun", "Huaijin Zhao", "Maoliang Li", "Zihao Zheng", "Jiayu Chen", "Yun Liang", "Xiang Chen"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2601.04205"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2601.04205v2"
published: "2025-12-07"
categories: ["cs.CL", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:03+09:00"
---

# STaRR: Spatial-Temporal Token-Dynamics-Aware Responsive Remasking for Diffusion Language Models

## Abstract
Diffusion Language Models (DLMs) enable parallel decoding via iterative denoising, where remasking strategies play a critical role in balancing inference speed and output quality. Existing methods predominantly rely on static confidence thresholds, overlooking the spatial-temporal dynamics of token confidence, causing unnecessary remasking. We propose Spatial-Temporal Token-Dynamics-Aware Responsive Remasking (STaRR), a training-free framework that dynamically adapts remasking decisions based on token confidence evolution. STaRR introduces two metrics, temporal variance and spatial deviance, to guide fine-grained, step-wise dynamic thresholding. We further introduce a step-wise dynamic thresholding strategy, further enhanced with responsiveness optimizations for scalability and robustness. Experiments show that STaRR achieves an average speedup of 4.1 and up to 8.9 while maintaining comparable accuracy.

## Metadata
- venue: arXiv
- year: 2025
- authors: Xinhao Sun, Huaijin Zhao, Maoliang Li, Zihao Zheng, Jiayu Chen, Yun Liang, Xiang Chen
- arxiv_id: 2601.04205
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2601.04205v2
- published: 2025-12-07

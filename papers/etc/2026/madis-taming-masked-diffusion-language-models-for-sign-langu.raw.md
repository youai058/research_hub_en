---
title: "MaDiS: Taming Masked Diffusion Language Models for Sign Language Generation"
authors: ["Ronglai Zuo", "Rolandos Alexandros Potamias", "Qi Sun", "Evangelos Ververas", "Jiankang Deng", "Stefanos Zafeiriou"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2601.19577"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2601.19577v2"
published: "2026-01-27"
categories: ["cs.CV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:21+09:00"
---

# MaDiS: Taming Masked Diffusion Language Models for Sign Language Generation

## Abstract
Sign language generation (SLG) aims to translate written texts into expressive sign motions, bridging communication barriers for the Deaf and Hard-of-Hearing communities. Recent studies formulate SLG within the language modeling framework using autoregressive language models, which suffer from unidirectional context modeling and slow token-by-token inference. To address these limitations, we present MaDiS, a masked-diffusion-based language model for SLG that captures bidirectional dependencies and supports efficient parallel multi-token generation. We further introduce a tri-level cross-modal pretraining scheme that jointly learns from token-, latent-, and 3D physical-space objectives to leverage complementary, multi-level sign representations. To accelerate model convergence in the fine-tuning stage, we design a novel unmasking strategy with temporal checkpoints, which restructures generation in a coarse-to-fine manner and reduces the combinatorial complexity of unmasking orders by over $10^{41}$ times. In addition, a mixture-of-parts embedding layer is developed to effectively fuse information stored in different part-wise sign tokens through a learnable gate and well-optimized codebooks. Extensive experiments on CSL-Daily, Phoenix-2014T, and How2Sign demonstrate that MaDiS achieves superior performance across multiple metrics, including DTW error and two newly introduced metrics, SiBLEU and SiCLIP, while delivering a 40\% higher throughput. Code and models will be publicly released.

## Metadata
- venue: arXiv
- year: 2026
- authors: Ronglai Zuo, Rolandos Alexandros Potamias, Qi Sun, Evangelos Ververas, Jiankang Deng, Stefanos Zafeiriou
- arxiv_id: 2601.19577
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2601.19577v2
- published: 2026-01-27

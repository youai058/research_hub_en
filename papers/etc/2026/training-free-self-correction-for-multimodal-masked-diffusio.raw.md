---
title: "Training-Free Self-Correction for Multimodal Masked Diffusion Models"
authors: ["Yidong Ouyang", "Panwen Hu", "Zhengyan Wan", "Zhe Wang", "Liyan Xie", "Dmitriy Bespalov", "Ying Nian Wu", "Guang Cheng", "Hongyuan Zha", "Qiang Sun"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.02927"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.02927v1"
published: "2026-02-02"
categories: ["stat.ML", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:17+09:00"
---

# Training-Free Self-Correction for Multimodal Masked Diffusion Models

## Abstract
Masked diffusion models have emerged as a powerful framework for text and multimodal generation. However, their sampling procedure updates multiple tokens simultaneously and treats generated tokens as immutable, which may lead to error accumulation when early mistakes cannot be revised. In this work, we revisit existing self-correction methods and identify limitations stemming from additional training requirements or reliance on misaligned likelihood estimates. We propose a training-free self-correction framework that exploits the inductive biases of pre-trained masked diffusion models. Without modifying model parameters or introducing auxiliary evaluators, our method significantly improves generation quality on text-to-image generation and multimodal understanding tasks with reduced sampling steps. Moreover, the proposed framework generalizes across different masked diffusion architectures, highlighting its robustness and practical applicability. Code can be found in https://github.com/huge123/FreeCorrection.

## Metadata
- venue: arXiv
- year: 2026
- authors: Yidong Ouyang, Panwen Hu, Zhengyan Wan, Zhe Wang, Liyan Xie, Dmitriy Bespalov, Ying Nian Wu, Guang Cheng, Hongyuan Zha, Qiang Sun
- arxiv_id: 2602.02927
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.02927v1
- published: 2026-02-02

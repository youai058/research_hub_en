---
title: "Cubic Discrete Diffusion: Discrete Visual Generation on High-Dimensional Representation Tokens"
authors: ["Yuqing Wang", "Chuofan Ma", "Zhijie Lin", "Yao Teng", "Lijun Yu", "Shuai Wang", "Jiaming Han", "Jiashi Feng", "Yi Jiang", "Xihui Liu"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.19232"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.19232v1"
published: "2026-03-19"
categories: ["cs.CV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:24+09:00"
---

# Cubic Discrete Diffusion: Discrete Visual Generation on High-Dimensional Representation Tokens

## Abstract
Visual generation with discrete tokens has gained significant attention as it enables a unified token prediction paradigm shared with language models, promising seamless multimodal architectures. However, current discrete generation methods remain limited to low-dimensional latent tokens (typically 8-32 dims), sacrificing the semantic richness essential for understanding. While high-dimensional pretrained representations (768-1024 dims) could bridge this gap, their discrete generation poses fundamental challenges. In this paper, we present Cubic Discrete Diffusion (CubiD), the first discrete generation model for high-dimensional representations. CubiD performs fine-grained masking throughout the high-dimensional discrete representation -- any dimension at any position can be masked and predicted from partial observations. This enables the model to learn rich correlations both within and across spatial positions, with the number of generation steps fixed at $T$ regardless of feature dimensionality, where $T \ll hwd$. On ImageNet-256, CubiD achieves state-of-the-art discrete generation with strong scaling behavior from 900M to 3.7B parameters. Crucially, we validate that these discretized tokens preserve original representation capabilities, demonstrating that the same discrete tokens can effectively serve both understanding and generation tasks. We hope this work will inspire future research toward unified multimodal architectures. Code is available at: https://github.com/YuqingWang1029/CubiD.

## Metadata
- venue: arXiv
- year: 2026
- authors: Yuqing Wang, Chuofan Ma, Zhijie Lin, Yao Teng, Lijun Yu, Shuai Wang, Jiaming Han, Jiashi Feng, Yi Jiang, Xihui Liu
- arxiv_id: 2603.19232
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.19232v1
- published: 2026-03-19

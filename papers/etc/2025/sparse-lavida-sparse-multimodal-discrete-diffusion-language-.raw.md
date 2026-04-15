---
title: "Sparse-LaViDa: Sparse Multimodal Discrete Diffusion Language Models"
authors: ["Shufan Li", "Jiuxiang Gu", "Kangning Liu", "Zhe Lin", "Zijun Wei", "Aditya Grover", "Jason Kuen"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2512.14008"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2512.14008v1"
published: "2025-12-16"
categories: ["cs.CV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:33+09:00"
---

# Sparse-LaViDa: Sparse Multimodal Discrete Diffusion Language Models

## Abstract
Masked Discrete Diffusion Models (MDMs) have achieved strong performance across a wide range of multimodal tasks, including image understanding, generation, and editing. However, their inference speed remains suboptimal due to the need to repeatedly process redundant masked tokens at every sampling step. In this work, we propose Sparse-LaViDa, a novel modeling framework that dynamically truncates unnecessary masked tokens at each inference step to accelerate MDM sampling. To preserve generation quality, we introduce specialized register tokens that serve as compact representations for the truncated tokens. Furthermore, to ensure consistency between training and inference, we design a specialized attention mask that faithfully matches the truncated sampling procedure during training. Built upon the state-of-the-art unified MDM LaViDa-O, Sparse-LaViDa achieves up to a 2x speedup across diverse tasks including text-to-image generation, image editing, and mathematical reasoning, while maintaining generation quality.

## Metadata
- venue: arXiv
- year: 2025
- authors: Shufan Li, Jiuxiang Gu, Kangning Liu, Zhe Lin, Zijun Wei, Aditya Grover, Jason Kuen
- arxiv_id: 2512.14008
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2512.14008v1
- published: 2025-12-16

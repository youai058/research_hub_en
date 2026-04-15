---
title: "A Comprehensive Study on Visual Token Redundancy for Discrete Diffusion-based Multimodal Large Language Models"
authors: ["Duo Li", "Zuhao Yang", "Xiaoqin Zhang", "Ling Shao", "Shijian Lu"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2511.15098"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2511.15098v1"
published: "2025-11-19"
categories: ["cs.CV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:33+09:00"
---

# A Comprehensive Study on Visual Token Redundancy for Discrete Diffusion-based Multimodal Large Language Models

## Abstract
Discrete diffusion-based multimodal large language models (dMLLMs) have emerged as a promising alternative to autoregressive MLLMs thanks to their advantages in parallel decoding and bidirectional context modeling, but most existing dMLLMs incur significant computational overhead during inference due to the full-sequence attention computation in each denoising step. Pioneer studies attempt to resolve this issue from a modality-agnostic perspective via key-value cache optimization or efficient sampling but most of them overlook modality-specific visual token redundancy. In this work, we conduct a comprehensive study on how visual token redundancy evolves with different dMLLM architectures and tasks and how visual token pruning affects dMLLM responses and efficiency. Specifically, our study reveals that visual redundancy emerges only in from-scratch dMLLMs while handling long-answer tasks. In addition, we validate that visual token pruning introduces non-negligible information loss in dMLLMs and only from-scratch dMLLMs can recover the lost information progressively during late denoising steps. Furthermore, our study shows that layer-skipping is promising for accelerating AR-to-diffusion dMLLMs, whereas progressive or late-step pruning is more effective for from-scratch dMLLMs. Overall, this work offers a new perspective on efficiency optimization for dMLLMs, greatly advancing their applicability across various multimodal understanding tasks.

## Metadata
- venue: arXiv
- year: 2025
- authors: Duo Li, Zuhao Yang, Xiaoqin Zhang, Ling Shao, Shijian Lu
- arxiv_id: 2511.15098
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2511.15098v1
- published: 2025-11-19

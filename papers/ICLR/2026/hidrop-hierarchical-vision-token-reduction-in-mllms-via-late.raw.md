---
title: "HiDrop: Hierarchical Vision Token Reduction in MLLMs via Late Injection, Concave Pyramid Pruning, and Early Exit"
authors: ["Hao Wu", "Yingqi Fan", "Dai Jinyang", "Junlong Tong", "Yunpu Ma", "Xiaoyu Shen"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "2baJBgfr9S"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e620a85a9600bcae25662255daeab9a1fe7a8a2f.pdf"
published: "2026"
categories: []
keywords: ["MLLMs", "Vision Token Pruning", "Efficiency and Compression", "Interpretability and Analysis"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:19+09:00"
---

# HiDrop: Hierarchical Vision Token Reduction in MLLMs via Late Injection, Concave Pyramid Pruning, and Early Exit

## Abstract
The quadratic computational cost of processing vision tokens in Multimodal Large Language Models (MLLMs) hinders their widespread adoption. While progressive vision token pruning offers a promising solution, current methods misinterpret shallow layer functions and use rigid schedules, which fail to unlock the full efficiency potential. To address these issues, we propose HiDrop, a framework that aligns token pruning with the true hierarchical function of MLLM layers. HiDrop features two key innovations: (1) Late Injection, which bypasses passive shallow layers to introduce visual tokens exactly where active fusion begins; and (2) Concave Pyramid Pruning with an Early Exit mechanism to dynamically adjust pruning rates across middle and deep layers. This process is optimized via an inter-layer similarity measure and a differentiable top-$k$ operator.  To ensure practical efficiency, HiDrop further incorporates persistent positional encoding, FlashAttention-compatible token selection, and parallel decoupling of vision computation to eliminate hidden overhead associated with dynamic token reduction. Extensive experiments show that HiDrop compresses $\sim$90\% visual tokens while matching the original performance and accelerating training by 1.72$\times$. Our work not only sets a new state-of-the-art for efficient MLLM training and inference but also provides valuable insights into the hierarchical nature of multimodal fusion. The code is released at https://github.com/EIT-NLP/HiDrop.

## Metadata
- venue: ICLR
- year: 2026
- authors: Hao Wu, Yingqi Fan, Dai Jinyang, Junlong Tong, Yunpu Ma, Xiaoyu Shen
- arxiv_id: 
- openreview_id: 2baJBgfr9S
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e620a85a9600bcae25662255daeab9a1fe7a8a2f.pdf
- published: 2026
- keywords: MLLMs, Vision Token Pruning, Efficiency and Compression, Interpretability and Analysis

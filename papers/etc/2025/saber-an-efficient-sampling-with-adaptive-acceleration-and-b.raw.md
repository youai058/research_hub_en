---
title: "Saber: An Efficient Sampling with Adaptive Acceleration and Backtracking Enhanced Remasking for Diffusion Language Model"
authors: ["Yihong Dong", "Zhaoyu Ma", "Xue Jiang", "Zhiyuan Fan", "Jiaru Qian", "Yongmin Li", "Jianha Xiao", "Zhi Jin", "Rongyu Cao", "Binhua Li", "Fei Huang", "Yongbin Li", "Ge Li"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.18165"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.18165v1"
published: "2025-10-20"
categories: ["cs.AI", "cs.CL", "cs.LG", "cs.SE"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:06+09:00"
---

# Saber: An Efficient Sampling with Adaptive Acceleration and Backtracking Enhanced Remasking for Diffusion Language Model

## Abstract
Diffusion language models (DLMs) are emerging as a powerful and promising alternative to the dominant autoregressive paradigm, offering inherent advantages in parallel generation and bidirectional context modeling. However, the performance of DLMs on code generation tasks, which have stronger structural constraints, is significantly hampered by the critical trade-off between inference speed and output quality. We observed that accelerating the code generation process by reducing the number of sampling steps usually leads to a catastrophic collapse in performance. In this paper, we introduce efficient Sampling with Adaptive acceleration and Backtracking Enhanced Remasking (i.e., Saber), a novel training-free sampling algorithm for DLMs to achieve better inference speed and output quality in code generation. Specifically, Saber is motivated by two key insights in the DLM generation process: 1) it can be adaptively accelerated as more of the code context is established; 2) it requires a backtracking mechanism to reverse the generated tokens. Extensive experiments on multiple mainstream code generation benchmarks show that Saber boosts Pass@1 accuracy by an average improvement of 1.9% over mainstream DLM sampling methods, meanwhile achieving an average 251.4% inference speedup. By leveraging the inherent advantages of DLMs, our work significantly narrows the performance gap with autoregressive models in code generation.

## Metadata
- venue: arXiv
- year: 2025
- authors: Yihong Dong, Zhaoyu Ma, Xue Jiang, Zhiyuan Fan, Jiaru Qian, Yongmin Li, Jianha Xiao, Zhi Jin, Rongyu Cao, Binhua Li, Fei Huang, Yongbin Li, Ge Li
- arxiv_id: 2510.18165
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.18165v1
- published: 2025-10-20

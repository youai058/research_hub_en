---
title: "Gated Linear Attention Transformers with Hardware-Efficient Training"
authors: ["Songlin Yang", "Bailin Wang", "Yikang Shen", "Rameswar Panda", "Yoon Kim"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ia5XvxFUJT"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c83a4c1aed45c267e44d9f8c94b16e5a902bca84.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:34+09:00"
---

# Gated Linear Attention Transformers with Hardware-Efficient Training

## Abstract
Transformers with linear attention allow for efficient parallel training but can simultaneously be formulated as an RNN with 2D (matrix-valued) hidden states, thus enjoying linear-time inference complexity. However, linear attention generally underperforms ordinary softmax attention. Moreover, current implementations of linear attention lack I/O-awareness and are thus slower than highly optimized implementations of softmax attention. This work describes a hardware-efficient algorithm for linear attention that trades off memory movement against parallelizability. The resulting implementation, dubbed FlashLinearAttention, is faster than FlashAttention-2 as a standalone layer even on short sequence lengths (e.g., 1K). We then generalize this algorithm to a more expressive variant of linear attention with data-dependent gates. When used as a replacement for the standard attention layer in Transformers, the resulting gated linear attention (GLA) Transformer is found to perform competitively against the LLaMA-architecture Transformer as well recent linear-time-inference baselines such as RetNet and Mamba on moderate-scale language modeling experiments. GLA Transformer is especially effective at length generalization, enabling a model trained on 2K to generalize to sequences longer than 20K without significant perplexity degradations. For training speed, the GLA Transformer has higher throughput than a similarly-sized Mamba model.

## Metadata
- venue: ICML
- year: 2024
- authors: Songlin Yang, Bailin Wang, Yikang Shen, Rameswar Panda, Yoon Kim
- arxiv_id: 
- openreview_id: ia5XvxFUJT
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c83a4c1aed45c267e44d9f8c94b16e5a902bca84.pdf
- published: 2024

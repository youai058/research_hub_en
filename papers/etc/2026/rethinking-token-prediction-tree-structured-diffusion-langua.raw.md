---
title: "Rethinking Token Prediction: Tree-Structured Diffusion Language Model"
authors: ["Zihao Wu", "Haoming Yang", "Juncheng Dong", "Vahid Tarokh"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2604.03537"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2604.03537v1"
published: "2026-04-04"
categories: ["cs.CL", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:13:54+09:00"
---

# Rethinking Token Prediction: Tree-Structured Diffusion Language Model

## Abstract
Discrete diffusion language models have emerged as a competitive alternative to auto-regressive language models, but training them efficiently under limited parameter and memory budgets remains challenging. Modern architectures are predominantly based on a full-vocabulary token prediction layer, which accounts for a substantial fraction of model parameters (e.g., more than 20% in small scale DiT-style designs) and often dominates peak GPU memory usage. This leads to inefficient use of both parameters and memory under constrained training resources. To address this issue, we revisit the necessity of explicit full-vocabulary prediction, and instead exploit the inherent structure among tokens to build a tree-structured diffusion language model. Specifically, we model the diffusion process with intermediate latent states corresponding to a token's ancestor nodes in a pre-constructed vocabulary tree. This tree-structured factorization exponentially reduces the classification dimensionality, makes the prediction head negligible in size, and enables reallocation of parameters to deepen the attention blocks. Empirically, under the same parameter budget, our method reduces peak GPU memory usage by half while matching the perplexity performance of state-of-the-art discrete diffusion language models.

## Metadata
- venue: arXiv
- year: 2026
- authors: Zihao Wu, Haoming Yang, Juncheng Dong, Vahid Tarokh
- arxiv_id: 2604.03537
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2604.03537v1
- published: 2026-04-04

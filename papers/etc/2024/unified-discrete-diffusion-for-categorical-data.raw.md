---
title: "Unified Discrete Diffusion for Categorical Data"
authors: ["Lingxiao Zhao", "Xueying Ding", "Lijun Yu", "Leman Akoglu"]
venue: "arXiv"
year: 2024
venue_class: "etc"
arxiv_id: "2402.03701"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2402.03701v2"
published: "2024-02-06"
categories: ["cs.LG", "stat.ML"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:20:20+09:00"
---

# Unified Discrete Diffusion for Categorical Data

## Abstract
Discrete diffusion models have seen a surge of attention with applications on naturally discrete data such as language and graphs. Although discrete-time discrete diffusion has been established for a while, only recently Campbell et al. (2022) introduced the first framework for continuous-time discrete diffusion. However, their training and sampling processes differ significantly from the discrete-time version, necessitating nontrivial approximations for tractability. In this paper, we first present a series of mathematical simplifications of the variational lower bound that enable more accurate and easy-to-optimize training for discrete diffusion. In addition, we derive a simple formulation for backward denoising that enables exact and accelerated sampling, and importantly, an elegant unification of discrete-time and continuous-time discrete diffusion. Thanks to simpler analytical formulations, both forward and now also backward probabilities can flexibly accommodate any noise distribution, including different noise distributions for multi-element objects. Experiments show that our proposed USD3 (for Unified Simplified Discrete Denoising Diffusion) outperform all SOTA baselines on established datasets. We open-source our unified code at https://github.com/LingxiaoShawn/USD3.

## Metadata
- venue: arXiv
- year: 2024
- authors: Lingxiao Zhao, Xueying Ding, Lijun Yu, Leman Akoglu
- arxiv_id: 2402.03701
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2402.03701v2
- published: 2024-02-06

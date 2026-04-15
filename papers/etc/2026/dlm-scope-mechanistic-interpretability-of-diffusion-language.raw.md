---
title: "DLM-Scope: Mechanistic Interpretability of Diffusion Language Models via Sparse Autoencoders"
authors: ["Xu Wang", "Bingqing Jiang", "Yu Wan", "Baosong Yang", "Lingpeng Kong", "Difan Zou"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.05859"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.05859v1"
published: "2026-02-05"
categories: ["cs.LG", "cs.AI", "cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:05+09:00"
---

# DLM-Scope: Mechanistic Interpretability of Diffusion Language Models via Sparse Autoencoders

## Abstract
Sparse autoencoders (SAEs) have become a standard tool for mechanistic interpretability in autoregressive large language models (LLMs), enabling researchers to extract sparse, human-interpretable features and intervene on model behavior. Recently, as diffusion language models (DLMs) have become an increasingly promising alternative to the autoregressive LLMs, it is essential to develop tailored mechanistic interpretability tools for this emerging class of models. In this work, we present DLM-Scope, the first SAE-based interpretability framework for DLMs, and demonstrate that trained Top-K SAEs can faithfully extract interpretable features. Notably, we find that inserting SAEs affects DLMs differently than autoregressive LLMs: while SAE insertion in LLMs typically incurs a loss penalty, in DLMs it can reduce cross-entropy loss when applied to early layers, a phenomenon absent or markedly weaker in LLMs. Additionally, SAE features in DLMs enable more effective diffusion-time interventions, often outperforming LLM steering. Moreover, we pioneer certain new SAE-based research directions for DLMs: we show that SAEs can provide useful signals for DLM decoding order; and the SAE features are stable during the post-training phase of DLMs. Our work establishes a foundation for mechanistic interpretability in DLMs and shows a great potential of applying SAEs to DLM-related tasks and algorithms.

## Metadata
- venue: arXiv
- year: 2026
- authors: Xu Wang, Bingqing Jiang, Yu Wan, Baosong Yang, Lingpeng Kong, Difan Zou
- arxiv_id: 2602.05859
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.05859v1
- published: 2026-02-05

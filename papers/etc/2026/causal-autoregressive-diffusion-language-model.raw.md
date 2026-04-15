---
title: "Causal Autoregressive Diffusion Language Model"
authors: ["Junhao Ruan", "Bei Li", "Yongjing Yin", "Pengcheng Huang", "Xin Chen", "Jingang Wang", "Xunliang Cai", "Tong Xiao", "JingBo Zhu"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2601.22031"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2601.22031v1"
published: "2026-01-29"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:36+09:00"
---

# Causal Autoregressive Diffusion Language Model

## Abstract
In this work, we propose Causal Autoregressive Diffusion (CARD), a novel framework that unifies the training efficiency of ARMs with the high-throughput inference of diffusion models. CARD reformulates the diffusion process within a strictly causal attention mask, enabling dense, per-token supervision in a single forward pass. To address the optimization instability of causal diffusion, we introduce a soft-tailed masking schema to preserve local context and a context-aware reweighting mechanism derived from signal-to-noise principles. This design enables dynamic parallel decoding, where the model leverages KV-caching to adaptively generate variable-length token sequences based on confidence. Empirically, CARD outperforms existing discrete diffusion baselines while reducing training latency by 3 $\times$ compared to block diffusion methods. Our results demonstrate that CARD achieves ARM-level data efficiency while unlocking the latency benefits of parallel generation, establishing a robust paradigm for next-generation efficient LLMs.

## Metadata
- venue: arXiv
- year: 2026
- authors: Junhao Ruan, Bei Li, Yongjing Yin, Pengcheng Huang, Xin Chen, Jingang Wang, Xunliang Cai, Tong Xiao, JingBo Zhu
- arxiv_id: 2601.22031
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2601.22031v1
- published: 2026-01-29

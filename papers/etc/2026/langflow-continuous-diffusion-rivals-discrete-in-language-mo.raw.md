---
title: "LangFlow: Continuous Diffusion Rivals Discrete in Language Modeling"
authors: ["Yuxin Chen", "Chumeng Liang", "Hangke Sui", "Ruihan Guo", "Chaoran Cheng", "Jiaxuan You", "Ge Liu"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2604.11748"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2604.11748v1"
published: "2026-04-13"
categories: ["cs.CL", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:13:54+09:00"
---

# LangFlow: Continuous Diffusion Rivals Discrete in Language Modeling

## Abstract
Continuous diffusion models have achieved strong performance across domains such as images. However, in language modeling, prior continuous diffusion language models (DLMs) lag behind discrete counterparts. In this work, we close this gap with LangFlow, the first continuous DLM to rival discrete diffusion. Our approach connects embedding-space DLMs to Flow Matching via Bregman divergence and introduces three key innovations: (1) a novel ODE-based NLL bound for principled evaluation of continuous flow-based language models; (2) an information-uniform principle for noise scheduling, motivating a learnable scheduler based on a Gumbel distribution; and (3) an improved training protocol incorporating self-conditioning, which enhances both likelihood and sample quality.LangFlow achieves strong performance across benchmarks, reaching a perplexity (PPL) of 30.0 on LM1B and 24.6 on OpenWebText. It matches top discrete DLMs at comparable scale and surpasses autoregressive baselines in zero-shot transfer across multiple benchmarks. LangFlow provides clear evidence that continuous diffusion is a competitive and promising paradigm for language modeling.
  https://github.com/nealchen2003/LangFlow

## Metadata
- venue: arXiv
- year: 2026
- authors: Yuxin Chen, Chumeng Liang, Hangke Sui, Ruihan Guo, Chaoran Cheng, Jiaxuan You, Ge Liu
- arxiv_id: 2604.11748
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2604.11748v1
- published: 2026-04-13

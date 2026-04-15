---
title: "Characterizing Memorization in Diffusion Language Models: Generalized Extraction and Sampling Effects"
authors: ["Xiaoyu Luo", "Wenrui Yu", "Qiongxiu Li", "Johannes Bjerva"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.02333"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.02333v1"
published: "2026-03-02"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:02+09:00"
---

# Characterizing Memorization in Diffusion Language Models: Generalized Extraction and Sampling Effects

## Abstract
Autoregressive language models (ARMs) have been shown to memorize and occasionally reproduce training data verbatim, raising concerns about privacy and copyright liability. Diffusion language models (DLMs) have recently emerged as a competitive alternative, yet their memorization behavior remains largely unexplored due to fundamental differences in generation dynamics. To address this gap, we present a systematic theoretical and empirical characterization of memorization in DLMs. We propose a generalized probabilistic extraction framework that unifies prefix-conditioned decoding and diffusion-based generation under arbitrary masking patterns and stochastic sampling trajectories. Theorem 4.3 establishes a monotonic relationship between sampling resolution and memorization: increasing resolution strictly increases the probability of exact training data extraction, implying that autoregressive decoding corresponds to a limiting case of diffusion-based generation by setting the sampling resolution maximal. Extensive experiments across model scales and sampling strategies validate our theoretical predictions. Under aligned prefix-conditioned evaluations, we further demonstrate that DLMs exhibit substantially lower memorization-based leakage of personally identifiable information (PII) compared to ARMs.

## Metadata
- venue: arXiv
- year: 2026
- authors: Xiaoyu Luo, Wenrui Yu, Qiongxiu Li, Johannes Bjerva
- arxiv_id: 2603.02333
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.02333v1
- published: 2026-03-02

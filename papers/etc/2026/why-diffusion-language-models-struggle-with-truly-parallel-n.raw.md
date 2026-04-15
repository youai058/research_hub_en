---
title: "Why Diffusion Language Models Struggle with Truly Parallel (Non-Autoregressive) Decoding?"
authors: ["Pengxiang Li", "Dilxat Muhtar", "Tianlong Chen", "Lu Yin", "Shiwei Liu"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.23225"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.23225v2"
published: "2026-02-26"
categories: ["cs.CL", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:02+09:00"
---

# Why Diffusion Language Models Struggle with Truly Parallel (Non-Autoregressive) Decoding?

## Abstract
Diffusion Language Models (DLMs) are often advertised as enabling parallel token generation, yet practical fast DLMs frequently converge to left-to-right, autoregressive (AR)-like decoding dynamics. In contrast, genuinely non-AR generation is promising because it removes AR's sequential bottleneck, better exploiting parallel hardware to reduce synchronization/communication overhead and improve latency scaling with output length. We argue that a primary driver of AR-like decoding is a mismatch between DLM objectives and the highly sequential structure of widely used training data, including standard pretraining corpora and long chain-of-thought (CoT) supervision. Motivated by this diagnosis, we propose NAP (Non-Autoregressive Parallel DLMs), a proof-of-concept, data-centric approach that better aligns supervision with non-AR parallel decoding. NAP curates examples as multiple independent reasoning trajectories and couples them with a parallel-forced decoding strategy that encourages multi-token parallel updates. Across math reasoning benchmarks, NAP yields stronger performance under parallel decoding than DLMs trained on standard long CoT data, with gains growing as parallelism increases. Our results suggest that revisiting data and supervision is a principled direction for mitigating AR-like behavior and moving toward genuinely non-autoregressive parallel generation in DLMs. Our code is available at https://github.com/pixeli99/NAP.

## Metadata
- venue: arXiv
- year: 2026
- authors: Pengxiang Li, Dilxat Muhtar, Tianlong Chen, Lu Yin, Shiwei Liu
- arxiv_id: 2602.23225
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.23225v2
- published: 2026-02-26

---
title: "Blockwise SFT for Diffusion Language Models: Reconciling Bidirectional Attention and Autoregressive Decoding"
authors: ["Bowen Sun", "Yujun Cai", "Ming-Hsuan Yang", "Yiwei Wang"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2508.19529"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2508.19529v2"
published: "2025-08-27"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:14+09:00"
---

# Blockwise SFT for Diffusion Language Models: Reconciling Bidirectional Attention and Autoregressive Decoding

## Abstract
Discrete diffusion language models have shown strong potential for text generation, yet standard supervised fine-tuning (SFT) misaligns with their semi-autoregressive inference: training randomly masks tokens across the entire response, while inference generates fixed-size blocks sequentially. This mismatch introduces noisy prefixes and leaky suffixes, biasing gradients away from the desired blockwise likelihood. We propose Blockwise SFT, which partitions responses into fixed-size blocks, selects one active block per step for stochastic masking, freezes all preceding tokens, and fully hides future ones. Loss is computed only over the active block, directly mirroring the blockwise decoding process. Experiments on GSM8K, MATH, and MetaMathQA show consistent gains over classical SFT under equal compute or token budgets. Block size consistency studies and ablations confirm that improvements stem from faithful training-inference alignment rather than incidental masking effects. Our results highlight the importance of matching supervision granularity to the decoding procedure in diffusion-based language models.

## Metadata
- venue: arXiv
- year: 2025
- authors: Bowen Sun, Yujun Cai, Ming-Hsuan Yang, Yiwei Wang
- arxiv_id: 2508.19529
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2508.19529v2
- published: 2025-08-27

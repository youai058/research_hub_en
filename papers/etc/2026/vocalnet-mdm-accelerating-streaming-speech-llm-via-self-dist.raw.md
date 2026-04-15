---
title: "VocalNet-MDM: Accelerating Streaming Speech LLM via Self-Distilled Masked Diffusion Modeling"
authors: ["Ziyang Cheng", "Yuhao Wang", "Heyang Liu", "Ronghua Wu", "Qunshan Gu", "Yanfeng Wang", "Yu Wang"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.08607"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.08607v1"
published: "2026-02-09"
categories: ["cs.CL", "cs.SD"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:17+09:00"
---

# VocalNet-MDM: Accelerating Streaming Speech LLM via Self-Distilled Masked Diffusion Modeling

## Abstract
Recent Speech Large Language Models~(LLMs) have achieved impressive capabilities in end-to-end speech interaction. However, the prevailing autoregressive paradigm imposes strict serial constraints, limiting generation efficiency and introducing exposure bias. In this paper, we investigate Masked Diffusion Modeling~(MDM) as a non-autoregressive paradigm for speech LLMs and introduce VocalNet-MDM. To adapt MDM for streaming speech interaction, we address two critical challenges: training-inference mismatch and iterative overhead. We propose Hierarchical Block-wise Masking to align training objectives with the progressive masked states encountered during block diffusion decoding, and Iterative Self-Distillation to compress multi-step refinement into fewer steps for low-latency inference. Trained on a limited scale of only 6K hours of speech data, VocalNet-MDM achieves a 3.7$\times$--10$\times$ decoding speedup and reduces first-chunk latency by 34\% compared to AR baselines. It maintains competitive recognition accuracy while achieving state-of-the-art text quality and speech naturalness, demonstrating that MDM is a promising and scalable alternative for low-latency, efficient speech LLMs.

## Metadata
- venue: arXiv
- year: 2026
- authors: Ziyang Cheng, Yuhao Wang, Heyang Liu, Ronghua Wu, Qunshan Gu, Yanfeng Wang, Yu Wang
- arxiv_id: 2602.08607
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.08607v1
- published: 2026-02-09

---
title: "Adaptive Guidance for Retrieval-Augmented Masked Diffusion Models"
authors: ["Jaemin Kim", "Jong Chul Ye"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.17677"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.17677v2"
published: "2026-03-18"
categories: ["cs.CL", "cs.AI", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:09+09:00"
---

# Adaptive Guidance for Retrieval-Augmented Masked Diffusion Models

## Abstract
Retrieval-Augmented Generation (RAG) improves factual grounding by incorporating external knowledge into language model generation. However, when retrieved context is noisy, unreliable, or inconsistent with the model's parametric knowledge, it introduces retrieval-prior conflicts that can degrade generation quality. While this problem has been studied in autoregressive language models, it remains largely unexplored in diffusion-based language models, where the iterative denoising process introduces unique challenges for integrating retrieved context. In this work, we propose Adaptive Retrieval-Augmented Masked Diffusion (ARAM), a training-free adaptive guidance framework for Masked Diffusion Models (MDMs) in RAG settings. ARAM dynamically calibrates the guidance scale during denoising according to the Signal-to-Noise Ratio (SNR) of the distributional shift induced by retrieved context. Intuitively, the model strengthens guidance when the retrieved context provides reliable corrective evidence and suppresses it when the contextual signal is noisy or non-supportive. Extensive experiments on multiple knowledge-intensive QA benchmarks show that ARAM improves overall QA performance over competitive RAG baselines.

## Metadata
- venue: arXiv
- year: 2026
- authors: Jaemin Kim, Jong Chul Ye
- arxiv_id: 2603.17677
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.17677v2
- published: 2026-03-18

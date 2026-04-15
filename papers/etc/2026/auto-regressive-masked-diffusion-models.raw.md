---
title: "Auto-Regressive Masked Diffusion Models"
authors: ["Mahdi Karami", "Ali Ghodsi"]
venue: "29th International Conference on Artificial Intelligence and Statistics (AISTATS) 2026"
year: 2026
venue_class: "etc"
arxiv_id: "2601.16971"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2601.16971v1"
published: "2026-01-23"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:21+09:00"
---

# Auto-Regressive Masked Diffusion Models

## Abstract
Masked diffusion models (MDMs) have emerged as a promising approach for language modeling, yet they face a performance gap compared to autoregressive models (ARMs) and require more training iterations. In this work, we present the Auto-Regressive Masked Diffusion (ARMD) model, an architecture designed to close this gap by unifying the training efficiency of autoregressive models with the parallel generation capabilities of diffusion-based models. Our key insight is to reframe the masked diffusion process as a block-wise causal model. This perspective allows us to design a strictly causal, permutation-equivariant architecture that computes all conditional probabilities across multiple denoising steps in a single, parallel forward pass. The resulting architecture supports efficient, autoregressive-style decoding and a progressive permutation training scheme, allowing the model to learn both canonical left-to-right and random token orderings. Leveraging this flexibility, we introduce a novel strided parallel generation strategy that accelerates inference by generating tokens in parallel streams while maintaining global coherence. Empirical results demonstrate that ARMD achieves state-of-the-art performance on standard language modeling benchmarks, outperforming established diffusion baselines while requiring significantly fewer training steps. Furthermore, it establishes a new benchmark for parallel text generation, effectively bridging the performance gap between parallel and sequential decoding.

## Metadata
- venue: 29th International Conference on Artificial Intelligence and Statistics (AISTATS) 2026
- year: 2026
- authors: Mahdi Karami, Ali Ghodsi
- arxiv_id: 2601.16971
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2601.16971v1
- published: 2026-01-23

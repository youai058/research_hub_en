---
title: "DyLLM: Efficient Diffusion LLM Inference via Saliency-based Token Selection and Partial Attention"
authors: ["Younjoo Lee", "Junghoo Lee", "Seungkyun Dan", "Jaiyoung Park", "Jung Ho Ahn"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.08026"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.08026v1"
published: "2026-03-09"
categories: ["cs.CL", "cs.AI", "cs.PF"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:13:58+09:00"
---

# DyLLM: Efficient Diffusion LLM Inference via Saliency-based Token Selection and Partial Attention

## Abstract
Masked Diffusion Language Models (MDLMs) enable parallel token decoding, providing a promising alternative to the sequential nature of autoregressive generation. However, their iterative denoising process remains computationally expensive because it repeatedly processes the entire sequence at every step. We observe that across these diffusion steps, most token representations remain stable; only a small subset, which we term salient tokens, contributes meaningfully to the next update. Leveraging this temporal sparsity, we present DyLLM, a training-free inference framework that accelerates decoding by selectively computing only these salient tokens. DyLLM identifies saliency by measuring the cosine similarity of attention contexts between adjacent denoising steps. It recomputes feed-forward and attention operations only for salient tokens while reusing cached activations for the remainder. Across diverse reasoning and code-generation benchmarks, DyLLM achieves up to 9.6x higher throughput while largely preserving the baseline accuracy of state-of-the-art models like LLaDA and Dream.

## Metadata
- venue: arXiv
- year: 2026
- authors: Younjoo Lee, Junghoo Lee, Seungkyun Dan, Jaiyoung Park, Jung Ho Ahn
- arxiv_id: 2603.08026
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.08026v1
- published: 2026-03-09

---
title: "Not All Denoising Steps Are Equal: Model Scheduling for Faster Masked Diffusion Language Models"
authors: ["Ivan Sedykh", "Nikita Sorokin", "Valentin Malykh"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2604.02340"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2604.02340v2"
published: "2026-02-04"
categories: ["cs.LG", "cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:05+09:00"
---

# Not All Denoising Steps Are Equal: Model Scheduling for Faster Masked Diffusion Language Models

## Abstract
Recent advances in masked diffusion language models (MDLMs) narrow the quality gap to autoregressive LMs, but their sampling remains expensive because generation requires many full-sequence denoising passes with a large Transformer and, unlike autoregressive decoding, cannot benefit from KV caching. In this work, we exploit the flexibility of the diffusion framework and study model scheduling, where a smaller MDLM replaces the full model at a subset of denoising steps. Across models trained on OpenWebText and LM1B, we show that early and late denoising steps are substantially more robust to such replacement than middle steps, enabling up to a 17% reduction in FLOPs with only modest degradation in generative perplexity under both unconditional and prefix-conditional generation, while preserving sample diversity. We support these findings with a step-importance analysis based on loss and KL divergence between small and large models across timesteps, as well as an exhaustive search over coarse step segments, both of which identify the middle of the diffusion trajectory as most sensitive consistently across datasets. Our results suggest that simple, architecture-agnostic scheduling rules can significantly accelerate MDLM sampling while largely preserving generation quality.

## Metadata
- venue: arXiv
- year: 2026
- authors: Ivan Sedykh, Nikita Sorokin, Valentin Malykh
- arxiv_id: 2604.02340
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2604.02340v2
- published: 2026-02-04

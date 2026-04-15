---
title: "Aligning Diffusion Language Models via Unpaired Preference Optimization"
authors: ["Vaibhav Jindal", "Hejian Sang", "Chun-Mao Lai", "Yanning Chen", "Zhipeng Wang"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.23658"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.23658v2"
published: "2025-10-26"
categories: ["cs.LG", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:06+09:00"
---

# Aligning Diffusion Language Models via Unpaired Preference Optimization

## Abstract
Diffusion language models (dLLMs) are an emerging alternative to autoregressive (AR) generators, but aligning them to human preferences is challenging because sequence log-likelihoods are intractable and pairwise preference data are costly to collect. We introduce ELBO-KTO, which combines an ELBO surrogate for diffusion log-likelihoods with a prospect-theoretic, unpaired preference objective (Kahneman Tversky Optimization, KTO). We analyze the bias and variance induced by the ELBO substitution and employ variance-reduction practices that stabilize gradients during training. Applied to LLaDA-8B-Instruct, ELBO-KTO yields 65.9% and 62.3% adjusted win rates on kto-mix-14k and UltraFeedback-Binary, respectively, versus the base model under an automatic LLM judge. Across downstream tasks, including GSM8K, MMLU, and additional reasoning/knowledge benchmarks, ELBO-KTO trained on UltraFeedback-Binary performs on par with or better than the base model under identical decoding. This establishes unpaired preference optimization as a viable alternative to pairwise alignment in diffusion LLMs.

## Metadata
- venue: arXiv
- year: 2025
- authors: Vaibhav Jindal, Hejian Sang, Chun-Mao Lai, Yanning Chen, Zhipeng Wang
- arxiv_id: 2510.23658
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.23658v2
- published: 2025-10-26

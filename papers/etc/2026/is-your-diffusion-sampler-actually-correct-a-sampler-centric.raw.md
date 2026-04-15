---
title: "Is Your Diffusion Sampler Actually Correct? A Sampler-Centric Evaluation of Discrete Diffusion Language Models"
authors: ["Luhan Tang", "Longxuan Yu", "Shaorong Zhang", "Greg Ver Steeg"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.19619"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.19619v1"
published: "2026-02-23"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:02+09:00"
---

# Is Your Diffusion Sampler Actually Correct? A Sampler-Centric Evaluation of Discrete Diffusion Language Models

## Abstract
Discrete diffusion language models (dLLMs) provide a fast and flexible alternative to autoregressive models (ARMs) via iterative denoising with parallel updates. However, their evaluation is challenging: existing metrics conflate denoiser approximation error with sampler-induced error from the sampling dynamics, a problem that does not arise for ARMs whose autoregressive sampling exactly reflects the learned probability model. We introduce a sampler-centric oracle framework that replaces learned denoisers with an exact Hidden Markov Model posterior derived from a ground-truth Markov chain, isolating sampler-induced error in a controlled setting. We show that few-step discrete diffusion samplers are not distributionally correct even under an oracle denoiser, with transition-level mismatch that vanishes only as the number of steps approaches the sequence length. Moreover, improvements in negative log-likelihood, generative perplexity, or MAUVE do not imply correct sampling. Code is available at https://luhantang.github.io/dllm_sampler

## Metadata
- venue: arXiv
- year: 2026
- authors: Luhan Tang, Longxuan Yu, Shaorong Zhang, Greg Ver Steeg
- arxiv_id: 2602.19619
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.19619v1
- published: 2026-02-23

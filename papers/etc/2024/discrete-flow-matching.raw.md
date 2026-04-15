---
title: "Discrete Flow Matching"
authors: ["Itai Gat", "Tal Remez", "Neta Shaul", "Felix Kreuk", "Ricky T. Q. Chen", "Gabriel Synnaeve", "Yossi Adi", "Yaron Lipman"]
venue: "arXiv"
year: 2024
venue_class: "etc"
arxiv_id: "2407.15595"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2407.15595v2"
published: "2024-07-22"
categories: ["cs.LG", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:20:12+09:00"
---

# Discrete Flow Matching

## Abstract
Despite Flow Matching and diffusion models having emerged as powerful generative paradigms for continuous variables such as images and videos, their application to high-dimensional discrete data, such as language, is still limited. In this work, we present Discrete Flow Matching, a novel discrete flow paradigm designed specifically for generating discrete data. Discrete Flow Matching offers several key contributions:(i) it works with a general family of probability paths interpolating between source and target distributions; (ii) it allows for a generic formula for sampling from these probability paths using learned posteriors such as the probability denoiser ($x$-prediction) and noise-prediction ($ε$-prediction); (iii) practically, focusing on specific probability paths defined with different schedulers improves generative perplexity compared to previous discrete diffusion and flow models; and (iv) by scaling Discrete Flow Matching models up to 1.7B parameters, we reach 6.7% Pass@1 and 13.4% Pass@10 on HumanEval and 6.7% Pass@1 and 20.6% Pass@10 on 1-shot MBPP coding benchmarks. Our approach is capable of generating high-quality discrete data in a non-autoregressive fashion, significantly closing the gap between autoregressive models and discrete flow models.

## Metadata
- venue: arXiv
- year: 2024
- authors: Itai Gat, Tal Remez, Neta Shaul, Felix Kreuk, Ricky T. Q. Chen, Gabriel Synnaeve, Yossi Adi, Yaron Lipman
- arxiv_id: 2407.15595
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2407.15595v2
- published: 2024-07-22

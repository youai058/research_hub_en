---
title: "d2: Improved Techniques for Training Reasoning Diffusion Language Models"
authors: ["Guanghan Wang", "Gilad Turok", "Yair Schiff", "Marianne Arriola", "Volodymyr Kuleshov"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2509.21474"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2509.21474v3"
published: "2025-09-25"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:14+09:00"
---

# d2: Improved Techniques for Training Reasoning Diffusion Language Models

## Abstract
While diffusion language models (DLMs) have achieved competitive performance in text generation, improving their reasoning ability with reinforcement learning remains an active research area. Here, we introduce d2, a reasoning framework tailored for masked DLMs. Central to our framework is a new policy gradient algorithm that relies on accurate estimates of the sampling trajectory likelihoods. Our likelihood estimator, d2-AnyOrder, achieves exact trajectory likelihood with a single model pass for DLMs that support a sampling algorithm called any-order decoding. Through an empirical study of widely used DLMs, we show that any-order decoding is not universally supported in practice. Consequently, for DLMs that do not naturally support any-order decoding, we propose another estimator, d2-StepMerge, which, unlike d2-AnyOrder, only approximates the trajectory likelihood. d2-StepMerge trades off compute for approximation accuracy in an analytically tractable manner. Empirically, d2 significantly outperforms widely-used RL baselines when applied to popular DLMs, and sets a new state-of-the-art performance for DLMs on logical reasoning tasks (Countdown and Sudoku) and math reasoning benchmarks (GSM8K and MATH500). We provide the code along with a blog post on the project page: https://guanghanwang.com/d2

## Metadata
- venue: arXiv
- year: 2025
- authors: Guanghan Wang, Gilad Turok, Yair Schiff, Marianne Arriola, Volodymyr Kuleshov
- arxiv_id: 2509.21474
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2509.21474v3
- published: 2025-09-25

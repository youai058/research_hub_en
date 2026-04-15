---
title: "Reward-Guided Discrete Diffusion via Clean-Sample Markov Chain for Molecule and Biological Sequence Design"
authors: ["Prin Phunyaphibarn", "Minhyuk Sung"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.09424"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.09424v1"
published: "2026-02-10"
categories: ["cs.LG", "q-bio.QM"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:32+09:00"
---

# Reward-Guided Discrete Diffusion via Clean-Sample Markov Chain for Molecule and Biological Sequence Design

## Abstract
Discrete diffusion models have recently emerged as a powerful class of generative models for chemistry and biology data. In these fields, the goal is to generate various samples with high rewards (e.g., drug-likeness in molecules), making reward-based guidance crucial. Most existing methods are based on guiding the diffusion model using intermediate rewards but tend to underperform since intermediate rewards are noisy due to the non-smooth nature of reward functions used in scientific domains. To address this, we propose Clean-Sample Markov Chain (CSMC) Sampler, a method that performs effective test-time reward-guided sampling for discrete diffusion models, enabling local search without relying on intermediate rewards. CSMC constructs a Markov chain of clean samples using the Metropolis-Hastings algorithm such that its stationary distribution is the target distribution. We design a proposal distribution by sequentially applying the forward and backward diffusion processes, making the acceptance probability tractable. Experiments on molecule and biological sequence generation with various reward functions demonstrate that our method consistently outperforms prior approaches that rely on intermediate rewards.

## Metadata
- venue: arXiv
- year: 2026
- authors: Prin Phunyaphibarn, Minhyuk Sung
- arxiv_id: 2602.09424
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.09424v1
- published: 2026-02-10

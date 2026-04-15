---
title: "Improving Reasoning for Diffusion Language Models via Group Diffusion Policy Optimization"
authors: ["Kevin Rojas", "Jiahe Lin", "Kashif Rasul", "Anderson Schneider", "Yuriy Nevmyvaka", "Molei Tao", "Wei Deng"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.08554"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.08554v3"
published: "2025-10-09"
categories: ["cs.LG", "stat.ML"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:10+09:00"
---

# Improving Reasoning for Diffusion Language Models via Group Diffusion Policy Optimization

## Abstract
Diffusion language models (DLMs) enable parallel, order-agnostic generation with iterative refinement, offering a flexible alternative to autoregressive large language models (LLMs). However, adapting reinforcement learning (RL) fine-tuning to DLMs remains an open challenge because of the intractable likelihood. Pioneering work such as diffu-GRPO estimated token-level likelihoods via one-step unmasking. While computationally efficient, this approach is severely biased. A more principled foundation lies in sequence-level likelihoods, where the evidence lower bound (ELBO) serves as a surrogate. Yet, despite this clean mathematical connection, ELBO-based methods have seen limited adoption due to the prohibitive cost of likelihood evaluation. In this work, we revisit ELBO estimation and disentangle its sources of variance. This decomposition motivates reducing variance through fast, deterministic integral approximations along a few pivotal dimensions. Building on this insight, we introduce Group Diffusion Policy Optimization (GDPO), a new RL algorithm tailored for DLMs. GDPO leverages simple yet effective Semi-deterministic Monte Carlo schemes to mitigate the variance explosion of ELBO estimators under vanilla double Monte Carlo sampling, yielding a provably lower-variance estimator under tight evaluation budgets. Empirically, GDPO achieves consistent gains over pretrained checkpoints and outperforms diffu-GRPO, one of the state-of-the-art baselines, on the majority of math, reasoning, and coding benchmarks.

## Metadata
- venue: arXiv
- year: 2025
- authors: Kevin Rojas, Jiahe Lin, Kashif Rasul, Anderson Schneider, Yuriy Nevmyvaka, Molei Tao, Wei Deng
- arxiv_id: 2510.08554
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.08554v3
- published: 2025-10-09

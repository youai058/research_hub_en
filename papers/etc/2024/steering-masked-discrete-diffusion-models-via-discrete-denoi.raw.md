---
title: "Steering Masked Discrete Diffusion Models via Discrete Denoising Posterior Prediction"
authors: ["Jarrid Rector-Brooks", "Mohsin Hasan", "Zhangzhi Peng", "Zachary Quinn", "Chenghao Liu", "Sarthak Mittal", "Nouha Dziri", "Michael Bronstein", "Yoshua Bengio", "Pranam Chatterjee", "Alexander Tong", "Avishek Joey Bose"]
venue: "arXiv"
year: 2024
venue_class: "etc"
arxiv_id: "2410.08134"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2410.08134v1"
published: "2024-10-10"
categories: ["cs.LG", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:20:05+09:00"
---

# Steering Masked Discrete Diffusion Models via Discrete Denoising Posterior Prediction

## Abstract
Generative modeling of discrete data underlies important applications spanning text-based agents like ChatGPT to the design of the very building blocks of life in protein sequences. However, application domains need to exert control over the generated data by steering the generative process - typically via RLHF - to satisfy a specified property, reward, or affinity metric. In this paper, we study the problem of steering Masked Diffusion Models (MDMs), a recent class of discrete diffusion models that offer a compelling alternative to traditional autoregressive models. We introduce Discrete Denoising Posterior Prediction (DDPP), a novel framework that casts the task of steering pre-trained MDMs as a problem of probabilistic inference by learning to sample from a target Bayesian posterior. Our DDPP framework leads to a family of three novel objectives that are all simulation-free, and thus scalable while applying to general non-differentiable reward functions. Empirically, we instantiate DDPP by steering MDMs to perform class-conditional pixel-level image modeling, RLHF-based alignment of MDMs using text-based rewards, and finetuning protein language models to generate more diverse secondary structures and shorter proteins. We substantiate our designs via wet-lab validation, where we observe transient expression of reward-optimized protein sequences.

## Metadata
- venue: arXiv
- year: 2024
- authors: Jarrid Rector-Brooks, Mohsin Hasan, Zhangzhi Peng, Zachary Quinn, Chenghao Liu, Sarthak Mittal, Nouha Dziri, Michael Bronstein, Yoshua Bengio, Pranam Chatterjee, Alexander Tong, Avishek Joey Bose
- arxiv_id: 2410.08134
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2410.08134v1
- published: 2024-10-10

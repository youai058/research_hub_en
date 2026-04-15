---
title: "Latent-Augmented Discrete Diffusion Models"
authors: ["Dario Shariatian", "Alain Durmus", "Umut Simsekli", "Stefano Peluchetti"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.18114"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.18114v2"
published: "2025-10-20"
categories: ["cs.LG", "cs.AI", "stat.ML"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:40+09:00"
---

# Latent-Augmented Discrete Diffusion Models

## Abstract
Discrete diffusion models have emerged as a powerful class of models and a promising route to fast language generation, but practical implementations typically rely on factored reverse transitions that ignore cross-token dependencies and degrade performance in the few-step regime. We propose Latent-Augmented Discrete Diffusion (LADD), which introduces a learnable auxiliary latent channel and performs diffusion over the joint (token, latent) space. The latent variables provide an intermediate representation that can express joint structure while preserving tractable parameterizations. We instantiate LADD with continuous latents (Co-LADD) and discrete latents (Di-LADD), and study two inference schedules: a joint diffusion that denoises data and latents together, and a sequential diffusion that first resolves latents and then samples tokens conditionally. We derive ELBO-style objectives and analyze design choices that balance latent expressivity with diffusion compatibility. In experiments, LADDs yield improvements on unconditional generation metrics as compared to state-of-the-art masked discrete diffusion baselines, and are effective at lower sampling budgets, where unmasking many tokens per step is desirable.

## Metadata
- venue: arXiv
- year: 2025
- authors: Dario Shariatian, Alain Durmus, Umut Simsekli, Stefano Peluchetti
- arxiv_id: 2510.18114
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.18114v2
- published: 2025-10-20

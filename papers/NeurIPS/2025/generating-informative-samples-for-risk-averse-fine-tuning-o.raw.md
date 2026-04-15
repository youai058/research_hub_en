---
title: "Generating Informative Samples for Risk-Averse Fine-Tuning of Downstream Tasks"
authors: ["Heasung Kim", "Taekyun Lee", "Hyeji Kim", "Gustavo De Veciana"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "kfB5Ciz2XZ"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b25b05c74fe4ba2989d38be8b7a439cfe68c26e8.pdf"
published: "2025"
categories: []
keywords: ["Generative models", "data augmentation", "score-based generative models", "risk", "importance sampling", "wireless communications", "applications"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:42+09:00"
---

# Generating Informative Samples for Risk-Averse Fine-Tuning of Downstream Tasks

## Abstract
Risk-averse modeling is critical in safety-sensitive and high-stakes applications. Conditional Value-at-Risk (CVaR) quantifies such risk by measuring the expected loss in the tail of the loss distribution, and minimizing it provides a principled framework for training robust models. However, direct CVaR minimization remains challenging due to the difficulty of accurately estimating rare, high-loss events—particularly at extreme quantiles. In this work, we propose a novel training framework that synthesizes informative samples for CVaR optimization using score-based generative models. Specifically, we guide a diffusion-based generative model to sample from a reweighted distribution that emphasizes inputs likely to incur high loss under a pretrained reference model. These samples are then incorporated via a loss-weighted importance sampling scheme to reduce noise in stochastic optimization. We establish convergence guarantees and show that the synthesized, high-loss-emphasized dataset substantially contributes to the noise reduction. Empirically, we validate the effectiveness of our approach across multiple settings, including a real-world wireless channel compression task, where our method achieves significant improvements over standard risk minimization strategies.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Heasung Kim, Taekyun Lee, Hyeji Kim, Gustavo De Veciana
- arxiv_id: 
- openreview_id: kfB5Ciz2XZ
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b25b05c74fe4ba2989d38be8b7a439cfe68c26e8.pdf
- published: 2025
- keywords: Generative models, data augmentation, score-based generative models, risk, importance sampling, wireless communications, applications

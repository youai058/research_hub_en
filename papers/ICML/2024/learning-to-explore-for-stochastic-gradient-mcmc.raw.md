---
title: "Learning to Explore for Stochastic Gradient MCMC"
authors: ["SeungHyun Kim", "Seohyeon Jung", "SeongHyeon Kim", "Juho Lee"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "aECamk9izk"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/7cd61fdb7890bbefac2f566b377407eef3758202.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:20+09:00"
---

# Learning to Explore for Stochastic Gradient MCMC

## Abstract
Bayesian Neural Networks(BNNs) with high-dimensional parameters pose a challenge for posterior inference due to the multi-modality of the posterior distributions. Stochastic Gradient Markov Chain Monte Carlo(SGMCMC) with cyclical learning rate scheduling is a promising solution, but it requires a large number of sampling steps to explore high-dimensional multi-modal posteriors, making it computationally expensive. In this paper, we propose a meta-learning strategy to build SGMCMC which can efficiently explore the multi-modal target distributions. Our algorithm allows the learned SGMCMC to quickly explore the high-density region of the posterior landscape. Also, we show that this exploration property is transferrable to various tasks, even for the ones unseen during a meta-training stage. Using popular image classification benchmarks and a variety of downstream tasks, we demonstrate that our method significantly improves the sampling efficiency, achieving better performance than vanilla SGMCMC without incurring significant computational overhead.

## Metadata
- venue: ICML
- year: 2024
- authors: SeungHyun Kim, Seohyeon Jung, SeongHyeon Kim, Juho Lee
- arxiv_id: 
- openreview_id: aECamk9izk
- anthology_id: 
- pdf_url: https://openreview.net/pdf/7cd61fdb7890bbefac2f566b377407eef3758202.pdf
- published: 2024

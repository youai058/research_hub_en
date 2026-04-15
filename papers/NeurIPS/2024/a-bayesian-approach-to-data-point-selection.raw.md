---
title: "A Bayesian Approach to Data Point Selection"
authors: ["Xinnuo Xu", "Minyoung Kim", "Royson Lee", "Brais Martinez", "Timothy Hospedales"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "9f5tOXKoMC"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/1cf4e6286ba1fb1d307ff6af679b5fb16b07aada.pdf"
published: "2024"
categories: []
keywords: ["Bayesian", "LLM", "Data selection", "Data unbalancing", "Data denoising", "Domain adaptation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:58+09:00"
---

# A Bayesian Approach to Data Point Selection

## Abstract
Data point selection (DPS) is becoming a critical topic in deep learning due to the ease of acquiring uncurated training data compared to the difficulty of obtaining curated or processed data. 
Existing approaches to DPS are predominantly based on a bi-level optimisation (BLO) formulation, which is demanding in terms of memory and computation, and exhibits some theoretical defects regarding minibatches.
Thus, we propose a novel Bayesian approach to DPS. We view the DPS problem as posterior inference in a novel Bayesian model where the posterior distributions of the instance-wise weights and the main neural network parameters are inferred under a reasonable prior and likelihood model.
We employ stochastic gradient Langevin MCMC sampling to learn the main network and instance-wise weights jointly, ensuring convergence even with minibatches. Our update equation is comparable to the widely used SGD and much more efficient than existing BLO-based methods. Through controlled experiments in both the vision and language domains, we present the proof-of-concept. Additionally, we demonstrate that our method scales effectively to large language models and facilitates automated per-task optimization for instruction fine-tuning datasets.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Xinnuo Xu, Minyoung Kim, Royson Lee, Brais Martinez, Timothy Hospedales
- arxiv_id: 
- openreview_id: 9f5tOXKoMC
- anthology_id: 
- pdf_url: https://openreview.net/pdf/1cf4e6286ba1fb1d307ff6af679b5fb16b07aada.pdf
- published: 2024
- keywords: Bayesian, LLM, Data selection, Data unbalancing, Data denoising, Domain adaptation

---
title: "Collaborative Heterogeneous Causal Inference Beyond Meta-analysis"
authors: ["Tianyu Guo", "Sai Praneeth Karimireddy", "Michael Jordan"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "LJ34pX1U5g"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d80004b5aec30f201b8c35adbe8d2616f49c8ed6.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:45+09:00"
---

# Collaborative Heterogeneous Causal Inference Beyond Meta-analysis

## Abstract
Collaboration between different data centers is often challenged by heterogeneity across sites. To account for the heterogeneity, the state-of-the-art method is to re-weight the covariate distributions in each site to match the distribution of the target population. Nevertheless, this method still relies on the concept of traditional meta-analysis after adjusting for the distribution shift. This work proposes a collaborative inverse propensity score weighting estimator for causal inference with heterogeneous data. Instead of adjusting the distribution shift separately, we use weighted propensity score models to collaboratively adjust for the distribution shift. Our method shows significant improvements over the methods based on meta-analysis when heterogeneity increases. By incorporating outcome regression models, we prove the asymptotic normality when the covariates have dimension $d<8$. Our methods preserve privacy at individual sites by implementing federated learning protocols.

## Metadata
- venue: ICML
- year: 2024
- authors: Tianyu Guo, Sai Praneeth Karimireddy, Michael Jordan
- arxiv_id: 
- openreview_id: LJ34pX1U5g
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d80004b5aec30f201b8c35adbe8d2616f49c8ed6.pdf
- published: 2024

---
title: "Simulation-Based Inference with Quantile Regression"
authors: ["He Jia"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "vGHOFeUQi8"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/62f78fde0ad702666284f4b7604e01aed73b240c.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:32+09:00"
---

# Simulation-Based Inference with Quantile Regression

## Abstract
We present Neural Quantile Estimation (NQE), a novel Simulation-Based Inference (SBI) method based on conditional quantile regression. NQE autoregressively learns individual one dimensional quantiles for each posterior dimension, conditioned on the data and previous posterior dimensions. Posterior samples are obtained by interpolating the predicted quantiles using monotonic cubic Hermite spline, with specific treatment for the tail behavior and multi-modal distributions. We introduce an alternative definition for the Bayesian credible region using the local Cumulative Density Function (CDF), offering substantially faster evaluation than the traditional Highest Posterior Density Region (HPDR). In case of limited simulation budget and/or known model misspecification, a post-processing calibration step can be integrated into NQE to ensure the unbiasedness of the posterior estimation with negligible additional computational cost. We demonstrate that NQE achieves state-of-the-art performance on a variety of benchmark problems.

## Metadata
- venue: ICML
- year: 2024
- authors: He Jia
- arxiv_id: 
- openreview_id: vGHOFeUQi8
- anthology_id: 
- pdf_url: https://openreview.net/pdf/62f78fde0ad702666284f4b7604e01aed73b240c.pdf
- published: 2024

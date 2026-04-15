---
title: "Unsupervised Anomaly Detection via Masked Diffusion Posterior Sampling"
authors: ["Di Wu", "Shicai Fan", "Xue Zhou", "Li Yu", "Yuzhong Deng", "Jianxiao Zou", "Baihong Lin"]
venue: "International Joint Conference on Artificial Intelligence 2024"
year: 2024
venue_class: "etc"
arxiv_id: "2404.17900"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2404.17900v1"
published: "2024-04-27"
categories: ["cs.CV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:20:05+09:00"
---

# Unsupervised Anomaly Detection via Masked Diffusion Posterior Sampling

## Abstract
Reconstruction-based methods have been commonly used for unsupervised anomaly detection, in which a normal image is reconstructed and compared with the given test image to detect and locate anomalies. Recently, diffusion models have shown promising applications for anomaly detection due to their powerful generative ability. However, these models lack strict mathematical support for normal image reconstruction and unexpectedly suffer from low reconstruction quality. To address these issues, this paper proposes a novel and highly-interpretable method named Masked Diffusion Posterior Sampling (MDPS). In MDPS, the problem of normal image reconstruction is mathematically modeled as multiple diffusion posterior sampling for normal images based on the devised masked noisy observation model and the diffusion-based normal image prior under Bayesian framework. Using a metric designed from pixel-level and perceptual-level perspectives, MDPS can effectively compute the difference map between each normal posterior sample and the given test image. Anomaly scores are obtained by averaging all difference maps for multiple posterior samples. Exhaustive experiments on MVTec and BTAD datasets demonstrate that MDPS can achieve state-of-the-art performance in normal image reconstruction quality as well as anomaly detection and localization.

## Metadata
- venue: International Joint Conference on Artificial Intelligence 2024
- year: 2024
- authors: Di Wu, Shicai Fan, Xue Zhou, Li Yu, Yuzhong Deng, Jianxiao Zou, Baihong Lin
- arxiv_id: 2404.17900
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2404.17900v1
- published: 2024-04-27

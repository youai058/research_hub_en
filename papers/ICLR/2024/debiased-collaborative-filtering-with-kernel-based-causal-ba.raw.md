---
title: "Debiased Collaborative Filtering with Kernel-Based Causal Balancing"
authors: ["Haoxuan Li", "Chunyuan Zheng", "Yanghao Xiao", "Peng Wu", "Zhi Geng", "Xu Chen", "Peng Cui"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Ffjc8ApSbt"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c070b5e86750458e4f0f6540b5c8528297d494f8.pdf"
published: "2024"
categories: []
keywords: ["Recommender System", "Causal Inference", "Bias", "Debias", "Balancing"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:55+09:00"
---

# Debiased Collaborative Filtering with Kernel-Based Causal Balancing

## Abstract
Collaborative filtering builds personalized models from the collected user feedback. However, the collected data is observational rather than experimental, leading to various biases in the data, which can significantly affect the learned model. To address this issue, many studies have focused on propensity-based methods to combat the selection bias by reweighting the sample loss, and demonstrate that
balancing is important for debiasing both theoretically and empirically. However, there are two questions that still need to be addressed: which function class should be balanced and how to effectively balance that function class? In this paper, we first perform theoretical analysis to show the effect of balancing finite-dimensional function classes on the bias of IPS and DR methods, and based on this, we propose a universal kernel-based balancing method to balance functions on the reproducing kernel Hilbert space. In addition, we propose a novel adaptive causal balancing method during the alternating update between unbiased evaluation and training of the prediction model. Specifically, the prediction loss of the model is projected in the kernel-based covariate function space, and the projection coefficients are used to determine which functions should be prioritized for balancing to reduce the estimation bias. We conduct extensive experiments on three real-world datasets to demonstrate the effectiveness of the proposed approach.

## Metadata
- venue: ICLR
- year: 2024
- authors: Haoxuan Li, Chunyuan Zheng, Yanghao Xiao, Peng Wu, Zhi Geng, Xu Chen, Peng Cui
- arxiv_id: 
- openreview_id: Ffjc8ApSbt
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c070b5e86750458e4f0f6540b5c8528297d494f8.pdf
- published: 2024
- keywords: Recommender System, Causal Inference, Bias, Debias, Balancing

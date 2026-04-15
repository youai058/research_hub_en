---
title: "Locality Sensitive Sparse Encoding for Learning World Models Online"
authors: ["Zichen Liu", "Chao Du", "Wee Sun Lee", "Min Lin"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "i8PjQT3Uig"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/0149a804bccf18bec867875f9e9fb664c4288f4b.pdf"
published: "2024"
categories: []
keywords: ["model-based rl", "online learning", "incremental learning", "catastrophic forgetting"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:47+09:00"
---

# Locality Sensitive Sparse Encoding for Learning World Models Online

## Abstract
Acquiring an accurate world model $\textit{online}$ for model-based reinforcement learning (MBRL) is challenging due to data nonstationarity, which typically causes catastrophic forgetting for neural networks (NNs). From the online learning perspective, a Follow-The-Leader (FTL) world model is desirable, which optimally fits all previous experiences at each round. Unfortunately, NN-based models need re-training on all accumulated data at every interaction step to achieve FTL, which is computationally expensive for lifelong agents. In this paper, we revisit models that can achieve FTL with incremental updates. Specifically, our world model is a linear regression model supported by nonlinear random features. The linear part ensures efficient FTL update while the nonlinear random feature empowers the fitting of complex environments. To best trade off model capacity and computation efficiency, we introduce a locality sensitive sparse encoding, which allows us to conduct efficient sparse updates even with very high dimensional nonlinear features. We validate the representation power of our encoding and verify that it allows efficient online learning under data covariate shift. We also show, in the Dyna MBRL setting, that our world models learned online using a $\textit{single pass}$ of trajectory data either surpass or match the performance of deep world models trained with replay and other continual learning methods.

## Metadata
- venue: ICLR
- year: 2024
- authors: Zichen Liu, Chao Du, Wee Sun Lee, Min Lin
- arxiv_id: 
- openreview_id: i8PjQT3Uig
- anthology_id: 
- pdf_url: https://openreview.net/pdf/0149a804bccf18bec867875f9e9fb664c4288f4b.pdf
- published: 2024
- keywords: model-based rl, online learning, incremental learning, catastrophic forgetting

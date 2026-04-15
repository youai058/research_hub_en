---
title: "Scalable Wasserstein Gradient Flow for Generative Modeling through Unbalanced Optimal Transport"
authors: ["Jaemoo Choi", "Jaewoong Choi", "Myungjoo Kang"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "dMhF96PfQi"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9dd6ffcb20c0f55c16a4bcde34bc1141e26da208.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:23+09:00"
---

# Scalable Wasserstein Gradient Flow for Generative Modeling through Unbalanced Optimal Transport

## Abstract
Wasserstein gradient flow (WGF) describes the gradient dynamics of probability density within the Wasserstein space. WGF provides a promising approach for conducting optimization over the probability distributions. Numerically approximating the continuous WGF requires the time discretization method. The most well-known method for this is the JKO scheme. In this regard, previous WGF models employ the JKO scheme and parametrized transport map for each JKO step. However, this approach results in quadratic training complexity $O(K^2)$ with the number of JKO step $K$. This severely limits the scalability of WGF models. In this paper, we introduce a scalable WGF-based generative model, called Semi-dual JKO (S-JKO). Our model is based on the semi-dual form of the JKO step, derived from the equivalence between the JKO step and the Unbalanced Optimal Transport. Our approach reduces the training complexity to $O(K)$. We demonstrate that our model significantly outperforms existing WGF-based generative models, achieving FID scores of 2.62 on CIFAR-10 and 6.42 on CelebA-HQ-256, which are comparable to state-of-the-art image generative models.

## Metadata
- venue: ICML
- year: 2024
- authors: Jaemoo Choi, Jaewoong Choi, Myungjoo Kang
- arxiv_id: 
- openreview_id: dMhF96PfQi
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9dd6ffcb20c0f55c16a4bcde34bc1141e26da208.pdf
- published: 2024

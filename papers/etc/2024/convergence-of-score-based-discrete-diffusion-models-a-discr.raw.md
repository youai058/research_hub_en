---
title: "Convergence of Score-Based Discrete Diffusion Models: A Discrete-Time Analysis"
authors: ["Zikun Zhang", "Zixiang Chen", "Quanquan Gu"]
venue: "The Thirteenth International Conference on Learning Representations, 2025"
year: 2024
venue_class: "etc"
arxiv_id: "2410.02321"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2410.02321v2"
published: "2024-10-03"
categories: ["cs.LG", "stat.ML"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:20:12+09:00"
---

# Convergence of Score-Based Discrete Diffusion Models: A Discrete-Time Analysis

## Abstract
Diffusion models have achieved great success in generating high-dimensional samples across various applications. While the theoretical guarantees for continuous-state diffusion models have been extensively studied, the convergence analysis of the discrete-state counterparts remains under-explored. In this paper, we study the theoretical aspects of score-based discrete diffusion models under the Continuous Time Markov Chain (CTMC) framework. We introduce a discrete-time sampling algorithm in the general state space $[S]^d$ that utilizes score estimators at predefined time points. We derive convergence bounds for the Kullback-Leibler (KL) divergence and total variation (TV) distance between the generated sample distribution and the data distribution, considering both scenarios with and without early stopping under reasonable assumptions. Notably, our KL divergence bounds are nearly linear in the dimension $d$, aligning with state-of-the-art results for diffusion models. Our convergence analysis employs a Girsanov-based method and establishes key properties of the discrete score function, which are essential for characterizing the discrete-time sampling process.

## Metadata
- venue: The Thirteenth International Conference on Learning Representations, 2025
- year: 2024
- authors: Zikun Zhang, Zixiang Chen, Quanquan Gu
- arxiv_id: 2410.02321
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2410.02321v2
- published: 2024-10-03

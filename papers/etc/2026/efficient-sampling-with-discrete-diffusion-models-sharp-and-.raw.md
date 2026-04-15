---
title: "Efficient Sampling with Discrete Diffusion Models: Sharp and Adaptive Guarantees"
authors: ["Daniil Dmitriev", "Zhihan Huang", "Yuting Wei"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.15008"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.15008v1"
published: "2026-02-16"
categories: ["cs.LG", "cs.IT", "math.ST", "stat.ML"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:32+09:00"
---

# Efficient Sampling with Discrete Diffusion Models: Sharp and Adaptive Guarantees

## Abstract
Diffusion models over discrete spaces have recently shown striking empirical success, yet their theoretical foundations remain incomplete. In this paper, we study the sampling efficiency of score-based discrete diffusion models under a continuous-time Markov chain (CTMC) formulation, with a focus on $τ$-leaping-based samplers. We establish sharp convergence guarantees for attaining $\varepsilon$ accuracy in Kullback-Leibler (KL) divergence for both uniform and masking noising processes. For uniform discrete diffusion, we show that the $τ$-leaping algorithm achieves an iteration complexity of order $\tilde O(d/\varepsilon)$, with $d$ the ambient dimension of the target distribution, eliminating linear dependence on the vocabulary size $S$ and improving existing bounds by a factor of $d$; moreover, we establish a matching algorithmic lower bound showing that linear dependence on the ambient dimension is unavoidable in general. For masking discrete diffusion, we introduce a modified $τ$-leaping sampler whose convergence rate is governed by an intrinsic information-theoretic quantity, termed the effective total correlation, which is bounded by $d \log S$ but can be sublinear or even constant for structured data. As a consequence, the sampler provably adapts to low-dimensional structure without prior knowledge or algorithmic modification, yielding sublinear convergence rates for various practical examples (such as hidden Markov models, image data, and random graphs). Our analysis requires no boundedness or smoothness assumptions on the score estimator beyond control of the score entropy loss.

## Metadata
- venue: arXiv
- year: 2026
- authors: Daniil Dmitriev, Zhihan Huang, Yuting Wei
- arxiv_id: 2602.15008
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.15008v1
- published: 2026-02-16

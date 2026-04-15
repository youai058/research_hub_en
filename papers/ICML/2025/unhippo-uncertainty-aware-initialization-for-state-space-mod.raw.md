---
title: "UnHiPPO: Uncertainty-aware Initialization for State Space Models"
authors: ["Marten Lienen", "Abdullah Saydemir", "Stephan Günnemann"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "U8GUmxnzXn"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/20432296a22e025c99c7606bf8be6f3b437ebc58.pdf"
published: "2025"
categories: []
keywords: ["state space", "uncertainty", "hippo", "mamba", "kalman", "noise", "filter"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:02+09:00"
---

# UnHiPPO: Uncertainty-aware Initialization for State Space Models

## Abstract
State space models are emerging as a dominant model class for sequence problems with many relying on the HiPPO framework to initialize their dynamics. However, HiPPO fundamentally assumes data to be noise-free; an assumption often violated in practice. We extend the HiPPO theory with measurement noise and derive an uncertainty-aware initialization for state space model dynamics. In our analysis, we interpret HiPPO as a linear stochastic control problem where the data enters as a noise-free control signal. We then reformulate the problem so that the data become noisy outputs of a latent system and arrive at an alternative dynamics initialization that infers the posterior of this latent system from the data without increasing runtime. Our experiments show that our initialization improves the resistance of state-space models to noise both at training and inference time.

## Metadata
- venue: ICML
- year: 2025
- authors: Marten Lienen, Abdullah Saydemir, Stephan Günnemann
- arxiv_id: 
- openreview_id: U8GUmxnzXn
- anthology_id: 
- pdf_url: https://openreview.net/pdf/20432296a22e025c99c7606bf8be6f3b437ebc58.pdf
- published: 2025
- keywords: state space, uncertainty, hippo, mamba, kalman, noise, filter

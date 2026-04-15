---
title: "Compositional simulation-based inference for time series"
authors: ["Manuel Gloeckler", "Shoji Toyota", "Kenji Fukumizu", "Jakob H. Macke"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "uClUUJk05H"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/1dbae3c70d8c2fc5739a83e2aa1534ecb821b10c.pdf"
published: "2025"
categories: []
keywords: ["Simulation-based inference", "Bayesian inference", "time series", "markovian simulators", "Amortized Bayesian inference"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:41+09:00"
---

# Compositional simulation-based inference for time series

## Abstract
Amortized simulation-based inference (SBI) methods train neural networks on simulated data to perform Bayesian inference. While this strategy avoids the need for tractable likelihoods, it often requires a large number of simulations and has been challenging to scale to time series data. Scientific simulators frequently emulate real-world dynamics through thousands of single-state transitions over time. We propose an SBI approach that can exploit such Markovian simulators by locally identifying parameters consistent with individual state transitions. We then compose these local results to obtain a posterior over parameters that align with the entire time series observation. We focus on applying this approach to neural posterior score estimation but also show how it can be applied, e.g., to neural likelihood (ratio) estimation. We demonstrate that our approach is more simulation-efficient than directly estimating the global posterior on several synthetic benchmark tasks and simulators used in ecology and epidemiology. Finally, we validate scalability and simulation efficiency of our approach by applying it to a high-dimensional Kolmogorov flow simulator with around one million data dimensions.

## Metadata
- venue: ICLR
- year: 2025
- authors: Manuel Gloeckler, Shoji Toyota, Kenji Fukumizu, Jakob H. Macke
- arxiv_id: 
- openreview_id: uClUUJk05H
- anthology_id: 
- pdf_url: https://openreview.net/pdf/1dbae3c70d8c2fc5739a83e2aa1534ecb821b10c.pdf
- published: 2025
- keywords: Simulation-based inference, Bayesian inference, time series, markovian simulators, Amortized Bayesian inference

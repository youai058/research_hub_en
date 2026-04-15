---
title: "LEAPS: A discrete neural sampler via locally equivariant networks"
authors: ["Peter Holderrieth", "Michael Samuel Albergo", "Tommi Jaakkola"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Hq2RniQAET"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/17fc3bc856b7088c261326a99542cbb83974ca11.pdf"
published: "2025"
categories: []
keywords: ["CTMC", "Bayesian inference", "MCMC", "sampling"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:37+09:00"
---

# LEAPS: A discrete neural sampler via locally equivariant networks

## Abstract
We propose *LEAPS*, an algorithm to sample from discrete distributions known up to normalization by learning a rate matrix of a continuous-time Markov chain (CTMC). LEAPS can be seen as a continuous-time formulation of annealed importance sampling and sequential Monte Carlo methods, extended so that the variance of the importance weights is offset by the inclusion of the CTMC. To derive these importance weights, we introduce a set of Radon-Nikodym derivatives of CTMCs over their path measures. Because the computation of these weights is intractable with standard neural network parameterizations of rate matrices, we devise a new compact representation for rate matrices via what we call \textit{locally equivariant} functions. To parameterize them, we introduce a family of locally equivariant multilayer perceptrons, attention layers, and convolutional networks, and provide an approach to make deep networks that preserve the local equivariance. This property allows us to propose a scalable training algorithm for the rate matrix such that the variance of the importance weights associated to the CTMC are minimal. We demonstrate the efficacy of LEAPS on problems in statistical physics. We provide code in https://github.com/malbergo/leaps/.

## Metadata
- venue: ICML
- year: 2025
- authors: Peter Holderrieth, Michael Samuel Albergo, Tommi Jaakkola
- arxiv_id: 
- openreview_id: Hq2RniQAET
- anthology_id: 
- pdf_url: https://openreview.net/pdf/17fc3bc856b7088c261326a99542cbb83974ca11.pdf
- published: 2025
- keywords: CTMC, Bayesian inference, MCMC, sampling

---
title: "Discrete generative diffusion models without stochastic differential equations: a tensor network approach"
authors: ["Luke Causer", "Grant M. Rotskoff", "Juan P. Garrahan"]
venue: "arXiv"
year: 2024
venue_class: "etc"
arxiv_id: "2407.11133"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2407.11133v1"
published: "2024-07-15"
categories: ["cond-mat.stat-mech", "cond-mat.dis-nn", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:20:12+09:00"
---

# Discrete generative diffusion models without stochastic differential equations: a tensor network approach

## Abstract
Diffusion models (DMs) are a class of generative machine learning methods that sample a target distribution by transforming samples of a trivial (often Gaussian) distribution using a learned stochastic differential equation. In standard DMs, this is done by learning a ``score function'' that reverses the effect of adding diffusive noise to the distribution of interest. Here we consider the generalisation of DMs to lattice systems with discrete degrees of freedom, and where noise is added via Markov chain jump dynamics. We show how to use tensor networks (TNs) to efficiently define and sample such ``discrete diffusion models'' (DDMs) without explicitly having to solve a stochastic differential equation. We show the following: (i) by parametrising the data and evolution operators as TNs, the denoising dynamics can be represented exactly; (ii) the auto-regressive nature of TNs allows to generate samples efficiently and without bias; (iii) for sampling Boltzmann-like distributions, TNs allow to construct an efficient learning scheme that integrates well with Monte Carlo. We illustrate this approach to study the equilibrium of two models with non-trivial thermodynamics, the $d=1$ constrained Fredkin chain and the $d=2$ Ising model.

## Metadata
- venue: arXiv
- year: 2024
- authors: Luke Causer, Grant M. Rotskoff, Juan P. Garrahan
- arxiv_id: 2407.11133
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2407.11133v1
- published: 2024-07-15

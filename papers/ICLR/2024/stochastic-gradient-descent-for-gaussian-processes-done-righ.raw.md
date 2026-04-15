---
title: "Stochastic Gradient Descent for Gaussian Processes Done Right"
authors: ["Jihao Andreas Lin", "Shreyas Padhy", "Javier Antoran", "Austin Tripp", "Alexander Terenin", "Csaba Szepesvari", "José Miguel Hernández-Lobato", "David Janz"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "fj2E5OcLFn"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/1a24ae39cc44caaeb65f4c46067a7b5c53a0ed95.pdf"
published: "2024"
categories: []
keywords: ["Gaussian process", "stochastic gradient descent"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:19+09:00"
---

# Stochastic Gradient Descent for Gaussian Processes Done Right

## Abstract
As is well known, both sampling from the posterior and computing the mean of the posterior in Gaussian process regression reduces to solving a large linear system of equations. We study the use of stochastic gradient descent for solving this linear system, and show that when done right---by which we mean using specific insights from the optimisation and kernel communities---stochastic gradient descent is highly effective. To that end, we introduce a particularly simple stochastic dual descent algorithm, explain its design in an intuitive manner and illustrate the design choices through a series of ablation studies. Further experiments demonstrate that our new method is highly competitive. In particular, our evaluations on the UCI regression tasks and on Bayesian optimisation set our approach apart from preconditioned conjugate gradients and variational Gaussian process approximations. Moreover, our method places Gaussian process regression on par with state-of-the-art graph neural networks for molecular binding affinity prediction.

## Metadata
- venue: ICLR
- year: 2024
- authors: Jihao Andreas Lin, Shreyas Padhy, Javier Antoran, Austin Tripp, Alexander Terenin, Csaba Szepesvari, José Miguel Hernández-Lobato, David Janz
- arxiv_id: 
- openreview_id: fj2E5OcLFn
- anthology_id: 
- pdf_url: https://openreview.net/pdf/1a24ae39cc44caaeb65f4c46067a7b5c53a0ed95.pdf
- published: 2024
- keywords: Gaussian process, stochastic gradient descent

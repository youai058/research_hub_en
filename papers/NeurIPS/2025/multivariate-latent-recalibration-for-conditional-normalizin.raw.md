---
title: "Multivariate Latent Recalibration for Conditional Normalizing Flows"
authors: ["Victor Dheur", "Souhaib Ben Taieb"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "nO8ShqG2ci"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/94e55dfc1d323eb5ce11bb763f966c3be6075766.pdf"
published: "2025"
categories: []
keywords: ["Uncertainty Quantification", "Model Calibration", "Multi-response regression", "Model Recalibration", "Generative Models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:33+09:00"
---

# Multivariate Latent Recalibration for Conditional Normalizing Flows

## Abstract
A reliable estimate of the full conditional distribution of a multivariate response given a set of covariates is essential in many decision-making applications. However, misspecified or miscalibrated models can lead to poor approximations of the joint distribution, resulting in unreliable predictions and suboptimal decisions. Standard recalibration methods are largely restricted to univariate settings, and while conformal prediction techniques yield multivariate regions with coverage guarantees, they do not provide an explicit form of the underlying probability distribution. We address this gap by first introducing a novel notion of latent calibration, which assesses probabilistic calibration in the latent space of conditional invertible generative models such as normalizing flows and flow matching. Second, we propose latent recalibration (LR), a post-hoc model recalibration method that learns a transformation of the latent space with finite-sample bounds on latent calibration. Unlike existing recalibration methods, LR produces a recalibrated distribution with an explicit multivariate density function while remaining computationally efficient. Extensive experiments on both tabular and image datasets show that LR consistently improves latent calibration error and the negative log-likelihood of the recalibrated models.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Victor Dheur, Souhaib Ben Taieb
- arxiv_id: 
- openreview_id: nO8ShqG2ci
- anthology_id: 
- pdf_url: https://openreview.net/pdf/94e55dfc1d323eb5ce11bb763f966c3be6075766.pdf
- published: 2025
- keywords: Uncertainty Quantification, Model Calibration, Multi-response regression, Model Recalibration, Generative Models

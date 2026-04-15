---
title: "Nonsmooth Implicit Differentiation: Deterministic and Stochastic Convergence Rates"
authors: ["Riccardo Grazzi", "Massimiliano Pontil", "Saverio Salzo"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "SlRcJvf1yd"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/025bbee5bd20d29f0f87e25a9ae97921d508ad88.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:48+09:00"
---

# Nonsmooth Implicit Differentiation: Deterministic and Stochastic Convergence Rates

## Abstract
We study the problem of efficiently computing the derivative of the fixed-point of a parametric nondifferentiable contraction map. This problem has wide applications in machine learning, including hyperparameter optimization, meta-learning and data poisoning attacks. We analyze two popular approaches: iterative differentiation (ITD) and approximate implicit differentiation (AID). A key challenge behind the nonsmooth setting is that the chain rule does not hold anymore. We build upon the work by Bolte et al. (2022), who prove linear convergence of nonsmooth ITD under a piecewise Lipschitz smooth assumption. In the deterministic case, we provide a linear rate for AID and an improved linear rate for ITD which closely match the ones for the smooth setting. We further introduce NSID, a new stochastic method to compute the implicit derivative when the contraction map is defined as the composition of an outer map and an inner map which is accessible only through a stochastic unbiased estimator. We establish rates for the convergence of NSID, encompassing the best available rates in the smooth setting. We also present illustrative experiments confirming our analysis.

## Metadata
- venue: ICML
- year: 2024
- authors: Riccardo Grazzi, Massimiliano Pontil, Saverio Salzo
- arxiv_id: 
- openreview_id: SlRcJvf1yd
- anthology_id: 
- pdf_url: https://openreview.net/pdf/025bbee5bd20d29f0f87e25a9ae97921d508ad88.pdf
- published: 2024

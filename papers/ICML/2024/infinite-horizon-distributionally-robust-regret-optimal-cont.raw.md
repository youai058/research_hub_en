---
title: "Infinite-Horizon Distributionally Robust Regret-Optimal Control"
authors: ["Taylan Kargin", "Joudi Hajar", "Vikrant Malik", "Babak Hassibi"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "h3SGdpI4Ta"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/bc8ca3fcd7d9386d49cc99289316c7a286e82ecf.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:19+09:00"
---

# Infinite-Horizon Distributionally Robust Regret-Optimal Control

## Abstract
We study the infinite-horizon distributionally robust (DR) control of linear systems with quadratic costs, where disturbances have unknown, possibly time-correlated distribution within a Wasserstein-2 ambiguity set. We aim to minimize the worst-case expected regret—the excess cost of a causal policy compared to a non-causal one with access to future disturbance. Though the optimal policy lacks a finite-order state-space realization (i.e., it is non-rational), it can be characterized by a finite-dimensional parameter. Leveraging this, we develop an efficient frequency-domain algorithm to compute this optimal control policy and present a convex optimization method to construct a near-optimal state-space controller that approximates the optimal non-rational controller in the $\mathit{H}_\infty$-norm. This approach avoids solving a computationally expensive semi-definite program (SDP) that scales with the time horizon in the finite-horizon setting.

## Metadata
- venue: ICML
- year: 2024
- authors: Taylan Kargin, Joudi Hajar, Vikrant Malik, Babak Hassibi
- arxiv_id: 
- openreview_id: h3SGdpI4Ta
- anthology_id: 
- pdf_url: https://openreview.net/pdf/bc8ca3fcd7d9386d49cc99289316c7a286e82ecf.pdf
- published: 2024

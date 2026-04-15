---
title: "SILVER: Single-loop variance reduction and application to federated learning"
authors: ["Kazusato Oko", "Shunta Akiyama", "Denny Wu", "Tomoya Murata", "Taiji Suzuki"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "pOgMluzEIH"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/0f3db8fcef596676b00a10c815489412de542703.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:21+09:00"
---

# SILVER: Single-loop variance reduction and application to federated learning

## Abstract
Most variance reduction methods require multiple times of full gradient computation, which is time-consuming and hence a bottleneck in application to distributed optimization. We present a single-loop variance-reduced gradient estimator named SILVER (SIngle-Loop VariancE-Reduction) for the finite-sum non-convex optimization, which does not require multiple full gradients but nevertheless achieves the optimal gradient complexity. Notably, unlike existing methods, SILVER provably reaches second-order optimality, with exponential convergence in the Polyak-Łojasiewicz (PL) region, and achieves further speedup depending on the data heterogeneity. Owing to these advantages, SILVER serves as a new base method to design communication-efficient federated learning algorithms: we combine SILVER with local updates which gives the best communication rounds and number of communicated gradients across all range of Hessian heterogeneity, and, at the same time, guarantees second-order optimality and exponential convergence in the PL region.

## Metadata
- venue: ICML
- year: 2024
- authors: Kazusato Oko, Shunta Akiyama, Denny Wu, Tomoya Murata, Taiji Suzuki
- arxiv_id: 
- openreview_id: pOgMluzEIH
- anthology_id: 
- pdf_url: https://openreview.net/pdf/0f3db8fcef596676b00a10c815489412de542703.pdf
- published: 2024

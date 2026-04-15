---
title: "Neural SPH: Improved Neural Modeling of Lagrangian Fluid Dynamics"
authors: ["Artur Toshev", "Jonas A. Erbesdobler", "Nikolaus A. Adams", "Johannes Brandstetter"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Pbey7LqBRl"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/53182af45fcf0099abe6b0bb31019b2e0bb08060.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:45+09:00"
---

# Neural SPH: Improved Neural Modeling of Lagrangian Fluid Dynamics

## Abstract
Smoothed particle hydrodynamics (SPH) is omnipresent in modern engineering and scientific disciplines. SPH is a class of Lagrangian schemes that discretize fluid dynamics via finite material points that are tracked through the evolving velocity field. Due to the particle-like nature of the simulation, graph neural networks (GNNs) have emerged as appealing and successful surrogates. However, the practical utility of such GNN-based simulators relies on their ability to faithfully model physics, providing accurate and stable predictions over long time horizons - which is a notoriously hard problem. In this work, we identify particle clustering originating from tensile instabilities as one of the primary pitfalls. Based on these insights, we enhance both training and rollout inference of state-of-the-art GNN-based simulators with varying components from standard SPH solvers, including pressure, viscous, and external force components. All Neural SPH-enhanced simulators achieve better performance than the baseline GNNs, often by orders of magnitude in terms of rollout error, allowing for significantly longer rollouts and significantly better physics modeling. Code available under https://github.com/tumaer/neuralsph.

## Metadata
- venue: ICML
- year: 2024
- authors: Artur Toshev, Jonas A. Erbesdobler, Nikolaus A. Adams, Johannes Brandstetter
- arxiv_id: 
- openreview_id: Pbey7LqBRl
- anthology_id: 
- pdf_url: https://openreview.net/pdf/53182af45fcf0099abe6b0bb31019b2e0bb08060.pdf
- published: 2024

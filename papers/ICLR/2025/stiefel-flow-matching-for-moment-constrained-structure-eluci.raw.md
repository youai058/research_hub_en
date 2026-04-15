---
title: "Stiefel Flow Matching for Moment-Constrained Structure Elucidation"
authors: ["Austin Henry Cheng", "Alston Lo", "Kin Long Kelvin Lee", "Santiago Miret", "Alan Aspuru-Guzik"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "84WmbzikPP"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/48437bde94e3e6e0bc10c12ac74393c4c5538f1e.pdf"
published: "2025"
categories: []
keywords: ["3D molecular generative models", "flow matching", "Stiefel manifold", "structure elucidation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:06+09:00"
---

# Stiefel Flow Matching for Moment-Constrained Structure Elucidation

## Abstract
Molecular structure elucidation is a fundamental step in understanding chemical phenomena, with applications in identifying molecules in natural products, lab syntheses, forensic samples, and the interstellar medium.
We consider the task of predicting a molecule's all-atom 3D structure given only its molecular formula and moments of inertia, motivated by the ability of rotational spectroscopy to measure these moments.
While existing generative models can conditionally sample 3D structures with approximately correct moments, this soft conditioning fails to leverage the many digits of precision afforded by experimental rotational spectroscopy.
To address this, we first show that the space of $n$-atom point clouds with a fixed set of moments of inertia is embedded in the Stiefel manifold $\mathrm{St}(n, 4)$.
We then propose Stiefel Flow Matching as a generative model for elucidating 3D structure under exact moment constraints.
Additionally, we learn simpler and shorter flows by finding approximate solutions for equivariant optimal transport on the Stiefel manifold.
Empirically, enforcing exact moment constraints allows Stiefel Flow Matching to achieve higher success rates and faster sampling than Euclidean diffusion models, even on high-dimensional manifolds corresponding to large molecules in the GEOM dataset.

## Metadata
- venue: ICLR
- year: 2025
- authors: Austin Henry Cheng, Alston Lo, Kin Long Kelvin Lee, Santiago Miret, Alan Aspuru-Guzik
- arxiv_id: 
- openreview_id: 84WmbzikPP
- anthology_id: 
- pdf_url: https://openreview.net/pdf/48437bde94e3e6e0bc10c12ac74393c4c5538f1e.pdf
- published: 2025
- keywords: 3D molecular generative models, flow matching, Stiefel manifold, structure elucidation

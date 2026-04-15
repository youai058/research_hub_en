---
title: "Vectorized Conditional Neural Fields: A Framework for Solving Time-dependent Parametric Partial Differential Equations"
authors: ["Jan Hagnberger", "Marimuthu Kalimuthu", "Daniel Musekamp", "Mathias Niepert"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "sF9epWkNUG"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/5bad764e1fd18165eabdd65b63bb4dfcf9c92826.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:41+09:00"
---

# Vectorized Conditional Neural Fields: A Framework for Solving Time-dependent Parametric Partial Differential Equations

## Abstract
Transformer models are increasingly used for solving Partial Differential Equations (PDEs). Several adaptations have been proposed, all of which suffer from the typical problems of Transformers, such as quadratic memory and time complexity. Furthermore, all prevalent architectures for PDE solving lack at least one of several desirable properties of an ideal surrogate model, such as (i) generalization to PDE parameters not seen during training, (ii) spatial and temporal zero-shot super-resolution, (iii) continuous temporal extrapolation, (iv) support for 1D, 2D, and 3D PDEs, and (v) efficient inference for longer temporal rollouts. To address these limitations, we propose *Vectorized Conditional Neural Fields* (VCNeFs), which represent the solution of time-dependent PDEs as neural fields. Contrary to prior methods, however, VCNeFs compute, for a set of multiple spatio-temporal query points, their solutions in parallel and model their dependencies through attention mechanisms. Moreover, VCNeF can condition the neural field on both the initial conditions and the parameters of the PDEs. An extensive set of experiments demonstrates that VCNeFs are competitive with and often outperform existing ML-based surrogate models.

## Metadata
- venue: ICML
- year: 2024
- authors: Jan Hagnberger, Marimuthu Kalimuthu, Daniel Musekamp, Mathias Niepert
- arxiv_id: 
- openreview_id: sF9epWkNUG
- anthology_id: 
- pdf_url: https://openreview.net/pdf/5bad764e1fd18165eabdd65b63bb4dfcf9c92826.pdf
- published: 2024

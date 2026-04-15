---
title: "Solving Inverse Problems via Diffusion Optimal Control"
authors: ["Henry Li", "Marcus Aloysius Pereira"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "wqLC4G1GN3"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/05d77a296e09e3facb8599ac339e22b4399d0782.pdf"
published: "2024"
categories: []
keywords: ["diffusion models", "inverse problems", "optimal control"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:52+09:00"
---

# Solving Inverse Problems via Diffusion Optimal Control

## Abstract
Existing approaches to diffusion-based inverse problem solvers frame the signal recovery task as a probabilistic sampling episode, where the solution is drawn from the desired posterior distribution. This framework suffers from several critical drawbacks, including the intractability of the conditional likelihood function, strict dependence on the score network approximation, and poor $\mathbf{x}_0$ prediction quality. We demonstrate that these limitations can be sidestepped by reframing the generative process as a discrete optimal control episode. We derive a diffusion-based optimal controller inspired by the iterative Linear Quadratic Regulator (iLQR) algorithm. This framework is fully general and able to handle any differentiable forward measurement operator, including super-resolution, inpainting, Gaussian deblurring, nonlinear deblurring, and even highly nonlinear neural classifiers. Furthermore, we show that the idealized posterior sampling equation can be recovered as a special case of our algorithm. We then evaluate our method against a selection of neural inverse problem solvers, and establish a new baseline in image reconstruction with inverse problems.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Henry Li, Marcus Aloysius Pereira
- arxiv_id: 
- openreview_id: wqLC4G1GN3
- anthology_id: 
- pdf_url: https://openreview.net/pdf/05d77a296e09e3facb8599ac339e22b4399d0782.pdf
- published: 2024
- keywords: diffusion models, inverse problems, optimal control

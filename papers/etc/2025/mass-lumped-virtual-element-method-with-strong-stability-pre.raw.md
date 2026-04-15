---
title: "Mass-Lumped Virtual Element Method with Strong Stability-Preserving Runge-Kutta Time Stepping for Two-Dimensional Parabolic Problems"
authors: ["Paulo Akira F. Enabe", "Rodrigo Provasi"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.06653"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.06653v2"
published: "2025-10-08"
categories: ["math.NA"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:40+09:00"
---

# Mass-Lumped Virtual Element Method with Strong Stability-Preserving Runge-Kutta Time Stepping for Two-Dimensional Parabolic Problems

## Abstract
This paper presents a mass-lumped Virtual Element Method (VEM) with explicit Strong Stability-Preserving Runge--Kutta (SSP-RK) time integration for two-dimensional parabolic problems on general polygonal meshes. A diagonal mass matrix is constructed via row-sum operations combined with flooring to ensure uniform positivity. Stabilization terms vanish identically under row summation, so the lumped weights derive solely from the $L^2$ projector and are computable through a small polynomial system at cost $\mathcal{O}(N_k^3)$ per element. The resulting lumped bilinear form satisfies $L^2$-equivalence with constants independent of the number of element edges, yielding a symmetric positive definite discrete inner product. A mesh-robust spectral estimate is established, showing that the largest eigenvalue of the discrete diffusion operator scales like $h^{-2}$, with constants depending only on the space dimension, polynomial degree, and mesh regularity. This yields the classical diffusion-type CFL condition $Δt=\mathcal{O}(h^2)$ for forward Euler stability and extends to higher-order SSP-RK schemes, ensuring the preservation of stability properties inherited from the forward Euler step. Numerical experiments on distorted quadrilateral, serendipity, and Voronoi meshes validate the theoretical predictions: for $k=1$, the lumped VEM attains optimal convergence rates, namely $\mathcal{O}(h)$ in the $H^1$-seminorm and $\mathcal{O}(h^2)$ in the $L^2$-norm, without degradation due to mesh distortion or diagonal mass approximation, while the SSP-RK methods remain stable under the predicted $Δt\propto h^2$ scaling. Additional tests on accuracy versus efficiency and on heterogeneous anisotropic diffusion further illustrate the practical competitiveness and robustness of the proposed formulation.

## Metadata
- venue: arXiv
- year: 2025
- authors: Paulo Akira F. Enabe, Rodrigo Provasi
- arxiv_id: 2510.06653
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.06653v2
- published: 2025-10-08

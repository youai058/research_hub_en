---
title: "Optimal Boundary Control of Diffusion on Graphs via Linear Programming"
authors: ["Harbir Antil", "Rainald Löhner", "Felipe Pérez"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2511.03129"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2511.03129v1"
published: "2025-11-05"
categories: ["math.OC", "cs.AI", "physics.comp-ph"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:37+09:00"
---

# Optimal Boundary Control of Diffusion on Graphs via Linear Programming

## Abstract
We propose a linear programming (LP) framework for steady-state diffusion and flux optimization on geometric networks. The state variable satisfies a discrete diffusion law on a weighted, oriented graph, where conductances are scaled by edge lengths to preserve geometric fidelity. Boundary potentials act as controls that drive interior fluxes according to a linear network Laplacian. The optimization problem enforces physically meaningful sign and flux-cap constraints at all boundary edges, derived directly from a gradient bound. This yields a finite-dimensional LP whose feasible set is polyhedral, and whose boundedness and solvability follow from simple geometric or algebraic conditions on the network data.
  We prove that under the absence of negative recession directions--automatically satisfied in the presence of finite box bounds, flux caps, or sign restrictions--the LP admits a global minimizer. Several sufficient conditions guaranteeing boundedness of the feasible region are identified, covering both full-rank and rank-deficient flux maps. The analysis connects classical results such as the Minkowski--Weyl decomposition, Hoffman's bound, and the fundamental theorem of linear programming with modern network-based diffusion modeling.
  Two large-scale examples illustrate the framework: (i) A typical large stadium in a major modern city, which forms a single connected component with relatively uniform corridor widths, and a (ii) A complex street network emanating from a large, historical city center, which forms a multi-component system.

## Metadata
- venue: arXiv
- year: 2025
- authors: Harbir Antil, Rainald Löhner, Felipe Pérez
- arxiv_id: 2511.03129
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2511.03129v1
- published: 2025-11-05

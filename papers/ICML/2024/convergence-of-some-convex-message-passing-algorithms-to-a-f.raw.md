---
title: "Convergence of Some Convex Message Passing Algorithms to a Fixed Point"
authors: ["Vaclav Voracek", "Tomas Werner"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "CaxQ5IbHgF"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c51ff165c9706dbb542a753de9f0ec70ee0a2555.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:48+09:00"
---

# Convergence of Some Convex Message Passing Algorithms to a Fixed Point

## Abstract
A popular approach to the MAP inference problem in graphical models is to minimize an upper bound obtained from a dual linear programming or Lagrangian relaxation by (block-)coordinate descent. This is also known as convex/convergent message passing; examples are max-sum diffusion and sequential tree-reweighted message passing (TRW-S). Convergence properties of these methods are currently not fully understood. They have been proved to converge to the set characterized by local consistency of active constraints, with unknown convergence rate; however, it was not clear if the iterates converge at all (to any point). We prove a stronger result (conjectured before but never proved): the iterates converge to a fixed point of the method. Moreover, we show that the algorithm terminates within $\mathcal{O}(1/\varepsilon)$ iterations. We first prove this for a version of coordinate descent applied to a general piecewise-affine convex objective. Then we show that several convex message passing methods are special cases of this method. Finally, we show that a slightly different version of coordinate descent can cycle.

## Metadata
- venue: ICML
- year: 2024
- authors: Vaclav Voracek, Tomas Werner
- arxiv_id: 
- openreview_id: CaxQ5IbHgF
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c51ff165c9706dbb542a753de9f0ec70ee0a2555.pdf
- published: 2024

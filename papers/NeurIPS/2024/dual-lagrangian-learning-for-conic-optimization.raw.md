---
title: "Dual Lagrangian Learning for Conic Optimization"
authors: ["Mathieu Tanneau", "Pascal Van Hentenryck"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "gN1iKwxlL5"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/48b918d5a9e144d44d30a3ba37a5a5d0976b906b.pdf"
published: "2024"
categories: []
keywords: ["Conic optimization", "optimization proxies", "duality", "self-supervised learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:00+09:00"
---

# Dual Lagrangian Learning for Conic Optimization

## Abstract
This paper presents Dual Lagrangian Learning (DLL), a principled learning methodology for dual conic optimization proxies.
DLL leverages conic duality and the representation power of ML models to provide high-duality, dual-feasible solutions, and therefore valid Lagrangian dual bounds, for linear and nonlinear conic optimization problems.
The paper introduces a systematic dual completion procedure, differentiable conic projection layers, and a self-supervised learning framework based on Lagrangian duality.
It also provides closed-form dual completion formulae for broad classes of conic problems, which eliminate the need for costly implicit layers.
The effectiveness of DLL is demonstrated on linear and nonlinear conic optimization problems.
The proposed methodology significantly outperforms a state-of-the-art learning-based method, and achieves 1000x speedups over commercial interior-point solvers with optimality gaps under 0.5\% on average.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Mathieu Tanneau, Pascal Van Hentenryck
- arxiv_id: 
- openreview_id: gN1iKwxlL5
- anthology_id: 
- pdf_url: https://openreview.net/pdf/48b918d5a9e144d44d30a3ba37a5a5d0976b906b.pdf
- published: 2024
- keywords: Conic optimization, optimization proxies, duality, self-supervised learning

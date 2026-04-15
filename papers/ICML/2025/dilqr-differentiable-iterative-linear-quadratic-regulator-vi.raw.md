---
title: "DiLQR: Differentiable Iterative Linear Quadratic Regulator via Implicit Differentiation"
authors: ["Shuyuan Wang", "Philip D Loewen", "Michael Forbes", "Bhushan Gopaluni", "Wei Pan"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "m2EfTrbv4o"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e220cdad93dab9e2cb263ff057715c2a98d504ae.pdf"
published: "2025"
categories: []
keywords: ["iLQR; Differentiable control; Learning based control"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:29+09:00"
---

# DiLQR: Differentiable Iterative Linear Quadratic Regulator via Implicit Differentiation

## Abstract
While differentiable control has emerged as a powerful paradigm combining model-free flexibility with model-based efficiency, the iterative Linear Quadratic Regulator (iLQR) remains underexplored as a differentiable component. The scalability of differentiating through extended iterations and horizons poses significant challenges, hindering iLQR from being an effective differentiable controller. This paper introduces DiLQR, a framework that facilitates differentiation through iLQR, allowing it to serve as a trainable and differentiable module, either as or within a neural network. A novel aspect of this framework is the analytical solution that it provides for the gradient of an iLQR controller through implicit differentiation, which ensures a constant backward cost regardless of iteration, while producing an accurate gradient. We evaluate our framework on imitation tasks on famous control benchmarks. Our analytical method demonstrates superior computational performance, achieving up to $\textbf{128x}$ speedup and a minimum of $\textbf{21x}$ speedup compared to automatic differentiation. Our method also demonstrates superior learning performance ($\mathbf{10^6x}$) compared to traditional neural network policies and better model loss with differentiable controllers that lack exact analytical gradients. Furthermore, we integrate our module into a larger network with visual inputs to demonstrate the capacity of our method for high-dimensional, fully end-to-end tasks. Codes can be found on the project homepage~\url{https://sites.google.com/view/dilqr/}.

## Metadata
- venue: ICML
- year: 2025
- authors: Shuyuan Wang, Philip D Loewen, Michael Forbes, Bhushan Gopaluni, Wei Pan
- arxiv_id: 
- openreview_id: m2EfTrbv4o
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e220cdad93dab9e2cb263ff057715c2a98d504ae.pdf
- published: 2025
- keywords: iLQR; Differentiable control; Learning based control

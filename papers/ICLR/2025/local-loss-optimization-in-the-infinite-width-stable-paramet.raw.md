---
title: "Local Loss Optimization in the Infinite Width: Stable Parameterization of Predictive Coding Networks and Target Propagation"
authors: ["Satoki Ishikawa", "Rio Yokota", "Ryo Karakida"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "g6syfIrVuS"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/8a1ccf4e448997c7251dad971f6cebb28a74acd4.pdf"
published: "2025"
categories: []
keywords: ["deep learning", "feature learning", "local learning", "predictive coding", "target propagation", "infinite width", "maximal update parameterization (muP)"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:57+09:00"
---

# Local Loss Optimization in the Infinite Width: Stable Parameterization of Predictive Coding Networks and Target Propagation

## Abstract
Local learning, which trains a network through layer-wise local targets and losses, has been studied as an alternative to backpropagation (BP) in neural computation. However, its algorithms often become more complex or require additional hyperparameters due to the locality, making it challenging to identify desirable settings where the algorithm progresses in a stable manner.
To provide theoretical and quantitative insights, we introduce  maximal update parameterization ($\mu$P) in the infinite-width limit for two representative designs of local targets: predictive coding (PC) and target propagation (TP). We verify that $\mu$P enables hyperparameter transfer across models of different widths.
Furthermore, our analysis reveals unique and intriguing properties of $\mu$P that are not present in conventional BP. By analyzing deep linear networks, we find that PC's gradients interpolate between first-order and Gauss-Newton-like gradients, depending on the parameterization.  
We demonstrate that, in specific standard settings, PC in the infinite-width limit behaves more similarly to the first-order gradient.
For TP, even with the standard scaling of the last layer differing from classical $\mu$P, its local loss optimization favors the feature learning regime over the kernel regime.

## Metadata
- venue: ICLR
- year: 2025
- authors: Satoki Ishikawa, Rio Yokota, Ryo Karakida
- arxiv_id: 
- openreview_id: g6syfIrVuS
- anthology_id: 
- pdf_url: https://openreview.net/pdf/8a1ccf4e448997c7251dad971f6cebb28a74acd4.pdf
- published: 2025
- keywords: deep learning, feature learning, local learning, predictive coding, target propagation, infinite width, maximal update parameterization (muP)

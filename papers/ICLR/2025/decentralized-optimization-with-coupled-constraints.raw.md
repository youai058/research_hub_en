---
title: "Decentralized Optimization with Coupled Constraints"
authors: ["Demyan Yarmoshik", "Alexander Rogozin", "Nikita Kiselev", "Daniil Dorin", "Alexander Gasnikov", "Dmitry Kovalev"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "AJM52ygi6Y"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/955f27be28ce3c755cafccab6cfe814f005c05d4.pdf"
published: "2025"
categories: []
keywords: ["decentralized optimization", "convex optimization", "affine constraints"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:58+09:00"
---

# Decentralized Optimization with Coupled Constraints

## Abstract
We consider the decentralized minimization of a separable objective $\sum_{i=1}^{n} f_i(x_i)$, where the variables are coupled through an affine constraint $\sum_{i=1}^n\left(\mathbf{A}_i x_i - b_i\right) = 0$.
We assume that the functions $f_i$, matrices $\mathbf{A}_i$, and vectors $b_i$ are stored locally by the nodes of a computational network, and that the functions $f_i$ are smooth and strongly convex. 

This problem has significant applications in resource allocation and systems control and can also arise in distributed machine learning.
We propose lower complexity bounds for decentralized optimization problems with coupled constraints and a first-order algorithm achieving the lower bounds. To the best of our knowledge, our method is also the first linearly convergent first-order decentralized algorithm for problems with general affine coupled constraints.

## Metadata
- venue: ICLR
- year: 2025
- authors: Demyan Yarmoshik, Alexander Rogozin, Nikita Kiselev, Daniil Dorin, Alexander Gasnikov, Dmitry Kovalev
- arxiv_id: 
- openreview_id: AJM52ygi6Y
- anthology_id: 
- pdf_url: https://openreview.net/pdf/955f27be28ce3c755cafccab6cfe814f005c05d4.pdf
- published: 2025
- keywords: decentralized optimization, convex optimization, affine constraints

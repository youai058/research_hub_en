---
title: "Beyond Least Squares: Uniform Approximation and the Hidden Cost of Misspecification"
authors: ["Davide Maran", "Csaba Szepesvari"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "2T2zMiqcY6"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2415f32eb0a2a2cedb27d52f71a22e00e3ed34e1.pdf"
published: "2025"
categories: []
keywords: ["Uniform error", "Regression", "Lebesgue constant"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:53+09:00"
---

# Beyond Least Squares: Uniform Approximation and the Hidden Cost of Misspecification

## Abstract
We study the problem of controlling worst-case errors in misspecified linear regression under the random design setting, where the regression function is estimated via (penalized) least-squares. This setting arises naturally in value function approximation for bandit algorithms and reinforcement learning (RL).
Our first main contribution is the observation that the amplification of the misspecification error when using least-squares is governed by the \emph{Lebesgue constant}, a classical quantity from approximation theory that depends on the choice of the feature subspace and the covariate distribution.
We also show that this dependence on the misspecification error is tight for least-squares regression: in general, no method minimizing the empirical squared loss, including regularized least-squares, can improve it substantially.
We argue  this explains the empirical observation that some feature-maps (e.g., those derived from the Fourier bases) ``work better in RL'' than others (e.g., polynomials): 
given some covariate distribution, the Lebesgue constant is known to be highly sensitive to choice of the feature-map.
As a second contribution, we propose a method that augments the original feature set with auxiliary features designed to reduce the error amplification. 
We then prove that the method successfully competes with an "oracle'' that knows the best way of using
the auxiliary features to reduce this amplification.
For example, when the domain is a real interval and the features are monomials, 
our method reduces the amplification factor to $O(1)$ as $d\to\infty$, while 
without our method, least-squares with the monomials (and in fact polynomials) will suffer a worst-case error amplification of order $\Omega(d)$. It follows that there are functions and feature maps for which our method is consistent, while least-squares is inconsistent.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Davide Maran, Csaba Szepesvari
- arxiv_id: 
- openreview_id: 2T2zMiqcY6
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2415f32eb0a2a2cedb27d52f71a22e00e3ed34e1.pdf
- published: 2025
- keywords: Uniform error, Regression, Lebesgue constant

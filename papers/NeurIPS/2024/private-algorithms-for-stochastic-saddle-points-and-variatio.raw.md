---
title: "Private Algorithms for Stochastic Saddle Points and Variational Inequalities: Beyond Euclidean Geometry"
authors: ["Raef Bassily", "Cristóbal A Guzmán", "Michael Menart"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "8ugOlbjJpp"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/da8c6874934a6777aed682067394c03bec1f6f9a.pdf"
published: "2024"
categories: []
keywords: ["Differential Privacy", "Stochastic Saddle Point Problem", "Stochastic Variational Inequality", "Strong Gap", "Stochastic Minimax Optimization", "Algorithmic Stability"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:04+09:00"
---

# Private Algorithms for Stochastic Saddle Points and Variational Inequalities: Beyond Euclidean Geometry

## Abstract
In this work, we conduct a systematic study of stochastic saddle point problems (SSP) and stochastic variational inequalities (SVI) under the constraint of $(\epsilon,\delta)$-differential privacy (DP) in both Euclidean and non-Euclidean setups. We first consider Lipschitz convex-concave SSPs in the $\ell_p/\ell_q$ setup, $p,q\in[1,2]$. That is, we consider the case where the primal problem has an $\ell_p$-setup (i.e., the primal parameter is constrained to an $\ell_p$ bounded domain and the loss is $\ell_p$-Lipschitz with respect to the primal parameter) and the dual problem has an $\ell_q$ setup. Here, we obtain a bound of $\tilde{O}\big(\frac{1}{\sqrt{n}} + \frac{\sqrt{d}}{n\epsilon}\big)$ on the strong SP-gap, where $n$ is the number of samples and $d$ is the dimension. This rate is nearly optimal for any $p,q\in[1,2]$. Without additional assumptions, such as smoothness or linearity requirements, prior work under DP has only obtained this rate when $p=q=2$ (i.e., only in the Euclidean setup). Further, existing algorithms have each only been shown to work for specific settings of $p$ and $q$ and under certain assumptions on the loss and the feasible set, whereas we provide a general algorithm for DP SSPs whenever $p,q\in[1,2]$. Our result is obtained via a novel analysis of the recursive regularization algorithm. In particular, we develop new tools for analyzing generalization, which may be of independent interest. Next, we turn our attention towards SVIs with a monotone, bounded and Lipschitz operator and consider $\ell_p$-setups, $p\in[1,2]$. Here, we provide the first analysis which obtains a bound on the strong VI-gap of $\tilde{O}\big(\frac{1}{\sqrt{n}} + \frac{\sqrt{d}}{n\epsilon}\big)$. For $p-1=\Omega(1)$, this rate is near optimal due to existing lower bounds. To obtain this result, we develop a modified version of recursive regularization. Our analysis builds on the techniques we develop for SSPs as well as employing additional novel components which handle difficulties arising from adapting the recursive regularization framework to SVIs.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Raef Bassily, Cristóbal A Guzmán, Michael Menart
- arxiv_id: 
- openreview_id: 8ugOlbjJpp
- anthology_id: 
- pdf_url: https://openreview.net/pdf/da8c6874934a6777aed682067394c03bec1f6f9a.pdf
- published: 2024
- keywords: Differential Privacy, Stochastic Saddle Point Problem, Stochastic Variational Inequality, Strong Gap, Stochastic Minimax Optimization, Algorithmic Stability

---
title: "Quasi-Bayes meets Vines"
authors: ["David Huk", "Yuanhe Zhang", "Ritabrata Dutta", "Mark Steel"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "gcpeEg88R3"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/023de631b175ded4a58c6738161d28950a2bd270.pdf"
published: "2024"
categories: []
keywords: ["Quasi-Bayesian", "Copula", "Vine Copula", "Nonparametric Bayesian", "density estimation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:46+09:00"
---

# Quasi-Bayes meets Vines

## Abstract
Recently developed quasi-Bayesian (QB) methods \cite{fong2023martingale}  proposed a stimulating change of paradigm in Bayesian computation by directly constructing the Bayesian predictive distribution through recursion, removing the need for expensive computations involved in sampling the Bayesian posterior distribution. This has proved to be data-efficient for univariate predictions, however, existing constructions for higher dimensional densities are only possible by relying on restrictive assumptions on the model's multivariate structure. Here, we propose a wholly different approach to extend Quasi-Bayesian prediction to high dimensions through the use of Sklar's theorem, by decomposing the predictive distribution into one-dimensional predictive marginals and a high-dimensional copula. We use the efficient recursive QB construction for the one-dimensional marginals and model the dependence using highly expressive vine copulas. Further, we tune hyperparameters using robust divergences (eg. energy score) and show that our proposed Quasi-Bayesian Vine (QB-Vine) is a fully non-parametric density estimator with \emph{an analytical form} and convergence rate independent of the dimension of the data in some situations. Our experiments illustrate that the QB-Vine is appropriate for high dimensional distributions ($\sim$64), needs very few samples to train ($\sim$200) and outperforms state-of-the-art methods with analytical forms for density estimation and supervised tasks by a considerable margin.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: David Huk, Yuanhe Zhang, Ritabrata Dutta, Mark Steel
- arxiv_id: 
- openreview_id: gcpeEg88R3
- anthology_id: 
- pdf_url: https://openreview.net/pdf/023de631b175ded4a58c6738161d28950a2bd270.pdf
- published: 2024
- keywords: Quasi-Bayesian, Copula, Vine Copula, Nonparametric Bayesian, density estimation

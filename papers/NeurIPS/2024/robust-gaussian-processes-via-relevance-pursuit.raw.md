---
title: "Robust Gaussian Processes via Relevance Pursuit"
authors: ["Sebastian Ament", "Elizabeth Santorella", "David Eriksson", "Benjamin Letham", "Maximilian Balandat", "Eytan Bakshy"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "5FATPIlWUJ"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c3f00fefd4cde92eb2ed8a2e5330bc7db487cd9a.pdf"
published: "2024"
categories: []
keywords: ["Gaussian process", "robust regression", "Bayesian optimization", "submodular"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:03+09:00"
---

# Robust Gaussian Processes via Relevance Pursuit

## Abstract
Gaussian processes (GPs) are non-parametric probabilistic regression models that are popular due to their flexibility, data efficiency, and well-calibrated uncertainty estimates. However, standard GP models assume homoskedastic Gaussian noise, while many real-world applications are subject to non-Gaussian corruptions. Variants of GPs that are more robust to alternative noise models have been proposed, and entail significant trade-offs between accuracy and robustness, and between computational requirements and theoretical guarantees. In this work, we propose and study a GP model that achieves robustness against sparse outliers by inferring data-point-specific noise levels with a sequential selection procedure maximizing the log marginal likelihood that we refer to as relevance pursuit. We show, surprisingly, that the model can be parameterized such that the associated log marginal likelihood is strongly concave in the data-point-specific noise variances, a property rarely found in either robust regression objectives or GP marginal likelihoods. This in turn implies the weak submodularity of the corresponding subset selection problem, and thereby proves approximation guarantees for the proposed algorithm. We compare the model’s performance relative to other approaches on diverse regression and Bayesian optimization tasks, including the challenging but common setting of sparse corruptions of the labels within or close to the function range.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Sebastian Ament, Elizabeth Santorella, David Eriksson, Benjamin Letham, Maximilian Balandat, Eytan Bakshy
- arxiv_id: 
- openreview_id: 5FATPIlWUJ
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c3f00fefd4cde92eb2ed8a2e5330bc7db487cd9a.pdf
- published: 2024
- keywords: Gaussian process, robust regression, Bayesian optimization, submodular

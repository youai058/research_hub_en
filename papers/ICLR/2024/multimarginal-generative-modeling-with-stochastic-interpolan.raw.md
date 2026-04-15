---
title: "Multimarginal Generative Modeling with Stochastic Interpolants"
authors: ["Michael Samuel Albergo", "Nicholas Matthew Boffi", "Michael Lindsey", "Eric Vanden-Eijnden"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "FHqAzWl2wE"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ffbe0129551a2886a81d49db461b05400f637dee.pdf"
published: "2024"
categories: []
keywords: ["multi-marginal", "unsupervised learning", "generative modeling", "measure transport", "optimal transport"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:57+09:00"
---

# Multimarginal Generative Modeling with Stochastic Interpolants

## Abstract
Given a set of $K$ probability densities, we consider the multimarginal generative modeling problem of learning a joint distribution that recovers these densities as marginals. The structure of this joint distribution should identify multi-way correspondences among the prescribed marginals. We formalize an approach to this task within a generalization of the stochastic interpolant framework, leading to efficient learning algorithms built upon dynamical transport of measure. Our generative models are defined by velocity and score fields that can be characterized as the minimizers of simple quadratic objectives, and they are defined on a simplex that generalizes the time variable in the usual dynamical transport framework. The resulting transport on the simplex is influenced by all marginals, and we show that multi-way correspondences can be extracted. The identification of such correspondences has applications to style transfer, algorithmic fairness, and data decorruption.  In addition, the multimarginal perspective enables an efficient algorithm for optimizing the dynamical transport cost in the ordinary two-marginal setting. We demonstrate these capacities with several numerical examples.

## Metadata
- venue: ICLR
- year: 2024
- authors: Michael Samuel Albergo, Nicholas Matthew Boffi, Michael Lindsey, Eric Vanden-Eijnden
- arxiv_id: 
- openreview_id: FHqAzWl2wE
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ffbe0129551a2886a81d49db461b05400f637dee.pdf
- published: 2024
- keywords: multi-marginal, unsupervised learning, generative modeling, measure transport, optimal transport

---
title: "Wasserstein Gradient Boosting: A Framework for Distribution-Valued Supervised Learning"
authors: ["Takuo Matsubara"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "cuO0DenqMl"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/01e42d5db022fcd6854bdd7ed84df75057882975.pdf"
published: "2024"
categories: []
keywords: ["Gradient Boosting; Wasserstein Gradient Flow; Uncertainty Quantification"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:46+09:00"
---

# Wasserstein Gradient Boosting: A Framework for Distribution-Valued Supervised Learning

## Abstract
Gradient boosting is a sequential ensemble method that fits a new weaker learner to pseudo residuals at each iteration. We propose Wasserstein gradient boosting, a novel extension of gradient boosting, which fits a new weak learner to alternative pseudo residuals that are Wasserstein gradients of loss functionals of probability distributions assigned at each input. It solves distribution-valued supervised learning, where the output values of the training dataset are probability distributions. In classification and regression, a model typically returns, for each input, a point estimate of a parameter of a noise distribution specified for a response variable, such as the class probability parameter of a categorical distribution specified for a response label. A main application of Wasserstein gradient boosting in this paper is tree-based evidential learning, which returns a distributional estimate of the response parameter for each input. We empirically demonstrate the competitive performance of the probabilistic prediction by Wasserstein gradient boosting in comparison with existing uncertainty quantification methods.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Takuo Matsubara
- arxiv_id: 
- openreview_id: cuO0DenqMl
- anthology_id: 
- pdf_url: https://openreview.net/pdf/01e42d5db022fcd6854bdd7ed84df75057882975.pdf
- published: 2024
- keywords: Gradient Boosting; Wasserstein Gradient Flow; Uncertainty Quantification

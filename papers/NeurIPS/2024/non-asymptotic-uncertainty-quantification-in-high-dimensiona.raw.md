---
title: "Non-Asymptotic Uncertainty Quantification in High-Dimensional Learning"
authors: ["Frederik Hoppe", "Claudio Mayrink Verdun", "Hannah Laus", "Felix Krahmer", "Holger Rauhut"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "RQCmMSSzvI"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/671e6746eaf5082a512cdfed10dc26c04a8dfb64.pdf"
published: "2024"
categories: []
keywords: ["high-dimensional regression", "uncertainty quantification", "model-based deep learning", "debiased estimator", "inverse problems"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:55+09:00"
---

# Non-Asymptotic Uncertainty Quantification in High-Dimensional Learning

## Abstract
Uncertainty quantification (UQ) is a crucial but challenging task in many high-dimensional learning problems to increase the confidence of a given predictor. We develop a new data-driven approach for UQ in regression that applies both to classical optimization approaches such as the LASSO as well as to neural networks. One of the most notable UQ techniques is the debiased LASSO, which modifies the LASSO to allow for the construction of asymptotic confidence intervals by decomposing the estimation error into a Gaussian and an asymptotically vanishing bias component. However, in real-world problems with finite-dimensional data, the bias term is often too significant to disregard, resulting in overly narrow confidence intervals. Our work rigorously addresses this issue and derives a data-driven adjustment that corrects the confidence intervals for a large class of predictors by estimating the means and variances of the bias terms from training data, exploiting high-dimensional concentration phenomena. This gives rise to non-asymptotic confidence intervals, which can help avoid overestimating certainty in critical applications such as MRI diagnosis. Importantly, our analysis extends beyond sparse regression to data-driven predictors like neural networks, enhancing the reliability of model-based deep learning. Our findings bridge the gap between established theory and the practical applicability of such methods.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Frederik Hoppe, Claudio Mayrink Verdun, Hannah Laus, Felix Krahmer, Holger Rauhut
- arxiv_id: 
- openreview_id: RQCmMSSzvI
- anthology_id: 
- pdf_url: https://openreview.net/pdf/671e6746eaf5082a512cdfed10dc26c04a8dfb64.pdf
- published: 2024
- keywords: high-dimensional regression, uncertainty quantification, model-based deep learning, debiased estimator, inverse problems

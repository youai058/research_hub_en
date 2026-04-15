---
title: "Generalization error of spectral algorithms"
authors: ["Maksim Velikanov", "Maxim Panov", "Dmitry Yarotsky"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "3SJE1WLB4M"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2ec1e556e2638c8f90cf327da20ee024055d1426.pdf"
published: "2024"
categories: []
keywords: ["gradient descent", "kernel ridge regression", "optimal algorithm", "generalization", "asymptotic error rates", "power-laws"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:54+09:00"
---

# Generalization error of spectral algorithms

## Abstract
The asymptotically precise estimation of the generalization of kernel methods has recently received attention due to the parallels between neural networks and their associated kernels. However, prior works derive such estimates for training by kernel ridge regression (KRR), whereas neural networks are typically trained with gradient descent (GD). In the present work, we consider the training of kernels with a family of \emph{spectral algorithms} specified by profile $h(\lambda)$, and including KRR and GD as special cases. Then, we derive the generalization error as a functional of learning profile $h(\lambda)$ for two data models: high-dimensional Gaussian and low-dimensional translation-invariant model. 
Under power-law assumptions on the spectrum of the kernel and target, we use our framework to (i) give full loss asymptotics for both noisy and noiseless observations (ii) show that the loss localizes on certain spectral scales, giving a new perspective on the KRR saturation phenomenon (iii) conjecture, and demonstrate for the considered data models, the universality of the loss w.r.t. non-spectral details of the problem, but only in case of noisy observation.

## Metadata
- venue: ICLR
- year: 2024
- authors: Maksim Velikanov, Maxim Panov, Dmitry Yarotsky
- arxiv_id: 
- openreview_id: 3SJE1WLB4M
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2ec1e556e2638c8f90cf327da20ee024055d1426.pdf
- published: 2024
- keywords: gradient descent, kernel ridge regression, optimal algorithm, generalization, asymptotic error rates, power-laws

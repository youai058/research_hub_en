---
title: "Learning in Feature Spaces via Coupled Covariances: Asymmetric Kernel SVD and Nyström method"
authors: ["Qinghua Tao", "Francesco Tonin", "Alex Lambert", "Yingyi Chen", "Panagiotis Patrinos", "Johan Suykens"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Gp0xZDmrA2"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b0796df605b106d5168c1bddbd4347df1a4f65bc.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:13+09:00"
---

# Learning in Feature Spaces via Coupled Covariances: Asymmetric Kernel SVD and Nyström method

## Abstract
In contrast with Mercer kernel-based approaches as used e.g. in Kernel Principal Component Analysis (KPCA), it was previously shown that Singular Value Decomposition (SVD) inherently relates to asymmetric kernels and Asymmetric Kernel Singular Value Decomposition (KSVD) has been proposed. However, the existing formulation to KSVD cannot work with infinite-dimensional feature mappings, the variational objective can be unbounded, and needs further numerical evaluation and exploration towards machine learning. In this work, i) we introduce a new asymmetric learning paradigm based on coupled covariance eigenproblem (CCE) through covariance operators, allowing infinite-dimensional feature maps. The solution to CCE is ultimately obtained from the SVD of the induced asymmetric kernel matrix, providing links to KSVD. ii) Starting from the integral equations corresponding to a pair of coupled adjoint eigenfunctions, we formalize the asymmetric Nyström method through a finite sample approximation to speed up training. iii) We provide the first empirical evaluations verifying the practical utility and benefits of KSVD and compare with methods resorting to symmetrization or linear SVD across multiple tasks.

## Metadata
- venue: ICML
- year: 2024
- authors: Qinghua Tao, Francesco Tonin, Alex Lambert, Yingyi Chen, Panagiotis Patrinos, Johan Suykens
- arxiv_id: 
- openreview_id: Gp0xZDmrA2
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b0796df605b106d5168c1bddbd4347df1a4f65bc.pdf
- published: 2024

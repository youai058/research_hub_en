---
title: "Be a Goldfish: Forgetting Bad Conditioning in Sparse Linear Regression via Variational Autoencoders"
authors: ["Kuheli Pratihar", "Debdeep Mukhopadhyay"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "aTQtGq7IyT"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/398fad1085215c60c639127a7085a907e0f3b841.pdf"
published: "2025"
categories: []
keywords: ["Variational Autoencoders", "Sparse Linear Regression", "NP-Hard", "Smoothing", "Sparsity", "Matrix Conditioning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:18+09:00"
---

# Be a Goldfish: Forgetting Bad Conditioning in Sparse Linear Regression via Variational Autoencoders

## Abstract
Variational Autoencoders (VAEs), a class of latent-variable generative models, have seen extensive use in high-fidelity synthesis tasks, yet their loss landscape remains poorly understood. Prior theoretical works on VAE loss analysis have focused on their latent-space representational capabilities, both in the optimal and limiting cases. Although these insights have guided better VAE designs, they also often restrict VAEs to problem settings where classical algorithms, such as Principal Component Analysis (PCA), can trivially guarantee globally optimal solutions. In this work, we push the boundaries of our understanding of VAEs beyond these traditional regimes to tackle NP-hard sparse inverse problems, for which no classical algorithms exist. Specifically, we examine the nontrivial Sparse Linear Regression (SLR) problem of recovering optimal sparse inputs in the presence of an ill-conditioned design matrix having correlated features. We provably show that, under a linear encoder-decoder architecture incorporating the product of the SLR design matrix with a trainable, sparsity-promoting diagonal matrix, any minimum of VAE loss is guaranteed to be an optimal solution. This property is especially useful for identifying (a) a preconditioning factor that reduces the eigenvalue spread, and (b) the corresponding optimal sparse representation. Lastly, our empirical analysis with different types of design matrices validates these findings and even demonstrates a higher recovery rate at low sparsity where traditional algorithms fail. Overall, this work highlights the flexible nature of the VAE loss, which can be adapted to efficiently solve computationally hard problems under specific constraints.

## Metadata
- venue: ICML
- year: 2025
- authors: Kuheli Pratihar, Debdeep Mukhopadhyay
- arxiv_id: 
- openreview_id: aTQtGq7IyT
- anthology_id: 
- pdf_url: https://openreview.net/pdf/398fad1085215c60c639127a7085a907e0f3b841.pdf
- published: 2025
- keywords: Variational Autoencoders, Sparse Linear Regression, NP-Hard, Smoothing, Sparsity, Matrix Conditioning

---
title: "The Quest for Universal Master Key Filters in DS-CNNs"
authors: ["Zahra Babaiee", "Peyman Kiasari", "Daniela Rus", "Radu Grosu"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "lYnNzmFt7r"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e1fa47d211d2531ab85e0aa5b97cfe6165bc3e74.pdf"
published: "2025"
categories: []
keywords: ["Convolutional Neural Networks", "Depthwise Separable Convolutions", "Gaussian Derivatives"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:47+09:00"
---

# The Quest for Universal Master Key Filters in DS-CNNs

## Abstract
A recent study has proposed the ``Master Key Filters Hypothesis" for convolutional neural network filters. This paper extends this hypothesis by radically constraining its scope to a single set of just 8 universal filters that depthwise separable convolutional networks inherently converge to. While conventional DS-CNNs employ thousands of distinct trained filters, our analysis reveals these filters are predominantly linear shifts (ax+b) of our discovered universal set. Through systematic unsupervised search, we extracted these fundamental patterns across different architectures and datasets. Remarkably, networks initialized with these 8 unique frozen filters achieve over 80\% ImageNet accuracy, and even outperform models with thousands of trainable parameters when applied to smaller datasets. The identified master key filters closely match Difference of Gaussians (DoGs), Gaussians, and their derivatives, structures that are not only fundamental to classical image processing but also strikingly similar to receptive fields in mammalian visual systems. Our findings provide compelling evidence that depthwise convolutional layers naturally gravitate toward this fundamental set of spatial operators regardless of task or architecture. This work offers new insights for understanding generalization and transfer learning through the universal language of these master key filters.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Zahra Babaiee, Peyman Kiasari, Daniela Rus, Radu Grosu
- arxiv_id: 
- openreview_id: lYnNzmFt7r
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e1fa47d211d2531ab85e0aa5b97cfe6165bc3e74.pdf
- published: 2025
- keywords: Convolutional Neural Networks, Depthwise Separable Convolutions, Gaussian Derivatives

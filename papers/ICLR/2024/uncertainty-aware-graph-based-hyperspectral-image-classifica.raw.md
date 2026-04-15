---
title: "Uncertainty-aware Graph-based Hyperspectral Image Classification"
authors: ["Linlin Yu", "Yifei Lou", "Feng Chen"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "8dN7gApKm3"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/5cb7dbbaad37d6d8ad2e4be0826caf667a69732a.pdf"
published: "2024"
categories: []
keywords: ["Uncertainty Quantification", "Graph", "Hyperspectral Image Classification"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:08+09:00"
---

# Uncertainty-aware Graph-based Hyperspectral Image Classification

## Abstract
Hyperspectral imaging (HSI) technology captures spectral information across a broad wavelength range, providing richer pixel features compared to traditional color images with only three channels. Although pixel classification in HSI  has been extensively studied, especially using graph convolution neural networks (GCNs), quantifying epistemic and aleatoric uncertainties associated with the HSI classification (HSIC) results remains an unexplored area. These two uncertainties are effective for out-of-distribution (OOD) and misclassification detection, respectively. In this paper, we adapt two advanced uncertainty quantification models, evidential GCNs (EGCN) and graph posterior networks (GPN), designed for node classifications in graphs, into the realm of HSIC. We first reveal theoretically that a popular uncertainty cross-entropy (UCE) loss function is insufficient to produce good epistemic uncertainty when learning EGCNs. To mitigate the limitations, we propose two regularization terms. One leverages the inherent property of HSI data where each feature vector is a linear combination of the spectra signatures of the confounding materials, while the other is the total variation (TV) regularization to enforce the spatial smoothness of the evidence with edge-preserving. We demonstrate the effectiveness of the proposed regularization terms on both EGCN and GPN on three real-world HSIC datasets for OOD and misclassification detection tasks. The code is available at GitHub.

## Metadata
- venue: ICLR
- year: 2024
- authors: Linlin Yu, Yifei Lou, Feng Chen
- arxiv_id: 
- openreview_id: 8dN7gApKm3
- anthology_id: 
- pdf_url: https://openreview.net/pdf/5cb7dbbaad37d6d8ad2e4be0826caf667a69732a.pdf
- published: 2024
- keywords: Uncertainty Quantification, Graph, Hyperspectral Image Classification

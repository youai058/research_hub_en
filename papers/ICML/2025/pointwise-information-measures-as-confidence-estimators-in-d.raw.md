---
title: "Pointwise Information Measures as Confidence Estimators in Deep Neural Networks: A Comparative Study"
authors: ["Shelvia Wongso", "Rohan Ghosh", "Mehul Motani"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "MPlcU7Sxzs"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d6e8a0d13585b14c828e7b506d0cf5ba1909f3ec.pdf"
published: "2025"
categories: []
keywords: ["information theory", "confidence estimation", "deep neural networks"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:42+09:00"
---

# Pointwise Information Measures as Confidence Estimators in Deep Neural Networks: A Comparative Study

## Abstract
Estimating the confidence of deep neural network predictions is crucial for safe deployment in high-stakes applications. While softmax probabilities are commonly used, they are often poorly calibrated, and existing calibration methods have been shown to be detrimental to failure prediction. In this paper, we propose using information-theoretic measures to estimate prediction confidence in a post-hoc manner, without modifying network architecture or training. Specifically, we compare three pointwise information (PI) measures: pointwise mutual information (PMI), pointwise $\mathcal{V}$-information (PVI), and the recently proposed pointwise sliced mutual information (PSI). These measures are theoretically grounded in their relevance to predictive uncertainty, with properties such as invariance, convergence rates, and sensitivity to geometric attributes like margin and intrinsic dimensionality. Through extensive experiments on benchmark computer vision models and datasets, we find that PVI consistently outperforms PMI, PSI and existing post-hoc baselines in failure prediction across metrics. For confidence calibration, PVI matches the performance of temperature-scaled softmax, which is already regarded as a highly effective baseline. This indicates that PVI achieves superior failure prediction without compromising its calibration performance. This aligns with our theoretical insights, which suggest that PVI offers the most balanced trade-offs.

## Metadata
- venue: ICML
- year: 2025
- authors: Shelvia Wongso, Rohan Ghosh, Mehul Motani
- arxiv_id: 
- openreview_id: MPlcU7Sxzs
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d6e8a0d13585b14c828e7b506d0cf5ba1909f3ec.pdf
- published: 2025
- keywords: information theory, confidence estimation, deep neural networks

---
title: "Cardinality-Aware Set Prediction and Top-$k$ Classification"
authors: ["Corinna Cortes", "Anqi Mao", "Christopher Mohri", "Mehryar Mohri", "Yutao Zhong"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "WAT3qu737X"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/0bf258277eb5e67e5b9ec4b8f645c1d5d1bdb42d.pdf"
published: "2024"
categories: []
keywords: ["top-k classification", "cardinality-aware algorithms", "consistency", "cost-sensitive loss", "learning theory"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:55+09:00"
---

# Cardinality-Aware Set Prediction and Top-$k$ Classification

## Abstract
We present a detailed study of cardinality-aware top-$k$ classification, a novel approach that aims to learn an accurate top-$k$ set predictor while maintaining a low cardinality. We introduce a new target loss function tailored to this setting that accounts for both the classification error and the cardinality of the set predicted. To optimize this loss function, we propose two families of surrogate losses: cost-sensitive comp-sum losses and cost-sensitive constrained losses. Minimizing these loss functions leads to new cardinality-aware algorithms that we describe in detail in the case of both top-$k$ and threshold-based classifiers. We establish $H$-consistency bounds for our cardinality-aware surrogate loss functions, thereby providing a strong theoretical foundation for our algorithms. We report the results of extensive experiments on CIFAR-10, CIFAR-100, ImageNet, and SVHN datasets demonstrating the effectiveness and benefits of our cardinality-aware algorithms.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Corinna Cortes, Anqi Mao, Christopher Mohri, Mehryar Mohri, Yutao Zhong
- arxiv_id: 
- openreview_id: WAT3qu737X
- anthology_id: 
- pdf_url: https://openreview.net/pdf/0bf258277eb5e67e5b9ec4b8f645c1d5d1bdb42d.pdf
- published: 2024
- keywords: top-k classification, cardinality-aware algorithms, consistency, cost-sensitive loss, learning theory

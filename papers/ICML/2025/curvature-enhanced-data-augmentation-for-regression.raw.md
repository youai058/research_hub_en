---
title: "Curvature Enhanced Data Augmentation for Regression"
authors: ["Ilya Kaufman", "Omri Azencot"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "l1sx5KiM7Z"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ebedcf08aa61fa70f9fe9203dcfe4d8c6cafdf25.pdf"
published: "2025"
categories: []
keywords: ["Manifold learning", "Data augmentation", "Regression"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:28+09:00"
---

# Curvature Enhanced Data Augmentation for Regression

## Abstract
Deep learning models with a large number of parameters, often referred to as over-parameterized models, have achieved exceptional performance across various tasks. Despite concerns about overfitting, these models frequently generalize well to unseen data, thanks to effective regularization techniques, with data augmentation being among the most widely used. While data augmentation has shown great success in classification tasks using label-preserving transformations, its application in regression problems has received less attention. Recently, a novel manifold learning approach for generating synthetic data was proposed, utilizing a first-order approximation of the data manifold. Building on this foundation, we present a theoretical framework and practical tools for approximating and sampling general data manifolds. Furthermore, we introduce the Curvature-Enhanced Manifold Sampling (CEMS) method for regression tasks. CEMS leverages a second-order representation of the data manifold to enable efficient sampling and reconstruction of new data points. Extensive evaluations across multiple datasets and comparisons with state-of-the-art methods demonstrate that CEMS delivers superior performance in both in-distribution and out-of-distribution scenarios, while introducing only minimal computational overhead. Code is available at https://github.com/azencot-group/CEMS.

## Metadata
- venue: ICML
- year: 2025
- authors: Ilya Kaufman, Omri Azencot
- arxiv_id: 
- openreview_id: l1sx5KiM7Z
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ebedcf08aa61fa70f9fe9203dcfe4d8c6cafdf25.pdf
- published: 2025
- keywords: Manifold learning, Data augmentation, Regression

---
title: "Pushing Boundaries: Mixup's Influence on Neural Collapse"
authors: ["Quinn LeBlanc Fisher", "Haoming Meng", "Vardan Papyan"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "jTSKkcbEsj"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/fc3d9e6d2cf3f29c440ba403f9ad95a4ef697601.pdf"
published: "2024"
categories: []
keywords: ["mixup", "neural collapse", "unconstrained features model"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:07+09:00"
---

# Pushing Boundaries: Mixup's Influence on Neural Collapse

## Abstract
Mixup is a data augmentation strategy that employs convex combinations of training instances and their respective labels to improve the robustness and calibration of deep neural networks. Despite its widespread adoption, the nuanced mechanisms that underpin its success are not entirely understood. The observed phenomenon of Neural Collapse, where the last-layer activations and classifier of deep networks converge to a simplex equiangular tight frame (ETF), provides a compelling motivation to explore whether mixup induces alternative geometric configurations and whether those could explain its success. In this study, we delve into the last-layer activations of training data for deep networks subjected to mixup, aiming to uncover insights into its operational efficacy. Our investigation, spanning various architectures and dataset pairs, reveals that mixup's last-layer activations predominantly converge to a distinctive configuration different than one might expect. In this configuration, activations from mixed-up examples of identical classes align with the classifier, while those from different classes delineate channels along the decision boundary. These findings are unexpected, as mixed-up features are not simple convex combinations of feature class means (as one might get, for example, by training mixup with the mean squared error loss). By analyzing this distinctive geometric configuration, we elucidate the mechanisms by which mixup enhances model calibration. To further validate our empirical observations, we conduct a theoretical analysis under the assumption of an unconstrained features model, utilizing the mixup loss. Through this, we characterize and derive the optimal last-layer features under the assumption that the classifier forms a simplex ETF.

## Metadata
- venue: ICLR
- year: 2024
- authors: Quinn LeBlanc Fisher, Haoming Meng, Vardan Papyan
- arxiv_id: 
- openreview_id: jTSKkcbEsj
- anthology_id: 
- pdf_url: https://openreview.net/pdf/fc3d9e6d2cf3f29c440ba403f9ad95a4ef697601.pdf
- published: 2024
- keywords: mixup, neural collapse, unconstrained features model

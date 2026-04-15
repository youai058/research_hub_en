---
title: "Improving Robustness to Multiple Spurious Correlations by Multi-Objective Optimization"
authors: ["Nayeong Kim", "Juwon Kang", "Sungsoo Ahn", "Jungseul Ok", "Suha Kwak"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "CbbTF6tDhW"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9f78a2f076c28d47f30480231e6908378b569466.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:27+09:00"
---

# Improving Robustness to Multiple Spurious Correlations by Multi-Objective Optimization

## Abstract
We study the problem of training an unbiased and accurate model given a dataset with multiple biases. This problem is challenging since the multiple biases cause multiple undesirable shortcuts during training, and even worse, mitigating one may exacerbate the other. We propose a novel training method to tackle this challenge. Our method first groups training data so that different groups induce different shortcuts, and then optimizes a linear combination of group-wise losses while adjusting their weights dynamically to alleviate conflicts between the groups in performance; this approach, rooted in the multi-objective optimization theory, encourages to achieve the minimax Pareto solution. We also present a new benchmark with multiple biases, dubbed MultiCelebA, for evaluating debiased training methods under realistic and challenging scenarios. Our method achieved the best on three datasets with multiple biases, and also showed superior performance on conventional single-bias datasets.

## Metadata
- venue: ICML
- year: 2024
- authors: Nayeong Kim, Juwon Kang, Sungsoo Ahn, Jungseul Ok, Suha Kwak
- arxiv_id: 
- openreview_id: CbbTF6tDhW
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9f78a2f076c28d47f30480231e6908378b569466.pdf
- published: 2024

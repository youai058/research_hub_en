---
title: "Lightweight Dataset Pruning without Full Training via Example Difficulty and Prediction Uncertainty"
authors: ["Yeseul Cho", "Baekrok Shin", "Changmin Kang", "Chulhee Yun"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "9rLxi2cnZC"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/6e0f622c3e9a20f999ad21d6c0aeb12b2b72491a.pdf"
published: "2025"
categories: []
keywords: ["Dataset Pruning", "Coreset Selection", "Example Difficulty", "Prediction Uncertainty"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:19+09:00"
---

# Lightweight Dataset Pruning without Full Training via Example Difficulty and Prediction Uncertainty

## Abstract
Recent advances in deep learning rely heavily on massive datasets, leading to substantial storage and training costs. Dataset pruning aims to alleviate this demand by discarding redundant examples. However, many existing methods require training a model with a full dataset over a large number of epochs before being able to prune the dataset, which ironically makes the pruning process more expensive than just training the model on the entire dataset. To overcome this limitation, we introduce the **Difficulty and Uncertainty-Aware Lightweight (DUAL)** score, which aims to identify important samples from the early training stage by considering both example difficulty and prediction uncertainty. To address a catastrophic accuracy drop at an extreme pruning ratio, we further propose a pruning ratio-adaptive sampling using Beta distribution.
Experiments on various datasets and learning scenarios such as image classification with label noise and image corruption, and model architecture generalization demonstrate the superiority of our method over previous state-of-the-art (SOTA) approaches. Specifically, on ImageNet-1k, our method reduces the time cost for pruning to 66\% compared to previous methods while achieving a SOTA 60\% test accuracy at a 90\% pruning ratio. On CIFAR datasets, the time cost is reduced to just 15\% while maintaining SOTA performance.

## Metadata
- venue: ICML
- year: 2025
- authors: Yeseul Cho, Baekrok Shin, Changmin Kang, Chulhee Yun
- arxiv_id: 
- openreview_id: 9rLxi2cnZC
- anthology_id: 
- pdf_url: https://openreview.net/pdf/6e0f622c3e9a20f999ad21d6c0aeb12b2b72491a.pdf
- published: 2025
- keywords: Dataset Pruning, Coreset Selection, Example Difficulty, Prediction Uncertainty

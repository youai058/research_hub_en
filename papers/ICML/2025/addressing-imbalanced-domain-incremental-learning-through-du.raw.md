---
title: "Addressing Imbalanced Domain-Incremental Learning through Dual-Balance Collaborative Experts"
authors: ["Lan Li", "Da-Wei Zhou", "Han-Jia Ye", "De-Chuan Zhan"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "dwjwvTwV3V"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/5aa1aab9ff4467612e8189b847d33ecddd38c642.pdf"
published: "2025"
categories: []
keywords: ["Domain-incremental learning，Class-imbalanced learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:36+09:00"
---

# Addressing Imbalanced Domain-Incremental Learning through Dual-Balance Collaborative Experts

## Abstract
Domain-Incremental Learning (DIL) focuses on continual learning in non-stationary environments, requiring models to adjust to evolving domains while preserving historical knowledge. DIL faces two critical challenges in the context of imbalanced data: intra-domain class imbalance and cross-domain class distribution shifts.  These challenges significantly hinder model performance, as intra-domain imbalance leads to underfitting of few-shot classes, while cross-domain shifts require maintaining well-learned many-shot classes and transferring knowledge to improve few-shot class performance in old domains. To overcome these challenges, we introduce the Dual-Balance Collaborative Experts (DCE) framework. DCE employs a frequency-aware expert group, where each expert is guided by specialized loss functions to learn features for specific frequency groups, effectively addressing intra-domain class imbalance. Subsequently, a dynamic expert selector is learned by synthesizing pseudo-features through balanced Gaussian sampling from historical class statistics. This mechanism navigates the trade-off between preserving many-shot knowledge of previous domains and leveraging new data to improve few-shot class performance in earlier tasks. Extensive experimental results on four benchmark datasets demonstrate DCE’s state-of-the-art performance.

## Metadata
- venue: ICML
- year: 2025
- authors: Lan Li, Da-Wei Zhou, Han-Jia Ye, De-Chuan Zhan
- arxiv_id: 
- openreview_id: dwjwvTwV3V
- anthology_id: 
- pdf_url: https://openreview.net/pdf/5aa1aab9ff4467612e8189b847d33ecddd38c642.pdf
- published: 2025
- keywords: Domain-incremental learning，Class-imbalanced learning

---
title: "Rotation Has Two Sides: Evaluating Data Augmentation for Deep One-class Classification"
authors: ["Guodong Wang", "Yunhong Wang", "Xiuguo Bao", "Di Huang"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Ad81awoBVS"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/7bf21feb9bcffeac0dec9c48b1b50d05663b5a16.pdf"
published: "2024"
categories: []
keywords: ["self-supervised learning", "deep one-class cilassification"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:07+09:00"
---

# Rotation Has Two Sides: Evaluating Data Augmentation for Deep One-class Classification

## Abstract
One-class classification (OCC) involves predicting whether a new data is normal or anomalous based solely on the data from a single class during training. Various attempts have been made to learn suitable representations for OCC within a self-supervised framework. Notably, discriminative methods that use geometric visual transformations, such as rotation, to generate pseudo-anomaly samples have exhibited impressive detection performance. Although rotation is commonly viewed as a distribution-shifting transformation and is widely used in the literature, the cause of its effectiveness remains a mystery. In this study, we are the first to make a surprising observation: there exists a strong linear relationship (Pearson's Correlation, $r > 0.9$) between the accuracy of rotation prediction and the performance of OCC. This suggests that a classifier that effectively distinguishes different rotations is more likely to excel in OCC, and vice versa. The root cause of this phenomenon can be attributed to the transformation bias in the dataset, where representations learned from transformations already present in the dataset tend to be less effective, making it essential to accurately estimate the transformation distribution before utilizing pretext tasks involving these transformations for reliable self-supervised representation learning. To the end, we propose a novel two-stage method to estimate the transformation distribution within the dataset. In the first stage, we learn general representations through standard contrastive pre-training. In the second stage, we select potentially semantics-preserving samples from the entire augmented dataset, which includes all rotations, by employing density matching with the provided reference distribution. By sorting samples based on semantics-preserving versus shifting transformations, we achieve improved performance on OCC benchmarks.

## Metadata
- venue: ICLR
- year: 2024
- authors: Guodong Wang, Yunhong Wang, Xiuguo Bao, Di Huang
- arxiv_id: 
- openreview_id: Ad81awoBVS
- anthology_id: 
- pdf_url: https://openreview.net/pdf/7bf21feb9bcffeac0dec9c48b1b50d05663b5a16.pdf
- published: 2024
- keywords: self-supervised learning, deep one-class cilassification

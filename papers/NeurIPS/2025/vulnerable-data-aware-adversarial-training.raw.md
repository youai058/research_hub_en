---
title: "Vulnerable Data-Aware Adversarial Training"
authors: ["Yuqi Feng", "Jiahao Fan", "Yanan Sun"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "yrrU5YChQr"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/0c873f68a38655feeef37be13f358ee0fb16d4da.pdf"
published: "2025"
categories: []
keywords: ["Adversarial Training", "Adversarial Robustness", "Decision Boundary Analysis"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:21+09:00"
---

# Vulnerable Data-Aware Adversarial Training

## Abstract
Fast adversarial training (FAT) has been considered as one of the most effective alternatives to the computationally-intensive adversarial training. Generally, FAT methods pay equal attention to each sample of the target task. However, the distance between each sample and the decision boundary is different, learning samples which are far from the decision boundary (i.e., less important to adversarial robustness) brings additional training cost and leads to sub-optimal results. To tackle this issue, we present vulnerable data-aware adversarial training (VDAT) in this study. Specifically, we first propose a margin-based vulnerability calculation method to measure the vulnerability of data samples. Moreover, we propose a vulnerability-aware data filtering method to reduce the training data for adversarial training thus improve the training efficiency. The experiments are conducted in terms of adversarial training and robust neural architecture search on CIFAR-10, CIFAR-100, and ImageNet-1K. The results demonstrate that VDAT is up to 76% more efficient than state-of-the-art FAT methods, while achieving improvements regarding the natural accuracy and adversarial accuracy in both scenarios. Furthermore, the visualizations and ablation studies show the effectiveness of both core components designed in VDAT.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Yuqi Feng, Jiahao Fan, Yanan Sun
- arxiv_id: 
- openreview_id: yrrU5YChQr
- anthology_id: 
- pdf_url: https://openreview.net/pdf/0c873f68a38655feeef37be13f358ee0fb16d4da.pdf
- published: 2025
- keywords: Adversarial Training, Adversarial Robustness, Decision Boundary Analysis

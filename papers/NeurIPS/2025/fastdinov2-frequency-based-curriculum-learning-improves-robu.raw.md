---
title: "FastDINOv2: Frequency Based Curriculum Learning Improves Robustness and Training Speed"
authors: ["Jiaqi Zhang", "Juntuo Wang", "Zhixin Sun", "John Zou", "Randall Balestriero"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "wN7aPpCfSx"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ef0278e63d126d9bb3ccb914f20ba734bfe91063.pdf"
published: "2025"
categories: []
keywords: ["Self-Supervised Learning", "Vision Foundation Model", "Robustness", "Efficient Training", "Curriculum Learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:41+09:00"
---

# FastDINOv2: Frequency Based Curriculum Learning Improves Robustness and Training Speed

## Abstract
Large-scale vision foundation models such as DINOv2 boast impressive performances by leveraging massive architectures and training datasets. The expense of large-scale pre-training puts such research out of reach for many, hence limiting scientific advancements. We thus propose a novel pretraining strategy for DINOv2 that simultaneously accelerates convergence–and strengthens robustness to common corruptions as a by-product. Our approach involves a frequency filtering curriculum–low-frequency being seen first–and the Gaussian noise patching augmentation. Applied to a ViT-B/16 backbone trained on ImageNet-1K, while pre-training time is reduced by 1.6×–from 16.64 to 10.32 NVIDIA L40S days–and FLOPs by 2.25×, our method still achieves matching robustness in corruption benchmarks (ImageNet-C) and maintains competitive linear probing performance compared with the DINOv2 baseline. This dual benefit of efficiency and robustness makes large-scale self-supervised foundation modeling more attainable, while opening the door to novel exploration around data curriculum and augmentation as a means to improve self-supervised learning models robustness.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Jiaqi Zhang, Juntuo Wang, Zhixin Sun, John Zou, Randall Balestriero
- arxiv_id: 
- openreview_id: wN7aPpCfSx
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ef0278e63d126d9bb3ccb914f20ba734bfe91063.pdf
- published: 2025
- keywords: Self-Supervised Learning, Vision Foundation Model, Robustness, Efficient Training, Curriculum Learning

---
title: "Boosting Adversarial Transferability with Spatial Adversarial Alignment"
authors: ["Zhaoyu Chen", "HaiJing Guo", "Kaixun Jiang", "Jiyuan Fu", "Xinyu Zhou", "Dingkang Yang", "Hao Tang", "Bo Li", "Wenqiang Zhang"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "seCBUZYs5c"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d355db067eebed3d25368123d661ba0f7e83e2a5.pdf"
published: "2025"
categories: []
keywords: ["adversarial transferability", "model alignment"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:52+09:00"
---

# Boosting Adversarial Transferability with Spatial Adversarial Alignment

## Abstract
Deep neural networks are vulnerable to adversarial examples that exhibit transferability across various models. Numerous approaches are proposed to enhance the transferability of adversarial examples, including advanced optimization, data augmentation, and model modifications. However, these methods still show limited transferability, partiovovocularly in cross-architecture scenarios, such as from CNN to ViT. To achieve high transferability, we propose a technique termed Spatial Adversarial Alignment (SAA), which employs an alignment loss and leverages a witness model to fine-tune the surrogate model. Specifically, SAA consists of two key parts: spatial-aware alignment and adversarial-aware alignment. First, we minimize the divergences of features between the two models in both global and local regions, facilitating spatial alignment. Second, we introduce a self-adversarial strategy that leverages adversarial examples to impose further constraints, aligning features from an adversarial perspective. Through this alignment, the surrogate model is trained to concentrate on the common features extracted by the witness model. This facilitates adversarial attacks on these shared features, thereby yielding perturbations that exhibit enhanced transferability. Extensive experiments on various architectures on ImageNet show that aligned surrogate models based on SAA can provide higher transferable adversarial examples, especially in cross-architecture attacks.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Zhaoyu Chen, HaiJing Guo, Kaixun Jiang, Jiyuan Fu, Xinyu Zhou, Dingkang Yang, Hao Tang, Bo Li, Wenqiang Zhang
- arxiv_id: 
- openreview_id: seCBUZYs5c
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d355db067eebed3d25368123d661ba0f7e83e2a5.pdf
- published: 2025
- keywords: adversarial transferability, model alignment

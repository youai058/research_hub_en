---
title: "M3-JEPA: Multimodal Alignment via Multi-gate MoE based on the Joint-Embedding Predictive Architecture"
authors: ["Hongyang Lei", "Xiaolong Cheng", "Qi Qin", "Dan Wang", "Huazhen Huang", "Qingqing Gu", "Yetao Wu", "Luo Ji"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "tYwKQMMjJA"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/cfd555921ac63c395a14cd1edab05f9f21e5efe7.pdf"
published: "2025"
categories: []
keywords: ["JEPA", "MoE", "multimodal", "alignment"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:21+09:00"
---

# M3-JEPA: Multimodal Alignment via Multi-gate MoE based on the Joint-Embedding Predictive Architecture

## Abstract
Current multimodal learning strategies primarily optimize in the original token space. Such a framework is easy to incorporate with the backbone of pretrained language model, but might result in modality collapse. To alleviate such issues, we leverage the Joint-Embedding Predictive Architecture (JEPA) on the multimodal tasks, which converts the input embedding into the output embedding space by a predictor and then conducts the cross-modal alignment on the latent space. We implement this predictor by a Multi-Gate Mixture of Experts (MMoE) and name the framework as M3-JEPA, accordingly. The gating function disentangles the modality-specific and shared information and derives information-theoretic optimality. The framework is implemented with both contrastive and regularization loss, and solved by alternative gradient descent (AGD) between different multimodal tasks. By thoroughly designed experiments, we show that M3-JEPA can obtain state-of-the-art performance on different modalities and tasks, generalize to unseen datasets and domains, and is computationally efficient in both training and inference. Our observation suggests that M3-JEPA might become a new basis to self-supervised learning in the open world.

## Metadata
- venue: ICML
- year: 2025
- authors: Hongyang Lei, Xiaolong Cheng, Qi Qin, Dan Wang, Huazhen Huang, Qingqing Gu, Yetao Wu, Luo Ji
- arxiv_id: 
- openreview_id: tYwKQMMjJA
- anthology_id: 
- pdf_url: https://openreview.net/pdf/cfd555921ac63c395a14cd1edab05f9f21e5efe7.pdf
- published: 2025
- keywords: JEPA, MoE, multimodal, alignment

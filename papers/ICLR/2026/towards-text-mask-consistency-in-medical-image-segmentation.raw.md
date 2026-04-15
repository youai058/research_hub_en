---
title: "Towards Text-Mask Consistency in Medical Image Segmentation"
authors: ["Jie Gui", "HangTu", "Wen Sha", "Xiuquan Du"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "riOevy2RwZ"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/7849795079d2dae90beb2ef1ed944d294d8dd953.pdf"
published: "2026"
categories: []
keywords: ["Medical image segmentation", "Vision language models", "Multimodal learning", "Kolmogorov–Arnold Networks"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:16+09:00"
---

# Towards Text-Mask Consistency in Medical Image Segmentation

## Abstract
Vision-language models for medical image segmentation often produce masks that conflict with the accompanying text, especially under multi-site/multi-lesion descriptions. We trace this failure to two factors: (i) highly templated and repetitive clinical language causes one-to-one hard contrastive learning to yield numerous false negatives, weakening cross-modal alignment; and (ii) predominantly vision-driven, one-way cross-attention lacks a language-dominant, spatially aware pathway, hindering effective injection of textual semantics into the spatial visual domain. To this end, we propose Consistency-enhanced Two-stage Segmentation (C2Seg). In the pretraining stage, Cluster-aware Contrastive Learning uses a frozen strong baseline to construct an intra-batch text similarity matrix as soft labels, thereby alleviating false negative conflicts and producing more discriminative visual representations. In the fusion stage, we introduce a Bidirectional Complementary Attention Module, where each modality dominates attention along its own path, fostering deep interaction and structural consistency between visual and textual representations. In order to enhance the expressive power of multimodal features, we further adopt KAN-based Attention Gating. Without updating the language encoder, our approach significantly improves text-mask consistency and segmentation accuracy on four public medical imaging datasets.

## Metadata
- venue: ICLR
- year: 2026
- authors: Jie Gui, HangTu, Wen Sha, Xiuquan Du
- arxiv_id: 
- openreview_id: riOevy2RwZ
- anthology_id: 
- pdf_url: https://openreview.net/pdf/7849795079d2dae90beb2ef1ed944d294d8dd953.pdf
- published: 2026
- keywords: Medical image segmentation, Vision language models, Multimodal learning, Kolmogorov–Arnold Networks

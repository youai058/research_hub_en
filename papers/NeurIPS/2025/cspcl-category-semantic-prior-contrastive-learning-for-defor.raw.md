---
title: "CSPCL: Category Semantic Prior Contrastive Learning for Deformable DETR-Based Prohibited Item Detectors"
authors: ["Mingyuan Li", "Tong Jia", "Hao Wang", "Bowen Ma", "Luhui", "Shiyi Guo", "Da Cai", "Dongyue Chen"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "bzjlMvUKDv"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c8e5f6562f6e08923550b33ca8227145cf72447d.pdf"
published: "2025"
categories: []
keywords: ["object detection", "X-ray inspection", "detection transformer"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:55+09:00"
---

# CSPCL: Category Semantic Prior Contrastive Learning for Deformable DETR-Based Prohibited Item Detectors

## Abstract
Prohibited item detection based on X-ray images is one of the most effective security inspection methods. However, the foreground-background feature coupling caused by the overlapping phenomenon specific to X-ray images makes general detectors designed for natural images perform poorly. To address this issue, we propose a Category Semantic Prior Contrastive Learning (CSPCL) mechanism, which aligns the class prototypes perceived by the classifier with the content queries to correct and supplement the missing semantic information responsible for classification, thereby enhancing the model sensitivity to foreground features. To achieve this alignment, we design a specific contrastive loss, CSP loss, which comprises the Intra-Class Truncated Attraction (ITA) loss and the Inter-Class Adaptive Repulsion (IAR) loss, and outperforms classic contrastive losses. Specifically, the ITA loss leverages class prototypes to attract intra-class content queries and preserves essential intra-class diversity via a gradient truncation function. The IAR loss employs class prototypes to adaptively repel inter-class content queries, with the repulsion strength scaled by prototype-prototype similarity, thereby improving inter-class discriminability, especially among similar categories. CSPCL is general and can be easily integrated into Deformable DETR-based models. Extensive experiments on the PIXray, OPIXray, PIDray, and CLCXray datasets demonstrate that CSPCL significantly enhances the performance of various state-of-the-art models without increasing inference complexity. The code is publicly available at https://github.com/Limingyuan001/CSPCL.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Mingyuan Li, Tong Jia, Hao Wang, Bowen Ma, Luhui, Shiyi Guo, Da Cai, Dongyue Chen
- arxiv_id: 
- openreview_id: bzjlMvUKDv
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c8e5f6562f6e08923550b33ca8227145cf72447d.pdf
- published: 2025
- keywords: object detection, X-ray inspection, detection transformer

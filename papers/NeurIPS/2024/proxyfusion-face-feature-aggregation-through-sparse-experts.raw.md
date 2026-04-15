---
title: "ProxyFusion: Face Feature Aggregation Through Sparse Experts"
authors: ["Bhavin Jawade", "Alexander Stone", "Deen Dayal Mohan", "Xiao Wang", "Srirangaraj Setlur", "Venu Govindaraju"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "FIs87Iro9j"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/48cc7416cd826958e6d304e688becc14404abc2f.pdf"
published: "2024"
categories: []
keywords: ["Feature Fusion", "Face Recognition", "Pooling"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:45+09:00"
---

# ProxyFusion: Face Feature Aggregation Through Sparse Experts

## Abstract
Face feature fusion is indispensable for robust face recognition, particularly in scenarios involving long-range, low-resolution media (unconstrained environments) where not all frames or features are equally informative. Existing methods often rely on large intermediate feature maps or face metadata information, making them incompatible with legacy biometric template databases that store pre-computed features. Additionally, real-time inference and generalization to large probe sets remains challenging. 
To address these limitations, we introduce a linear time O(N) proxy based sparse expert selection and pooling approach for context driven feature-set attention. Our approach is order invariant on the feature-set, generalizes to large sets, is compatible with legacy template stores, and utilizes significantly less parameters making it suitable real-time inference and edge use-cases. Through qualitative experiments, we demonstrate that ProxyFusion learns discriminative information for importance weighting of face features without relying on intermediate features. Quantitative evaluations on challenging low-resolution face verification datasets such as IARPA BTS3.1 and DroneSURF show the superiority of ProxyFusion in unconstrained long-range face recognition setting. 
Our code and pretrained models are available at: https://github.com/bhavinjawade/ProxyFusion

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Bhavin Jawade, Alexander Stone, Deen Dayal Mohan, Xiao Wang, Srirangaraj Setlur, Venu Govindaraju
- arxiv_id: 
- openreview_id: FIs87Iro9j
- anthology_id: 
- pdf_url: https://openreview.net/pdf/48cc7416cd826958e6d304e688becc14404abc2f.pdf
- published: 2024
- keywords: Feature Fusion, Face Recognition, Pooling

---
title: "First-Order Manifold Data Augmentation for Regression Learning"
authors: ["Ilya Kaufman", "Omri Azencot"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "geajNKab7g"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a592ba7491315e210828c16006295f4dc2d00591.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:46+09:00"
---

# First-Order Manifold Data Augmentation for Regression Learning

## Abstract
Data augmentation (DA) methods tailored to specific domains generate synthetic samples by applying transformations that are appropriate for the characteristics of the underlying data domain, such as rotations on images and time warping on time series data. In contrast, *domain-independent* approaches, e.g. *mixup*, are applicable to various data modalities, and as such they are general and versatile. While regularizing classification tasks via DA is a well-explored research topic, the effect of DA on regression problems received less attention. To bridge this gap, we study the problem of domain-independent augmentation for regression, and we introduce *FOMA*: a new data-driven domain-independent data augmentation method. Essentially, our approach samples new examples from the tangent planes of the train distribution. Augmenting data in this way aligns with the network tendency towards capturing the dominant features of its input signals. We evaluate *FOMA* on in-distribution generalization and out-of-distribution robustness benchmarks, and we show that it improves the generalization of several neural architectures. We also find that strong baselines based on *mixup* are less effective in comparison to our approach. Our code is publicly available at https://github.com/azencot-group/FOMA

## Metadata
- venue: ICML
- year: 2024
- authors: Ilya Kaufman, Omri Azencot
- arxiv_id: 
- openreview_id: geajNKab7g
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a592ba7491315e210828c16006295f4dc2d00591.pdf
- published: 2024

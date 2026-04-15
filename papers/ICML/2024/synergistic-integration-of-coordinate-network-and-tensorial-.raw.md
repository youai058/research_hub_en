---
title: "Synergistic Integration of Coordinate Network and Tensorial Feature for Improving Neural Radiance Fields from Sparse Inputs"
authors: ["Mingyu Kim", "Kim Jun-Seong", "Se-Young Yun", "Jin-Hwa Kim"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "7tyAO5tUF8"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/efdc06962d0bf807cded3fd790dfbb0087791634.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:40+09:00"
---

# Synergistic Integration of Coordinate Network and Tensorial Feature for Improving Neural Radiance Fields from Sparse Inputs

## Abstract
The multi-plane representation has been highlighted for its fast training and inference across static and dynamic neural radiance fields. This approach constructs relevant features via projection onto learnable grids and interpolating adjacent vertices. However, it has limitations in capturing low-frequency details and tends to overuse parameters for low-frequency features due to its bias toward fine details, despite its multi-resolution concept. This phenomenon leads to instability and inefficiency when training poses are sparse. In this work, we propose a method that synergistically integrates multi-plane representation with a coordinate-based MLP network known for strong bias toward low-frequency signals. The coordinate-based network is responsible for capturing low-frequency details, while the multi-plane representation focuses on capturing fine-grained details. We demonstrate that using residual connections between them seamlessly preserves their own inherent properties. Additionally, the proposed progressive training scheme accelerates the disentanglement of these two features. We demonstrate empirically that our proposed method not only outperforms baseline models for both static and dynamic NeRFs with sparse inputs, but also achieves comparable results with fewer parameters.

## Metadata
- venue: ICML
- year: 2024
- authors: Mingyu Kim, Kim Jun-Seong, Se-Young Yun, Jin-Hwa Kim
- arxiv_id: 
- openreview_id: 7tyAO5tUF8
- anthology_id: 
- pdf_url: https://openreview.net/pdf/efdc06962d0bf807cded3fd790dfbb0087791634.pdf
- published: 2024

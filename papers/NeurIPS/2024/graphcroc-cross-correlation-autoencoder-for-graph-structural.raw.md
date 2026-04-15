---
title: "GraphCroc: Cross-Correlation Autoencoder for Graph Structural Reconstruction"
authors: ["Shijin Duan", "Ruyi Ding", "Jiaxing He", "Aidong Adam Ding", "Yunsi Fei", "Xiaolin Xu"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "zn6s6VQYb0"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/57096dd4679d0699198e3899786b24845b43c7a8.pdf"
published: "2024"
categories: []
keywords: ["Graph Neural Network", "Graph Representation", "Auto-Encoder"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:03+09:00"
---

# GraphCroc: Cross-Correlation Autoencoder for Graph Structural Reconstruction

## Abstract
Graph-structured data is integral to many applications, prompting the development of various graph representation methods. Graph autoencoders (GAEs), in particular, reconstruct graph structures from node embeddings. Current GAE models primarily utilize self-correlation to represent graph structures and focus on node-level tasks, often overlooking multi-graph scenarios. Our theoretical analysis indicates that self-correlation generally falls short in accurately representing specific graph features such as islands, symmetrical structures, and directional edges, particularly in smaller or multiple graph contexts.To address these limitations, we introduce a cross-correlation mechanism that significantly enhances the GAE representational capabilities. Additionally, we propose the GraphCroc, a new GAE that supports flexible encoder architectures tailored for various downstream tasks and ensures robust structural reconstruction, through a mirrored encoding-decoding process. This model also tackles the challenge of representation bias during optimization by implementing a loss-balancing strategy. Both theoretical analysis and numerical evaluations demonstrate that our methodology significantly outperforms existing self-correlation-based GAEs in graph structure reconstruction.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Shijin Duan, Ruyi Ding, Jiaxing He, Aidong Adam Ding, Yunsi Fei, Xiaolin Xu
- arxiv_id: 
- openreview_id: zn6s6VQYb0
- anthology_id: 
- pdf_url: https://openreview.net/pdf/57096dd4679d0699198e3899786b24845b43c7a8.pdf
- published: 2024
- keywords: Graph Neural Network, Graph Representation, Auto-Encoder

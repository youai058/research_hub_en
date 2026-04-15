---
title: "Cross-Domain Graph Data Scaling: A Showcase with Diffusion Models"
authors: ["Wenzhuo Tang", "Haitao Mao", "Danial Dervovic", "Ivan Brugere", "Saumitra Mishra", "Yuying Xie", "Jiliang Tang"]
venue: "arXiv"
year: 2024
venue_class: "etc"
arxiv_id: "2406.01899"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2406.01899v3"
published: "2024-06-04"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:20:17+09:00"
---

# Cross-Domain Graph Data Scaling: A Showcase with Diffusion Models

## Abstract
Models for natural language and images benefit from data scaling behavior: the more data fed into the model, the better they perform. This 'better with more' phenomenon enables the effectiveness of large-scale pre-training on vast amounts of data. However, current graph pre-training methods struggle to scale up data due to heterogeneity across graphs. To achieve effective data scaling, we aim to develop a general model that is able to capture diverse data patterns of graphs and can be utilized to adaptively help the downstream tasks. To this end, we propose UniAug, a universal graph structure augmentor built on a diffusion model. We first pre-train a discrete diffusion model on thousands of graphs across domains to learn the graph structural patterns. In the downstream phase, we provide adaptive enhancement by conducting graph structure augmentation with the help of the pre-trained diffusion model via guided generation. By leveraging the pre-trained diffusion model for structure augmentation, we consistently achieve performance improvements across various downstream tasks in a plug-and-play manner. To the best of our knowledge, this study represents the first demonstration of a data-scaling graph structure augmentor on graphs across domains.

## Metadata
- venue: arXiv
- year: 2024
- authors: Wenzhuo Tang, Haitao Mao, Danial Dervovic, Ivan Brugere, Saumitra Mishra, Yuying Xie, Jiliang Tang
- arxiv_id: 2406.01899
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2406.01899v3
- published: 2024-06-04

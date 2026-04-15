---
title: "Path-Enhanced Contrastive Learning for Recommendation"
authors: ["Haoran Sun", "Fei Xiong", "Yuanzhe Hu", "Liang Wang"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "xKmlBQhgI4"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f68206ec049476ef519d4d121f30a3a4b1176561.pdf"
published: "2025"
categories: []
keywords: ["graph mining", "recommender systems", "self-supervised learning", "Contrastive Learning", "Data Augmentation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:41+09:00"
---

# Path-Enhanced Contrastive Learning for Recommendation

## Abstract
Collaborative filtering (CF) methods are now facing the challenge of data sparsity in recommender systems. In order to reduce the effect of data sparsity, researchers proposed contrastive learning methods to extract self-supervised signals from raw data. Contrastive learning methods address this problem by graph augmentation and maximizing the consistency of node representations between different augmented graphs. However, these methods tends to unintentionally distance the target node from its path nodes on the interaction path, thus limiting its effectiveness. In this regard, we propose a solution that uses paths as samples in the contrastive loss function. In order to obtain the path samples, we design a path sampling method. In addition to the contrast of the relationship between the target node and the nodes within the path (intra-path contrast), we also designed a method of contrasting the relationship between the paths (inter-path contrast) to better pull the target node and its path nodes closer to each other. We use Simplifying and Powering Graph Convolution Network (LightGCN) as the basis and combine with a new path-enhanced graph approach proposed for graph augmentation. It effectively improves the performance of recommendation models. Our proposed Path Enhanced Contrastive Loss (PECL) model replaces the common contrastive loss function with our novel loss function, showing significant performance improvement. Experiments on three real-world datasets demonstrate the effectiveness of our model.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Haoran Sun, Fei Xiong, Yuanzhe Hu, Liang Wang
- arxiv_id: 
- openreview_id: xKmlBQhgI4
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f68206ec049476ef519d4d121f30a3a4b1176561.pdf
- published: 2025
- keywords: graph mining, recommender systems, self-supervised learning, Contrastive Learning, Data Augmentation

---
title: "Scalable Feature Learning on Huge Knowledge Graphs for Downstream Machine Learning"
authors: ["Félix Lefebvre", "Gaël Varoquaux"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "PJrvX7Jz2c"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a2374ceb7fdfd9c80b4cbd5c2c5c6c4ef5db3746.pdf"
published: "2025"
categories: []
keywords: ["Knowledge graph", "Downstream tasks", "Scalable", "Feature learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:48+09:00"
---

# Scalable Feature Learning on Huge Knowledge Graphs for Downstream Machine Learning

## Abstract
Many machine learning tasks can benefit from external knowledge. Large knowledge graphs store such knowledge, and embedding methods can be used to distill it into ready-to-use vector representations for downstream applications. For this purpose, current models have however two limitations: they are primarily optimized for link prediction, via local contrastive learning, and their application to the largest graphs requires significant engineering effort due to GPU memory limits. To address these, we introduce SEPAL: a Scalable Embedding Propagation ALgorithm for large knowledge graphs designed to produce high-quality embeddings for downstream tasks at scale. The key idea of SEPAL is to ensure global embedding consistency by optimizing embeddings only on a small core of entities, and then propagating them to the rest of the graph with message passing. We evaluate SEPAL on 7 large-scale knowledge graphs and 46 downstream machine learning tasks. Our results show that SEPAL significantly outperforms previous methods on downstream tasks. In addition, SEPAL scales up its base embedding model, enabling fitting huge knowledge graphs on commodity hardware. Our code is available at: <https://github.com/soda-inria/sepal>.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Félix Lefebvre, Gaël Varoquaux
- arxiv_id: 
- openreview_id: PJrvX7Jz2c
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a2374ceb7fdfd9c80b4cbd5c2c5c6c4ef5db3746.pdf
- published: 2025
- keywords: Knowledge graph, Downstream tasks, Scalable, Feature learning

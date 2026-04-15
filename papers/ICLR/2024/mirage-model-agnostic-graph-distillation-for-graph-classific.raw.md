---
title: "Mirage: Model-agnostic Graph Distillation for Graph Classification"
authors: ["Mridul Gupta", "Sahil Manchanda", "HARIPRASAD KODAMANA", "Sayan Ranu"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "78iGZdqxYY"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/6734ad0e165c7017f3c6c0f400183a1bae684654.pdf"
published: "2024"
categories: []
keywords: ["graph distillation", "graph classification", "frequent pattern mining"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:49+09:00"
---

# Mirage: Model-agnostic Graph Distillation for Graph Classification

## Abstract
GNNs, like other deep learning models, are data and computation hungry. There is a pressing need to scale training of GNNs on large datasets to enable their usage on low-resource environments. Graph distillation is an effort in that direction with the aim to construct a smaller synthetic training set from the original training data without significantly compromising model performance. While initial efforts are promising, this work is motivated by two key observations: (1) Existing graph distillation algorithms themselves rely on training with the full dataset, which undermines the very premise of graph distillation. (2) The distillation process is specific to the target GNN architecture and hyper-parameters and thus not robust to changes in the modeling pipeline. We circumvent these limitations by designing a distillation algorithm called MIRAGE for graph classification. MIRAGE is built on the insight that a message-passing GNN decomposes the input graph into a multiset of computation trees. Furthermore, the frequency distribution of computation trees is often skewed in nature, enabling us to condense this data into a concise distilled summary. By compressing the computation data itself, as opposed to emulating gradient flows on the original training set—a prevalent approach to date—MIRAGE transforms into an unsupervised and architecture-agnostic distillation algorithm. Extensive benchmarking on real-world datasets underscores MIRAGE’s superiority, showcasing enhanced generalization accuracy, data compression, and distillation efficiency when compared to state-of-the-art baselines.

## Metadata
- venue: ICLR
- year: 2024
- authors: Mridul Gupta, Sahil Manchanda, HARIPRASAD KODAMANA, Sayan Ranu
- arxiv_id: 
- openreview_id: 78iGZdqxYY
- anthology_id: 
- pdf_url: https://openreview.net/pdf/6734ad0e165c7017f3c6c0f400183a1bae684654.pdf
- published: 2024
- keywords: graph distillation, graph classification, frequent pattern mining

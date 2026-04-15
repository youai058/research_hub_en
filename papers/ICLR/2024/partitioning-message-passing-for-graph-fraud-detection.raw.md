---
title: "Partitioning Message Passing for Graph Fraud Detection"
authors: ["Wei Zhuo", "Zemin Liu", "Bryan Hooi", "Bingsheng He", "Guang Tan", "Rizal Fathony", "Jia Chen"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "tEgrUrUuwA"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/7abe6053f04ef235ce8ddd5996dd27e266c6e058.pdf"
published: "2024"
categories: []
keywords: ["Graph Neural Networks", "Fraud Detection"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:55+09:00"
---

# Partitioning Message Passing for Graph Fraud Detection

## Abstract
Label imbalance and homophily-heterophily mixture are the fundamental problems encountered when applying Graph Neural Networks (GNNs) to Graph Fraud Detection (GFD) tasks. Existing GNN-based GFD models are designed to augment graph structure to accommodate the inductive bias of GNNs towards homophily, by excluding heterophilic neighbors during message passing. In our work, we argue that the key to applying GNNs for GFD is not to exclude but to {\em distinguish} neighbors with different labels. Grounded in this perspective, we introduce Partitioning Message Passing (PMP), an intuitive yet effective message passing paradigm expressly crafted for GFD. Specifically, in the neighbor aggregation stage of PMP, neighbors with different classes are aggregated with distinct node-specific aggregation functions. By this means, the center node can adaptively adjust the information aggregated from its heterophilic and homophilic neighbors, thus avoiding the model gradient being dominated by benign nodes which occupy the majority of the population. We theoretically establish a connection between the spatial formulation of PMP and spectral analysis to characterize that PMP operates an adaptive node-specific spectral graph filter, which demonstrates the capability of PMP to handle heterophily-homophily mixed graphs. Extensive experimental results show that PMP can significantly boost the performance on GFD tasks.

## Metadata
- venue: ICLR
- year: 2024
- authors: Wei Zhuo, Zemin Liu, Bryan Hooi, Bingsheng He, Guang Tan, Rizal Fathony, Jia Chen
- arxiv_id: 
- openreview_id: tEgrUrUuwA
- anthology_id: 
- pdf_url: https://openreview.net/pdf/7abe6053f04ef235ce8ddd5996dd27e266c6e058.pdf
- published: 2024
- keywords: Graph Neural Networks, Fraud Detection

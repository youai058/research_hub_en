---
title: "Consistency Training with Learnable Data Augmentation for Graph Anomaly Detection with Limited Supervision"
authors: ["Nan Chen", "Zemin Liu", "Bryan Hooi", "Bingsheng He", "Rizal Fathony", "Jun Hu", "Jia Chen"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "elMKXvhhQ9"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/0a2aa8c65cf0939e67a21de44b554069cb961a25.pdf"
published: "2024"
categories: []
keywords: ["Graph anomaly detection", "consistency training", "learnable data augmentation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:50+09:00"
---

# Consistency Training with Learnable Data Augmentation for Graph Anomaly Detection with Limited Supervision

## Abstract
Graph Anomaly Detection (GAD) has surfaced as a significant field of research, predominantly due to its substantial influence in production environments. Although existing approaches for node anomaly detection have shown effectiveness, they have yet to fully address two major challenges: operating in settings with limited supervision and managing class imbalance effectively. In response to these challenges, we propose a novel model, ConsisGAD, which is tailored for GAD in scenarios characterized by limited supervision and is anchored in the principles of consistency training. Under limited supervision, ConsisGAD effectively leverages the abundance of unlabeled data for consistency training by incorporating a novel learnable data augmentation mechanism, thereby introducing controlled noise into the dataset. Moreover, ConsisGAD takes advantage of the variance in homophily distribution between normal and anomalous nodes to craft a simplified GNN backbone, enhancing its capability to distinguish effectively between these two classes. Comprehensive experiments on several benchmark datasets validate the superior performance of ConsisGAD in comparison to state-of-the-art baselines. Our code is available at https://github.com/Xtra-Computing/ConsisGAD.

## Metadata
- venue: ICLR
- year: 2024
- authors: Nan Chen, Zemin Liu, Bryan Hooi, Bingsheng He, Rizal Fathony, Jun Hu, Jia Chen
- arxiv_id: 
- openreview_id: elMKXvhhQ9
- anthology_id: 
- pdf_url: https://openreview.net/pdf/0a2aa8c65cf0939e67a21de44b554069cb961a25.pdf
- published: 2024
- keywords: Graph anomaly detection, consistency training, learnable data augmentation

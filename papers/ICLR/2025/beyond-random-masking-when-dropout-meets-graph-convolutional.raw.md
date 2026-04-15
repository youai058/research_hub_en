---
title: "Beyond Random Masking: When Dropout meets Graph Convolutional Networks"
authors: ["Yuankai Luo", "Xiao-Ming Wu", "Hao Zhu"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "PwxYoMvmvy"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2630e5206aeeb0a02cc48e38f5890bb07d7b7f77.pdf"
published: "2025"
categories: []
keywords: ["Graph neural networks", "Dropout"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:38+09:00"
---

# Beyond Random Masking: When Dropout meets Graph Convolutional Networks

## Abstract
Graph Convolutional Networks (GCNs) have emerged as powerful tools for learning on graph-structured data, yet the behavior of dropout in these models remains poorly understood. This paper presents a comprehensive theoretical analysis of dropout in GCNs, revealing that its primary role differs fundamentally from standard neural networks - preventing oversmoothing rather than co-adaptation. We demonstrate that dropout in GCNs creates dimension-specific stochastic sub-graphs, leading to a form of structural regularization not present in standard neural networks. Our analysis shows that dropout effects are inherently degree-dependent, resulting in adaptive regularization that considers the topological importance of nodes. We provide new insights into dropout's role in mitigating oversmoothing and derive novel generalization bounds that account for graph-specific dropout effects. Furthermore, we analyze the synergistic interaction between dropout and batch normalization in GCNs, uncovering a mechanism that enhances overall regularization. Our theoretical findings are validated through extensive experiments on both node-level and graph-level tasks across 14 datasets. Notably, GCN with dropout and batch normalization outperforms state-of-the-art methods on several benchmarks, demonstrating the practical impact of our theoretical insights.

## Metadata
- venue: ICLR
- year: 2025
- authors: Yuankai Luo, Xiao-Ming Wu, Hao Zhu
- arxiv_id: 
- openreview_id: PwxYoMvmvy
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2630e5206aeeb0a02cc48e38f5890bb07d7b7f77.pdf
- published: 2025
- keywords: Graph neural networks, Dropout

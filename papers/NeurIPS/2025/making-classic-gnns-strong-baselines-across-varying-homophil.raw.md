---
title: "Making Classic GNNs Strong Baselines Across Varying Homophily: A Smoothness–Generalization Perspective"
authors: ["Ming Gu", "Zhuonan Zheng", "Sheng Zhou", "Meihan Liu", "Jiawei Chen", "Qiaoyu Tan", "Liangcheng Li", "Jiajun Bu"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "IAGbhDARZd"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/588e396fd45dc8356713cdad78fc81086b926876.pdf"
published: "2025"
categories: []
keywords: ["Heterophily", "Varying Homophily", "Message Passing", "Graph Neural Networks", "Oversmoothing"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:44+09:00"
---

# Making Classic GNNs Strong Baselines Across Varying Homophily: A Smoothness–Generalization Perspective

## Abstract
Graph Neural Networks (GNNs) have achieved great success but are often considered to be challenged by varying levels of homophily in graphs. Recent empirical studies have surprisingly shown that homophilic GNNs can perform well across datasets of different homophily levels with proper hyperparameter tuning, but the underlying theory and effective architectures remain unclear. To advance GNN universality across varying homophily, we theoretically revisit GNN message passing and uncover a novel \textit{smoothness-generalization dilemma}, where increasing hops inevitably enhances smoothness at the cost of generalization. This dilemma hinders learning in high-order homophilic neighborhoods and all heterophilic ones, where generalization is critical due to complex neighborhood class distributions that are sensitive to shifts induced by noise or sparsity. To address this, we introduce the Inceptive Graph Neural Network (IGNN) built on three simple yet effective design principles, which alleviate the dilemma by enabling distinct hop-wise generalization alongside improved overall generalization with adaptive smoothness. Benchmarking against 30 baselines demonstrates IGNN's superiority and reveals notable universality in certain homophilic GNN variants. Our code and datasets are available at \href{https://github.com/galogm/IGNN}{https://github.com/galogm/IGNN}.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Ming Gu, Zhuonan Zheng, Sheng Zhou, Meihan Liu, Jiawei Chen, Qiaoyu Tan, Liangcheng Li, Jiajun Bu
- arxiv_id: 
- openreview_id: IAGbhDARZd
- anthology_id: 
- pdf_url: https://openreview.net/pdf/588e396fd45dc8356713cdad78fc81086b926876.pdf
- published: 2025
- keywords: Heterophily, Varying Homophily, Message Passing, Graph Neural Networks, Oversmoothing

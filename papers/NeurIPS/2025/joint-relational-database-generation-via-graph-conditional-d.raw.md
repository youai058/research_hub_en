---
title: "Joint Relational Database Generation via Graph-Conditional Diffusion Models"
authors: ["Mohamed Amine Ketata", "David Lüdke", "Leo Schwinn", "Stephan Günnemann"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Z3OtNSwuXX"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ff6ba6a62b743faae2f6e9815bdc9bb23a0002b5.pdf"
published: "2025"
categories: []
keywords: ["relational databases", "tabular data", "generative models", "diffusion models", "graph neural networks", "graph generation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:49+09:00"
---

# Joint Relational Database Generation via Graph-Conditional Diffusion Models

## Abstract
Building generative models for relational databases (RDBs) is important for many applications, such as privacy-preserving data release and augmenting real datasets. However, most prior works either focus on single-table generation or adapt single-table models to the multi-table setting by relying on autoregressive factorizations and sequential generation. These approaches limit parallelism, restrict flexibility in downstream applications, and compound errors due to commonly made conditional independence assumptions. In this paper, we propose a fundamentally different approach: jointly modeling all tables in an RDB without imposing any table order. By using a natural graph representation of RDBs, we propose the Graph-Conditional Relational Diffusion Model (GRDM), which leverages a graph neural network to jointly denoise row attributes and capture complex inter-table dependencies. Extensive experiments on six real-world RDBs demonstrate that our approach substantially outperforms autoregressive baselines in modeling multi-hop inter-table correlations and achieves state-of-the-art performance on single-table fidelity metrics. Our code is available at https://github.com/ketatam/rdb-diffusion.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Mohamed Amine Ketata, David Lüdke, Leo Schwinn, Stephan Günnemann
- arxiv_id: 
- openreview_id: Z3OtNSwuXX
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ff6ba6a62b743faae2f6e9815bdc9bb23a0002b5.pdf
- published: 2025
- keywords: relational databases, tabular data, generative models, diffusion models, graph neural networks, graph generation

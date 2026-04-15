---
title: "Causality-Inspired Spatial-Temporal Explanations for Dynamic Graph Neural Networks"
authors: ["Kesen Zhao", "Liang Zhang"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "AJBkfwXh3u"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/da061144568aad672fd37e90edc5b87a39b91ba9.pdf"
published: "2024"
categories: []
keywords: ["Dynamic Graph", "Graph Explanation", "Graph Neural Network", "Causal Inference"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:49+09:00"
---

# Causality-Inspired Spatial-Temporal Explanations for Dynamic Graph Neural Networks

## Abstract
Dynamic Graph Neural Networks (DyGNNs) have gained significant popularity in the research of dynamic graphs, but are limited by the low transparency, such that human-understandable insights can hardly be drawn from their predictions. Although a number of existing research have been devoted to investigating the interpretability of graph neural networks (GNNs), achieving the interpretability of DyGNNs is pivotally challenging due to the complex spatial-temporal correlations in dynamic graphs. To this end, we propose an innovative causality-inspired generative model based on structural causal model (SCM), which explores the underlying philosophies of DyGNN predictions by identifying the trivial, static, and dynamic causal relationships. To reach this goal, two critical tasks need to be accomplished including (1) disentangling the complex causal relationships, and (2) fitting the spatial-temporal explanations of DyGNNs in the SCM architecture. To tackle these challenges, the proposed method incorporates a contrastive learning module to disentangle trivial and causal relationships, and a dynamic correlating module to disentangle dynamic and static causal relationships, respectively. A dynamic VGAE-based framework is further developed, which generates causal-and-dynamic masks for spatial interpretability, and recognizes dynamic relationships along the time horizon through causal invention for temporal interpretability. Comprehensive experiments have been conducted on both synthetic and real-world datasets, where our approach yields substantial improvements, thereby demonstrating significant superiority.

## Metadata
- venue: ICLR
- year: 2024
- authors: Kesen Zhao, Liang Zhang
- arxiv_id: 
- openreview_id: AJBkfwXh3u
- anthology_id: 
- pdf_url: https://openreview.net/pdf/da061144568aad672fd37e90edc5b87a39b91ba9.pdf
- published: 2024
- keywords: Dynamic Graph, Graph Explanation, Graph Neural Network, Causal Inference

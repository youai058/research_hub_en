---
title: "Learning Posterior Predictive Distributions for Node Classification from Synthetic Graph Priors"
authors: ["Jeongwhan Choi", "Jongwoo Kim", "Woosung Kang", "Noseong Park"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "FmxRzlu0rT"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/cfca33016f2179ac712d1ebf285dde020d653114.pdf"
published: "2026"
categories: []
keywords: ["graph machine learning", "node classification"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:25+09:00"
---

# Learning Posterior Predictive Distributions for Node Classification from Synthetic Graph Priors

## Abstract
One of the most challenging problems in graph machine learning is generalizing across graphs with diverse properties. Graph neural networks (GNNs) face a fundamental limitation: they require separate training for each new graph, preventing universal generalization across diverse graph datasets. A critical challenge facing GNNs lies in their reliance on labeled training data for each individual graph, a requirement that hinders the capacity for universal node classification due to the heterogeneity inherent in graphs --- differences in homophily levels, community structures, and feature distributions across datasets. Inspired by the success of large language models (LLMs) that achieve in-context learning through massive-scale pre-training on diverse datasets, we introduce NodePFN. This universal node classification method generalizes to arbitrary graphs without graph-specific training. NodePFN learns posterior predictive distributions (PPDs) by training only on thousands of synthetic graphs generated from carefully designed priors. Our synthetic graph generation covers real-world graphs through the use of random networks with controllable homophily levels and structural causal models for complex feature-label relationships. We develop a dual-branch architecture combining context-query attention mechanisms with local message passing to enable graph-aware in-context learning. Extensive evaluation on 23 benchmarks demonstrates that a single pre-trained NodePFN achieves 71.27\% average accuracy. These results validate that universal graph learning patterns can be effectively learned from synthetic priors, establishing a new paradigm for generalization in node classification.

## Metadata
- venue: ICLR
- year: 2026
- authors: Jeongwhan Choi, Jongwoo Kim, Woosung Kang, Noseong Park
- arxiv_id: 
- openreview_id: FmxRzlu0rT
- anthology_id: 
- pdf_url: https://openreview.net/pdf/cfca33016f2179ac712d1ebf285dde020d653114.pdf
- published: 2026
- keywords: graph machine learning, node classification

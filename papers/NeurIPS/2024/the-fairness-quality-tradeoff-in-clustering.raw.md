---
title: "The Fairness-Quality Tradeoff in Clustering"
authors: ["Rashida Hakim", "Ana-Andreea Stoica", "Christos Papadimitriou", "Mihalis Yannakakis"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "bUi2xECa7w"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/dc96b5d71f0a1381f1c7e849579b36b8e561a9eb.pdf"
published: "2024"
categories: []
keywords: ["clustering", "algorithmic-fairness", "multiobjective-optimization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:44+09:00"
---

# The Fairness-Quality Tradeoff in Clustering

## Abstract
Fairness in clustering has been considered extensively in the past; however, the trade-off between the two objectives --- e.g., can we sacrifice just a little in the quality of the clustering to significantly increase fairness, or vice-versa? --- has rarely been addressed. We introduce novel algorithms for tracing the complete trade-off curve, or Pareto front, between quality and fairness in clustering problems; that is, computing all clusterings that are not dominated in both objectives by other clusterings. Unlike previous work that deals with specific objectives for quality and fairness, we deal with all objectives for fairness and quality in two general classes encompassing most of the special cases addressed in previous work. Our algorithm must take exponential time in the worst case as the Parero front itself can be exponential. Even when the Pareto front is polynomial, our algorithm may take exponential time, and we prove that this is inevitable unless P = NP. However, we also present a new polynomial-time algorithm for computing the entire Pareto front when the cluster centers are fixed, and for perhaps the most natural fairness objective: minimizing the sum, over all clusters, of the imbalance between the two groups in each cluster.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Rashida Hakim, Ana-Andreea Stoica, Christos Papadimitriou, Mihalis Yannakakis
- arxiv_id: 
- openreview_id: bUi2xECa7w
- anthology_id: 
- pdf_url: https://openreview.net/pdf/dc96b5d71f0a1381f1c7e849579b36b8e561a9eb.pdf
- published: 2024
- keywords: clustering, algorithmic-fairness, multiobjective-optimization

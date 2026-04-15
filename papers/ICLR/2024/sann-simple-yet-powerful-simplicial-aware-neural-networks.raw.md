---
title: "SaNN: Simple Yet Powerful Simplicial-aware Neural Networks"
authors: ["Sravanthi Gurugubelli", "Sundeep Prabhakar Chepuri"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "eUgS9Ig8JG"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b5b2e785dec69b9ea0c8b01d6e2eca5896246cce.pdf"
published: "2024"
categories: []
keywords: ["Graph Neural Networks", "Higher-order Representation Learning", "Simplicial Complexes", "Simplicial Neural Networks", "Weisfeiler-Lehman Isomorphism Test"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:46+09:00"
---

# SaNN: Simple Yet Powerful Simplicial-aware Neural Networks

## Abstract
Simplicial neural networks (SNNs) are deep models for higher-order graph representation learning. SNNs learn low-dimensional embeddings of simplices in a simplicial complex by aggregating features of their respective upper, lower, boundary, and coboundary adjacent simplices. The aggregation in SNNs is carried out during training. Since the number of simplices of various orders in a simplicial complex is significantly large, the memory and training-time requirement in SNNs is enormous. In this work, we propose a scalable simplicial-aware neural network (SaNN) model with a constant run-time and memory requirements independent of the size of the simplicial complex and the density of interactions in it. SaNN is based on pre-aggregated simplicial-aware features as inputs to a neural network, so it has a strong simplicial-structural inductive bias. We provide theoretical conditions under which SaNN is provably more powerful than the Weisfeiler-Lehman (WL) graph isomorphism test and as powerful as the simplicial Weisfeiler-Lehman (SWL) test. We also show that SaNN is permutation and orientation equivariant and satisfies simplicial-awareness of the highest order in a simplicial complex. We demonstrate via numerical experiments that despite being computationally economical, the proposed model achieves state-of-the-art performance in predicting trajectories,  simplicial closures, and classifying graphs.

## Metadata
- venue: ICLR
- year: 2024
- authors: Sravanthi Gurugubelli, Sundeep Prabhakar Chepuri
- arxiv_id: 
- openreview_id: eUgS9Ig8JG
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b5b2e785dec69b9ea0c8b01d6e2eca5896246cce.pdf
- published: 2024
- keywords: Graph Neural Networks, Higher-order Representation Learning, Simplicial Complexes, Simplicial Neural Networks, Weisfeiler-Lehman Isomorphism Test

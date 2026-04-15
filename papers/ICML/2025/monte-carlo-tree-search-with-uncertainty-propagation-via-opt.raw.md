---
title: "Monte-Carlo Tree Search with Uncertainty Propagation via Optimal Transport"
authors: ["Tuan Quang Dam", "Pascal Stenger", "Lukas Schneider", "Joni Pajarinen", "Carlo D'Eramo", "Odalric-Ambrym Maillard"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "DUGFTH9W8B"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c6941e1eb6e0217febce89b2ba5f53f6c9f74195.pdf"
published: "2025"
categories: []
keywords: ["Monte-Carlo Tree Search", "Planning under Uncertainty"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:30+09:00"
---

# Monte-Carlo Tree Search with Uncertainty Propagation via Optimal Transport

## Abstract
This paper introduces a novel backup strategy for Monte-Carlo Tree Search (MCTS) tailored for highly stochastic and partially observable Markov decision processes. We adopt a probabilistic approach, modeling both value and action-value nodes as Gaussian distributions, to introduce a novel backup operator that computes value nodes as the Wasserstein barycenter of their action-value children nodes; thus, propagating the uncertainty of the estimate across the tree to the root node. We study our novel backup operator when using a novel combination of $L^1$-Wasserstein barycenter with $\alpha$-divergence, by drawing a crucial connection to the generalized mean backup operator. We complement our probabilistic backup operator with two sampling strategies, based on optimistic selection and Thompson sampling, obtaining our Wasserstein MCTS algorithm. We provide theoretical guarantees of asymptotic convergence of $\mathcal{O}(n^{-1/2})$, with $n$ as the number of visited trajectories, to the optimal policy and an empirical evaluation on several stochastic and partially observable environments, where our approach outperforms well-known related baselines.

## Metadata
- venue: ICML
- year: 2025
- authors: Tuan Quang Dam, Pascal Stenger, Lukas Schneider, Joni Pajarinen, Carlo D'Eramo, Odalric-Ambrym Maillard
- arxiv_id: 
- openreview_id: DUGFTH9W8B
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c6941e1eb6e0217febce89b2ba5f53f6c9f74195.pdf
- published: 2025
- keywords: Monte-Carlo Tree Search, Planning under Uncertainty

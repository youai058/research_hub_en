---
title: "Relax and Merge: A Simple Yet Effective Framework for Solving Fair $k$-Means and $k$-sparse Wasserstein Barycenter Problems"
authors: ["Shihong Song", "Guanlin Mo", "Hu Ding"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "n8h1z588eu"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d4e612794c2412e54938fa021f1e42ee55eabb50.pdf"
published: "2025"
categories: []
keywords: ["clustering", "k-means", "fairness", "approxiamte algorithm", "optimal transport"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:55+09:00"
---

# Relax and Merge: A Simple Yet Effective Framework for Solving Fair $k$-Means and $k$-sparse Wasserstein Barycenter Problems

## Abstract
The fairness of clustering algorithms has gained widespread attention across various areas, including machine learning, In this paper, we study fair $k$-means clustering in Euclidean space. 
  Given a dataset comprising several groups, the fairness constraint requires that each cluster should contain a proportion of points from each group within specified lower and upper bounds. 
  Due to these fairness constraints, determining the optimal locations of $k$ centers is a quite challenging task. 
  We propose a novel ``Relax and Merge'' framework that returns a $(1+4\rho + O(\epsilon))$-approximate solution,  where $\rho$ is the approximate ratio of an off-the-shelf vanilla $k$-means algorithm and $O(\epsilon)$ can be an arbitrarily small positive number. If equipped with a PTAS of $k$-means, our solution can achieve an approximation ratio of $(5+O(\epsilon))$  with only a slight violation of the fairness constraints, which improves the current state-of-the-art approximation guarantee. Furthermore, using our framework, we can also obtain a $(1+4\rho +O(\epsilon))$-approximate solution for the $k$-sparse Wasserstein Barycenter problem, which is a fundamental optimization problem in the field of optimal transport, and a $(2+6\rho)$-approximate solution for the strictly fair $k$-means clustering with no violation, both of which are better than the current state-of-the-art methods. In addition, the empirical results demonstrate that our proposed algorithm can significantly outperform baseline approaches in terms of clustering  cost.

## Metadata
- venue: ICLR
- year: 2025
- authors: Shihong Song, Guanlin Mo, Hu Ding
- arxiv_id: 
- openreview_id: n8h1z588eu
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d4e612794c2412e54938fa021f1e42ee55eabb50.pdf
- published: 2025
- keywords: clustering, k-means, fairness, approxiamte algorithm, optimal transport

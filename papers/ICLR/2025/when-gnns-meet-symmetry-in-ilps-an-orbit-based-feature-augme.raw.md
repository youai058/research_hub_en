---
title: "When GNNs meet symmetry in ILPs: an orbit-based feature augmentation approach"
authors: ["Qian Chen", "Lei Li", "Qian Li", "Jianghua Wu", "Akang Wang", "Ruoyu Sun", "Xiaodong Luo", "Tsung-Hui Chang", "Qingjiang Shi"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "wVTJRnZ11Z"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9e7bf20d0de6af278a2706124eee743427ede879.pdf"
published: "2025"
categories: []
keywords: ["integer linear programming", "symmetry", "machine learning", "graph neural networks"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:41+09:00"
---

# When GNNs meet symmetry in ILPs: an orbit-based feature augmentation approach

## Abstract
A common characteristic in integer linear programs (ILPs) is symmetry, allowing variables to be permuted without altering the underlying problem structure. Recently, GNNs have emerged as a promising approach for solving ILPs. 
However, a significant challenge arises when applying GNNs to ILPs with symmetry: classic GNN architectures struggle to differentiate between symmetric variables, which limits their predictive accuracy. In this work, we investigate the properties of permutation equivalence and invariance in GNNs, particularly in relation to the inherent symmetry of ILP formulations. We reveal that the interaction between these two factors contributes to the difficulty of distinguishing between symmetric variables.
To address this challenge, we explore the potential of feature augmentation and propose several guiding principles for constructing augmented features. Building on these principles, we develop an orbit-based augmentation scheme that first groups symmetric variables and then samples augmented features for each group from a discrete uniform distribution. Empirical results demonstrate that our proposed approach significantly enhances both training efficiency and predictive performance.

## Metadata
- venue: ICLR
- year: 2025
- authors: Qian Chen, Lei Li, Qian Li, Jianghua Wu, Akang Wang, Ruoyu Sun, Xiaodong Luo, Tsung-Hui Chang, Qingjiang Shi
- arxiv_id: 
- openreview_id: wVTJRnZ11Z
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9e7bf20d0de6af278a2706124eee743427ede879.pdf
- published: 2025
- keywords: integer linear programming, symmetry, machine learning, graph neural networks

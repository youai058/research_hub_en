---
title: "Clique Number Estimation via Differentiable Functions of Adjacency Matrix Permutations"
authors: ["Indradyumna Roy", "Eeshaan Jain", "Soumen Chakrabarti", "Abir De"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "DFSb67ksVr"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c827a3961d4fc71d35f295fe47af1a56513b177c.pdf"
published: "2025"
categories: []
keywords: ["Graph neural network", "distant supervision"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:47+09:00"
---

# Clique Number Estimation via Differentiable Functions of Adjacency Matrix Permutations

## Abstract
Estimating the clique number in a graph is central to various applications, e.g., community detection, graph retrieval, etc. 
Existing estimators often rely on non-differentiable combinatorial components. Here, we propose a full differentiable estimator for clique number estimation, which can be trained from distant supervision of clique numbers, rather than demonstrating actual cliques.
Our key insight is a formulation of the maximum clique problem (MCP) as a maximization of the size of fully dense square submatrix, within a suitably row-column-permuted adjacency matrix.
We design a differentiable mechanism to search for permutations that lead to the discovery of such dense blocks.
However, the optimal permutation is not unique, which leads to the learning of spurious permutations. To tackle this problem, we view the MCP problem as a sequence of subgraph matching tasks, each detecting progressively larger cliques in a nested manner. This allows effective navigation through suitable node permutations.
These steps result in MxNet, an end-to-end differentiable model, which learns to predict clique number without explicit clique demonstrations, with the added benefit of interpretability.  Experiments on eight datasets show the superior accuracy of our approach.

## Metadata
- venue: ICLR
- year: 2025
- authors: Indradyumna Roy, Eeshaan Jain, Soumen Chakrabarti, Abir De
- arxiv_id: 
- openreview_id: DFSb67ksVr
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c827a3961d4fc71d35f295fe47af1a56513b177c.pdf
- published: 2025
- keywords: Graph neural network, distant supervision

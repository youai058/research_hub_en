---
title: "QWO: Speeding Up Permutation-Based Causal Discovery in LiGAMs"
authors: ["Mohammad Shahverdikondori", "Ehsan Mokhtarian", "Negar Kiyavash"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "BptJGaPn9C"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/371aace23dbeed4b232f07124b02c6a205446743.pdf"
published: "2024"
categories: []
keywords: ["causal discovery", "permutation-based", "linear gaussian acyclic model", "DAG learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:57+09:00"
---

# QWO: Speeding Up Permutation-Based Causal Discovery in LiGAMs

## Abstract
Causal discovery is essential for understanding relationships among variables of interest in many scientific domains. In this paper, we focus on permutation-based methods for learning causal graphs in Linear Gaussian Acyclic Models (LiGAMs), where the permutation encodes a causal ordering of the variables. Existing methods in this setting are not scalable due to their high computational complexity. These methods are comprised of two main components: (i) constructing a specific DAG, $\mathcal{G}^\pi$, for a given permutation $\pi$, which represents the best structure that can be learned from the available data while adhering to $\pi$, and (ii) searching over the space of permutations (i.e., causal orders) to minimize the number of edges in $\mathcal{G}^\pi$. We introduce QWO, a novel approach that significantly enhances the efficiency of computing $\mathcal{G}^\pi$ for a given permutation $\pi$. QWO has a speed-up of $O(n^2)$ ($n$ is the number of variables) compared to the state-of-the-art BIC-based method, making it highly scalable. We show that our method is theoretically sound and can be integrated into existing search strategies such as GRASP and hill-climbing-based methods to improve their performance.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Mohammad Shahverdikondori, Ehsan Mokhtarian, Negar Kiyavash
- arxiv_id: 
- openreview_id: BptJGaPn9C
- anthology_id: 
- pdf_url: https://openreview.net/pdf/371aace23dbeed4b232f07124b02c6a205446743.pdf
- published: 2024
- keywords: causal discovery, permutation-based, linear gaussian acyclic model, DAG learning

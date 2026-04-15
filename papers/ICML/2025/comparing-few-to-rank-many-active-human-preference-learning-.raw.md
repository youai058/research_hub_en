---
title: "Comparing Few to Rank Many: Active Human Preference Learning Using Randomized Frank-Wolfe Method"
authors: ["Kiran Koshy Thekumparampil", "Gaurush Hiranandani", "Kousha Kalantari", "Shoham Sabach", "Branislav Kveton"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "cUNfm13VUR"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/bf05f501edc1ca9f2979bef5d6c125f616479259.pdf"
published: "2025"
categories: []
keywords: ["active learning", "human preference learning", "comparison feedback", "optimal design", "Frank-Wolfe method"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:15+09:00"
---

# Comparing Few to Rank Many: Active Human Preference Learning Using Randomized Frank-Wolfe Method

## Abstract
We study learning human preferences from limited comparison feedback, a core machine learning problem that is at the center of reinforcement learning from human feedback (RLHF). We formulate the problem as learning a Plackett-Luce (PL) model from a limited number of $K$-subset comparisons over a universe of $N$ items, where typically $K \ll N$. Our objective is to select the $K$-subsets such that all items can be ranked with minimal mistakes within the budget. We solve the problem using the D-optimal design, which minimizes the worst-case ranking loss under the estimated PL model. All known algorithms for this problem are computationally infeasible in our setting because we consider exponentially many subsets in $K$. To address this challenge, we propose a randomized Frank-Wolfe algorithm with memoization and sparse updates that has a low $O(N^2 + K^2)$ per-iteration complexity. We analyze it and demonstrate its empirical superiority on synthetic and open-source NLP datasets.

## Metadata
- venue: ICML
- year: 2025
- authors: Kiran Koshy Thekumparampil, Gaurush Hiranandani, Kousha Kalantari, Shoham Sabach, Branislav Kveton
- arxiv_id: 
- openreview_id: cUNfm13VUR
- anthology_id: 
- pdf_url: https://openreview.net/pdf/bf05f501edc1ca9f2979bef5d6c125f616479259.pdf
- published: 2025
- keywords: active learning, human preference learning, comparison feedback, optimal design, Frank-Wolfe method

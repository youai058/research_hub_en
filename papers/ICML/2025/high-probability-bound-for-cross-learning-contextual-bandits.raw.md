---
title: "High Probability Bound for Cross-Learning Contextual Bandits with Unknown Context Distributions"
authors: ["Ruiyuan Huang", "Zengfeng Huang"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "rTPq8VzhmZ"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/3404c0f109662ce93e299cd5a3f695ff28305d16.pdf"
published: "2025"
categories: []
keywords: ["bandit", "contextual bandit", "cross-learning", "high probability bounds"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:14+09:00"
---

# High Probability Bound for Cross-Learning Contextual Bandits with Unknown Context Distributions

## Abstract
Motivated by applications in online bidding and sleeping bandits, we examine the problem of contextual bandits with cross learning, where the learner observes the loss associated with the action across all possible contexts, not just the current round’s context. Our focus is on a setting where losses are chosen adversarially, and contexts are sampled i.i.d. from a specific distribution. This problem was first studied by Balseiro et al. (2019), who proposed an algorithm that achieves near-optimal regret under the assumption that the context distribution is known in advance. However, this assumption is often unrealistic. To address this issue, Schneider & Zimmert (2023) recently proposed a new algorithm that achieves nearly optimal expected regret. It is well-known that expected regret can be significantly weaker than high-probability bounds. In this paper, we present a novel, in-depth analysis of their algorithm and demonstrate that it actually achieves near-optimal regret with high probability. There are steps in the original analysis by Schneider & Zimmert (2023) that lead only to an expected bound by nature. In our analysis, we introduce several new insights. Specifically, we make extensive use of the weak dependency structure between different epochs, which was overlooked in previous analyses. Additionally, standard martingale inequalities are not directly applicable, so we refine martingale inequalities to complete our analysis.

## Metadata
- venue: ICML
- year: 2025
- authors: Ruiyuan Huang, Zengfeng Huang
- arxiv_id: 
- openreview_id: rTPq8VzhmZ
- anthology_id: 
- pdf_url: https://openreview.net/pdf/3404c0f109662ce93e299cd5a3f695ff28305d16.pdf
- published: 2025
- keywords: bandit, contextual bandit, cross-learning, high probability bounds

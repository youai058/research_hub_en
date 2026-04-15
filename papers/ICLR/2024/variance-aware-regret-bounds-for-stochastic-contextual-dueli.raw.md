---
title: "Variance-aware Regret Bounds for Stochastic Contextual Dueling Bandits"
authors: ["Qiwei Di", "Tao Jin", "Yue Wu", "Heyang Zhao", "Farzad Farnoud", "Quanquan Gu"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "rDH7dIFn20"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/4c1a08aad3975e9de1adbba054eea8e3f1287418.pdf"
published: "2024"
categories: []
keywords: ["Dueling Bandit", "Variance-aware", "contextual bandit"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:26+09:00"
---

# Variance-aware Regret Bounds for Stochastic Contextual Dueling Bandits

## Abstract
Dueling bandits is a prominent framework for decision-making involving preferential feedback, a valuable feature that fits various applications involving human interaction, such as ranking, information retrieval, and recommendation systems. While substantial efforts have been made to minimize the cumulative regret in dueling bandits, a notable gap in the current research is the absence of regret bounds that account for the inherent uncertainty in pairwise comparisons between the dueling arms. Intuitively, greater uncertainty suggests a higher level of difficulty in the problem.  To bridge this gap, this paper studies the problem of contextual dueling bandits, where the binary comparison of dueling arms is generated from a generalized linear model (GLM). We propose a new SupLinUCB-type algorithm that enjoys computational efficiency and a variance-aware regret bound $\tilde O\big(d\sqrt{\sum_{t=1}^T\sigma_t^2} + d\big)$, where $\sigma_t$ is the variance of the pairwise comparison at round $t$, $d$ is the dimension of the context vectors, and $T$ is the time horizon. Our regret bound naturally aligns with the intuitive expectation — in scenarios where the comparison is deterministic, the algorithm only suffers from an $\tilde O(d)$ regret. We perform empirical experiments on synthetic data to confirm the advantage of our method over previous variance-agnostic algorithms.

## Metadata
- venue: ICLR
- year: 2024
- authors: Qiwei Di, Tao Jin, Yue Wu, Heyang Zhao, Farzad Farnoud, Quanquan Gu
- arxiv_id: 
- openreview_id: rDH7dIFn20
- anthology_id: 
- pdf_url: https://openreview.net/pdf/4c1a08aad3975e9de1adbba054eea8e3f1287418.pdf
- published: 2024
- keywords: Dueling Bandit, Variance-aware, contextual bandit

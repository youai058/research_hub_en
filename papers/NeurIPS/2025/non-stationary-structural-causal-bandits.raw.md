---
title: "Non-Stationary Structural Causal Bandits"
authors: ["Yeahoon Kwon", "Yesong Choe", "Soungmin Park", "Neil Dhir", "Sanghack Lee"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "F4LhOqhxkk"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ee273457d1855fcccf336c1d78975ca0d8eb1464.pdf"
published: "2025"
categories: []
keywords: ["Non-stationarity", "Sequential Decision Making"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:55+09:00"
---

# Non-Stationary Structural Causal Bandits

## Abstract
We study the problem of sequential decision-making in environments governed by evolving causal mechanisms. Prior work on structural causal bandits--formulations that integrate causal graphs into multi-armed bandit problems to guide intervention selection--has shown that leveraging the causal structure can reduce unnecessary interventions by identifying possibly-optimal minimal intervention sets (POMISs). However, such formulations fall short in dynamic settings where reward distributions may vary over time, as their static, hence myopic, nature focuses on immediate rewards and overlooks the long-term effects of interventions. In this work, we propose a non-stationary structural causal bandit framework that leverages temporal structural causal models to capture evolving dynamics over time. We characterize how interventions propagate over time by developing graphical tools and assumptions, which form the basis for identifying non-myopic intervention strategies. Within this framework, we devise POMIS$^+$, which captures the existence of variables that contribute to maximizing both immediate and long-term rewards. Our framework provides a principled way to reason about temporally-aware interventions by explicitly modeling information propagation across time. Empirical results validate the effectiveness of our approach, demonstrating improved performance over myopic baselines.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Yeahoon Kwon, Yesong Choe, Soungmin Park, Neil Dhir, Sanghack Lee
- arxiv_id: 
- openreview_id: F4LhOqhxkk
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ee273457d1855fcccf336c1d78975ca0d8eb1464.pdf
- published: 2025
- keywords: Non-stationarity, Sequential Decision Making

---
title: "Geometry-Aware Approaches for Balancing Performance and Theoretical Guarantees in Linear Bandits"
authors: ["Yuwei Luo", "Mohsen Bayati"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Oeb0I3JcVc"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/83b325bb45438add11efd2a65fabbbb887598945.pdf"
published: "2025"
categories: []
keywords: ["Linear bandit", "Thompson sampling", "Greedy", "Data-driven exploration"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:03+09:00"
---

# Geometry-Aware Approaches for Balancing Performance and Theoretical Guarantees in Linear Bandits

## Abstract
This paper is motivated by recent research in the $d$-dimensional stochastic linear bandit literature, which has revealed an unsettling discrepancy: algorithms like Thompson sampling and Greedy demonstrate promising empirical performance, yet this contrasts with their pessimistic theoretical regret bounds. The challenge arises from the fact that while these algorithms may perform poorly in certain problem instances, they generally excel in typical instances. To address this, we propose a new data-driven technique that tracks the geometric properties of the uncertainty ellipsoid around the main problem parameter. This methodology enables us to formulate a data-driven frequentist regret bound, which incorporates the geometric information, for a broad class of base algorithms, including Greedy, OFUL, and Thompson sampling. This result allows us to identify and ``course-correct" problem instances in which the base algorithms perform poorly. The course-corrected algorithms achieve the minimax optimal regret of order $\tilde{\mathcal{O}}(d\sqrt{T})$ for a $T$-period decision-making scenario, effectively maintaining the desirable attributes of the base algorithms, including their empirical efficacy. We present simulation results to validate our findings using synthetic and real data.

## Metadata
- venue: ICLR
- year: 2025
- authors: Yuwei Luo, Mohsen Bayati
- arxiv_id: 
- openreview_id: Oeb0I3JcVc
- anthology_id: 
- pdf_url: https://openreview.net/pdf/83b325bb45438add11efd2a65fabbbb887598945.pdf
- published: 2025
- keywords: Linear bandit, Thompson sampling, Greedy, Data-driven exploration

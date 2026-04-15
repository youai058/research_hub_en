---
title: "A Differential and Pointwise Control Approach to Reinforcement Learning"
authors: ["Minh Phuong Nguyen", "Chandrajit L. Bajaj"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "xpVkYQofw9"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/81fbda097cab7501e7f2c3534c2a6862e4b180ba.pdf"
published: "2025"
categories: []
keywords: ["Hamiltonian Dynamics", "Policy Optimization", "Pointwise Convergence", "Continuous-Time Control", "Physics-Informed Learning", "Scientific Computing"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:47+09:00"
---

# A Differential and Pointwise Control Approach to Reinforcement Learning

## Abstract
Reinforcement learning (RL) in continuous state-action spaces remains challenging in scientific computing due to poor sample efficiency and lack of pathwise physical consistency. We introduce Differential Reinforcement Learning (Differential RL), a novel framework that reformulates RL from a continuous-time control perspective via a differential dual formulation. This induces a Hamiltonian structure that embeds physics priors and ensures consistent trajectories without requiring explicit constraints. To implement Differential RL, we develop Differential Policy Optimization (dfPO), a pointwise, stage-wise algorithm that refines local movement operators along the trajectory for improved sample efficiency and dynamic alignment. We establish pointwise convergence guarantees, a property not available in standard RL, and derive a competitive theoretical regret bound of $\mathcal{O}(K^{5/6})$. Empirically, dfPO outperforms standard RL baselines on representative scientific computing tasks, including surface modeling, grid control, and molecular dynamics, under low-data and physics-constrained conditions.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Minh Phuong Nguyen, Chandrajit L. Bajaj
- arxiv_id: 
- openreview_id: xpVkYQofw9
- anthology_id: 
- pdf_url: https://openreview.net/pdf/81fbda097cab7501e7f2c3534c2a6862e4b180ba.pdf
- published: 2025
- keywords: Hamiltonian Dynamics, Policy Optimization, Pointwise Convergence, Continuous-Time Control, Physics-Informed Learning, Scientific Computing

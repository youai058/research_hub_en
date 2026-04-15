---
title: "Federated Q-Learning: Linear Regret Speedup with Low Communication Cost"
authors: ["Zhong Zheng", "Fengyu Gao", "Lingzhou Xue", "Jing Yang"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "fe6ANBxcKM"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/6ae0807140d8835f40da63717a9baa1749faec87.pdf"
published: "2024"
categories: []
keywords: ["Federated Learning", "Reinforcement Learning", "Q-Learning", "Regret", "Communication Cost"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:16+09:00"
---

# Federated Q-Learning: Linear Regret Speedup with Low Communication Cost

## Abstract
In this paper, we consider federated reinforcement learning for tabular episodic Markov Decision Processes (MDP) where, under the coordination of a central server, multiple agents collaboratively explore the environment and learn an optimal policy without sharing their raw data.  While linear speedup in the number of agents has been achieved for some metrics, such as convergence rate and sample complexity, in similar settings, it is unclear whether it is possible to design a *model-free* algorithm to achieve linear *regret* speedup with low communication cost. We propose two federated Q-Learning algorithms termed as FedQ-Hoeffding and FedQ-Bernstein, respectively, and show that the corresponding total regrets achieve a linear speedup compared with their single-agent counterparts, while the communication cost scales logarithmically in the total number of time steps $T$. Those results rely on an event-triggered synchronization mechanism between the agents and the server, a novel step size selection when the server aggregates the local estimates of the state-action values to form the global estimates, and a set of new concentration inequalities to bound the sum of non-martingale differences. This is the first work showing that linear regret speedup and logarithmic communication cost can be achieved by model-free algorithms in federated reinforcement learning.

## Metadata
- venue: ICLR
- year: 2024
- authors: Zhong Zheng, Fengyu Gao, Lingzhou Xue, Jing Yang
- arxiv_id: 
- openreview_id: fe6ANBxcKM
- anthology_id: 
- pdf_url: https://openreview.net/pdf/6ae0807140d8835f40da63717a9baa1749faec87.pdf
- published: 2024
- keywords: Federated Learning, Reinforcement Learning, Q-Learning, Regret, Communication Cost

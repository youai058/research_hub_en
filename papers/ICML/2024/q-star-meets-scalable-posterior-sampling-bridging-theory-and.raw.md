---
title: "Q-Star Meets Scalable Posterior Sampling: Bridging Theory and Practice via HyperAgent"
authors: ["Yingru Li", "Jiawei Xu", "Lei Han", "Zhi-Quan Luo"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "OF7e0w1uon"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/21d1bbc8276fc96c77ad2ea600b16c1dfcd198ab.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:13+09:00"
---

# Q-Star Meets Scalable Posterior Sampling: Bridging Theory and Practice via HyperAgent

## Abstract
We propose HyperAgent, a reinforcement learning (RL) algorithm based on the hypermodel framework for exploration in RL. HyperAgent allows for the efficient incremental approximation of posteriors associated with an optimal action-value function ($Q^\star$) without the need for conjugacy and follows the greedy policies w.r.t. these approximate posterior samples. We demonstrate that HyperAgent offers robust performance in large-scale deep RL benchmarks. It can solve Deep Sea hard exploration problems with episodes that optimally scale with problem size and exhibits significant efficiency gains in the Atari suite. Implementing HyperAgent requires minimal code addition to well-established deep RL frameworks like DQN. We theoretically prove that, under tabular assumptions, HyperAgent achieves logarithmic per-step computational complexity while attaining sublinear regret, matching the best known randomized tabular RL algorithm.

## Metadata
- venue: ICML
- year: 2024
- authors: Yingru Li, Jiawei Xu, Lei Han, Zhi-Quan Luo
- arxiv_id: 
- openreview_id: OF7e0w1uon
- anthology_id: 
- pdf_url: https://openreview.net/pdf/21d1bbc8276fc96c77ad2ea600b16c1dfcd198ab.pdf
- published: 2024

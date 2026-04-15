---
title: "The Effective Horizon Explains Deep RL Performance in Stochastic Environments"
authors: ["Cassidy Laidlaw", "Banghua Zhu", "Stuart Russell", "Anca Dragan"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "5ES5Hdlbxw"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f82605ccc74bb3de9a73c5e505aaf9276c229c08.pdf"
published: "2024"
categories: []
keywords: ["reinforcement learning", "effective horizon", "RL theory", "theory of reinforcement learning", "instance-dependent bounds", "empirical validation of theory"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:00+09:00"
---

# The Effective Horizon Explains Deep RL Performance in Stochastic Environments

## Abstract
Reinforcement learning (RL) theory has largely focused on proving minimax sample complexity bounds. These require strategic exploration algorithms that use relatively limited function classes for representing the policy or value function. Our goal is to explain why deep RL algorithms often perform well in practice, despite using random exploration and much more expressive function classes like neural networks. Our work arrives at an explanation by showing that many stochastic MDPs can be solved by performing only a few steps of value iteration on the random policy’s Q function and then acting greedily. When this is true, we find that it is possible to separate the exploration and learning components of RL, making it much easier to analyze. We introduce a new RL algorithm, SQIRL, that iteratively learns a near-optimal policy by exploring randomly to collect rollouts and then performing a limited number of steps of fitted-Q iteration over those roll- outs. We find that any regression algorithm that satisfies basic in-distribution generalization properties can be used in SQIRL to efficiently solve common MDPs. This can explain why deep RL works with complex function approximators like neural networks, since it is empirically established that neural networks generalize well in-distribution. Furthermore, SQIRL explains why random exploration works well in practice, since we show many environments can be solved by effectively estimating the random policy’s Q-function and then applying zero or a few steps of value iteration. We leverage SQIRL to derive instance-dependent sample complexity bounds for RL that are exponential only in an “effective horizon” of lookahead—which is typically much smaller than the full horizon—and on the complexity of the class used for function approximation. Empirically, we also find that SQIRL performance strongly correlates with PPO and DQN performance in a variety of stochastic environments, supporting that our theoretical analysis is predictive of practical performance. Our code and data are available at https://github.com/cassidylaidlaw/effective-horizon.

## Metadata
- venue: ICLR
- year: 2024
- authors: Cassidy Laidlaw, Banghua Zhu, Stuart Russell, Anca Dragan
- arxiv_id: 
- openreview_id: 5ES5Hdlbxw
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f82605ccc74bb3de9a73c5e505aaf9276c229c08.pdf
- published: 2024
- keywords: reinforcement learning, effective horizon, RL theory, theory of reinforcement learning, instance-dependent bounds, empirical validation of theory

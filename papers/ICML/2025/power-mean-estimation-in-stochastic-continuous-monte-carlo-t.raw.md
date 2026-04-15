---
title: "Power Mean Estimation in Stochastic Continuous Monte-Carlo Tree Search"
authors: ["Tuan Quang Dam"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "LL8R2QUEvB"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/38b053208ebf49d4cf0a22e8b61c87dd520e4ca0.pdf"
published: "2025"
categories: []
keywords: ["Monte-Carlo Tree Search; Continuous Reinforcement Learning Planning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:30+09:00"
---

# Power Mean Estimation in Stochastic Continuous Monte-Carlo Tree Search

## Abstract
Monte Carlo Tree Search (MCTS) has demonstrated success in online planning for deterministic environments, yet significant challenges remain in adapting it to stochastic Markov Decision Processes (MDPs), particularly in continuous state-action spaces. Existing methods, such as HOOT, which combines MCTS with the Hierarchical Optimistic Optimization (HOO) bandit strategy, address continuous spaces but rely on a logarithmic exploration bonus that lacks theoretical guarantees in non-stationary, stochastic settings. Recent advancements, such as POLY-HOOT, introduced a polynomial bonus term to achieve convergence in deterministic MDPs, though a similar theory for stochastic MDPs remains undeveloped.
In this paper, we propose a novel MCTS algorithm, Stochastic-Power-HOOT, designed for continuous, stochastic MDPs. Stochastic-Power-HOOT integrates a power mean as a value backup operator, alongside a polynomial exploration bonus to address the non-stationarity inherent in continuous action spaces. Our theoretical analysis establishes that Stochastic-Power-HOOT converges at a polynomial rate of $\mathcal{O}(n^{-\zeta})$, $\zeta \in (0,1/2)$, where \( n \) is the number of visited trajectories, thereby extending the non-asymptotic convergence guarantees of POLY-HOOT to stochastic environments. Experimental results on stochastic tasks validate our theoretical findings, demonstrating the effectiveness of Stochastic-Power-HOOT in continuous, stochastic domains.

## Metadata
- venue: ICML
- year: 2025
- authors: Tuan Quang Dam
- arxiv_id: 
- openreview_id: LL8R2QUEvB
- anthology_id: 
- pdf_url: https://openreview.net/pdf/38b053208ebf49d4cf0a22e8b61c87dd520e4ca0.pdf
- published: 2025
- keywords: Monte-Carlo Tree Search; Continuous Reinforcement Learning Planning

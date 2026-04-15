---
title: "Stochastic Principal-Agent Problems: Computing and Learning Optimal History-Dependent Policies"
authors: ["Jiarui Gan", "R Majumdar", "Debmalya Mandal", "Goran Radanovic"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "u0rNHqMpFD"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2fbc7d10a63e1167402a84aef602f141e5300ee5.pdf"
published: "2025"
categories: []
keywords: ["stochastic games", "Markov games", "Stackelberg games", "information design", "mechanism design"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:38+09:00"
---

# Stochastic Principal-Agent Problems: Computing and Learning Optimal History-Dependent Policies

## Abstract
We study a stochastic principal-agent model. A principal and an agent interact in a stochastic environment, each privy to observations about the state not available to the other. The principal has the power of commitment, both to elicit information from the agent and to signal her own information. The players communicate with each other and then select actions independently. 
Both players are {\em far-sighted}, aiming to maximize their total payoffs over the entire time horizon. 
We consider both the computation and learning of the principal's optimal policy. 
The key challenge lies in enabling {\em history-dependent} policies, which are essential for achieving optimality in this model but difficult to cope with because of the exponential growth of possible histories as the size of the model increases; explicit representation of history-dependent policies is infeasible as a result.
To address this challenge, we develop algorithmic techniques based on the concept of {\em inducible value set}. The techniques yield an efficient algorithm that computes an $\epsilon$-approximate optimal policy in time polynomial in $1/\epsilon$. 
We also present an efficient learning algorithm for an episodic reinforcement learning setting with unknown transition probabilities. The algorithm achieves sublinear regret $\widetilde{\mathcal{O}}(T^{2/3})$ for both players over $T$ episodes.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Jiarui Gan, R Majumdar, Debmalya Mandal, Goran Radanovic
- arxiv_id: 
- openreview_id: u0rNHqMpFD
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2fbc7d10a63e1167402a84aef602f141e5300ee5.pdf
- published: 2025
- keywords: stochastic games, Markov games, Stackelberg games, information design, mechanism design

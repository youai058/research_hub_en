---
title: "Maximizing utility in multi-agent environments by anticipating the behavior of other learners"
authors: ["Angelos Assos", "Yuval Dagan", "Constantinos Costis Daskalakis"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "0uGlKYS7a2"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9d44235bc1b65c1b1ffa69d5cb4b2dc6095fe32b.pdf"
published: "2024"
categories: []
keywords: ["Game Theory; no regret; learning theory;"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:07+09:00"
---

# Maximizing utility in multi-agent environments by anticipating the behavior of other learners

## Abstract
Learning algorithms are often used to make decisions in sequential decision-making environments. In multi-agent settings, the decisions of each agent can affect the utilities/losses of the other agents. Therefore, if an agent is good at anticipating the behavior of the other agents, in particular how they will make decisions in each round as a function of their experience that far, it could try to judiciously make its own decisions over the rounds of the interaction so as to influence the other agents to behave in a way that ultimately benefits its own utility. In this paper, we study repeated two-player games involving two types of agents: a learner, which employs an online learning algorithm to choose its strategy in each round; and an optimizer, which knows the learner's utility function and the learner's online learning algorithm. The optimizer wants to plan ahead to maximize its own utility, while taking into account the learner's behavior. We provide two results: a positive result for repeated zero-sum games and a negative result for repeated general-sum games. Our positive result is an algorithm for the optimizer, which exactly maximizes its utility against a learner that plays the Replicator Dynamics --- the continuous-time analogue of Multiplicative Weights Update (MWU). Additionally, we use this result to provide an algorithm for the optimizer against MWU, i.e.~for the discrete-time setting, which guarantees an average utility for the optimizer that is higher than the value of the one-shot game. Our negative result shows that, unless P=NP, there is no Fully Polynomial Time Approximation Scheme (FPTAS) for maximizing the utility of an optimizer against a learner that best-responds to the history in each round. Yet, this still leaves open the question of whether there exists a polynomial-time algorithm that optimizes the utility up to $o(T)$.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Angelos Assos, Yuval Dagan, Constantinos Costis Daskalakis
- arxiv_id: 
- openreview_id: 0uGlKYS7a2
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9d44235bc1b65c1b1ffa69d5cb4b2dc6095fe32b.pdf
- published: 2024
- keywords: Game Theory; no regret; learning theory;

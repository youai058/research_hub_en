---
title: "On Evaluating Policies for Robust POMDPs"
authors: ["Merlijn Krale", "Eline M. Bovy", "Maris F. L. Galesloot", "Thiago D. Simão", "Nils Jansen"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "l2Wl77TSYY"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/78a37c35b1c236a47f3682d0a3ad799b0caad82c.pdf"
published: "2025"
categories: []
keywords: ["Robust POMDPs", "Policy evaluation", "Planning under uncertainty"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:53+09:00"
---

# On Evaluating Policies for Robust POMDPs

## Abstract
Robust partially observable Markov decision processes (RPOMDPs) model sequential decision-making problems under partial observability, where an agent must be robust against a range of dynamics. RPOMDPs can be viewed as a two-player game between an agent, who selects actions, and nature, who adversarially selects the dynamics. Evaluating an agent policy requires finding an adversarial nature
policy, which is computationally challenging. In this paper, we advance the evaluation of agent policies for RPOMDPs in three ways. First, we discuss suitable benchmarks. We observe that for some RPOMDPs, an optimal agent policy can be found by considering only subsets of nature policies, making them easier to solve. We formalize this concept of solvability and construct three benchmarks that are only solvable for expressive sets of nature policies. Second, we describe a new method to evaluate agent policies for RPOMDPs by solving an equivalent MDP. Third, we lift two well-known upper bounds from POMDPs to RPOMDPs, which can be used to efficiently approximate the optimality gap of a policy and serve as baselines. Our experimental evaluation shows that (1) our proposed benchmarks cannot be solved by assuming naive nature policies, (2) our method of evaluating policies is accurate, and (3) the upper bounds provide solid baselines for evaluation.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Merlijn Krale, Eline M. Bovy, Maris F. L. Galesloot, Thiago D. Simão, Nils Jansen
- arxiv_id: 
- openreview_id: l2Wl77TSYY
- anthology_id: 
- pdf_url: https://openreview.net/pdf/78a37c35b1c236a47f3682d0a3ad799b0caad82c.pdf
- published: 2025
- keywords: Robust POMDPs, Policy evaluation, Planning under uncertainty

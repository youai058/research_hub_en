---
title: "Frozen Policy Iteration: Computationally Efficient RL under Linear $Q^{\\pi}$ Realizability for Deterministic Dynamics"
authors: ["Yijing Ke", "Zihan Zhang", "Ruosong Wang"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "kW0SudrQEQ"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/27848e35b509cb27ef8f6eb179c63a8085aedb95.pdf"
published: "2026"
categories: []
keywords: ["Theory of Reinforcement Learning", "Policy Iteration", "Linear Function Approximation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:33+09:00"
---

# Frozen Policy Iteration: Computationally Efficient RL under Linear $Q^{\pi}$ Realizability for Deterministic Dynamics

## Abstract
We study computationally and statistically efficient reinforcement learning under the linear $Q^{\pi}$ realizability assumption, where any policy's $Q$-function is linear in a given state-action feature representation. Prior methods in this setting are either computationally intractable, or require (local) access to a simulator. In this paper, we propose a computationally efficient online RL algorithm, named *Frozen Policy Iteration*, under the linear $Q^{\pi}$ realizability setting that works for Markov Decision Processes (MDPs) with stochastic initial states, stochastic rewards and deterministic transitions. Our algorithm achieves a regret bound of $\widetilde{O}(\sqrt{d^2H^6T})$, where $d$ is the dimensionality of the feature space, $H$ is the horizon length, and $T$ is the total number of episodes. Our regret bound is optimal for linear (contextual) bandits which is a special case of our setting with $H = 1$. 


Existing policy iteration algorithms under the same setting heavily rely on repeatedly sampling the same state by access to the simulator, which is not implementable in the online setting with stochastic initial states studied in this paper.  In contrast, our new algorithm circumvents this limitation by strategically using only high-confidence part of the trajectory data and freezing the policy for well-explored states, which ensures that all data used by our algorithm remains effectively *on-policy* during the whole course of learning. 
We further demonstrate the versatility of our approach by extending it to the Uniform-PAC setting and to  function classes with bounded eluder dimension.

## Metadata
- venue: ICLR
- year: 2026
- authors: Yijing Ke, Zihan Zhang, Ruosong Wang
- arxiv_id: 
- openreview_id: kW0SudrQEQ
- anthology_id: 
- pdf_url: https://openreview.net/pdf/27848e35b509cb27ef8f6eb179c63a8085aedb95.pdf
- published: 2026
- keywords: Theory of Reinforcement Learning, Policy Iteration, Linear Function Approximation

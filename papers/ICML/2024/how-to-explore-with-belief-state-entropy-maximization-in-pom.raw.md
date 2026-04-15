---
title: "How to Explore with Belief: State Entropy Maximization in POMDPs"
authors: ["Riccardo Zamboni", "Duilio Cirino", "Marcello Restelli", "Mirco Mutti"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "LbcNAIgNnB"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/fffa46a5651fc7d1c6252b8eed82eb450a780573.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:20+09:00"
---

# How to Explore with Belief: State Entropy Maximization in POMDPs

## Abstract
Recent works have studied *state entropy maximization* in reinforcement learning, in which the agent's objective is to learn a policy inducing high entropy over states visitation (Hazan et al., 2019). They typically assume full observability of the state of the system, so that the entropy of the observations is maximized. In practice, the agent may only get *partial* observations, e.g., a robot perceiving the state of a physical space through proximity sensors and cameras. A significant mismatch between the entropy over observations and true states of the system can arise in those settings. In this paper, we address the problem of entropy maximization over the *true states* with a decision policy conditioned on partial observations *only*. The latter is a generalization of POMDPs, which is intractable in general. We develop a memory and computationally efficient *policy gradient* method to address a first-order relaxation of the objective defined on *belief* states, providing various formal characterizations of approximation gaps, the optimization landscape, and the *hallucination* problem. This paper aims to generalize state entropy maximization to more realistic domains that meet the challenges of applications.

## Metadata
- venue: ICML
- year: 2024
- authors: Riccardo Zamboni, Duilio Cirino, Marcello Restelli, Mirco Mutti
- arxiv_id: 
- openreview_id: LbcNAIgNnB
- anthology_id: 
- pdf_url: https://openreview.net/pdf/fffa46a5651fc7d1c6252b8eed82eb450a780573.pdf
- published: 2024

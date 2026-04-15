---
title: "Finite-Time Analysis of On-Policy Heterogeneous Federated Reinforcement Learning"
authors: ["Chenyu Zhang", "Han Wang", "Aritra Mitra", "James Anderson"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "D2eOVqPX9g"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f97ca95cc9cf273902a1eba91646203707a42223.pdf"
published: "2024"
categories: []
keywords: ["reinforcement learning", "federated learning", "temporal difference learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:15+09:00"
---

# Finite-Time Analysis of On-Policy Heterogeneous Federated Reinforcement Learning

## Abstract
Federated reinforcement learning (FRL) has emerged as a promising paradigm for reducing the sample complexity of reinforcement learning tasks by exploiting information from different agents. However, when each agent interacts with a potentially different environment, little to nothing is known theoretically about the non-asymptotic performance of FRL algorithms. The lack of such results can be attributed to various technical challenges and their intricate interplay: Markovian sampling, linear function approximation, multiple local updates to save communication, heterogeneity in the reward functions and transition kernels of the agents' MDPs, and continuous state-action spaces.  Moreover, in the on-policy setting, the behavior policies vary with time, further complicating the analysis. In response, we introduce FedSARSA, a novel federated on-policy reinforcement learning scheme, equipped with linear function approximation, to address these challenges and provide a comprehensive finite-time error analysis. Notably, we establish that FedSARSA converges to a policy that is near-optimal for all agents, with the extent of near-optimality proportional to the level of heterogeneity. Furthermore, we prove that FedSARSA leverages agent collaboration to enable linear speedups as the number of agents increases, which holds for both fixed and adaptive step-size configurations.

## Metadata
- venue: ICLR
- year: 2024
- authors: Chenyu Zhang, Han Wang, Aritra Mitra, James Anderson
- arxiv_id: 
- openreview_id: D2eOVqPX9g
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f97ca95cc9cf273902a1eba91646203707a42223.pdf
- published: 2024
- keywords: reinforcement learning, federated learning, temporal difference learning

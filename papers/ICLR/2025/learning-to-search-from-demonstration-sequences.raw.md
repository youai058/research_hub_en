---
title: "Learning to Search from Demonstration Sequences"
authors: ["Dixant Mittal", "Liwei Kang", "Wee Sun Lee"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "v593OaNePQ"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/0035d08afe5262daf4fe1ee8c8c2d52957d3dfd3.pdf"
published: "2025"
categories: []
keywords: ["planning", "reasoning", "learning to search", "reinforcement learning", "large language model"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:05+09:00"
---

# Learning to Search from Demonstration Sequences

## Abstract
Search and planning are essential for solving many real-world problems. However, in numerous learning scenarios, only action-observation sequences, such as demonstrations or instruction sequences, are available for learning. Relying solely on supervised learning with these sequences can lead to sub-optimal performance due to the vast, unseen search space encountered during training. In this paper, we introduce Differentiable Tree Search Network (D-TSN), a novel neural network architecture that learns to construct search trees from just sequences of demonstrations by performing gradient descent on a best-first search tree construction algorithm. D-TSN enables the joint learning of submodules, including an encoder, value function, and world model, which are essential for planning. To construct the search tree, we employ a stochastic tree expansion policy and formulate it as another decision-making task. Then, we optimize the tree expansion policy via REINFORCE with an effective variance reduction technique for the gradient computation. D-TSN can be applied to problems with a known world model or to scenarios where it needs to jointly learn a world model with a latent state space. We study problems from these two scenarios, including Game of 24, 2D grid navigation, and Procgen games, to understand when D-TSN is more helpful. Through our experiments, we show that D-TSN is effective, especially when the world model with a latent state space is jointly learned. The code is available at https://github.com/dixantmittal/differentiable-tree-search-network.

## Metadata
- venue: ICLR
- year: 2025
- authors: Dixant Mittal, Liwei Kang, Wee Sun Lee
- arxiv_id: 
- openreview_id: v593OaNePQ
- anthology_id: 
- pdf_url: https://openreview.net/pdf/0035d08afe5262daf4fe1ee8c8c2d52957d3dfd3.pdf
- published: 2025
- keywords: planning, reasoning, learning to search, reinforcement learning, large language model

---
title: "Understanding and Improving Hyperbolic Deep Reinforcement Learning"
authors: ["Timo Klein", "Thomas Lang", "Andrii Shkabrii", "Alexander Sturm", "Kevin Sidak", "Lukas Miklautz", "Claudia Plant", "Yllka Velaj", "Sebastian Tschiatschek"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "7rfdenlP1L"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d003abc5b46277b0f8c0811a9d4128991bc0b123.pdf"
published: "2026"
categories: []
keywords: ["reinforcement learning", "representation learning", "hyperbolic space", "hyperbolic deep learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:41+09:00"
---

# Understanding and Improving Hyperbolic Deep Reinforcement Learning

## Abstract
The exponential volume growth of hyperbolic geometry can embed the hierarchical relationships between states in reinforcement learning (RL) with far less distortion than Euclidean space. However, hyperbolic deep RL faces severe optimization challenges, and formal analysis of why optimization fails is lacking. We identify key factors that determine the success and failure of training hyperbolic deep RL agents. By analyzing the gradients of core operations in the Poincaré Ball and Hyperboloid models of hyperbolic geometry, we show that large-norm embeddings destabilize gradient-based training, leading to trust-region violations in proximal policy optimization (PPO). Based on these insights, we introduce Hyper++, a new hyperbolic deep RL agent that consists of three components: (1) feature regularization guaranteeing bounded norms while avoiding the curse of dimensionality from clipping; (2) a categorical value loss for stable critic training; and (3) a more optimization-friendly formulation of hyperbolic network layers. On ProcGen, we show that Hyper++ guarantees stable learning, outperforms prior hyperbolic agents, and reduces wall-clock time by approximately 30%. On Atari-5 with Double DQN, Hyper++ strongly outperforms Euclidean and hyperbolic baselines. We release our code at https://github.com/Probabilistic-and-Interactive-ML/hyper-rl.

## Metadata
- venue: ICLR
- year: 2026
- authors: Timo Klein, Thomas Lang, Andrii Shkabrii, Alexander Sturm, Kevin Sidak, Lukas Miklautz, Claudia Plant, Yllka Velaj, Sebastian Tschiatschek
- arxiv_id: 
- openreview_id: 7rfdenlP1L
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d003abc5b46277b0f8c0811a9d4128991bc0b123.pdf
- published: 2026
- keywords: reinforcement learning, representation learning, hyperbolic space, hyperbolic deep learning

---
title: "TR2-D2: Tree Search Guided Trajectory-Aware Fine-Tuning for Discrete Diffusion"
authors: ["Sophia Tang", "Yuchen Zhu", "Molei Tao", "Pranam Chatterjee"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2509.25171"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2509.25171v1"
published: "2025-09-29"
categories: ["cs.LG", "q-bio.BM"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:40+09:00"
---

# TR2-D2: Tree Search Guided Trajectory-Aware Fine-Tuning for Discrete Diffusion

## Abstract
Reinforcement learning with stochastic optimal control offers a promising framework for diffusion fine-tuning, where a pre-trained diffusion model is optimized to generate paths that lead to a reward-tilted distribution. While these approaches enable optimization without access to explicit samples from the optimal distribution, they require training on rollouts under the current fine-tuned model, making them susceptible to reinforcing sub-optimal trajectories that yield poor rewards. To overcome this challenge, we introduce TRee Search Guided TRajectory-Aware Fine-Tuning for Discrete Diffusion (TR2-D2), a novel framework that optimizes reward-guided discrete diffusion trajectories with tree search to construct replay buffers for trajectory-aware fine-tuning. These buffers are generated using Monte Carlo Tree Search (MCTS) and subsequently used to fine-tune a pre-trained discrete diffusion model under a stochastic optimal control objective. We validate our framework on single- and multi-objective fine-tuning of biological sequence diffusion models, highlighting the overall effectiveness of TR2-D2 for reliable reward-guided fine-tuning in discrete sequence generation.

## Metadata
- venue: arXiv
- year: 2025
- authors: Sophia Tang, Yuchen Zhu, Molei Tao, Pranam Chatterjee
- arxiv_id: 2509.25171
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2509.25171v1
- published: 2025-09-29

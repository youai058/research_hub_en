---
title: "Langevin Soft Actor-Critic: Efficient Exploration through Uncertainty-Driven Critic Learning"
authors: ["Haque Ishfaq", "Guangyuan Wang", "Sami Nur Islam", "Doina Precup"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "FvQsk3la17"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/cd0c8d7ae2ff9e613598dc4f01b80fb409713495.pdf"
published: "2025"
categories: []
keywords: ["Actor-Critic", "Exploration", "Reinforcement Learning", "Thompson Sampling", "Langevin Monte Carlo", "Deep Reinforcement learning", "Continuous Control"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:03+09:00"
---

# Langevin Soft Actor-Critic: Efficient Exploration through Uncertainty-Driven Critic Learning

## Abstract
Existing actor-critic algorithms, which are popular for continuous control reinforcement learning (RL) tasks, suffer from poor sample efficiency due to lack of principled exploration mechanism within them. Motivated by the success of Thompson sampling for efficient exploration in RL, we propose a novel model-free RL algorithm, \emph{Langevin Soft Actor Critic} (LSAC), which prioritizes enhancing critic learning through uncertainty estimation over policy optimization. LSAC employs three key innovations: approximate Thompson sampling through distributional Langevin Monte Carlo (LMC) based $Q$ updates, parallel tempering for exploring multiple modes of the posterior of the $Q$ function, and diffusion synthesized state-action samples regularized with $Q$ action gradients. Our extensive experiments demonstrate that LSAC outperforms or matches the performance of mainstream model-free RL algorithms for continuous control tasks.
Notably, LSAC marks the first successful application of an LMC based Thompson sampling in continuous control tasks with continuous action spaces.

## Metadata
- venue: ICLR
- year: 2025
- authors: Haque Ishfaq, Guangyuan Wang, Sami Nur Islam, Doina Precup
- arxiv_id: 
- openreview_id: FvQsk3la17
- anthology_id: 
- pdf_url: https://openreview.net/pdf/cd0c8d7ae2ff9e613598dc4f01b80fb409713495.pdf
- published: 2025
- keywords: Actor-Critic, Exploration, Reinforcement Learning, Thompson Sampling, Langevin Monte Carlo, Deep Reinforcement learning, Continuous Control

---
title: "Recurrent Action Transformer with Memory"
authors: ["Egor Cherepanov", "Aleksei Staroverov", "Alexey Kovalev", "Aleksandr Panov"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "kByN4v0M3e"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/af0c5881605f88cb023dbe6d71689d26261dfbb2.pdf"
published: "2026"
categories: []
keywords: ["RL", "Offline RL", "Memory", "Transformers", "POMDP"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:21+09:00"
---

# Recurrent Action Transformer with Memory

## Abstract
Transformers have become increasingly popular in offline reinforcement learning (RL) due to their ability to treat agent trajectories as sequences, reframing policy learning as a sequence modeling task. However, in partially observable environments (POMDPs), effective decision-making depends on retaining information about past events - something that standard transformers struggle with due to the quadratic complexity of self-attention, which limits their context length. One solution to this problem is to extend transformers with memory mechanisms. We propose the Recurrent Action Transformer with Memory (RATE), a novel transformer-based architecture for offline RL that incorporates a recurrent memory mechanism designed to regulate information retention. We evaluate RATE across a diverse set of environments: memory-intensive tasks (ViZDoom-Two-Colors, T-Maze, Memory Maze, Minigrid-Memory, and POPGym), as well as standard Atari and MuJoCo benchmarks. Our comprehensive experiments demonstrate that RATE significantly improves performance in memory-dependent settings while remaining competitive on standard tasks across a broad range of baselines. These findings underscore the pivotal role of integrated memory mechanisms in offline RL and establish RATE as a unified, high-capacity architecture for effective decision-making over extended horizons.

## Metadata
- venue: ICLR
- year: 2026
- authors: Egor Cherepanov, Aleksei Staroverov, Alexey Kovalev, Aleksandr Panov
- arxiv_id: 
- openreview_id: kByN4v0M3e
- anthology_id: 
- pdf_url: https://openreview.net/pdf/af0c5881605f88cb023dbe6d71689d26261dfbb2.pdf
- published: 2026
- keywords: RL, Offline RL, Memory, Transformers, POMDP

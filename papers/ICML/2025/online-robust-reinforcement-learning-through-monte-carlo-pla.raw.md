---
title: "Online Robust Reinforcement Learning Through Monte-Carlo Planning"
authors: ["Tuan Quang Dam", "Kishan Panaganti", "Brahim Driss", "Adam Wierman"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "m25ma7O7Ec"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/0f0680654855675738d2a2ad0369425064d1ffa2.pdf"
published: "2025"
categories: []
keywords: ["Monte-carlo tree search", "distributionally robust reinforcement learning", "online reinforcement learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:31+09:00"
---

# Online Robust Reinforcement Learning Through Monte-Carlo Planning

## Abstract
Monte Carlo Tree Search (MCTS) is a powerful framework for solving complex decision-making problems, yet it often relies on the assumption that the simulator and the real-world dynamics are identical. Although this assumption helps achieve the success of MCTS in games like Chess, Go, and Shogi, the real-world scenarios incur ambiguity due to their modeling mismatches in low-fidelity simulators. In this work, we present a new robust variant of MCTS that mitigates dynamical model ambiguities. Our algorithm addresses transition dynamics and reward distribution ambiguities to bridge the gap between simulation-based planning and real-world deployment. We incorporate a robust power mean backup operator and carefully designed exploration bonuses to ensure finite-sample convergence at every node in the search tree. We show that our algorithm achieves a convergence rate of $\mathcal{O}(n^{-1/2})$ for the value estimation at the root node, comparable to that of standard MCTS. Finally, we provide empirical evidence that our method achieves robust performance in planning problems even under significant ambiguity in the underlying reward distribution and transition dynamics.

## Metadata
- venue: ICML
- year: 2025
- authors: Tuan Quang Dam, Kishan Panaganti, Brahim Driss, Adam Wierman
- arxiv_id: 
- openreview_id: m25ma7O7Ec
- anthology_id: 
- pdf_url: https://openreview.net/pdf/0f0680654855675738d2a2ad0369425064d1ffa2.pdf
- published: 2025
- keywords: Monte-carlo tree search, distributionally robust reinforcement learning, online reinforcement learning

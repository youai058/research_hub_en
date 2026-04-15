---
title: "MIRACLE: Model-free Imitation and Reinforcement Learning for Adaptive Cut-Selection"
authors: ["Arjun M.", "Rijul Tandon", "Agam Gupta", "HARIPRASAD KODAMANA", "Manojkumar Ramteke"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "zZyxHmId3w"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/255454705b4a96aab0caa0a3aa8785397a0d404e.pdf"
published: "2026"
categories: []
keywords: ["Model-Based Reinforcement Learning", "Adversarial Reward Learning", "Proximal Policy Optimization", "Mixed-Integer Programming", "Combinatorial Optimization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:42+09:00"
---

# MIRACLE: Model-free Imitation and Reinforcement Learning for Adaptive Cut-Selection

## Abstract
Mixed-Integer Programming (MIP) solvers rely heavily on cutting planes to tighten LP relaxations, but traditional approaches generate thousands of cuts that consume gigabytes of memory while providing minimal benefit. We present an intelligent cut selection framework that achieves a 98.1\% reduction in memory usage while maintaining competitive solving with an objective gap of approximately 0.08\%. Within this RL framework, we use Proximal Policy Optimization (PPO) to learn a behavioral model that imitates the expert solver’s decisions. The adversarially imitated behavioral model drives an agent comprising these key innovations: (i) a cut-selection policy trained via curriculum learning; and (ii) adaptive inference that dynamically adjusts computational budgets. Through comprehensive evaluation across SetCover and diverse MIPLIB problems, we demonstrate consistent speedups (3.78$\times$ average on MIPLIB) and achieve a 100\% success rate on instances where traditional SCIP fails 47-53\% of the time. Our method also reduces peak memory consumption from 3.03GB to 46 MB, enabling optimization in previously inaccessible and other resource-constrained environments where traditional solvers face fundamental limitations.

## Metadata
- venue: ICLR
- year: 2026
- authors: Arjun M., Rijul Tandon, Agam Gupta, HARIPRASAD KODAMANA, Manojkumar Ramteke
- arxiv_id: 
- openreview_id: zZyxHmId3w
- anthology_id: 
- pdf_url: https://openreview.net/pdf/255454705b4a96aab0caa0a3aa8785397a0d404e.pdf
- published: 2026
- keywords: Model-Based Reinforcement Learning, Adversarial Reward Learning, Proximal Policy Optimization, Mixed-Integer Programming, Combinatorial Optimization

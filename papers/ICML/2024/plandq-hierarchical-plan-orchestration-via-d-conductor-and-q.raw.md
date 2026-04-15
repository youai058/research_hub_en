---
title: "PlanDQ: Hierarchical Plan Orchestration via D-Conductor and Q-Performer"
authors: ["Chang Chen", "Junyeob Baek", "Fei Deng", "Kenji Kawaguchi", "Caglar Gulcehre", "Sungjin Ahn"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "17ZwoHl65h"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/0649e0b33856133b26c1896cfb7349c299b4ea79.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:34+09:00"
---

# PlanDQ: Hierarchical Plan Orchestration via D-Conductor and Q-Performer

## Abstract
Despite the recent advancements in offline RL, no unified algorithm could achieve superior performance across a broad range of tasks. Offline *value function learning*, in particular, struggles with sparse-reward, long-horizon tasks due to the difficulty of solving credit assignment and extrapolation errors that accumulates as the horizon of the task grows. On the other hand, models that can perform well in long-horizon tasks are designed specifically for goal-conditioned tasks, which commonly perform worse than value function learning methods on short-horizon, dense-reward scenarios. To bridge this gap, we propose a hierarchical planner designed for offline RL called PlanDQ. PlanDQ incorporates a diffusion-based planner at the high level, named D-Conductor, which guides the low-level policy through sub-goals. At the low level, we used a Q-learning based approach called the Q-Performer to accomplish these sub-goals. Our experimental results suggest that PlanDQ can achieve superior or competitive performance on D4RL continuous control benchmark tasks as well as AntMaze, Kitchen, and Calvin as long-horizon tasks.

## Metadata
- venue: ICML
- year: 2024
- authors: Chang Chen, Junyeob Baek, Fei Deng, Kenji Kawaguchi, Caglar Gulcehre, Sungjin Ahn
- arxiv_id: 
- openreview_id: 17ZwoHl65h
- anthology_id: 
- pdf_url: https://openreview.net/pdf/0649e0b33856133b26c1896cfb7349c299b4ea79.pdf
- published: 2024

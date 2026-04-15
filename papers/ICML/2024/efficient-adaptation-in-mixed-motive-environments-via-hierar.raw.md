---
title: "Efficient Adaptation in Mixed-Motive Environments via Hierarchical Opponent Modeling and Planning"
authors: ["Yizhe Huang", "Anji Liu", "Fanqi Kong", "Yaodong Yang", "Song-Chun Zhu", "Xue Feng"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "disVlUOH4b"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e99b607dec6a0a5cd7339da61b4e0306ed4b9807.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:20+09:00"
---

# Efficient Adaptation in Mixed-Motive Environments via Hierarchical Opponent Modeling and Planning

## Abstract
Despite the recent successes of multi-agent reinforcement learning (MARL) algorithms, efficiently adapting to co-players in mixed-motive environments remains a significant challenge. One feasible approach is to hierarchically model co-players' behavior based on inferring their characteristics. However, these methods often encounter difficulties in efficient reasoning and utilization of inferred information. To address these issues, we propose Hierarchical Opponent modeling and Planning (HOP), a novel multi-agent decision-making algorithm that enables few-shot adaptation to unseen policies in mixed-motive environments. HOP is hierarchically composed of two modules: an opponent modeling module that infers others' goals and learns corresponding goal-conditioned policies, and a planning module that employs Monte Carlo Tree Search (MCTS) to identify the best response. Our approach improves efficiency by updating beliefs about others' goals both across and within episodes and by using information from the opponent modeling module to guide planning. Experimental results demonstrate that in mixed-motive environments, HOP exhibits superior few-shot adaptation capabilities when interacting with various unseen agents, and excels in self-play scenarios. Furthermore, the emergence of social intelligence during our experiments underscores the potential of our approach in complex multi-agent environments.

## Metadata
- venue: ICML
- year: 2024
- authors: Yizhe Huang, Anji Liu, Fanqi Kong, Yaodong Yang, Song-Chun Zhu, Xue Feng
- arxiv_id: 
- openreview_id: disVlUOH4b
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e99b607dec6a0a5cd7339da61b4e0306ed4b9807.pdf
- published: 2024

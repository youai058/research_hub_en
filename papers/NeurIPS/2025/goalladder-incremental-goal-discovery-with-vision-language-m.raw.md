---
title: "GoalLadder: Incremental Goal Discovery with Vision-Language Models"
authors: ["Alexey Zakharov", "Shimon Whiteson"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "BiowiwzQaO"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/1bd1725eab30686d6f19c7b22db26e952e0088e3.pdf"
published: "2025"
categories: []
keywords: ["reinforcement learning", "vision-language models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:22+09:00"
---

# GoalLadder: Incremental Goal Discovery with Vision-Language Models

## Abstract
Natural language can offer a concise and human-interpretable means of specifying reinforcement learning (RL) tasks. The ability to extract rewards from a language instruction can enable the development of robotic systems that can learn from human guidance; however, it remains a challenging problem, especially in visual environments. Existing approaches that employ large, pretrained language models either rely on non‑visual environment representations, require prohibitively large amounts of feedback, or generate noisy, ill‑shaped reward functions. In this paper, we propose a novel method, GoalLadder, that leverages vision-language models (VLMs) to train RL agents from a single language instruction in visual environments. GoalLadder works by incrementally discovering states that bring the agent closer to completing a task specified in natural language. To do so, it queries a VLM to identify states that represent an improvement in agent's task progress and to rank them using pairwise comparisons. Unlike prior work, GoalLadder does not trust VLM's feedback completely; instead, it uses it to rank potential goal states using an ELO-based rating system, thus reducing the detrimental effects of noisy VLM feedback. Over the course of training, the agent is tasked with minimising the distance to the top-ranked goal in a learned embedding space, which is trained on unlabelled visual data. This key feature allows us to bypass the need for abundant and accurate feedback typically required to train a well-shaped reward function. We demonstrate that GoalLadder outperforms existing related methods on classic control and robotic manipulation environments with the average final success rate of $\sim$95\% compared to only $\sim$45\% of the best competitor.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Alexey Zakharov, Shimon Whiteson
- arxiv_id: 
- openreview_id: BiowiwzQaO
- anthology_id: 
- pdf_url: https://openreview.net/pdf/1bd1725eab30686d6f19c7b22db26e952e0088e3.pdf
- published: 2025
- keywords: reinforcement learning, vision-language models

---
title: "Reinforcement Learning with Action Chunking"
authors: ["Qiyang Li", "Zhiyuan Zhou", "Sergey Levine"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "XUks1Y96NR"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/135bcf397192fe967b2919142b723e9782691533.pdf"
published: "2025"
categories: []
keywords: ["reinforcement learning", "offline-to-online RL", "exploration"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:59+09:00"
---

# Reinforcement Learning with Action Chunking

## Abstract
We present Q-chunking, a simple yet effective recipe for improving reinforcement learning (RL) algorithms for long-horizon, sparse-reward tasks. Our recipe is designed for the offline-to-online RL setting, where the goal is to leverage an offline prior dataset to maximize the sample-efficiency of online learning. Effective exploration and sample-efficient learning remain central challenges in this setting, as it is not obvious how the offline data should be utilized to acquire a good exploratory policy. Our key insight is that action chunking, a technique popularized in imitation learning where sequences of future actions are predicted rather than a single action at each timestep, can be applied to temporal difference (TD)-based RL methods to mitigate the exploration challenge. Q-chunking adopts action chunking by directly running RL in a *chunked* action space, enabling the agent to (1) leverage temporally consistent behaviors from offline data for more effective online exploration and (2) use unbiased $n$-step backups for more stable and efficient TD learning. Our experimental results demonstrate that Q-chunking exhibits strong offline performance and online sample efficiency, outperforming prior best offline-to-online methods on a range of long-horizon, sparse-reward manipulation tasks.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Qiyang Li, Zhiyuan Zhou, Sergey Levine
- arxiv_id: 
- openreview_id: XUks1Y96NR
- anthology_id: 
- pdf_url: https://openreview.net/pdf/135bcf397192fe967b2919142b723e9782691533.pdf
- published: 2025
- keywords: reinforcement learning, offline-to-online RL, exploration

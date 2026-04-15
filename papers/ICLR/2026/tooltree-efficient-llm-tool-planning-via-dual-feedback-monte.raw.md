---
title: "ToolTree: Efficient LLM Tool Planning via Dual-Feedback Monte Carlo Tree Search and Bidirectional Pruning"
authors: ["Shuo Yang", "Caren Han", "Yihao Ding", "Shuhe Wang", "Eduard Hovy"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Ef5O9gNNLE"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ddd85988dbbe26fa44b01f9372d1c2d599a8713c.pdf"
published: "2026"
categories: []
keywords: ["Tool Planning", "Monte-Carlo Tree Search", "Agent Tool Use"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:48+09:00"
---

# ToolTree: Efficient LLM Tool Planning via Dual-Feedback Monte Carlo Tree Search and Bidirectional Pruning

## Abstract
Large Language Model (LLM) agents are increasingly applied to complex, multi-step tasks that require interaction with diverse external tools across various domains. However, current LLM agent tool planning methods typically rely on greedy, reactive tool selection strategies that lack foresight and fail to account for inter-tool dependencies.
In this paper, we present ToolTree, a novel Monte-Carlo tree search-inspired planning paradigm for tool planning. ToolTree explores possible tool usage trajectories using a dual-stage LLM evaluation and bidirectional pruning mechanism that enables the agent to make informed, adaptive decisions over extended tool-use sequences while pruning less promising branches before and after the tool execution. Empirical evaluations across both open-set and closed-set tool planning tasks on 4 benchmarks demonstrate that ToolTree consistently improves performance while keeping the highest efficiency, achieving an average gain of around 10\% compared to the state-of-the-art planning paradigm.

## Metadata
- venue: ICLR
- year: 2026
- authors: Shuo Yang, Caren Han, Yihao Ding, Shuhe Wang, Eduard Hovy
- arxiv_id: 
- openreview_id: Ef5O9gNNLE
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ddd85988dbbe26fa44b01f9372d1c2d599a8713c.pdf
- published: 2026
- keywords: Tool Planning, Monte-Carlo Tree Search, Agent Tool Use

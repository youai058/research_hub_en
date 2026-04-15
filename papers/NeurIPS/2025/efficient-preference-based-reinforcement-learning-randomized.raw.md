---
title: "Efficient Preference-Based Reinforcement Learning: Randomized Exploration meets Experimental Design"
authors: ["Andreas Schlaginhaufen", "Reda Ouhamma", "Maryam Kamgarpour"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "qEfgajdKea"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/741b01ab9338378b6a7ee3a884ceebe29405b5c3.pdf"
published: "2025"
categories: []
keywords: ["RLHF", "Preference learning", "RL", "Optimal design"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:54+09:00"
---

# Efficient Preference-Based Reinforcement Learning: Randomized Exploration meets Experimental Design

## Abstract
We study reinforcement learning from human feedback in general Markov decision processes, where agents learn from trajectory-level preference comparisons. A central challenge in this setting is to design algorithms that select informative preference queries to identify the underlying reward while ensuring theoretical guarantees. We propose a meta-algorithm based on randomized exploration, which avoids the computational challenges associated with optimistic approaches and remains tractable. We establish both regret and last-iterate guarantees under mild reinforcement learning oracle assumptions. To improve query complexity, we introduce and analyze an improved algorithm that collects batches of trajectory pairs and applies optimal experimental design to select informative comparison queries. The batch structure also enables parallelization of preference queries, which is relevant in practical deployment as feedback can be gathered concurrently. Empirical evaluation confirms that the proposed method is competitive with reward-based reinforcement learning while requiring a small number of preference queries.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Andreas Schlaginhaufen, Reda Ouhamma, Maryam Kamgarpour
- arxiv_id: 
- openreview_id: qEfgajdKea
- anthology_id: 
- pdf_url: https://openreview.net/pdf/741b01ab9338378b6a7ee3a884ceebe29405b5c3.pdf
- published: 2025
- keywords: RLHF, Preference learning, RL, Optimal design

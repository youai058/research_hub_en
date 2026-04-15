---
title: "Can I Have Your Order? Monte-Carlo Tree Search for Slot Filling Ordering in Diffusion Language Models"
authors: ["Joshua Ong Jun Leang", "Yu Zhao", "Mihaela Cătălina Stoian", "Wenda Li", "Shay B. Cohen", "Eleonora Giunchiglia"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.12586"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.12586v1"
published: "2026-02-13"
categories: ["cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:13+09:00"
---

# Can I Have Your Order? Monte-Carlo Tree Search for Slot Filling Ordering in Diffusion Language Models

## Abstract
While plan-and-infill decoding in Masked Diffusion Models (MDMs) shows promise for mathematical and code reasoning, performance remains highly sensitive to slot infilling order, often yielding substantial output variance. We introduce McDiffuSE, a framework that formulates slot selection as decision making and optimises infilling orders through Monte Carlo Tree Search (MCTS). McDiffuSE uses look-ahead simulations to evaluate partial completions before commitment, systematically exploring the combinatorial space of generation orders. Experiments show an average improvement of 3.2% over autoregressive baselines and 8.0% over baseline plan-and-infill, with notable gains of 19.5% on MBPP and 4.9% on MATH500. Our analysis reveals that while McDiffuSE predominantly follows sequential ordering, incorporating non-sequential generation is essential for maximising performance. We observe that larger exploration constants, rather than increased simulations, are necessary to overcome model confidence biases and discover effective orderings. These findings establish MCTS-based planning as an effective approach for enhancing generation quality in MDMs.

## Metadata
- venue: arXiv
- year: 2026
- authors: Joshua Ong Jun Leang, Yu Zhao, Mihaela Cătălina Stoian, Wenda Li, Shay B. Cohen, Eleonora Giunchiglia
- arxiv_id: 2602.12586
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.12586v1
- published: 2026-02-13

---
title: "Layerwise Proximal Replay: A Proximal Point Method for Online Continual Learning"
authors: ["Jinsoo Yoo", "Yunpeng Liu", "Frank Wood", "Geoff Pleiss"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Lg8nw3ltvX"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/1080532fb7bb0a3e2372d54362391fc8ae97ec00.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:42+09:00"
---

# Layerwise Proximal Replay: A Proximal Point Method for Online Continual Learning

## Abstract
In online continual learning, a neural network incrementally learns from a non-i.i.d. data stream. Nearly all online continual learning methods employ experience replay to simultaneously prevent catastrophic forgetting and underfitting on past data. Our work demonstrates a limitation of this approach: neural networks trained with experience replay tend to have unstable optimization trajectories, impeding their overall accuracy. Surprisingly, these instabilities persist even when the replay buffer stores all previous training examples, suggesting that this issue is orthogonal to catastrophic forgetting. We minimize these instabilities through a simple modification of the optimization geometry. Our solution, Layerwise Proximal Replay (LPR), balances learning from new and replay data while only allowing for gradual changes in the hidden activation of past data. We demonstrate that LPR consistently improves replay-based online continual learning across multiple problem settings, regardless of the amount of available replay memory.

## Metadata
- venue: ICML
- year: 2024
- authors: Jinsoo Yoo, Yunpeng Liu, Frank Wood, Geoff Pleiss
- arxiv_id: 
- openreview_id: Lg8nw3ltvX
- anthology_id: 
- pdf_url: https://openreview.net/pdf/1080532fb7bb0a3e2372d54362391fc8ae97ec00.pdf
- published: 2024

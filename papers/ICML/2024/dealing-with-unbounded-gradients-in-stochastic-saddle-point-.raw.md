---
title: "Dealing With Unbounded Gradients in Stochastic Saddle-point Optimization"
authors: ["Gergely Neu", "Nneka Okolo"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "RPMTNGMq0O"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/89c85399f4e4e6fce278b636fdcac5873471f16f.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:47+09:00"
---

# Dealing With Unbounded Gradients in Stochastic Saddle-point Optimization

## Abstract
We study the performance of stochastic first-order methods for finding saddle points of convex-concave functions. A notorious challenge faced by such methods is that the gradients can grow arbitrarily large during optimization, which may result in instability and divergence. In this paper, we propose a simple and effective regularization technique that stabilizes the iterates and yields meaningful performance guarantees even if the domain and the gradient noise scales linearly with the size of the iterates (and is thus potentially unbounded). Besides providing a set of general results, we also apply our algorithm to a specific problem in reinforcement learning, where it leads to performance guarantees for finding near-optimal policies in an average-reward MDP without prior knowledge of the bias span.

## Metadata
- venue: ICML
- year: 2024
- authors: Gergely Neu, Nneka Okolo
- arxiv_id: 
- openreview_id: RPMTNGMq0O
- anthology_id: 
- pdf_url: https://openreview.net/pdf/89c85399f4e4e6fce278b636fdcac5873471f16f.pdf
- published: 2024

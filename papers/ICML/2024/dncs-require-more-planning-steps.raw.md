---
title: "DNCs Require More Planning Steps"
authors: ["Yara Shamshoum", "Nitzan Hodos", "Yuval Sieradzki", "Assaf Schuster"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "tu5fCCuua2"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/3dc48dd4d3b7c8fd2e2767e60fc6026970806b48.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:28+09:00"
---

# DNCs Require More Planning Steps

## Abstract
Many recent works use machine learning models to solve various complex algorithmic problems. However, these models attempt to reach a solution without considering the problem's required computational complexity, which can be detrimental to their ability to solve it correctly. In this work we investigate the effect of computational time and memory on generalization of implicit algorithmic solvers. To do so, we focus on the Differentiable Neural Computer (DNC), a general problem solver that also lets us reason directly about its usage of time and memory. In this work, we argue that the number of planning steps the model is allowed to take, which we call ”planning budget”, is a constraint that can cause the model to generalize poorly and hurt its ability to fully utilize its external memory. We evaluate our method on Graph Shortest Path, Convex Hull, Graph MinCut and Associative Recall, and show how the planning budget can drastically change the behavior of the learned algorithm, in terms of learned time complexity, training time, stability and generalization to inputs larger than those seen during training.

## Metadata
- venue: ICML
- year: 2024
- authors: Yara Shamshoum, Nitzan Hodos, Yuval Sieradzki, Assaf Schuster
- arxiv_id: 
- openreview_id: tu5fCCuua2
- anthology_id: 
- pdf_url: https://openreview.net/pdf/3dc48dd4d3b7c8fd2e2767e60fc6026970806b48.pdf
- published: 2024

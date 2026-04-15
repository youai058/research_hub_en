---
title: "Recurrent Distance Filtering for Graph Representation Learning"
authors: ["Yuhui Ding", "Antonio Orvieto", "Bobby He", "Thomas Hofmann"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "5kGfm3Pa41"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ca861d3641e4b415bb49139b50ab50d6ecc32309.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:33+09:00"
---

# Recurrent Distance Filtering for Graph Representation Learning

## Abstract
Graph neural networks based on iterative one-hop message passing have been shown to struggle in harnessing the information from distant nodes effectively. Conversely, graph transformers allow each node to attend to all other nodes directly, but lack graph inductive bias and have to rely on ad-hoc positional encoding. In this paper, we propose a new architecture to reconcile these challenges. Our approach stems from the recent breakthroughs in long-range modeling provided by deep state-space models: for a given target node, our model aggregates other nodes by their shortest distances to the target and uses a linear RNN to encode the sequence of hop representations. The linear RNN is parameterized in a particular diagonal form for stable long-range signal propagation and is theoretically expressive enough to encode the neighborhood hierarchy. With no need for positional encoding, we empirically show that the performance of our model is comparable to or better than that of state-of-the-art graph transformers on various benchmarks, with a significantly reduced computational cost. Our code is open-source at https://github.com/skeletondyh/GRED.

## Metadata
- venue: ICML
- year: 2024
- authors: Yuhui Ding, Antonio Orvieto, Bobby He, Thomas Hofmann
- arxiv_id: 
- openreview_id: 5kGfm3Pa41
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ca861d3641e4b415bb49139b50ab50d6ecc32309.pdf
- published: 2024

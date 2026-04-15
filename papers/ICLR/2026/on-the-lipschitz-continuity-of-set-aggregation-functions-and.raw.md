---
title: "On the Lipschitz Continuity of Set Aggregation Functions and Neural Networks for Sets"
authors: ["Giannis Nikolentzos", "Konstantinos Skianis"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "sPRK6XefjY"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/bd6f6eb8c76221846ccd1d3ef09bf90c9a2586bc.pdf"
published: "2026"
categories: []
keywords: ["set aggregation functions", "Lipschitz continuity", "stability"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:28+09:00"
---

# On the Lipschitz Continuity of Set Aggregation Functions and Neural Networks for Sets

## Abstract
The Lipschitz constant of a neural network is connected to several important properties of the network such as its robustness and generalization. It is thus useful in many settings to estimate the Lipschitz constant of a model. Prior work has focused mainly on estimating the Lipschitz constant of multi-layer perceptrons and convolutional neural networks. Here we focus on data modeled as sets or multisets of vectors and on neural networks that can handle such data. These models typically apply some permutation invariant aggregation function, such as the sum, mean or max operator, to the input multisets to produce a single vector for each input sample. In this paper, we investigate whether these aggregation functions, along with an attention-based aggregation function, are Lipschitz continuous with respect to three distance functions for unordered multisets, and we compute their Lipschitz constants. In the general case, we find that each aggregation function is Lipschitz continuous with respect to only one of the three distance functions, while the attention-based function is not Lipschitz continuous with respect to any of them. Then, we build on these results to derive upper bounds on the Lipschitz constant of neural networks that can process multisets of vectors, while we also study their stability to perturbations and generalization under distribution shifts. To empirically verify our theoretical analysis, we conduct a series of experiments on datasets from different domains.

## Metadata
- venue: ICLR
- year: 2026
- authors: Giannis Nikolentzos, Konstantinos Skianis
- arxiv_id: 
- openreview_id: sPRK6XefjY
- anthology_id: 
- pdf_url: https://openreview.net/pdf/bd6f6eb8c76221846ccd1d3ef09bf90c9a2586bc.pdf
- published: 2026
- keywords: set aggregation functions, Lipschitz continuity, stability

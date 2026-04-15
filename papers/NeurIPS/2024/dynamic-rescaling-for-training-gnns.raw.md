---
title: "Dynamic Rescaling for Training GNNs"
authors: ["Nimrah Mustafa", "Rebekka Burkholz"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "IfZwSRpqHl"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/488104c772d4f1415d513de9258af76ef4ee3425.pdf"
published: "2024"
categories: []
keywords: ["graph neural network", "rescale invariance", "generalization", "network balance"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:43+09:00"
---

# Dynamic Rescaling for Training GNNs

## Abstract
Graph neural networks (GNNs) with a rescale invariance, such as GATs, can be re-parameterized during optimization through dynamic rescaling of network parameters and gradients while keeping the loss invariant. In this work, we explore dynamic rescaling as a tool to influence GNN training dynamics in two key ways: i) balancing the network with respect to various criteria, and ii) controlling the relative learning speeds of different layers. We gain novel insights, unique to GNNs, that reveal distinct training modes for different tasks. For heterophilic graphs, achieving balance based on relative gradients leads to faster training and better generalization. In contrast, homophilic graphs benefit from delaying the learning of later layers. Additionally, we show that training in balance supports larger learning rates, which can improve generalization. Moreover, controlling layer-wise training speeds is linked to grokking-like phenomena, which may be of independent interest.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Nimrah Mustafa, Rebekka Burkholz
- arxiv_id: 
- openreview_id: IfZwSRpqHl
- anthology_id: 
- pdf_url: https://openreview.net/pdf/488104c772d4f1415d513de9258af76ef4ee3425.pdf
- published: 2024
- keywords: graph neural network, rescale invariance, generalization, network balance

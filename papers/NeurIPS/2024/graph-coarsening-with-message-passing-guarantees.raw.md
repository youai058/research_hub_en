---
title: "Graph Coarsening with Message-Passing Guarantees"
authors: ["Antonin Joly", "Nicolas Keriven"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "rIOTceoNc8"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/18c2962b68647987ac2041fa833e47449b2d7b51.pdf"
published: "2024"
categories: []
keywords: ["graph coarsening", "message passing", "graph neural network"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:53+09:00"
---

# Graph Coarsening with Message-Passing Guarantees

## Abstract
Graph coarsening aims to reduce the size of a large graph while preserving some of its key properties, which has been used in many applications to reduce computational load and memory footprint. For instance, in graph machine learning, training Graph Neural Networks (GNNs) on coarsened graphs leads to drastic savings in time and memory. However, GNNs rely on the Message-Passing (MP) paradigm, and classical spectral preservation guarantees for graph coarsening do not directly lead to theoretical guarantees when performing naive message-passing on the coarsened graph.

In this work, we propose a new message-passing operation specific to coarsened graphs, which exhibit theoretical guarantees on the preservation of the propagated signal. Interestingly, and in a sharp departure from previous proposals, this operation on coarsened graphs is oriented, even when the original graph is undirected. We conduct node classification tasks on synthetic and real data and observe improved results compared to performing naive message-passing on the coarsened graph.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Antonin Joly, Nicolas Keriven
- arxiv_id: 
- openreview_id: rIOTceoNc8
- anthology_id: 
- pdf_url: https://openreview.net/pdf/18c2962b68647987ac2041fa833e47449b2d7b51.pdf
- published: 2024
- keywords: graph coarsening, message passing, graph neural network

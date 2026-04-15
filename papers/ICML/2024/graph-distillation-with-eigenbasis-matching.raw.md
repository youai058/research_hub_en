---
title: "Graph Distillation with Eigenbasis Matching"
authors: ["Yang Liu", "Deyu Bo", "Chuan Shi"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "DYN66IJCI9"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/317826b87750d6350c6761ef82758f92a2942fad.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:29+09:00"
---

# Graph Distillation with Eigenbasis Matching

## Abstract
The increasing amount of graph data places requirements on the efficient training of graph neural networks (GNNs). The emerging graph distillation (GD) tackles this challenge by distilling a small synthetic graph to replace the real large graph, ensuring GNNs trained on real and synthetic graphs exhibit comparable performance. However, existing methods rely on GNN-related information as supervision, including gradients, representations, and trajectories, which have two limitations. First, GNNs can affect the spectrum (*i.e*., eigenvalues) of the real graph, causing *spectrum bias* in the synthetic graph. Second, the variety of GNN architectures leads to the creation of different synthetic graphs, requiring *traversal* to obtain optimal performance. To tackle these issues, we propose Graph Distillation with Eigenbasis Matching (GDEM), which aligns the eigenbasis and node features of real and synthetic graphs. Meanwhile, it directly replicates the spectrum of the real graph and thus prevents the influence of GNNs. Moreover, we design a discrimination constraint to balance the effectiveness and generalization of GDEM. Theoretically, the synthetic graphs distilled by GDEM are restricted spectral approximations of the real graphs. Extensive experiments demonstrate that GDEM outperforms state-of-the-art GD methods with powerful cross-architecture generalization ability and significant distillation efficiency. Our code is available at https://github.com/liuyang-tian/GDEM.

## Metadata
- venue: ICML
- year: 2024
- authors: Yang Liu, Deyu Bo, Chuan Shi
- arxiv_id: 
- openreview_id: DYN66IJCI9
- anthology_id: 
- pdf_url: https://openreview.net/pdf/317826b87750d6350c6761ef82758f92a2942fad.pdf
- published: 2024

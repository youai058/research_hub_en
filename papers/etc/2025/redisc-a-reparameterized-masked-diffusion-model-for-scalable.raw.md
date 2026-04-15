---
title: "ReDiSC: A Reparameterized Masked Diffusion Model for Scalable Node Classification with Structured Predictions"
authors: ["Yule Li", "Yifeng Lu", "Zhen Wang", "Zhewei Wei", "Yaliang Li", "Bolin Ding"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2507.14484"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2507.14484v1"
published: "2025-07-19"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:29+09:00"
---

# ReDiSC: A Reparameterized Masked Diffusion Model for Scalable Node Classification with Structured Predictions

## Abstract
In recent years, graph neural networks (GNN) have achieved unprecedented successes in node classification tasks. Although GNNs inherently encode specific inductive biases (e.g., acting as low-pass or high-pass filters), most existing methods implicitly assume conditional independence among node labels in their optimization objectives. While this assumption is suitable for traditional classification tasks such as image recognition, it contradicts the intuitive observation that node labels in graphs remain correlated, even after conditioning on the graph structure. To make structured predictions for node labels, we propose ReDiSC, namely, Reparameterized masked Diffusion model for Structured node Classification. ReDiSC estimates the joint distribution of node labels using a reparameterized masked diffusion model, which is learned through the variational expectation-maximization (EM) framework. Our theoretical analysis shows the efficiency advantage of ReDiSC in the E-step compared to DPM-SNC, a state-of-the-art model that relies on a manifold-constrained diffusion model in continuous domain. Meanwhile, we explicitly link ReDiSC's M-step objective to popular GNN and label propagation hybrid approaches. Extensive experiments demonstrate that ReDiSC achieves superior or highly competitive performance compared to state-of-the-art GNN, label propagation, and diffusion-based baselines across both homophilic and heterophilic graphs of varying sizes. Notably, ReDiSC scales effectively to large-scale datasets on which previous structured diffusion methods fail due to computational constraints, highlighting its significant practical advantage in structured node classification tasks.

## Metadata
- venue: arXiv
- year: 2025
- authors: Yule Li, Yifeng Lu, Zhen Wang, Zhewei Wei, Yaliang Li, Bolin Ding
- arxiv_id: 2507.14484
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2507.14484v1
- published: 2025-07-19

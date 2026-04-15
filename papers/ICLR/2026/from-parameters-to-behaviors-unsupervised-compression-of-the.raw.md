---
title: "From Parameters to Behaviors: Unsupervised Compression of the Policy Space"
authors: ["Davide Tenedini", "Riccardo Zamboni", "Mirco Mutti", "Marcello Restelli"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "VqnBaeu43F"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2d1ce939e6e48a9081ed66ccdf77676416b951b1.pdf"
published: "2026"
categories: []
keywords: ["reinforcement learning", "unsupervised reinforcement learning", "unsupervised representation learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:24+09:00"
---

# From Parameters to Behaviors: Unsupervised Compression of the Policy Space

## Abstract
Despite its recent successes, Deep Reinforcement Learning (DRL) is notoriously sample-inefficient. We argue that this inefficiency stems from the standard practice of optimizing policies directly in the high-dimensional and highly redundant parameter space $\\Theta$. This challenge is greatly compounded in multi-task settings. In this work, we develop a novel, unsupervised approach that compresses the policy parameter space $\\Theta$ into a low-dimensional latent space $\\mathcal Z$. We train a generative model $g:\\mathcal Z\\to\\Theta$ by optimizing a behavioral reconstruction loss, which ensures that the latent space is organized by functional similarity rather than proximity in parameterization. We conjecture that the inherent dimensionality of this manifold is a function of the environment's complexity, rather than the size of the policy network. We validate our approach in continuous control domains, showing that the parameterization of standard policy networks can be compressed up to five orders of magnitude while retaining most of its expressivity. As a byproduct, we show that the learned manifold enables task-specific adaptation via Policy Gradient operating in the latent space $\\mathcal{Z}$.

## Metadata
- venue: ICLR
- year: 2026
- authors: Davide Tenedini, Riccardo Zamboni, Mirco Mutti, Marcello Restelli
- arxiv_id: 
- openreview_id: VqnBaeu43F
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2d1ce939e6e48a9081ed66ccdf77676416b951b1.pdf
- published: 2026
- keywords: reinforcement learning, unsupervised reinforcement learning, unsupervised representation learning

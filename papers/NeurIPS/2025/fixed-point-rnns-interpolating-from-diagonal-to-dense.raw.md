---
title: "Fixed-Point RNNs: Interpolating from Diagonal to Dense"
authors: ["Sajad Movahedi", "Felix Sarnthein", "Nicola Muca Cirone", "Antonio Orvieto"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "KT8y9pFgJE"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e76140ca8a27d51bcb73d98746f2e5ec88965a0d.pdf"
published: "2025"
categories: []
keywords: ["Deep Learning", "Sequence Architecture", "Recurrent Neural Network", "State Space Model", "Linear RNN", "SSM", "Mamba", "Linear Attention", "RWKV", "DeltaNet", "DeltaProduct", "Looped Architecture", "Recurrent Depth", "Equilibrium Model", "DEQ", "Implicit Neural Network", "Implicit Model", "Neural ODE", "Adaptive Computation Time", "ACT", "Test-Time Computation", "Test-Time Compute", "Reasoning", "State-Tracking", "A5", "S5", "Copying", "CatbAbi"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:51+09:00"
---

# Fixed-Point RNNs: Interpolating from Diagonal to Dense

## Abstract
Linear recurrent neural networks (RNNs) and state-space models (SSMs) such as Mamba have become promising alternatives to softmax-attention as sequence mixing layers in Transformer architectures. Current models, however, do not exhibit the full state-tracking expressivity of RNNs because they rely on channel-wise (i.e. diagonal) sequence mixing. 
In this paper, we investigate parameterizations of a large class of dense linear RNNs as fixed-points of parallelizable diagonal linear RNNs.
The resulting models can naturally trade expressivity for efficiency at a fixed number of parameters
and achieve state-of-the-art results on the state-tracking benchmarks $A_5$ and $S_5$, while matching performance on copying and other tasks.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Sajad Movahedi, Felix Sarnthein, Nicola Muca Cirone, Antonio Orvieto
- arxiv_id: 
- openreview_id: KT8y9pFgJE
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e76140ca8a27d51bcb73d98746f2e5ec88965a0d.pdf
- published: 2025
- keywords: Deep Learning, Sequence Architecture, Recurrent Neural Network, State Space Model, Linear RNN, SSM, Mamba, Linear Attention, RWKV, DeltaNet, DeltaProduct, Looped Architecture, Recurrent Depth, Equilibrium Model, DEQ, Implicit Neural Network, Implicit Model, Neural ODE, Adaptive Computation Time, ACT, Test-Time Computation, Test-Time Compute, Reasoning, State-Tracking, A5, S5, Copying, CatbAbi

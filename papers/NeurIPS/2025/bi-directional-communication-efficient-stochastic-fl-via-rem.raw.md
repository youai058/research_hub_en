---
title: "Bi-Directional Communication-Efficient Stochastic FL via Remote Source Generation"
authors: ["Maximilian Egger", "Rawad Bitar", "Antonia Wachter-Zeh", "Nir Weinberger", "Deniz Gunduz"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "KL9yKasAcZ"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/0140c3c227f733a5b7c86f9399fe1ce3149d96b1.pdf"
published: "2025"
categories: []
keywords: ["Communication-efficiency", "Importance sampling", "Minimal Random Coding", "Stochastic federated learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:56+09:00"
---

# Bi-Directional Communication-Efficient Stochastic FL via Remote Source Generation

## Abstract
Federated Learning (FL) incurs high communication costs in both uplink and downlink. The literature largely focuses on lossy compression of model updates in deterministic FL. In contrast, stochastic (Bayesian) FL considers distributions over parameters, enabling uncertainty quantification, better generalization, and, crucially, inherent communication-regularized training through a mirror-descent structure. 
In this paper, we consider both uplink and downlink communication in stochastic FL, and propose a communication framework based on remote source generation. Employing Minimal Random Coding (MRC) for remote generation, we allow the server and the clients to sample from local and global posteriors (sources), respectively, rather than transmitting locally sampled updates. The framework encompasses communication-regularized local optimization and principled compression of model updates, leveraging gradually updated prior distributions as side information. 
Through extensive simulations, we show that our method achieves $5-32\times$ reduction in total communication cost while preserving accuracy. We further analyze the communication cost, refining existing MRC bounds and enabling precise quantification of uplink and downlink trade-offs. We also extend our method to conventional FL via stochastic quantization and prove a contraction property for the biased MRC compressor to facilitate convergence analysis.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Maximilian Egger, Rawad Bitar, Antonia Wachter-Zeh, Nir Weinberger, Deniz Gunduz
- arxiv_id: 
- openreview_id: KL9yKasAcZ
- anthology_id: 
- pdf_url: https://openreview.net/pdf/0140c3c227f733a5b7c86f9399fe1ce3149d96b1.pdf
- published: 2025
- keywords: Communication-efficiency, Importance sampling, Minimal Random Coding, Stochastic federated learning

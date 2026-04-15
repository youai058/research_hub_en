---
title: "COGNATE: Acceleration of Sparse Tensor Programs on Emerging Hardware using Transfer Learning"
authors: ["Chamika Sudusinghe", "Gerasimos Gerogiannis", "Damitha Lenadora", "Charles Block", "Josep Torrellas", "Charith Mendis"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "EV0itGFjmm"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/5c5ead800da90764a17b89b71a660f259cd77cb4.pdf"
published: "2025"
categories: []
keywords: ["machine learning for systems", "transfer learning", "hardware accelerators", "learned cost models", "sparse tensor programs"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:34+09:00"
---

# COGNATE: Acceleration of Sparse Tensor Programs on Emerging Hardware using Transfer Learning

## Abstract
Sparse tensor programs are essential in deep learning and graph analytics, driving the need for optimized processing. To meet this demand, specialized hardware accelerators are being developed. Optimizing these programs for accelerators is challenging for two reasons: program performance is highly sensitive to variations in sparse inputs, and early-stage accelerators rely on expensive simulators. Therefore, ML-based cost models used for optimizing such programs on general-purpose hardware are often ineffective for early-stage accelerators, as they require large datasets for proper training. To this end, we introduce COGNATE, a novel framework that leverages inexpensive data samples from general-purpose hardware (e.g., CPUs) to train cost models, followed by few-shot fine-tuning on emerging hardware. COGNATE exploits the homogeneity of input features across hardware platforms while effectively mitigating heterogeneity, enabling cost model training with just 5% of the data samples needed by accelerator-specific models to achieve comparable performance. We conduct extensive experiments to demonstrate that COGNATE outperforms existing techniques, achieving average speedups of 1.47× (up to 5.46×) for SpMM and 1.39× (up to 4.22×) for SDDMM.

## Metadata
- venue: ICML
- year: 2025
- authors: Chamika Sudusinghe, Gerasimos Gerogiannis, Damitha Lenadora, Charles Block, Josep Torrellas, Charith Mendis
- arxiv_id: 
- openreview_id: EV0itGFjmm
- anthology_id: 
- pdf_url: https://openreview.net/pdf/5c5ead800da90764a17b89b71a660f259cd77cb4.pdf
- published: 2025
- keywords: machine learning for systems, transfer learning, hardware accelerators, learned cost models, sparse tensor programs

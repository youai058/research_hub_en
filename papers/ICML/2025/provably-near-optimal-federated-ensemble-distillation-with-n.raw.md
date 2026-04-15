---
title: "Provably Near-Optimal Federated Ensemble Distillation with Negligible Overhead"
authors: ["Won-Jun Jang", "Hyeon-Seo Park", "Si-Hyeon Lee"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "6znPjYn11w"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f90034103cd5f0a035090571a9a19852ee23a8d5.pdf"
published: "2025"
categories: []
keywords: ["Federated learning", "ensemble distillation", "data heterogeneity", "generative adversarial network"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:24+09:00"
---

# Provably Near-Optimal Federated Ensemble Distillation with Negligible Overhead

## Abstract
Federated ensemble distillation addresses client heterogeneity by generating pseudo-labels for an unlabeled server dataset based on client predictions and training the server model using the pseudo-labeled dataset. The unlabeled server dataset can either be pre-existing or generated through a data-free approach. The effectiveness of this approach critically depends on the method of assigning weights to client predictions when creating pseudo-labels, especially in highly heterogeneous settings. Inspired by theoretical results from GANs, we propose a provably near-optimal weighting method that leverages client discriminators trained with a server-distributed generator and local datasets. Our experiments on various image classification tasks demonstrate that the proposed method significantly outperforms baselines.  Furthermore, we show that the additional communication cost, client-side privacy leakage, and client-side computational overhead introduced by our method are negligible, both in scenarios with and without a pre-existing server dataset.

## Metadata
- venue: ICML
- year: 2025
- authors: Won-Jun Jang, Hyeon-Seo Park, Si-Hyeon Lee
- arxiv_id: 
- openreview_id: 6znPjYn11w
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f90034103cd5f0a035090571a9a19852ee23a8d5.pdf
- published: 2025
- keywords: Federated learning, ensemble distillation, data heterogeneity, generative adversarial network

---
title: "PDEfuncta: Spectrally-Aware Neural Representation for PDE Solution Modeling"
authors: ["Minju Jo", "Woojin Cho", "Uvini Balasuriya Mudiyanselage", "Seungjun Lee", "Noseong Park", "Kookjin Lee"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "NfBrMDF0Xi"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/5d62e42c555992383ebb5e6582544b9d046566a6.pdf"
published: "2025"
categories: []
keywords: ["SciML", "meta-learning", "data compression"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:39+09:00"
---

# PDEfuncta: Spectrally-Aware Neural Representation for PDE Solution Modeling

## Abstract
Scientific machine learning often involves representing complex solution fields that exhibit high-frequency features such as sharp transitions, fine-scale oscillations, and localized structures. While implicit neural representations (INRs) have shown promise for continuous function modeling, capturing such high-frequency behavior remains a challenge—especially when modeling multiple solution fields with a shared network. Prior work addressing spectral bias in INRs has primarily focused on single-instance settings, limiting scalability and generalization. In this work, we propose Global Fourier Modulation (GFM), a novel modulation technique that injects high-frequency information at each layer of the INR through Fourier-based reparameterization. This enables compact and accurate representation of multiple solution fields using low-dimensional latent vectors. Building upon GFM, we introduce PDEfuncta, a meta-learning framework designed to learn multi-modal solution fields and support generalization to new tasks. Through empirical studies on diverse scientific problems, we demonstrate that our method not only improves representational quality but also shows potential for forward and inverse inference tasks without the need for retraining.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Minju Jo, Woojin Cho, Uvini Balasuriya Mudiyanselage, Seungjun Lee, Noseong Park, Kookjin Lee
- arxiv_id: 
- openreview_id: NfBrMDF0Xi
- anthology_id: 
- pdf_url: https://openreview.net/pdf/5d62e42c555992383ebb5e6582544b9d046566a6.pdf
- published: 2025
- keywords: SciML, meta-learning, data compression

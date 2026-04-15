---
title: "Normalization Layer Per-Example Gradients are Sufficient to Predict Gradient Noise Scale in Transformers"
authors: ["Gavia Gray", "Aman Tiwari", "Shane Bergsma", "Joel Hestness"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "S7THlpvH8i"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/79e5936b7e0de175d888d3daf5d92fb33ab065d0.pdf"
published: "2024"
categories: []
keywords: ["Efficient deep learning", "gradient noise scale", "critical batch size", "language models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:35+09:00"
---

# Normalization Layer Per-Example Gradients are Sufficient to Predict Gradient Noise Scale in Transformers

## Abstract
Per-example gradient norms are a vital ingredient for estimating gradient noise scale (GNS) with minimal variance. Observing the tensor contractions required to compute them, we propose a method with minimal FLOPs in 3D or greater tensor regimes by simultaneously computing the norms while computing the parameter gradients. Using this method we are able to observe the GNS of different layers at higher accuracy than previously possible. We find that the total GNS of contemporary transformer models is predicted well by the GNS of only the normalization layers. As a result, focusing only on the normalization layer, we develop a custom kernel to compute the per-example gradient norms while performing the LayerNorm backward pass with zero throughput overhead. Tracking GNS on only those layers, we are able to guide a practical batch size schedule that reduces training time by 18% on a Chinchilla-optimal language model.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Gavia Gray, Aman Tiwari, Shane Bergsma, Joel Hestness
- arxiv_id: 
- openreview_id: S7THlpvH8i
- anthology_id: 
- pdf_url: https://openreview.net/pdf/79e5936b7e0de175d888d3daf5d92fb33ab065d0.pdf
- published: 2024
- keywords: Efficient deep learning, gradient noise scale, critical batch size, language models

---
title: "Compositional Generalization via Forced Rendering of Disentangled Latents"
authors: ["Qiyao Liang", "Daoyuan Qian", "Liu Ziyin", "Ila R Fiete"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "rkHCHI5H5W"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d94a41221acd289b56e4f17f3a3a6390c9c0cee9.pdf"
published: "2025"
categories: []
keywords: ["Factorization", "Compositionality", "Compositional Generalization", "Data Efficiency"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:06+09:00"
---

# Compositional Generalization via Forced Rendering of Disentangled Latents

## Abstract
Composition—the ability to generate myriad variations from finite means—is believed to underlie powerful generalization. However, compositional generalization remains a key challenge for deep learning. A widely held assumption is that learning disentangled (factorized) representations naturally supports this kind of extrapolation. Yet, empirical results are mixed, with many generative models failing to recognize and compose factors to generate out-of-distribution (OOD) samples. In this work, we investigate a controlled 2D Gaussian "bump" generation task with fully disentangled $(x,y)$ inputs, demonstrating that standard generative architectures still fail in OOD regions when training with partial data, by re-entangling latent representations  in subsequent layers. By examining the model's learned kernels and manifold geometry, we show that this failure reflects a "memorization" strategy for generation via data superposition rather than via composition of the true factorized features. We show that when models are forced—through architectural modifications with regularization or curated training data—to render the disentangled latents into the full-dimensional representational (pixel) space, they can be highly data-efficient and effective at composing in OOD regions. These findings underscore that disentangled latents in an abstract representation are insufficient and show that if models can represent disentangled factors directly in the output representational space, it can achieve robust compositional generalization.

## Metadata
- venue: ICML
- year: 2025
- authors: Qiyao Liang, Daoyuan Qian, Liu Ziyin, Ila R Fiete
- arxiv_id: 
- openreview_id: rkHCHI5H5W
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d94a41221acd289b56e4f17f3a3a6390c9c0cee9.pdf
- published: 2025
- keywords: Factorization, Compositionality, Compositional Generalization, Data Efficiency

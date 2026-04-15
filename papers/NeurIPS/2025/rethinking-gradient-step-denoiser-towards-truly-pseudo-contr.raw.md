---
title: "Rethinking Gradient Step Denoiser: Towards Truly Pseudo-Contractive Operator"
authors: ["Shuchang Zhang", "Yaoyun Zeng", "Kangkang Deng", "Hongxia Wang"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "J5XXBS6wPz"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/568017104bdf3b860f572fee1e2caf609b4408c4.pdf"
published: "2025"
categories: []
keywords: ["Plug-and-Play prior", "Regularization by Denoising", "Pseudo-contractive denoiser", "Image restoration"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:57+09:00"
---

# Rethinking Gradient Step Denoiser: Towards Truly Pseudo-Contractive Operator

## Abstract
Learning pseudo-contractive denoisers is a fundamental challenge in the theoretical analysis of Plug-and-Play (PnP) methods and the Regularization by Denoising  (RED) framework. While spectral methods attempt to address this challenge using the power iteration method, they fail to guarantee the truly pseudo-contractive property and suffer from high computational complexity. In this work, we rethink
gradient step (GS) denoisers and establish a theoretical connection between GS denoisers and pseudo-contractive operators. We show that GS denoisers, with the gradients of convex potential functions parameterized by input convex neural networks (ICNNs), can achieve truly pseudo-contractive properties. Furthermore, we integrate the learned truly pseudo-contractive denoiser into the RED-PRO (RED
via fixed-point projection) model, definitely ensuring convergence in terms of both iterative sequences and objective functions. Extensive numerical experiments confirm that the learned GS denoiser satisfies the truly pseudo-contractive property and, when integrated into RED-PRO, provides a favorable trade-off between interpretability and empirical performance on inverse problems.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Shuchang Zhang, Yaoyun Zeng, Kangkang Deng, Hongxia Wang
- arxiv_id: 
- openreview_id: J5XXBS6wPz
- anthology_id: 
- pdf_url: https://openreview.net/pdf/568017104bdf3b860f572fee1e2caf609b4408c4.pdf
- published: 2025
- keywords: Plug-and-Play prior, Regularization by Denoising, Pseudo-contractive denoiser, Image restoration

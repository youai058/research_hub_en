---
title: "Hybrid Latent Representations for PDE Emulation"
authors: ["Ali Can Bekar", "Siddhant Agarwal", "Christian Hüttig", "Nicola Tosi", "David S. Greenberg"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Hh8ebJYQs3"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c30c0fbbf8472d48ae5287d525afe6c6c578654d.pdf"
published: "2025"
categories: []
keywords: ["PDE Integration", "Physics Informed Learning", "Neural PDE Solvers"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:35+09:00"
---

# Hybrid Latent Representations for PDE Emulation

## Abstract
For classical PDE solvers, adjusting the spatial resolution and time step offers a trade-off between speed and accuracy. Neural emulators often achieve better speed-accuracy trade-offs by operating on a compact representation of the PDE system. Coarsened PDE fields are a simple and effective representation, but cannot exploit fine spatial scales in the high-fidelity numerical solutions. Alternatively, unstructured latent representations provide efficient autoregressive rollouts, but cannot enforce local interactions or physical laws as inductive biases. To overcome these limitations, we introduce hybrid representations that augment coarsened PDE fields with spatially structured latent variables extracted from high-resolution inputs. Hybrid representations provide efficient rollouts, can be trained on a simple loss defined on coarsened PDE fields, and support hard physical constraints. When predicting fine- and coarse-scale features across multiple PDE emulation tasks, they outperform or match the speed-accuracy trade-offs of the best convolutional, attentional, Fourier operator-based and autoencoding baselines.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Ali Can Bekar, Siddhant Agarwal, Christian Hüttig, Nicola Tosi, David S. Greenberg
- arxiv_id: 
- openreview_id: Hh8ebJYQs3
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c30c0fbbf8472d48ae5287d525afe6c6c578654d.pdf
- published: 2025
- keywords: PDE Integration, Physics Informed Learning, Neural PDE Solvers

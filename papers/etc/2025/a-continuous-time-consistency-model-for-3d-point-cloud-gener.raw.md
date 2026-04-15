---
title: "A Continuous-Time Consistency Model for 3D Point Cloud Generation"
authors: ["Sebastian Eilermann", "René Heesch", "Oliver Niggemann"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2509.01492"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2509.01492v1"
published: "2025-09-01"
categories: ["cs.CV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:44+09:00"
---

# A Continuous-Time Consistency Model for 3D Point Cloud Generation

## Abstract
Fast and accurate 3D shape generation from point clouds is essential for applications in robotics, AR/VR, and digital content creation. We introduce ConTiCoM-3D, a continuous-time consistency model that synthesizes 3D shapes directly in point space, without discretized diffusion steps, pre-trained teacher models, or latent-space encodings. The method integrates a TrigFlow-inspired continuous noise schedule with a Chamfer Distance-based geometric loss, enabling stable training on high-dimensional point sets while avoiding expensive Jacobian-vector products. This design supports efficient one- to two-step inference with high geometric fidelity. In contrast to previous approaches that rely on iterative denoising or latent decoders, ConTiCoM-3D employs a time-conditioned neural network operating entirely in continuous time, thereby achieving fast generation. Experiments on the ShapeNet benchmark show that ConTiCoM-3D matches or outperforms state-of-the-art diffusion and latent consistency models in both quality and efficiency, establishing it as a practical framework for scalable 3D shape generation.

## Metadata
- venue: arXiv
- year: 2025
- authors: Sebastian Eilermann, René Heesch, Oliver Niggemann
- arxiv_id: 2509.01492
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2509.01492v1
- published: 2025-09-01

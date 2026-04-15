---
title: "PartDiffuser: Part-wise 3D Mesh Generation via Discrete Diffusion"
authors: ["Yichen Yang", "Hong Li", "Haodong Zhu", "Linin Yang", "Guojun Lei", "Sheng Xu", "Baochang Zhang"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2511.18801"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2511.18801v2"
published: "2025-11-24"
categories: ["cs.CV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:33+09:00"
---

# PartDiffuser: Part-wise 3D Mesh Generation via Discrete Diffusion

## Abstract
Existing autoregressive (AR) methods for generating artist-designed meshes struggle to balance global structural consistency with high-fidelity local details, and are susceptible to error accumulation. To address this, we propose PartDiffuser, a novel semi-autoregressive diffusion framework for point-cloud-to-mesh generation. The method first performs semantic segmentation on the mesh and then operates in a "part-wise" manner: it employs autoregression between parts to ensure global topology, while utilizing a parallel discrete diffusion process within each semantic part to precisely reconstruct high-frequency geometric features. PartDiffuser is based on the DiT architecture and introduces a part-aware cross-attention mechanism, using point clouds as hierarchical geometric conditioning to dynamically control the generation process, thereby effectively decoupling the global and local generation tasks. Experiments demonstrate that this method significantly outperforms state-of-the-art (SOTA) models in generating 3D meshes with rich detail, exhibiting exceptional detail representation suitable for real-world applications.

## Metadata
- venue: arXiv
- year: 2025
- authors: Yichen Yang, Hong Li, Haodong Zhu, Linin Yang, Guojun Lei, Sheng Xu, Baochang Zhang
- arxiv_id: 2511.18801
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2511.18801v2
- published: 2025-11-24

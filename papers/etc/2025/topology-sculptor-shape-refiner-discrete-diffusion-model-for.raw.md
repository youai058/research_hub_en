---
title: "Topology Sculptor, Shape Refiner: Discrete Diffusion Model for High-Fidelity 3D Meshes Generation"
authors: ["Kaiyu Song", "Hanjiang Lai", "Yaqing Zhang", "Chuangjian Cai", "Yan Pan Kun Yue", "Jian Yin"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.21264"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.21264v2"
published: "2025-10-24"
categories: ["cs.CV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:37+09:00"
---

# Topology Sculptor, Shape Refiner: Discrete Diffusion Model for High-Fidelity 3D Meshes Generation

## Abstract
In this paper, we introduce Topology Sculptor, Shape Refiner (TSSR), a novel method for generating high-quality, artist-style 3D meshes based on Discrete Diffusion Models (DDMs). Our primary motivation for TSSR is to achieve highly accurate token prediction while enabling parallel generation, a significant advantage over sequential autoregressive methods. By allowing TSSR to "see" all mesh tokens concurrently, we unlock a new level of efficiency and control. We leverage this parallel generation capability through three key innovations: 1) Decoupled Training and Hybrid Inference, which distinctly separates the DDM-based generation into a topology sculpting stage and a subsequent shape refinement stage. This strategic decoupling enables TSSR to effectively capture both intricate local topology and overarching global shape. 2) An Improved Hourglass Architecture, featuring bidirectional attention enriched by face-vertex-sequence level Rotational Positional Embeddings (RoPE), thereby capturing richer contextual information across the mesh structure. 3) A novel Connection Loss, which acts as a topological constraint to further enhance the realism and fidelity of the generated meshes. Extensive experiments on complex datasets demonstrate that TSSR generates high-quality 3D artist-style meshes, capable of achieving up to 10,000 faces at a remarkable spatial resolution of $1024^3$. The code will be released at: https://github.com/psky1111/Tencent-TSSR.

## Metadata
- venue: arXiv
- year: 2025
- authors: Kaiyu Song, Hanjiang Lai, Yaqing Zhang, Chuangjian Cai, Yan Pan Kun Yue, Jian Yin
- arxiv_id: 2510.21264
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.21264v2
- published: 2025-10-24

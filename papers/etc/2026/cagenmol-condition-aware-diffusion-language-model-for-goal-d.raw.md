---
title: "CAGenMol: Condition-Aware Diffusion Language Model for Goal-Directed Molecular Generation"
authors: ["Yanting Li", "Zhuoyang Jiang", "Enyan Dai", "Lei Wang", "Wen-Cai Ye", "Li Liu"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2604.11483"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2604.11483v1"
published: "2026-04-13"
categories: ["cs.LG", "q-bio.QM"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:13:54+09:00"
---

# CAGenMol: Condition-Aware Diffusion Language Model for Goal-Directed Molecular Generation

## Abstract
Goal-directed molecular generation requires satisfying heterogeneous constraints such as protein--ligand compatibility and multi-objective drug-like properties, yet existing methods often optimize these constraints in isolation, failing to reconcile conflicting objectives (e.g., affinity vs. safety), and struggle to navigate the non-differentiable chemical space without compromising structural validity. To address these challenges, we propose CAGenMol, a condition-aware discrete diffusion framework over molecular sequences that formulates molecular design as conditional denoising guided by heterogeneous structural and property signals. By coupling discrete diffusion with reinforcement learning, the model aligns the generation trajectory with non-differentiable objectives while preserving chemical validity and diversity. The non-autoregressive nature of diffusion language model further enables iterative refinement of molecular fragments at inference time. Experiments on structure-conditioned, property-conditioned, and dual-conditioned benchmarks demonstrate consistent improvements over state-of-the-art methods in binding affinity, drug-likeness, and success rate, highlighting the effectiveness of our framework.

## Metadata
- venue: arXiv
- year: 2026
- authors: Yanting Li, Zhuoyang Jiang, Enyan Dai, Lei Wang, Wen-Cai Ye, Li Liu
- arxiv_id: 2604.11483
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2604.11483v1
- published: 2026-04-13

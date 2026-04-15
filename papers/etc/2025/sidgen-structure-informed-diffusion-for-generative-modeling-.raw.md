---
title: "SiDGen: Structure-informed Diffusion for Generative modeling of Ligands for Proteins"
authors: ["Samyak Sanghvi", "Nishant Ranjan", "Tarak Karmakar"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2511.09529"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2511.09529v3"
published: "2025-11-12"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:37+09:00"
---

# SiDGen: Structure-informed Diffusion for Generative modeling of Ligands for Proteins

## Abstract
Structure-based drug design (SBDD) faces a fundamental scaling fidelity dilemma: rich pocket-aware conditioning captures interaction geometry but can be costly, often scales quadratically ($O(L^2)$) or worse with protein length ($L$), while efficient sequence-only conditioning can miss key interaction structure. We propose SiDGen, a structure-informed discrete diffusion framework that resolves this trade-off through a Topological Information Bottleneck (TIB). SiDGen leverages a learned, soft assignment mechanism to compress residue-level protein representations into a compact bottleneck enabling downstream pairwise computations on the coarse grid ($O(L^2/s^2)$). This design reduces memory and computational cost without compromising generative accuracy. Our approach achieves state-of-the-art performance on CrossDocked2020 and DUD-E benchmarks while significantly reducing pairwise-tensor memory. SiDGen bridges the gap between sequence-based efficiency and pocket-aware conditioning, offering a scalable path for high-throughput structure-based discovery.

## Metadata
- venue: arXiv
- year: 2025
- authors: Samyak Sanghvi, Nishant Ranjan, Tarak Karmakar
- arxiv_id: 2511.09529
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2511.09529v3
- published: 2025-11-12

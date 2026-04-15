---
title: "Empirical Analysis of Decoding Biases in Masked Diffusion Models"
authors: ["Pengcheng Huang", "Tianming Liu", "Zhenghao Liu", "Yukun Yan", "Shuo Wang", "Tong Xiao", "Zulong Chen", "Maosong Sun"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2508.13021"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2508.13021v3"
published: "2025-08-18"
categories: ["cs.AI", "cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:29+09:00"
---

# Empirical Analysis of Decoding Biases in Masked Diffusion Models

## Abstract
Masked diffusion models (MDMs), which leverage bidirectional attention and a denoising process, are narrowing the performance gap with autoregressive models (ARMs). However, their internal attention mechanisms remain under-explored. This paper investigates the attention behaviors in MDMs, revealing the phenomenon of Attention Floating. Unlike ARMs, where attention converges to a fixed sink, MDMs exhibit dynamic, dispersed attention anchors that shift across denoising steps and layers. Further analysis reveals its Shallow Structure-Aware, Deep Content-Focused attention mechanism: shallow layers utilize floating tokens to build a global structural framework, while deeper layers allocate more capability toward capturing semantic content. Empirically, this distinctive attention pattern provides a mechanistic explanation for the strong in-context learning capabilities of MDMs, allowing them to double the performance compared to ARMs in knowledge-intensive tasks. All codes are available at https://github.com/NEUIR/Uncode.

## Metadata
- venue: arXiv
- year: 2025
- authors: Pengcheng Huang, Tianming Liu, Zhenghao Liu, Yukun Yan, Shuo Wang, Tong Xiao, Zulong Chen, Maosong Sun
- arxiv_id: 2508.13021
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2508.13021v3
- published: 2025-08-18

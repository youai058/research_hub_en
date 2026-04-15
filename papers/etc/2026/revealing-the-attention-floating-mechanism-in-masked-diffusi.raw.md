---
title: "Revealing the Attention Floating Mechanism in Masked Diffusion Models"
authors: ["Xin Dai", "Pengcheng Huang", "Zhenghao Liu", "Shuo Wang", "Yukun Yan", "Chaojun Xiao", "Yu Gu", "Ge Yu", "Maosong Sun"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2601.07894"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2601.07894v1"
published: "2026-01-12"
categories: ["cs.LG", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:21+09:00"
---

# Revealing the Attention Floating Mechanism in Masked Diffusion Models

## Abstract
Masked diffusion models (MDMs), which leverage bidirectional attention and a denoising process, are narrowing the performance gap with autoregressive models (ARMs). However, their internal attention mechanisms remain under-explored. This paper investigates the attention behaviors in MDMs, revealing the phenomenon of Attention Floating. Unlike ARMs, where attention converges to a fixed sink, MDMs exhibit dynamic, dispersed attention anchors that shift across denoising steps and layers. Further analysis reveals its Shallow Structure-Aware, Deep Content-Focused attention mechanism: shallow layers utilize floating tokens to build a global structural framework, while deeper layers allocate more capability toward capturing semantic content. Empirically, this distinctive attention pattern provides a mechanistic explanation for the strong in-context learning capabilities of MDMs, allowing them to double the performance compared to ARMs in knowledge-intensive tasks. All codes and datasets are available at https://github.com/NEUIR/Attention-Floating.

## Metadata
- venue: arXiv
- year: 2026
- authors: Xin Dai, Pengcheng Huang, Zhenghao Liu, Shuo Wang, Yukun Yan, Chaojun Xiao, Yu Gu, Ge Yu, Maosong Sun
- arxiv_id: 2601.07894
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2601.07894v1
- published: 2026-01-12

---
title: "ReFusion: A Diffusion Large Language Model with Parallel Autoregressive Decoding"
authors: ["Jia-Nan Li", "Jian Guan", "Wei Wu", "Chongxuan Li"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2512.13586"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2512.13586v2"
published: "2025-12-15"
categories: ["cs.CL", "cs.AI", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:19+09:00"
---

# ReFusion: A Diffusion Large Language Model with Parallel Autoregressive Decoding

## Abstract
Autoregressive models (ARMs) are hindered by slow sequential inference. While masked diffusion models (MDMs) offer a parallel alternative, they suffer from critical drawbacks: high computational overhead from precluding Key-Value (KV) caching, and incoherent generation arising from learning dependencies over an intractable space of token combinations. To address these limitations, we introduce \textsc{ReFusion}, a novel masked diffusion model that integrates sequence reorganization into the causal attention framework. By elevating parallel decoding from the token level to a higher slot level, \textsc{ReFusion} interleaves inter-slot diffusion-based selection with intra-slot autoregressive infilling, while reordering newly generated slots ahead of the remaining masks after each iteration. Consequently, this design simultaneously unlocks full KV cache reuse and reduces learning complexity from an intractable token combination space to a manageable slot-level permutation space. Extensive experiments on seven diverse benchmarks show that \textsc{ReFusion} not only overwhelmingly surpasses prior MDMs with a 34\% performance gain and an over 18$\times$ speedup on average, but also bridges the performance gap to strong ARMs while maintaining a 2.33$\times$ average speedup.

## Metadata
- venue: arXiv
- year: 2025
- authors: Jia-Nan Li, Jian Guan, Wei Wu, Chongxuan Li
- arxiv_id: 2512.13586
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2512.13586v2
- published: 2025-12-15

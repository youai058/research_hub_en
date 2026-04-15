---
title: "Learning Permutation Distributions via Reflected Diffusion on Ranks"
authors: ["Sizhuang He", "Yangtian Zhang", "Shiyang Zhang", "David van Dijk"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.17353"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.17353v1"
published: "2026-03-18"
categories: ["cs.LG", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:24+09:00"
---

# Learning Permutation Distributions via Reflected Diffusion on Ranks

## Abstract
The finite symmetric group S_n provides a natural domain for permutations, yet learning probability distributions on S_n is challenging due to its factorially growing size and discrete, non-Euclidean structure. Recent permutation diffusion methods define forward noising via shuffle-based random walks (e.g., riffle shuffles) and learn reverse transitions with Plackett-Luce (PL) variants, but the resulting trajectories can be abrupt and increasingly hard to denoise as n grows. We propose Soft-Rank Diffusion, a discrete diffusion framework that replaces shuffle-based corruption with a structured soft-rank forward process: we lift permutations to a continuous latent representation of order by relaxing discrete ranks into soft ranks, yielding smoother and more tractable trajectories. For the reverse process, we introduce contextualized generalized Plackett-Luce (cGPL) denoisers that generalize prior PL-style parameterizations and improve expressivity for sequential decision structures. Experiments on sorting and combinatorial optimization benchmarks show that Soft-Rank Diffusion consistently outperforms prior diffusion baselines, with particularly strong gains in long-sequence and intrinsically sequential settings.

## Metadata
- venue: arXiv
- year: 2026
- authors: Sizhuang He, Yangtian Zhang, Shiyang Zhang, David van Dijk
- arxiv_id: 2603.17353
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.17353v1
- published: 2026-03-18

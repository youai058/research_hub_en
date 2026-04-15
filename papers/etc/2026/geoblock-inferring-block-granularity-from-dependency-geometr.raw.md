---
title: "GeoBlock: Inferring Block Granularity from Dependency Geometry in Diffusion Language Models"
authors: ["Lipeng Wan", "Junjie Ma", "Jianhui Gu", "Zeyang Liu", "Xuyang Lu", "Xuguang Lan"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.26675"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.26675v1"
published: "2026-03-04"
categories: ["cs.CL", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:13:58+09:00"
---

# GeoBlock: Inferring Block Granularity from Dependency Geometry in Diffusion Language Models

## Abstract
Block diffusion enables efficient parallel refinement in diffusion language models, but its decoding behavior depends critically on block size. Existing block-sizing strategies rely on fixed rules or heuristic signals and do not account for the dependency geometry that determines which tokens can be safely refined together. This motivates a geometry view of diffusion decoding: \emph{regions with strong causal ordering require sequential updates, whereas semantically cohesive regions admit parallel refinement.} We introduce GeoBlock, a geometry-aware block inference framework that determines block granularity directly from attention-derived dependency geometry. Instead of relying on predefined schedules or local confidence heuristics, GeoBlock analyzes cross-token dependency patterns to identify geometrically stable refinement regions and dynamically determines appropriate block boundaries during decoding. By adapting block granularity to the dependency geometry, GeoBlock preserves the parallel efficiency of block diffusion while enforcing dependency-consistent refinement that exhibits autoregressive reliability. GeoBlock requires no additional training and integrates seamlessly into existing block diffusion architectures. Extensive experiments across multiple benchmarks show that GeoBlock reliably identifies geometry-consistent block boundaries and improves the accuracy of block diffusion with only a small additional computational budget.

## Metadata
- venue: arXiv
- year: 2026
- authors: Lipeng Wan, Junjie Ma, Jianhui Gu, Zeyang Liu, Xuyang Lu, Xuguang Lan
- arxiv_id: 2603.26675
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.26675v1
- published: 2026-03-04

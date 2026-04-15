---
title: "D5P4: Partition Determinantal Point Process for Diversity in Parallel Discrete Diffusion Decoding"
authors: ["Jonathan Lys", "Vincent Gripon", "Bastien Pasdeloup", "Axel Marmoret", "Lukas Mauch", "Fabien Cardinaux", "Ghouthi Boukli Hacene"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.19146"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.19146v1"
published: "2026-03-19"
categories: ["cs.AI", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:24+09:00"
---

# D5P4: Partition Determinantal Point Process for Diversity in Parallel Discrete Diffusion Decoding

## Abstract
Discrete diffusion models are promising alternatives to autoregressive approaches for text generation, yet their decoding methods remain under-studied. Standard decoding methods for autoregressive models, such as beam search, do not directly apply to iterative denoising, and existing diffusion decoding techniques provide limited control over in-batch diversity. To bridge this gap, we introduce a generalized beam-search framework for discrete diffusion that generates candidates in parallel and supports modular beam-selection objectives. As a diversity-focused instantiation, we propose D5P4, which formulates the selection step as MAP inference over a Determinantal Point Process. Leveraging a scalable greedy solver, D5P4 maintains multi-GPU compatibility and enables an explicit trade-off between model probability and target diversity with near-zero compute overhead. Experiments on free-form generation and question answering demonstrate that D5P4 improves diversity over strong baselines while maintaining competitive generation quality.

## Metadata
- venue: arXiv
- year: 2026
- authors: Jonathan Lys, Vincent Gripon, Bastien Pasdeloup, Axel Marmoret, Lukas Mauch, Fabien Cardinaux, Ghouthi Boukli Hacene
- arxiv_id: 2603.19146
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.19146v1
- published: 2026-03-19

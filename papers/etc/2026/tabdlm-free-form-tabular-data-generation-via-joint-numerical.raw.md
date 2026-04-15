---
title: "TabDLM: Free-Form Tabular Data Generation via Joint Numerical-Language Diffusion"
authors: ["Donghong Cai", "Jiarui Feng", "Yanbo Wang", "Da Zheng", "Yixin Chen", "Muhan Zhang"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.22586"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.22586v1"
published: "2026-02-26"
categories: ["cs.LG", "cs.AI", "cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:02+09:00"
---

# TabDLM: Free-Form Tabular Data Generation via Joint Numerical-Language Diffusion

## Abstract
Synthetic tabular data generation has attracted growing attention due to its importance for data augmentation, foundation models, and privacy. However, real-world tabular datasets increasingly contain free-form text fields (e.g., reviews or clinical notes) alongside structured numerical and categorical attributes. Generating such heterogeneous tables with joint modeling of different modalities remains challenging. Existing approaches broadly fall into two categories: diffusion-based methods and LLM-based methods. Diffusion models can capture complex dependencies over numerical and categorical features in continuous or discrete spaces, but extending them to open-ended text is nontrivial and often leads to degraded text quality. In contrast, LLM-based generators naturally produce fluent text, yet their discrete tokenization can distort precise or wide-range numerical values, hindering accurate modeling of both numbers and language. In this work, we propose TabDLM, a unified framework for free-form tabular data generation via a joint numerical--language diffusion model built on masked diffusion language models (MDLMs). TabDLM models textual and categorical features through masked diffusion, while modeling numerical features with a continuous diffusion process through learned specialized numeric tokens embedding; bidirectional attention then captures cross-modality interactions within a single model. Extensive experiments on diverse benchmarks demonstrate the effectiveness of TabDLM compared to strong diffusion- and LLM-based baselines.

## Metadata
- venue: arXiv
- year: 2026
- authors: Donghong Cai, Jiarui Feng, Yanbo Wang, Da Zheng, Yixin Chen, Muhan Zhang
- arxiv_id: 2602.22586
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.22586v1
- published: 2026-02-26

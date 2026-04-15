---
title: "Fast-dVLM: Efficient Block-Diffusion VLM via Direct Conversion from Autoregressive VLM"
authors: ["Chengyue Wu", "Shiyi Lan", "Yonggan Fu", "Sensen Gao", "Jin Wang", "Jincheng Yu", "Jose M. Alvarez", "Pavlo Molchanov", "Ping Luo", "Song Han", "Ligeng Zhu", "Enze Xie"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2604.06832"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2604.06832v2"
published: "2026-04-08"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:24+09:00"
---

# Fast-dVLM: Efficient Block-Diffusion VLM via Direct Conversion from Autoregressive VLM

## Abstract
Vision-language models (VLMs) predominantly rely on autoregressive decoding, which generates tokens one at a time and fundamentally limits inference throughput. This limitation is especially acute in physical AI scenarios such as robotics and autonomous driving, where VLMs are deployed on edge devices at batch size one, making AR decoding memory-bandwidth-bound and leaving hardware parallelism underutilized. While block-wise discrete diffusion has shown promise for parallel text generation, extending it to VLMs remains challenging due to the need to jointly handle continuous visual representations and discrete text tokens while preserving pretrained multimodal capabilities. We present Fast-dVLM, a block-diffusion-based VLM that enables KV-cache-compatible parallel decoding and speculative block decoding for inference acceleration. We systematically compare two AR-to-diffusion conversion strategies: a two-stage approach that first adapts the LLM backbone with text-only diffusion fine-tuning before multimodal training, and a direct approach that converts the full AR VLM in one stage. Under comparable training budgets, direct conversion proves substantially more efficient by leveraging the already multimodally aligned VLM; we therefore adopt it as our recommended recipe. We introduce a suite of multimodal diffusion adaptations, block size annealing, causal context attention, auto-truncation masking, and vision efficient concatenation, that collectively enable effective block diffusion in the VLM setting. Extensive experiments across 11 multimodal benchmarks show Fast-dVLM matches its autoregressive counterpart in generation quality. With SGLang integration and FP8 quantization, Fast-dVLM achieves over 6x end-to-end inference speedup over the AR baseline.

## Metadata
- venue: arXiv
- year: 2026
- authors: Chengyue Wu, Shiyi Lan, Yonggan Fu, Sensen Gao, Jin Wang, Jincheng Yu, Jose M. Alvarez, Pavlo Molchanov, Ping Luo, Song Han, Ligeng Zhu, Enze Xie
- arxiv_id: 2604.06832
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2604.06832v2
- published: 2026-04-08

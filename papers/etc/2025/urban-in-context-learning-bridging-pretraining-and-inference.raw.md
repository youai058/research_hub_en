---
title: "Urban In-Context Learning: Bridging Pretraining and Inference through Masked Diffusion for Urban Profiling"
authors: ["Ruixing Zhang", "Bo Wang", "Tongyu Zhu", "Leilei Sun", "Weifeng Lv"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2508.03042"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2508.03042v1"
published: "2025-08-05"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:29+09:00"
---

# Urban In-Context Learning: Bridging Pretraining and Inference through Masked Diffusion for Urban Profiling

## Abstract
Urban profiling aims to predict urban profiles in unknown regions and plays a critical role in economic and social censuses. Existing approaches typically follow a two-stage paradigm: first, learning representations of urban areas; second, performing downstream prediction via linear probing, which originates from the BERT era. Inspired by the development of GPT style models, recent studies have shown that novel self-supervised pretraining schemes can endow models with direct applicability to downstream tasks, thereby eliminating the need for task-specific fine-tuning. This is largely because GPT unifies the form of pretraining and inference through next-token prediction. However, urban data exhibit structural characteristics that differ fundamentally from language, making it challenging to design a one-stage model that unifies both pretraining and inference. In this work, we propose Urban In-Context Learning, a framework that unifies pretraining and inference via a masked autoencoding process over urban regions. To capture the distribution of urban profiles, we introduce the Urban Masked Diffusion Transformer, which enables each region' s prediction to be represented as a distribution rather than a deterministic value. Furthermore, to stabilize diffusion training, we propose the Urban Representation Alignment Mechanism, which regularizes the model's intermediate features by aligning them with those from classical urban profiling methods. Extensive experiments on three indicators across two cities demonstrate that our one-stage method consistently outperforms state-of-the-art two-stage approaches. Ablation studies and case studies further validate the effectiveness of each proposed module, particularly the use of diffusion modeling.

## Metadata
- venue: arXiv
- year: 2025
- authors: Ruixing Zhang, Bo Wang, Tongyu Zhu, Leilei Sun, Weifeng Lv
- arxiv_id: 2508.03042
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2508.03042v1
- published: 2025-08-05

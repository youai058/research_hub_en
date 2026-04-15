---
title: "Fine-Grained Captioning of Long Videos through Scene Graph Consolidation"
authors: ["Sanghyeok Chu", "Seonguk Seo", "Bohyung Han"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "aTC2euLwnh"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c961731b02183da65b53077d1d3442100a774279.pdf"
published: "2025"
categories: []
keywords: ["Long video captioning", "zero-shot video captioning", "scene graph"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:21+09:00"
---

# Fine-Grained Captioning of Long Videos through Scene Graph Consolidation

## Abstract
Recent advances in vision-language models have led to impressive progress in caption generation for images and short video clips. However, these models remain constrained by their limited temporal receptive fields, making it difficult to produce
coherent and comprehensive captions for long videos. While several methods have been proposed to aggregate information across video segments, they often rely on supervised fine-tuning or incur significant computational overhead. To address these challenges, we introduce a novel framework for long video captioning based on graph consolidation. Our approach first generates segment-level captions, corresponding to individual frames or short video intervals, using off-the-shelf visual captioning models. These captions are then parsed into individual scene graphs, which are subsequently consolidated into a unified graph representation that preserves both holistic context and fine-grained details throughout the video. A lightweight graph-to-text decoder then produces the final video-level caption. This framework effectively extends the temporal understanding capabilities of existing models without requiring any additional fine-tuning on long video datasets. Experimental results show that our method significantly outperforms existing LLM-based consolidation approaches, achieving strong zero-shot performance while substantially reducing computational costs.

## Metadata
- venue: ICML
- year: 2025
- authors: Sanghyeok Chu, Seonguk Seo, Bohyung Han
- arxiv_id: 
- openreview_id: aTC2euLwnh
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c961731b02183da65b53077d1d3442100a774279.pdf
- published: 2025
- keywords: Long video captioning, zero-shot video captioning, scene graph

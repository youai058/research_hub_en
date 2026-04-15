---
title: "ST-SimDiff: Balancing Spatiotemporal Similarity and Difference for Efficient Video Understanding with MLLMs"
authors: ["Bingjun Luo", "Tony Wang", "Chaoqi Chen", "Xinpeng Ding"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "he8kYNcoMA"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b697cea955353f3b35057bb9055738474d679568.pdf"
published: "2026"
categories: []
keywords: ["Video Understanding", "Visual Token Reduction", "Multimodal Large Language Models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:30+09:00"
---

# ST-SimDiff: Balancing Spatiotemporal Similarity and Difference for Efficient Video Understanding with MLLMs

## Abstract
Multimodal Large Language Models (MLLMs) face significant computational overhead when processing long videos due to the massive number of visual tokens required. To improve efficiency, existing methods primarily reduce redundancy by pruning or merging tokens based on importance or similarity. However, these approaches largely overlook a critical dimension of video content, i.e., changes and turning points, and they lack a collaborative model for spatio-temporal relationships.
To address this, we propose a new perspective: similarity is for identifying redundancy, while difference is for capturing key events. Based on this, we designed a training-free framework named ST-SimDiff. We first construct a spatio-temporal graph from the visual tokens to uniformly model their complex associations. Subsequently, we employ a parallel dual-selection strategy: 1) similarity-based selection uses community detection to retain representative tokens, compressing static information; 2) temporal difference-based selection precisely locates content-changing points to preserve tokens that capture key dynamic shifts. This allows it to preserve both static and dynamic content with a minimal number of tokens. Extensive experiments show our method significantly outperforms state-of-the-art approaches while substantially reducing computational costs.
Our code is available in [https://github.com/bingjunluo/ST-SimDiff](https://github.com/bingjunluo/ST-SimDiff).

## Metadata
- venue: ICLR
- year: 2026
- authors: Bingjun Luo, Tony Wang, Chaoqi Chen, Xinpeng Ding
- arxiv_id: 
- openreview_id: he8kYNcoMA
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b697cea955353f3b35057bb9055738474d679568.pdf
- published: 2026
- keywords: Video Understanding, Visual Token Reduction, Multimodal Large Language Models

---
title: "Dynin-Omni: Omnimodal Unified Large Diffusion Language Model"
authors: ["Jaeik Kim", "Woojin Kim", "Jihwan Hong", "Yejoon Lee", "Sieun Hyeon", "Mintaek Lim", "Yunseok Han", "Dogeun Kim", "Hoeun Lee", "Hyunggeun Kim", "Jaeyoung Do"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2604.00007"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2604.00007v1"
published: "2026-03-09"
categories: ["cs.CL", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:09+09:00"
---

# Dynin-Omni: Omnimodal Unified Large Diffusion Language Model

## Abstract
We present Dynin-Omni, the first masked-diffusion-based omnimodal foundation model that unifies text, image, and speech understanding and generation, together with video understanding, within a single architecture. Unlike autoregressive unified models that serialize heterogeneous modalities, or compositional unified models that require orchestration with external modality-specific decoders, Dynin-Omni natively formulates omnimodal modeling as masked diffusion over a shared discrete token space, enabling iterative refinement under bidirectional context. Dynin-Omni adopts a multi-stage training strategy with model-merging-based modality expansion and omnimodal alignment. We evaluate Dynin-Omni across 19 multimodal benchmarks spanning language reasoning, image generation and editing, video understanding, and speech recognition and synthesis. Dynin-Omni achieves 87.6 on GSM8K, 1733.6 on MME-P, 61.4 on VideoMME, 0.87 on GenEval, and 2.1 WER on LibriSpeech test-clean, consistently outperforming existing open-source unified models while remaining competitive with strong modality-specific expert systems. These results demonstrate the potential of masked diffusion as a unified paradigm for any-to-any modeling, providing a flexible foundation for real-time omnimodal systems, unified cross-modal retrieval and generation, and embodied multimodal agents.

## Metadata
- venue: arXiv
- year: 2026
- authors: Jaeik Kim, Woojin Kim, Jihwan Hong, Yejoon Lee, Sieun Hyeon, Mintaek Lim, Yunseok Han, Dogeun Kim, Hoeun Lee, Hyunggeun Kim, Jaeyoung Do
- arxiv_id: 2604.00007
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2604.00007v1
- published: 2026-03-09

---
title: "RIV: Recursive Introspection Mask Diffusion Vision Language Model"
authors: ["YuQian Li", "Limeng Qiao", "Lin Ma"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2509.23625"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2509.23625v1"
published: "2025-09-28"
categories: ["cs.CV", "cs.AI", "cs.CL", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:26+09:00"
---

# RIV: Recursive Introspection Mask Diffusion Vision Language Model

## Abstract
Mask Diffusion-based Vision Language Models (MDVLMs) have achieved remarkable progress in multimodal understanding tasks. However, these models are unable to correct errors in generated tokens, meaning they lack self-correction capability. In this paper, we propose Recursive Introspection Mask Diffusion Vision Language Model (RIV), which equips the model with self-correction ability through two novel mechanisms. The first is Introspection Training, where an Introspection Model is introduced to identify errors within generated sequences. Introspection Training enables the model to detect not only grammatical and spelling mistakes, but more importantly, logical errors. The second is Recursive Inference. Beginning with the standard unmasking step, the learned Introspection Model helps to identify errors in the output sequence and remask them. This alternating ($\text{unmask}\rightarrow\text{introspection}\rightarrow\text{remask}$) process is repeated recursively until reliable results are obtained. Experimental results on multiple benchmarks demonstrate that the proposed RIV achieves state-of-the-art performance, outperforming most existing MDVLMs.

## Metadata
- venue: arXiv
- year: 2025
- authors: YuQian Li, Limeng Qiao, Lin Ma
- arxiv_id: 2509.23625
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2509.23625v1
- published: 2025-09-28

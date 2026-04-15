---
title: "From Denoising to Refining: A Corrective Framework for Vision-Language Diffusion Model"
authors: ["Yatai Ji", "Teng Wang", "Yuying Ge", "Zhiheng Liu", "Sidi Yang", "Ying Shan", "Ping Luo"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.19871"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.19871v1"
published: "2025-10-22"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:40+09:00"
---

# From Denoising to Refining: A Corrective Framework for Vision-Language Diffusion Model

## Abstract
Discrete diffusion models have emerged as a promising direction for vision-language tasks, offering bidirectional context modeling and theoretical parallelization. However, their practical application is severely hindered by a train-inference discrepancy, which leads to catastrophic error cascades: initial token errors during parallel decoding pollute the generation context, triggering a chain reaction of compounding errors and leading to syntactic errors and semantic hallucinations. To address this fundamental challenge, we reframe the generation process from passive denoising to active refining. We introduce ReDiff, a refining-enhanced diffusion framework that teaches the model to identify and correct its own errors. Our approach features a two-stage training process: first, we instill a foundational revision capability by training the model to revise synthetic errors; second, we implement a novel online self-correction loop where the model is explicitly trained to revise its own flawed drafts by learning from an expert's corrections. This mistake-driven learning endows the model with the crucial ability to revisit and refine its already generated output, effectively breaking the error cascade. Extensive experiments demonstrate that ReDiff significantly improves the coherence and factual accuracy of generated content, enabling stable and efficient parallel generation far superior to traditional denoising methods. Our codes and models are available at https://rediff-hku.github.io/.

## Metadata
- venue: arXiv
- year: 2025
- authors: Yatai Ji, Teng Wang, Yuying Ge, Zhiheng Liu, Sidi Yang, Ying Shan, Ping Luo
- arxiv_id: 2510.19871
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.19871v1
- published: 2025-10-22

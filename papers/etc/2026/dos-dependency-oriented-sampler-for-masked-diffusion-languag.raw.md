---
title: "DOS: Dependency-Oriented Sampler for Masked Diffusion Language Models"
authors: ["Xueyu Zhou", "Yangrong Hu", "Jian Huang"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.15340"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.15340v1"
published: "2026-03-16"
categories: ["cs.CL", "stat.ML"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:13:58+09:00"
---

# DOS: Dependency-Oriented Sampler for Masked Diffusion Language Models

## Abstract
Masked diffusion language models (MDLMs) have recently emerged as a new paradigm in language modeling, offering flexible generation dynamics and enabling efficient parallel decoding. However, existing decoding strategies for pre-trained MDLMs predominantly rely on token-level uncertainty criteria, while largely overlooking sequence-level information and inter-token dependencies. To address this limitation, we propose Dependency-Oriented Sampler (DOS), a training-free decoding strategy that leverages inter-token dependencies to inform token updates during generation. Specifically, DOS exploits attention matrices from transformer blocks to approximate inter-token dependencies, emphasizing information from unmasked tokens when updating masked positions. Empirical results demonstrate that DOS consistently achieves superior performance on both code generation and mathematical reasoning tasks. Moreover, DOS can be seamlessly integrated with existing parallel sampling methods, leading to improved generation efficiency without sacrificing generation quality.

## Metadata
- venue: arXiv
- year: 2026
- authors: Xueyu Zhou, Yangrong Hu, Jian Huang
- arxiv_id: 2603.15340
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.15340v1
- published: 2026-03-16

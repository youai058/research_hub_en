---
title: "Guided Star-Shaped Masked Diffusion"
authors: ["Viacheslav Meshchaninov", "Egor Shibaev", "Artem Makoian", "Ivan Klimov", "Nikita Balagansky", "Daniil Gavrilov", "Aibek Alanov", "Dmitry Vetrov"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.08369"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.08369v2"
published: "2025-10-09"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:22+09:00"
---

# Guided Star-Shaped Masked Diffusion

## Abstract
The performance of pre-trained masked diffusion models is often constrained by their sampling procedure, which makes decisions irreversible and struggles in low-step generation regimes. We introduce a novel sampling algorithm that works with pre-trained models and, after a lightweight fine-tuning of a single layer, significantly improves sample quality and efficiency. Our method reformulates the generation process using a star-shaped paradigm, which inherently allows for error correction. To make this process effective, we augment it with a learnable re-masking scheduler that intelligently identifies and revises likely errors. This approach yields a substantial quality boost, particularly when using a small number of sampling steps. We extensively ablate key components of our approach and show its usability in different scenarios. In comprehensive experiments on text, and code generation, our sampling algorithm outperforms or matches existing methods.

## Metadata
- venue: arXiv
- year: 2025
- authors: Viacheslav Meshchaninov, Egor Shibaev, Artem Makoian, Ivan Klimov, Nikita Balagansky, Daniil Gavrilov, Aibek Alanov, Dmitry Vetrov
- arxiv_id: 2510.08369
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.08369v2
- published: 2025-10-09

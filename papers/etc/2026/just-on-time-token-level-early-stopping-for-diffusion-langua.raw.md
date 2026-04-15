---
title: "Just on Time: Token-Level Early Stopping for Diffusion Language Models"
authors: ["Zahar Kohut", "Severyn Shykula", "Dmytro Khamula", "Mykola Vysotskyi", "Taras Rumezhak", "Volodymyr Karpiv"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.11133"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.11133v1"
published: "2026-02-11"
categories: ["cs.LG", "cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:05+09:00"
---

# Just on Time: Token-Level Early Stopping for Diffusion Language Models

## Abstract
Diffusion language models generate text through iterative refinement, a process that is often computationally inefficient because many tokens reach stability long before the final denoising step. We introduce a training-free, token-level early stopping approach that identifies convergence independently at each position. Our method leverages lightweight signals derived from the model's predictions and local context to dynamically determine when individual tokens can be finalized. This yields adaptive per-token freezing without task-specific fine-tuning, substantially reducing the total number of diffusion steps required. Across diverse benchmarks, spanning mathematical reasoning, general question answering, and scientific understanding, our approach achieves state-of-the-art efficiency gains while preserving generation quality.

## Metadata
- venue: arXiv
- year: 2026
- authors: Zahar Kohut, Severyn Shykula, Dmytro Khamula, Mykola Vysotskyi, Taras Rumezhak, Volodymyr Karpiv
- arxiv_id: 2602.11133
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.11133v1
- published: 2026-02-11

---
title: "Learn from Your Mistakes: Self-Correcting Masked Diffusion Models"
authors: ["Yair Schiff", "Omer Belhasin", "Roy Uziel", "Guanghan Wang", "Marianne Arriola", "Gilad Turok", "Michael Elad", "Volodymyr Kuleshov"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.11590"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.11590v2"
published: "2026-02-12"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:17+09:00"
---

# Learn from Your Mistakes: Self-Correcting Masked Diffusion Models

## Abstract
Masked diffusion models (MDMs) have emerged as a promising alternative to autoregressive models, enabling parallel token generation while achieving competitive performance. Despite these advantages, MDMs face a fundamental limitation: once tokens are unmasked, they remain fixed, leading to error accumulation and ultimately degrading sample quality. We address this by proposing a framework that trains a model to perform both unmasking and correction. By reusing outputs from the MDM denoising network as inputs for corrector training, we train a model to recover from potential mistakes. During generation we apply additional corrective refinement steps between unmasking ones in order to change decoded tokens and improve outputs. We name our training and sampling method Progressive Self-Correction (ProSeCo) for its unique ability to iteratively refine an entire sequence, including already generated tokens. We conduct extensive experimental validation across multiple conditional and unconditional tasks, demonstrating that ProSeCo yields better quality-efficiency trade-offs (up to ~2-3x faster sampling) and enables inference-time compute scaling to further increase sample quality beyond standard MDMs (up to ~1.3x improvement on benchmarks).

## Metadata
- venue: arXiv
- year: 2026
- authors: Yair Schiff, Omer Belhasin, Roy Uziel, Guanghan Wang, Marianne Arriola, Gilad Turok, Michael Elad, Volodymyr Kuleshov
- arxiv_id: 2602.11590
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.11590v2
- published: 2026-02-12

---
title: "Search or Accelerate: Confidence-Switched Position Beam Search for Diffusion Language Models"
authors: ["Mingyu Cao", "Alvaro H. C. Correia", "Christos Louizos", "Shiwei Liu", "Lu Yin"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.10953"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.10953v2"
published: "2026-02-11"
categories: ["cs.CL", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:05+09:00"
---

# Search or Accelerate: Confidence-Switched Position Beam Search for Diffusion Language Models

## Abstract
Diffusion Language Models (DLMs) generate text by iteratively denoising a masked sequence, repeatedly deciding which positions to commit at each step. Standard decoding follows a greedy rule: unmask the most confident positions, yet this local choice can lock the model into a suboptimal unmasking order, especially on reasoning-heavy prompts. We present SOAR, a training-free decoding algorithm that adapts its behavior to the model's uncertainty. When confidence is low, SOAR briefly widens the search over alternative unmasking decisions to avoid premature commitments; when confidence is high, it collapses the search and decodes many positions in parallel to reduce the number of denoising iterations. Across mathematical reasoning and code generation benchmarks (GSM8K, MBPP, HumanEval) on Dream-7B and LLaDA-8B, SOAR improves generation quality while maintaining competitive inference speed, offering a practical way to balance quality and efficiency in DLM decoding. Our Code is available at https://github.com/duterscmy/SOAR

## Metadata
- venue: arXiv
- year: 2026
- authors: Mingyu Cao, Alvaro H. C. Correia, Christos Louizos, Shiwei Liu, Lu Yin
- arxiv_id: 2602.10953
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.10953v2
- published: 2026-02-11

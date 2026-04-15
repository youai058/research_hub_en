---
title: "SAFEPATH: Preventing Harmful Reasoning in Chain-of-Thought via Early Alignment"
authors: ["Wonje Jeung", "Sangyeon Yoon", "Minsuk Kahng", "Albert No"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "vIaNnnQxcl"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/bdb50a5d4b6df8189537be5d04e1a9bdd1dd5249.pdf"
published: "2025"
categories: []
keywords: ["Large Reasoning Models (LRMs)", "Chain-of-Thought Reasoning", "Safety Alignment", "Zero-shot Alignment"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:36+09:00"
---

# SAFEPATH: Preventing Harmful Reasoning in Chain-of-Thought via Early Alignment

## Abstract
Large Reasoning Models (LRMs) have become powerful tools for complex problem solving, but their structured reasoning pathways can lead to unsafe outputs when exposed to harmful prompts. Existing safety alignment methods reduce harmful outputs but can degrade reasoning depth, leading to significant trade-offs in complex, multi-step tasks, and remain vulnerable to sophisticated jailbreak attacks. To address this, we introduce SAFEPATH, a lightweight alignment method that fine-tunes LRMs to emit a short, 8-token Safety Primer at the start of their reasoning, in response to harmful prompts, while leaving the rest of the reasoning process unsupervised. Empirical results across multiple  benchmarks indicate that SAFEPATH effectively reduces harmful outputs while maintaining reasoning performance. Specifically, SAFEPATH reduces harmful responses by up to 90.0\% and blocks 83.3\% of jailbreak attempts in the DeepSeek-R1-Distill-Llama-8B model, while requiring 295.9x less compute than Direct Refusal and 314.1x less than SafeChain. We further introduce a zero-shot variant that requires no fine-tuning. In addition, we provide a comprehensive analysis of how existing methods in LLMs generalize, or fail, when applied to reasoning-centric models, revealing critical gaps and new directions for safer AI.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Wonje Jeung, Sangyeon Yoon, Minsuk Kahng, Albert No
- arxiv_id: 
- openreview_id: vIaNnnQxcl
- anthology_id: 
- pdf_url: https://openreview.net/pdf/bdb50a5d4b6df8189537be5d04e1a9bdd1dd5249.pdf
- published: 2025
- keywords: Large Reasoning Models (LRMs), Chain-of-Thought Reasoning, Safety Alignment, Zero-shot Alignment

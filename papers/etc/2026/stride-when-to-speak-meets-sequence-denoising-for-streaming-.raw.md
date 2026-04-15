---
title: "STRIDE: When to Speak Meets Sequence Denoising for Streaming Video Understanding"
authors: ["Junho Kim", "Hosu Lee", "James M. Rehg", "Minsu Kim", "Yong Man Ro"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.27593"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.27593v1"
published: "2026-03-29"
categories: ["cs.CV", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:09+09:00"
---

# STRIDE: When to Speak Meets Sequence Denoising for Streaming Video Understanding

## Abstract
Recent progress in video large language models (Video-LLMs) has enabled strong offline reasoning over long and complex videos. However, real-world deployments increasingly require streaming perception and proactive interaction, where video frames arrive online and the system must decide not only what to respond, but also when to respond. In this work, we revisit proactive activation in streaming video as a structured sequence modeling problem, motivated by the observation that temporal transitions in streaming video naturally form span-structured activation patterns. To capture this span-level structure, we model activation signals jointly over a sliding temporal window and update them iteratively as new frames arrive. We propose STRIDE (Structured Temporal Refinement with Iterative DEnoising), which employs a lightweight masked diffusion module at the activation interface to jointly predict and progressively refine activation signals across the window. Extensive experiments on diverse streaming benchmarks and downstream models demonstrate that STRIDE shows more reliable and temporally coherent proactive responses, significantly improving when-to-speak decision quality in online streaming scenarios.

## Metadata
- venue: arXiv
- year: 2026
- authors: Junho Kim, Hosu Lee, James M. Rehg, Minsu Kim, Yong Man Ro
- arxiv_id: 2603.27593
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.27593v1
- published: 2026-03-29

---
title: "Diffusion Language Models Are Natively Length-Aware"
authors: ["Vittorio Rossi", "Giacomo Cirò", "Davide Beltrame", "Luca Gandolfi", "Paul Röttger", "Dirk Hovy"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.06123"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.06123v1"
published: "2026-03-06"
categories: ["cs.CL", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:13:58+09:00"
---

# Diffusion Language Models Are Natively Length-Aware

## Abstract
Unlike autoregressive language models, which terminate variable-length generation upon predicting an End-of-Sequence (EoS) token, Diffusion Language Models (DLMs) operate over a fixed maximum-length context window for a predetermined number of denoising steps. However, this process is independent of the required response length, resulting in computational waste for the majority of short responses common in reasoning and chat tasks. To address this problem, we conjecture that the latent prompt representation contains sufficient information to estimate the required output length. We provide empirical evidence for this phenomenon and propose a zero-shot mechanism to dynamically crop the context window before generation begins, leading to fewer diffusion steps and substantial computational savings. We evaluate our approach on four benchmarks with diverse tasks -- GSM8K (reasoning), HumanEval (code generation), IfEval (instruction following), and LongFormQA (question answering) -- revealing massive efficiency gains at minimal performance impact. We report significant reductions in FLOPs across all tasks, with no statistically significant performance degradation, and significant performance improvements in 2 out of 4 tasks.

## Metadata
- venue: arXiv
- year: 2026
- authors: Vittorio Rossi, Giacomo Cirò, Davide Beltrame, Luca Gandolfi, Paul Röttger, Dirk Hovy
- arxiv_id: 2603.06123
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.06123v1
- published: 2026-03-06

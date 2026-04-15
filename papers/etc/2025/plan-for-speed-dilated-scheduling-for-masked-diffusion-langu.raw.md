---
title: "Plan for Speed: Dilated Scheduling for Masked Diffusion Language Models"
authors: ["Omer Luxembourg", "Haim Permuter", "Eliya Nachmani"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2506.19037"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2506.19037v3"
published: "2025-06-23"
categories: ["cs.CL", "cs.AI", "cs.IT", "cs.LG", "cs.NE"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:29+09:00"
---

# Plan for Speed: Dilated Scheduling for Masked Diffusion Language Models

## Abstract
Masked diffusion language models (MDLMs) promise fast, non-autoregressive text generation, yet existing samplers, which pick tokens to unmask based on model confidence, ignore interactions when unmasking multiple positions in parallel and effectively reduce to slow, autoregressive behavior. We propose the Dilated Unmasking Scheduler (DUS), an inference-only, planner-model-free method that partitions sequence positions into non-adjacent dilated groups and unmasked them in parallel so as to minimize an upper bound on joint entropy gain at each denoising step. By explicitly trading off the number of network calls against generation quality, DUS recovers most of the performance lost under traditional parallel unmasking strategies. Across math (GSM8K, MATH500), code (HumanEval, MBPP) and general-knowledge benchmarks (BBH, MMLU-Pro), DUS outperforms confidence-based planners, without modifying the underlying denoiser, and reveals the true speed-quality frontier of MDLMs.

## Metadata
- venue: arXiv
- year: 2025
- authors: Omer Luxembourg, Haim Permuter, Eliya Nachmani
- arxiv_id: 2506.19037
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2506.19037v3
- published: 2025-06-23

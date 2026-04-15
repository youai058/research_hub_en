---
title: "GIFT: Guided Importance-Aware Fine-Tuning for Diffusion Language Models"
authors: ["Guowei Xu", "Wenxin Xu", "Jiawang Zhao", "Kaisheng Ma"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2509.20863"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2509.20863v2"
published: "2025-09-25"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:14+09:00"
---

# GIFT: Guided Importance-Aware Fine-Tuning for Diffusion Language Models

## Abstract
Diffusion models have recently shown strong potential in language modeling, offering faster generation compared to traditional autoregressive approaches. However, applying supervised fine-tuning (SFT) to diffusion models remains challenging, as they lack precise probability estimates at each denoising step. While the diffusion mechanism enables the model to reason over entire sequences, it also makes the generation process less predictable and often inconsistent. This highlights the importance of controlling key tokens that guide the direction of generation. To address this issue, we propose GIFT, an importance-aware finetuning method for diffusion language models, where tokens are assigned different importance weights based on their entropy. Derived from diffusion theory, GIFT delivers substantial gains: across diverse settings including different mainstream training datasets ranging from 1k to 10k in size, utilizing LoRA or full parameter fine-tuning, and training on base or instruct models, GIFT consistently achieves superior overall performance compared to standard SFT on four widely used reasoning benchmarks (Sudoku, Countdown, GSM8K, and MATH-500).

## Metadata
- venue: arXiv
- year: 2025
- authors: Guowei Xu, Wenxin Xu, Jiawang Zhao, Kaisheng Ma
- arxiv_id: 2509.20863
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2509.20863v2
- published: 2025-09-25

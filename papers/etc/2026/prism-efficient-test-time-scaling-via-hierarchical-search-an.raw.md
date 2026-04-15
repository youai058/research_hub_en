---
title: "Prism: Efficient Test-Time Scaling via Hierarchical Search and Self-Verification for Discrete Diffusion Language Models"
authors: ["Jinbin Bai", "Yixuan Li", "Yuchen Zhu", "Yi Xin", "Qingyu Shi", "Aosong Feng", "Xiaohong Liu", "Molei Tao", "Jianru Xue", "Xiangtai Li", "Ming-Hsuan Yang"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.01842"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.01842v2"
published: "2026-02-02"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:05+09:00"
---

# Prism: Efficient Test-Time Scaling via Hierarchical Search and Self-Verification for Discrete Diffusion Language Models

## Abstract
Inference-time compute has re-emerged as a practical way to improve LLM reasoning. Most test-time scaling (TTS) algorithms rely on autoregressive decoding, which is ill-suited to discrete diffusion language models (dLLMs) due to their parallel decoding over the entire sequence. As a result, developing effective and efficient TTS methods to unlock dLLMs' full generative potential remains an underexplored challenge. To address this, we propose Prism (Pruning, Remasking, and Integrated Self-verification Method), an efficient TTS framework for dLLMs that (i) performs Hierarchical Trajectory Search (HTS) which dynamically prunes and reallocates compute in an early-to-mid denoising window, (ii) introduces Local branching with partial remasking to explore diverse implementations while preserving high-confidence tokens, and (iii) replaces external verifiers with Self-Verified Feedback (SVF) obtained via self-evaluation prompts on intermediate completions. Across four mathematical reasoning and code generation benchmarks on three dLLMs, including LLaDA 8B Instruct, Dream 7B Instruct, and LLaDA 2.0-mini, our Prism achieves a favorable performance-efficiency trade-off, matching best-of-N performance with substantially fewer function evaluations (NFE). The code is released at https://github.com/viiika/Prism.

## Metadata
- venue: arXiv
- year: 2026
- authors: Jinbin Bai, Yixuan Li, Yuchen Zhu, Yi Xin, Qingyu Shi, Aosong Feng, Xiaohong Liu, Molei Tao, Jianru Xue, Xiangtai Li, Ming-Hsuan Yang
- arxiv_id: 2602.01842
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.01842v2
- published: 2026-02-02

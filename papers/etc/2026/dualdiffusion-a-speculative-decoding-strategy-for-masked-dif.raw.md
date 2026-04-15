---
title: "DualDiffusion: A Speculative Decoding Strategy for Masked Diffusion Models"
authors: ["Satyam Goyal", "Kushal Patel", "Tanush Mittal", "Arjun Laxman"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2604.05250"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2604.05250v1"
published: "2026-04-06"
categories: ["cs.LG", "cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:13:54+09:00"
---

# DualDiffusion: A Speculative Decoding Strategy for Masked Diffusion Models

## Abstract
Masked Diffusion Models (MDMs) offer a promising alternative to autoregressive language models by enabling parallel token generation and bidirectional context modeling. However, their inference speed is significantly limited by the inability to cache key-value pairs due to bidirectional attention, requiring $O(N^2)$ computations at each generation step. While recent methods like FastDLLM and DkvCache improve inference speed through attention approximations and caching strategies, they achieve speedups at the cost of generation quality. We propose DualDiffusion, a speculative decoding framework for MDMs that combines fast drafter models (using efficient approximations) with slower, more accurate verifier models. By running multiple steps of a lightweight drafter followed by a single verification step, DualDiffusion achieves a superior Pareto frontier between generation steps and accuracy compared to existing approaches. We evaluate our method on MMLU and GSM8K, demonstrating that DualDiffusion maintains high accuracy while reducing the number of generation steps required, effectively pushing the quality-efficiency trade-off curve for masked diffusion language models.

## Metadata
- venue: arXiv
- year: 2026
- authors: Satyam Goyal, Kushal Patel, Tanush Mittal, Arjun Laxman
- arxiv_id: 2604.05250
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2604.05250v1
- published: 2026-04-06

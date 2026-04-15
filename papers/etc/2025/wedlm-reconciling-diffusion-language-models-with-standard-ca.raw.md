---
title: "WeDLM: Reconciling Diffusion Language Models with Standard Causal Attention for Fast Inference"
authors: ["Aiwei Liu", "Minghua He", "Shaoxun Zeng", "Sijun Zhang", "Linhao Zhang", "Chuhan Wu", "Wei Jia", "Yuan Liu", "Xiao Zhou", "Jie Zhou"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2512.22737"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2512.22737v1"
published: "2025-12-28"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:03+09:00"
---

# WeDLM: Reconciling Diffusion Language Models with Standard Causal Attention for Fast Inference

## Abstract
Autoregressive (AR) generation is the standard decoding paradigm for Large Language Models (LLMs), but its token-by-token nature limits parallelism at inference time. Diffusion Language Models (DLLMs) offer parallel decoding by recovering multiple masked tokens per step; however, in practice they often fail to translate this parallelism into deployment speed gains over optimized AR engines (e.g., vLLM). A key reason is that many DLLMs rely on bidirectional attention, which breaks standard prefix KV caching and forces repeated contextualization, undermining efficiency. We propose WeDLM, a diffusion decoding framework built entirely on standard causal attention to make parallel generation prefix-cache friendly. The core idea is to let each masked position condition on all currently observed tokens while keeping a strict causal mask, achieved by Topological Reordering that moves observed tokens to the physical prefix while preserving their logical positions. Building on this property, we introduce a streaming decoding procedure that continuously commits confident tokens into a growing left-to-right prefix and maintains a fixed parallel workload, avoiding the stop-and-wait behavior common in block diffusion methods. Experiments show that WeDLM preserves the quality of strong AR backbones while delivering substantial speedups, approaching 3x on challenging reasoning benchmarks and up to 10x in low-entropy generation regimes; critically, our comparisons are against AR baselines served by vLLM under matched deployment settings, demonstrating that diffusion-style decoding can outperform an optimized AR engine in practice.

## Metadata
- venue: arXiv
- year: 2025
- authors: Aiwei Liu, Minghua He, Shaoxun Zeng, Sijun Zhang, Linhao Zhang, Chuhan Wu, Wei Jia, Yuan Liu, Xiao Zhou, Jie Zhou
- arxiv_id: 2512.22737
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2512.22737v1
- published: 2025-12-28

---
title: "Efficient Low Rank Attention for Long-Context Inference in Large Language Models"
authors: ["Li Tenghui", "Guoxu Zhou", "Xuyang ZHAO", "Yuning Qiu", "Qibin Zhao"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Mc0eJHZhW5"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/782a279950afb7a019653682ea8ce33984f7b7c4.pdf"
published: "2025"
categories: []
keywords: ["LLM", "KV cache", "Low rank decomposition", "Long context inference"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:50+09:00"
---

# Efficient Low Rank Attention for Long-Context Inference in Large Language Models

## Abstract
As the length of input text increases, the key-value (KV) cache in LLMs imposes prohibitive GPU memory costs and limits long-context inference on resource constrained devices.
  Existing approaches, such as KV quantization and pruning, reduce memory usage but suffer from numerical precision loss or suboptimal retention of key-value pairs.
  In this work, Low Rank Query and Key attention (LRQK) is introduced, a two-stage framework that jointly decomposes full-precision query and key matrices into compact rank-\(r\) factors during the prefill stage, and then employs these low-dimensional projections to compute proxy attention scores in \(\mathcal{O}(lr)\) time at each decode step.
  By selecting only the top-\(k\) tokens and a small fixed set of recent tokens, LRQK employs a mixed GPU-CPU cache with a hit-and-miss mechanism where only missing full-precision KV pairs are transferred, thereby preserving exact attention outputs while reducing CPU-GPU data movement.
  Extensive experiments on the RULER and LongBench benchmarks with LLaMA-3-8B and Qwen2.5-7B demonstrate that LRQK matches or surpasses leading sparse-attention methods in long context settings, while delivering significant memory savings with minimal accuracy loss. Our code is available at \url{https://github.com/tenghuilee/LRQK}.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Li Tenghui, Guoxu Zhou, Xuyang ZHAO, Yuning Qiu, Qibin Zhao
- arxiv_id: 
- openreview_id: Mc0eJHZhW5
- anthology_id: 
- pdf_url: https://openreview.net/pdf/782a279950afb7a019653682ea8ce33984f7b7c4.pdf
- published: 2025
- keywords: LLM, KV cache, Low rank decomposition, Long context inference

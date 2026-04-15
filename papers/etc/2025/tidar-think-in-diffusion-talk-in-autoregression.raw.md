---
title: "TiDAR: Think in Diffusion, Talk in Autoregression"
authors: ["Jingyu Liu", "Xin Dong", "Zhifan Ye", "Rishabh Mehta", "Yonggan Fu", "Vartika Singh", "Jan Kautz", "Ce Zhang", "Pavlo Molchanov"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2511.08923"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2511.08923v1"
published: "2025-11-12"
categories: ["cs.CL", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:06+09:00"
---

# TiDAR: Think in Diffusion, Talk in Autoregression

## Abstract
Diffusion language models hold the promise of fast parallel generation, while autoregressive (AR) models typically excel in quality due to their causal structure aligning naturally with language modeling. This raises a fundamental question: can we achieve a synergy with high throughput, higher GPU utilization, and AR level quality? Existing methods fail to effectively balance these two aspects, either prioritizing AR using a weaker model for sequential drafting (speculative decoding), leading to lower drafting efficiency, or using some form of left-to-right (AR-like) decoding logic for diffusion, which still suffers from quality degradation and forfeits its potential parallelizability. We introduce TiDAR, a sequence-level hybrid architecture that drafts tokens (Thinking) in Diffusion and samples final outputs (Talking) AutoRegressively - all within a single forward pass using specially designed structured attention masks. This design exploits the free GPU compute density, achieving a strong balance between drafting and verification capacity. Moreover, TiDAR is designed to be serving-friendly (low overhead) as a standalone model. We extensively evaluate TiDAR against AR models, speculative decoding, and diffusion variants across generative and likelihood tasks at 1.5B and 8B scales. Thanks to the parallel drafting and sampling as well as exact KV cache support, TiDAR outperforms speculative decoding in measured throughput and surpasses diffusion models like Dream and Llada in both efficiency and quality. Most notably, TiDAR is the first architecture to close the quality gap with AR models while delivering 4.71x to 5.91x more tokens per second.

## Metadata
- venue: arXiv
- year: 2025
- authors: Jingyu Liu, Xin Dong, Zhifan Ye, Rishabh Mehta, Yonggan Fu, Vartika Singh, Jan Kautz, Ce Zhang, Pavlo Molchanov
- arxiv_id: 2511.08923
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2511.08923v1
- published: 2025-11-12

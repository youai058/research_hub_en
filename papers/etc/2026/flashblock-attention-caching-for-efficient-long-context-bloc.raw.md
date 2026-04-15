---
title: "FlashBlock: Attention Caching for Efficient Long-Context Block Diffusion"
authors: ["Zhuokun Chen", "Jianfei Cai", "Bohan Zhuang"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.05305"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.05305v2"
published: "2026-02-05"
categories: ["cs.CV", "cs.AI", "cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:05+09:00"
---

# FlashBlock: Attention Caching for Efficient Long-Context Block Diffusion

## Abstract
Generating long-form content, such as minute-long videos and extended texts, is increasingly important for modern generative models. Block diffusion improves inference efficiency via KV caching and block-wise causal inference and has been widely adopted in diffusion language models and video generation. However, in long-context settings, block diffusion still incurs substantial overhead from repeatedly computing attention over a growing KV cache. We identify an underexplored property of block diffusion: cross-step redundancy of attention within a block. Our analysis shows that attention outputs from tokens outside the current block remain largely stable across diffusion steps, while block-internal attention varies significantly. Based on this observation, we propose FlashBlock, a cached block-external attention mechanism that reuses stable attention output, reducing attention computation and KV cache access without modifying the diffusion process. Moreover, FlashBlock is orthogonal to sparse attention and can be combined as a complementary residual reuse strategy, substantially improving model accuracy under aggressive sparsification. Experiments on diffusion language models and video generation demonstrate up to 1.44$\times$ higher token throughput and up to 1.6$\times$ reduction in attention time, with negligible impact on generation quality. Project page: https://caesarhhh.github.io/FlashBlock/.

## Metadata
- venue: arXiv
- year: 2026
- authors: Zhuokun Chen, Jianfei Cai, Bohan Zhuang
- arxiv_id: 2602.05305
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.05305v2
- published: 2026-02-05

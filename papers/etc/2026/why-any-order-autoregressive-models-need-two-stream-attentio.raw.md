---
title: "Why Any-Order Autoregressive Models Need Two-Stream Attention: A Structural-Semantic Tradeoff"
authors: ["Patrick Pynadath", "Ruqi Zhang"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.16092"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.16092v1"
published: "2026-02-17"
categories: ["cs.LG", "cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:13+09:00"
---

# Why Any-Order Autoregressive Models Need Two-Stream Attention: A Structural-Semantic Tradeoff

## Abstract
Any-order autoregressive models (AO-ARMs) offer a promising path toward efficient masked diffusion by enabling native key-value caching, but competitive performance has so far required two-stream attention, typically motivated as a means of decoupling token content from position. In this work, we argue that two-stream attention may be serving a more subtle role. We identify a structural-semantic tradeoff in any-order generation: the hidden representation at each step must simultaneously attend to semantically informative tokens for prediction and structurally recent tokens for summarization, objectives that compete for attention capacity in a single stream but can specialize across two streams. To isolate this tradeoff from position-content separation, we propose Decoupled RoPE, a modification to rotary position embeddings that provides target position information without revealing target content. Decoupled RoPE performs competitively at short sequence lengths--where semantic and structural proximity coincide--but degrades as sequence length increases and the two orderings diverge. These results suggest that the success of two-stream attention stems not merely from separating position from content, but from circumventing the deeper structural-semantic tradeoff inherent to any-order generation.

## Metadata
- venue: arXiv
- year: 2026
- authors: Patrick Pynadath, Ruqi Zhang
- arxiv_id: 2602.16092
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.16092v1
- published: 2026-02-17

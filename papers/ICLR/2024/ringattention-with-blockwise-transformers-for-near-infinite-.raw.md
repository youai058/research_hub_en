---
title: "RingAttention with Blockwise Transformers for Near-Infinite Context"
authors: ["Hao Liu", "Matei Zaharia", "Pieter Abbeel"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "WsRHpHH4s0"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/46002918e58387fc0091aa342ec23ebe66fd93e4.pdf"
published: "2024"
categories: []
keywords: ["Language Model", "Large Context", "Transformers", "Long Context Model", "Memory Efficiency"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:58+09:00"
---

# RingAttention with Blockwise Transformers for Near-Infinite Context

## Abstract
Transformers have emerged as the architecture of choice for many state-of-the-art AI models, showcasing exceptional performance across a wide range of AI applications. However, the memory demands imposed by Transformers limit their ability to handle long sequences, thereby posing challenges in utilizing videos, actions, and other long-form sequences and modalities in complex environments. We present a novel approach, Blockwise RingAttention, which leverages blockwise computation of self-attention and feedforward to distribute long sequences across multiple devices while fully overlapping the communication of key-value blocks with the computation of blockwise attention. Our approach enables training and inference of sequences that are up to device count times longer than those achievable by prior memory-efficient Transformers, without resorting to approximations or incurring additional communication and computation overheads. Extensive experiments on language modeling and reinforcement learning tasks demonstrate the effectiveness of our approach in allowing millions of tokens context size and improving performance.

## Metadata
- venue: ICLR
- year: 2024
- authors: Hao Liu, Matei Zaharia, Pieter Abbeel
- arxiv_id: 
- openreview_id: WsRHpHH4s0
- anthology_id: 
- pdf_url: https://openreview.net/pdf/46002918e58387fc0091aa342ec23ebe66fd93e4.pdf
- published: 2024
- keywords: Language Model, Large Context, Transformers, Long Context Model, Memory Efficiency

---
title: "MagicDec: Breaking the Latency-Throughput Tradeoff for Long Context Generation with Speculative Decoding"
authors: ["Ranajoy Sadhukhan", "Jian Chen", "Zhuoming Chen", "Vashisth Tiwari", "Ruihang Lai", "Jinyuan Shi", "Ian En-Hsu Yen", "Avner May", "Tianqi Chen", "Beidi Chen"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "CS2JWaziYr"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ba6206117da0d8213b79a6a7a6dcc3cb6ec01dc6.pdf"
published: "2025"
categories: []
keywords: ["LLM Inference", "Speculative Decoding", "Performance Analysis"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:07+09:00"
---

# MagicDec: Breaking the Latency-Throughput Tradeoff for Long Context Generation with Speculative Decoding

## Abstract
Large Language Models (LLMs) have become more prevalent in long-context applications such as interactive chatbots, document analysis, and agent workflows, but it is challenging to serve long-context requests with low latency and high throughput. Speculative decoding (SD) is a widely used technique to reduce latency losslessly, but the conventional wisdom suggests that its efficacy is limited to small batch sizes. In MagicDec, we show that surprisingly SD can achieve speedup even for a high throughput inference regime for moderate to long sequences. More interestingly, an intelligent drafting strategy can achieve better speedup with increasing batch size based on our rigorous analysis. MagicDec first identifies the bottleneck shifts with increasing batch size and sequence length, and uses these insights to deploy SD more effectively for high throughput inference. We leverage draft model with sparse KV cache to address the KV bottleneck, which scales with both sequence length and batch size. Additionally, we propose a theoretical model to select the optimal drafting strategy for maximum speedup. Our work highlights the broad applicability of speculative decoding in long-context serving, as it can enhance throughput and reduce latency without compromising accuracy. For moderate to long sequences, we demonstrate up to 2.51x speedup for LLaMA-3.1-8B when serving batch sizes ranging from 32 to 256 on various types of hardware and tasks.

## Metadata
- venue: ICLR
- year: 2025
- authors: Ranajoy Sadhukhan, Jian Chen, Zhuoming Chen, Vashisth Tiwari, Ruihang Lai, Jinyuan Shi, Ian En-Hsu Yen, Avner May, Tianqi Chen, Beidi Chen
- arxiv_id: 
- openreview_id: CS2JWaziYr
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ba6206117da0d8213b79a6a7a6dcc3cb6ec01dc6.pdf
- published: 2025
- keywords: LLM Inference, Speculative Decoding, Performance Analysis

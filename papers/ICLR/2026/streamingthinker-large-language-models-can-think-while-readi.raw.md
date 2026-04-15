---
title: "StreamingThinker: Large Language Models Can Think While Reading"
authors: ["Junlong Tong", "Yingqi Fan", "Anhao Zhao", "Yunpu Ma", "Xiaoyu Shen"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "10Iiew095e"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/35e34cbd0b6604edc449bbbcd1e7c7d7d11d7f8d.pdf"
published: "2026"
categories: []
keywords: ["LLMs", "Reasoning", "Streaming"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:19+09:00"
---

# StreamingThinker: Large Language Models Can Think While Reading

## Abstract
Large language models (LLMs) have demonstrated remarkable capabilities in chain of thought (CoT) reasoning. However, the current LLM reasoning paradigm initiates thinking only after the entire input is available, which introduces unnecessary latency and weakens attention to earlier information in dynamic scenarios. Inspired by human cognition of thinking while reading, we first design a **streaming thinking** paradigm for LLMs, where reasoning unfolds in the order of input and further adjusts its depth once reading is complete. 
We instantiate this paradigm with *StreamingThinker*, a framework that enables LLMs to think while reading through the integration of streaming CoT generation, streaming-constraint training, and streaming parallel inference.
Specifically, StreamingThinker employs streaming reasoning units with quality control for CoT generation, enforces order-preserving reasoning through streaming attention masks and position encoding, and leverages parallel KV caches that decouple input encoding from reasoning generation, thereby ensuring alignment and enabling true concurrency. We evaluate StreamingThinker on the Qwen3 model family across math reasoning, logical reasoning, and context-based QA reasoning tasks. 
Experimental results show that the StreamingThinker preserves performance comparable to batch thinking, while yielding an 80\% reduction in token waiting before the onset of reasoning and a more than 60\% reduction in time-level latency for producing the final answer, demonstrating the effectiveness of the streaming paradigm for LLM reasoning.
Code is publicly available at [this repository](https://github.com/EIT-NLP/StreamingLLM/tree/main/StreamingThinker).

## Metadata
- venue: ICLR
- year: 2026
- authors: Junlong Tong, Yingqi Fan, Anhao Zhao, Yunpu Ma, Xiaoyu Shen
- arxiv_id: 
- openreview_id: 10Iiew095e
- anthology_id: 
- pdf_url: https://openreview.net/pdf/35e34cbd0b6604edc449bbbcd1e7c7d7d11d7f8d.pdf
- published: 2026
- keywords: LLMs, Reasoning, Streaming

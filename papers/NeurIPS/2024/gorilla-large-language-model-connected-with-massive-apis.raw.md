---
title: "Gorilla: Large Language Model Connected with Massive APIs"
authors: ["Shishir G Patil", "Tianjun Zhang", "Xin Wang", "Joseph E. Gonzalez"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "tBRNC6YemY"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/18a6a0d15f2abb68c940776e23e520a6e0894c93.pdf"
published: "2024"
categories: []
keywords: ["LLM", "Tool Use", "APIs", "Function Calling"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:30+09:00"
---

# Gorilla: Large Language Model Connected with Massive APIs

## Abstract
Large Language Models (LLMs) have seen an impressive wave of advances, with
models now excelling in a variety of tasks, such as mathematical reasoning and
program synthesis. However, their potential to effectively use tools via API calls
remains unfulfilled. This is a challenging task even for today’s state-of-the-art
LLMs such as GPT-4 largely due to their unawareness of what APIs are available
and how to use them in a frequently updated tool set. We develop Gorilla, a
finetuned LLaMA model that surpasses the performance of GPT-4 on writing API
calls. Trained with the novel Retriever Aware Training (RAT), when combined
with a document retriever, Gorilla demonstrates a strong capability to adapt to
test-time document changes, allowing flexible user updates or version changes.
It also substantially mitigates the issue of hallucination, commonly encountered
when prompting LLMs directly. To evaluate the model’s ability, we introduce
APIBench, a comprehensive dataset consisting of HuggingFace, TorchHub, and
TensorHub APIs. The successful integration of the retrieval system with Gorilla
demonstrates the potential for LLMs to use tools more accurately, keep up with
frequently updated documentation, and consequently increase the reliability and
applicability of their outputs. Gorilla’s code, model, data, and demo are available
at: https://gorilla.cs.berkeley.edu

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Shishir G Patil, Tianjun Zhang, Xin Wang, Joseph E. Gonzalez
- arxiv_id: 
- openreview_id: tBRNC6YemY
- anthology_id: 
- pdf_url: https://openreview.net/pdf/18a6a0d15f2abb68c940776e23e520a6e0894c93.pdf
- published: 2024
- keywords: LLM, Tool Use, APIs, Function Calling

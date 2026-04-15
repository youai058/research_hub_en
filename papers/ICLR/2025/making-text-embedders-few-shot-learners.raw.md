---
title: "Making Text Embedders Few-Shot Learners"
authors: ["Chaofan Li", "Minghao Qin", "Shitao Xiao", "Jianlyu Chen", "Kun Luo", "Defu Lian", "Yingxia Shao", "Zheng Liu"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "wfLuiDjQ0u"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e5da7c368734ad33d198e1c8c7ad11d86fdc531d.pdf"
published: "2025"
categories: []
keywords: ["large language model", "embedding model", "in-context learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:02+09:00"
---

# Making Text Embedders Few-Shot Learners

## Abstract
Large language models (LLMs) with decoder-only architectures have demonstrated exceptional text-generation capabilities across a variety of tasks. Some researchers have also adapted these models for text representation tasks. However, in text representation tasks, these models often face performance degradation on unseen tasks. In-context learning (ICL), which leverages examples provided in the input context, enables LLMs to handle unseen tasks effectively. Inspired by this, we aim to fully utilize the inherent properties of LLMs to enhance text representation performance across different tasks through the ICL approach.

In this paper, we introduce a simple yet effective training strategy, which significantly improves text representation capabilities. Unlike previous models that prepend task instructions to the text, our method randomly samples a varying number of examples during training, endowing the embedding model with in-context learning abilities while maintaining its zero-shot capabilities. This approach does not require additional data construction or modifications to the model architecture. On the contrary, we find that some popular modifications to the model, such as bidirectional attention, can degrade performance, undermining the inherent characteristics of LLMs. We have publicly released our method at this \href{https://github.com/FlagOpen/FlagEmbedding}{repo}.

## Metadata
- venue: ICLR
- year: 2025
- authors: Chaofan Li, Minghao Qin, Shitao Xiao, Jianlyu Chen, Kun Luo, Defu Lian, Yingxia Shao, Zheng Liu
- arxiv_id: 
- openreview_id: wfLuiDjQ0u
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e5da7c368734ad33d198e1c8c7ad11d86fdc531d.pdf
- published: 2025
- keywords: large language model, embedding model, in-context learning

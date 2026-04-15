---
title: "Q-RAG: Long Context Multi‑Step Retrieval via Value‑Based Embedder Training"
authors: ["Artyom Sorokin", "Nazar Buzun", "Aleksandr Anokhin", "Egor KONSTANTINOVICH VEDERNIKOV", "Petr Anokhin", "Mikhail Burtsev", "Evgeny Burnaev"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "MS9nWFY7LG"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/4949b625d7a7f3fa5138bd6098f1328306e019f6.pdf"
published: "2026"
categories: []
keywords: ["Reinforcement Learning", "RL", "QA", "Long-context", "RAG", "NLP"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:16+09:00"
---

# Q-RAG: Long Context Multi‑Step Retrieval via Value‑Based Embedder Training

## Abstract
Retrieval-Augmented Generation (RAG) methods enhance LLM performance by efficiently filtering relevant context for LLMs, reducing hallucinations and inference cost.
However, most existing RAG methods focus on single-step retrieval, which is often insufficient for answering complex questions that require multi-step search.
Recently, multi-step retrieval approaches have emerged, typically involving the fine-tuning of small LLMs to perform multi-step retrieval.
This type of fine-tuning is highly resource-intensive and does not enable the use of larger LLMs.
In this work, we propose Q-RAG, a novel approach that fine-tunes the Embedder model for multi-step retrieval using reinforcement learning (RL).
Q-RAG offers a competitive, resource-efficient alternative to existing multi-step retrieval methods for open-domain question answering and achieves state-of-the-art results on the popular long-context benchmarks BabiLong and RULER for contexts up to 10M tokens. Code is available at: https://github.com/griver/Q-RAG.

## Metadata
- venue: ICLR
- year: 2026
- authors: Artyom Sorokin, Nazar Buzun, Aleksandr Anokhin, Egor KONSTANTINOVICH VEDERNIKOV, Petr Anokhin, Mikhail Burtsev, Evgeny Burnaev
- arxiv_id: 
- openreview_id: MS9nWFY7LG
- anthology_id: 
- pdf_url: https://openreview.net/pdf/4949b625d7a7f3fa5138bd6098f1328306e019f6.pdf
- published: 2026
- keywords: Reinforcement Learning, RL, QA, Long-context, RAG, NLP

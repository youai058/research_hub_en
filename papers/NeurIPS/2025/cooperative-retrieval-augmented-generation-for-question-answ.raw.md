---
title: "Cooperative Retrieval-Augmented Generation for Question Answering: Mutual Information Exchange and Ranking by Contrasting Layers"
authors: ["Youmin Ko", "Sung Jong Seo", "Hyunjoon Kim"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "D2XdJf1tXW"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/52ab19e0ce1e465d8756bd720c363a39a11a8fb5.pdf"
published: "2025"
categories: []
keywords: ["retieval-augmented generation", "RAG", "multi-hop question answering", "contrasting layers", "question augmentation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:58+09:00"
---

# Cooperative Retrieval-Augmented Generation for Question Answering: Mutual Information Exchange and Ranking by Contrasting Layers

## Abstract
Since large language models (LLMs) have a tendency to generate factually inaccurate output, retrieval-augmented generation (RAG) has gained significant attention as a key means to mitigate this downside of harnessing only LLMs. However, existing RAG methods for simple and multi-hop question answering (QA) are still prone to incorrect retrievals and hallucinations. To address these limitations, we propose CoopRAG, a novel RAG framework for the question answering task in which a retriever and an LLM work cooperatively with each other by exchanging informative knowledge, and the earlier and later layers of the retriever model work cooperatively with each other to accurately rank the retrieved documents relevant to a given query. In this framework, we (i) unroll a question into sub-questions and a reasoning chain in which uncertain positions are masked, (ii) retrieve the documents relevant to the question augmented with the sub-questions and the reasoning chain, (iii) rerank the documents by contrasting layers of the retriever, and (iv) reconstruct the reasoning chain by filling the masked positions via the LLM. Our experiments demonstrate that CoopRAG consistently outperforms state-of-the-art QA methods on three multi-hop QA datasets as well as a simple QA dataset in terms of both the retrieval and QA performances. Our code is available.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Youmin Ko, Sung Jong Seo, Hyunjoon Kim
- arxiv_id: 
- openreview_id: D2XdJf1tXW
- anthology_id: 
- pdf_url: https://openreview.net/pdf/52ab19e0ce1e465d8756bd720c363a39a11a8fb5.pdf
- published: 2025
- keywords: retieval-augmented generation, RAG, multi-hop question answering, contrasting layers, question augmentation

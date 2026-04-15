---
title: "RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval"
authors: ["Parth Sarthi", "Salman Abdullah", "Aditi Tuli", "Shubh Khanna", "Anna Goldie", "Christopher D Manning"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "GN921JHCRw"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/1414c23eb8af2e30daa25a4f53471f69091f48d9.pdf"
published: "2024"
categories: []
keywords: ["Retrieval Augmented Language Models", "Information Retrieval", "summarization", "QA"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:57+09:00"
---

# RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval

## Abstract
Retrieval-augmented language models can better adapt to changes in world state and incorporate long-tail knowledge.  However, most existing methods retrieve only short contiguous chunks from a retrieval corpus, limiting holistic understanding of the overall document context. We introduce the novel approach of recursively embedding, clustering, and summarizing chunks of text, constructing a tree with differing levels of summarization from the bottom up. At inference time, our RAPTOR model retrieves from this tree, integrating information across lengthy documents at different levels of abstraction. Controlled experiments show that retrieval with recursive summaries offers significant improvements over traditional retrieval-augmented LMs on several tasks. On question-answering tasks that involve complex, multi-step reasoning, we show state-of-the-art results; for example, by coupling RAPTOR retrieval with the use of GPT-4, we can improve the best performance on the QuALITY benchmark by 20\% in absolute accuracy.

## Metadata
- venue: ICLR
- year: 2024
- authors: Parth Sarthi, Salman Abdullah, Aditi Tuli, Shubh Khanna, Anna Goldie, Christopher D Manning
- arxiv_id: 
- openreview_id: GN921JHCRw
- anthology_id: 
- pdf_url: https://openreview.net/pdf/1414c23eb8af2e30daa25a4f53471f69091f48d9.pdf
- published: 2024
- keywords: Retrieval Augmented Language Models, Information Retrieval, summarization, QA

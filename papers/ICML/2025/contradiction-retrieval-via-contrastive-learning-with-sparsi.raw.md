---
title: "Contradiction Retrieval via Contrastive Learning with Sparsity"
authors: ["Haike Xu", "Zongyu Lin", "Kai-Wei Chang", "Yizhou Sun", "Piotr Indyk"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "VzFXb6Au58"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ed0974ca9442b6019e91bebac9ef96cc8566a19f.pdf"
published: "2025"
categories: []
keywords: ["contradiction retrieval", "sentence embedding"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:40+09:00"
---

# Contradiction Retrieval via Contrastive Learning with Sparsity

## Abstract
Contradiction retrieval refers to identifying and extracting documents that explicitly disagree with or refute the content of a query, which is important to many downstream applications like fact checking and data cleaning. To retrieve contradiction argument to the query from large document corpora, existing methods such as similarity search and cross-encoder models exhibit different limitations.
To address these challenges, we introduce a novel approach: SparseCL that leverages specially trained sentence embeddings designed to preserve subtle, contradictory nuances between sentences. Our method utilizes a combined metric of cosine similarity and a sparsity function to efficiently identify and retrieve documents that contradict a given query. This approach dramatically enhances the speed of contradiction detection by reducing the need for exhaustive document comparisons to simple vector calculations. 
We conduct contradiction retrieval experiments on Arguana, MSMARCO, and HotpotQA, where our method produces an average improvement of $11.0\%$ across different models. We also validate our method on downstream tasks like natural language inference and cleaning corrupted corpora.
This paper outlines a promising direction for non-similarity-based information retrieval which is currently underexplored.

## Metadata
- venue: ICML
- year: 2025
- authors: Haike Xu, Zongyu Lin, Kai-Wei Chang, Yizhou Sun, Piotr Indyk
- arxiv_id: 
- openreview_id: VzFXb6Au58
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ed0974ca9442b6019e91bebac9ef96cc8566a19f.pdf
- published: 2025
- keywords: contradiction retrieval, sentence embedding

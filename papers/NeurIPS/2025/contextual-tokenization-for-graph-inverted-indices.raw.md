---
title: "Contextual Tokenization for Graph Inverted Indices"
authors: ["Pritish Chakraborty", "Indradyumna Roy", "Soumen Chakrabarti", "Abir De"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "BGwZsFLJFU"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/61f1ee234dff958f6f142cd4a29387bce9c34066.pdf"
published: "2025"
categories: []
keywords: ["graph indexing", "graph retrieval", "graph representation learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:59+09:00"
---

# Contextual Tokenization for Graph Inverted Indices

## Abstract
Retrieving graphs from a large corpus, that contain a subgraph isomorphic to a given query graph, is a core operation in many real-world applications. While recent multi-vector graph representations and scores based on set alignment and containment can provide accurate subgraph isomorphism tests, their use in retrieval remains limited by their need to score corpus graphs exhaustively.
We introduce CoRGII (COntextual Representation of Graphs for Inverted Indexing), a graph indexing framework in which, starting with a contextual dense graph representation, a differentiable discretization module computes sparse binary codes over a learned latent vocabulary. This text document-like representation allows us to leverage classic, highly optimized inverted indexes, while supporting soft (vector) set containment scores. Improving on this paradigm further, we replace the classical impact score of a `word' on a graph (such as defined by TFIDF or BM25) with a data-driven, trainable impact score.
Crucially, CoRGII is trained end-to-end using only binary relevance labels, without fine-grained supervision of query-to-document set alignments. Extensive experiments show that CoRGII provides better trade-offs between efficiency and accuracy, compared to several baselines.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Pritish Chakraborty, Indradyumna Roy, Soumen Chakrabarti, Abir De
- arxiv_id: 
- openreview_id: BGwZsFLJFU
- anthology_id: 
- pdf_url: https://openreview.net/pdf/61f1ee234dff958f6f142cd4a29387bce9c34066.pdf
- published: 2025
- keywords: graph indexing, graph retrieval, graph representation learning

---
title: "Iteratively Refined Early Interaction Alignment for Subgraph Matching based Graph Retrieval"
authors: ["Ashwin Ramachandran", "Vaibhav Raj", "Indradyumna Roy", "Soumen Chakrabarti", "Abir De"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "udTwwF7tks"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/4ae7afbdb746c97e2bfe511705355b40c1bce0e3.pdf"
published: "2024"
categories: []
keywords: ["Graph Neural Networks", "Graph Retrieval"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:56+09:00"
---

# Iteratively Refined Early Interaction Alignment for Subgraph Matching based Graph Retrieval

## Abstract
Graph retrieval based on subgraph isomorphism has several real-world applications such as scene graph retrieval, molecular fingerprint detection and circuit design. Roy et al. [35] proposed IsoNet, a late interaction model for subgraph matching, which first computes the node and edge embeddings of each graph independently of paired graph  and then computes a trainable alignment map. Here, we present $\texttt{IsoNet++}$, an early interaction graph neural network (GNN), based on several technical innovations. First, we compute embeddings of all nodes by passing messages within and across the two input graphs, guided by an *injective alignment* between their nodes. Second, we update this alignment in a lazy fashion over multiple *rounds*. Within each round, we run a layerwise GNN from scratch, based on the current state of the alignment. After the completion of one round of GNN, we use the last-layer embeddings to update the alignments, and proceed to the next round. Third, $\texttt{IsoNet++}$ incorporates a novel notion of node-pair partner interaction. Traditional early interaction computes attention between a node and its potential partners in the other graph, the attention then controlling messages passed across graphs. We consider *node pairs* (not single nodes) as potential partners. Existence of an edge between the nodes in one graph and non-existence in the other provide vital signals for refining the alignment. Our experiments on several datasets show that the alignments get progressively refined with successive rounds,
resulting in significantly better retrieval performance than existing methods. We demonstrate that all three innovations contribute to the enhanced accuracy. Our code and datasets are publicly available at https://github.com/structlearning/isonetpp.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Ashwin Ramachandran, Vaibhav Raj, Indradyumna Roy, Soumen Chakrabarti, Abir De
- arxiv_id: 
- openreview_id: udTwwF7tks
- anthology_id: 
- pdf_url: https://openreview.net/pdf/4ae7afbdb746c97e2bfe511705355b40c1bce0e3.pdf
- published: 2024
- keywords: Graph Neural Networks, Graph Retrieval

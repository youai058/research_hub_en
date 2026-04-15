---
title: "Uncertainty Estimation for Heterophilic Graphs Through the Lens of Information Theory"
authors: ["Dominik Fuchsgruber", "Tom Wollschläger", "Johannes Bordne", "Stephan Günnemann"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "GDvO6viRCF"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/014bed92f82a4c1a939b8611dd6ecc5c15a45d48.pdf"
published: "2025"
categories: []
keywords: ["Heterophilic Graphs", "Uncertainty Estimation", "Information Theory", "Graph Neural Networks"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:14+09:00"
---

# Uncertainty Estimation for Heterophilic Graphs Through the Lens of Information Theory

## Abstract
While uncertainty estimation for graphs recently gained traction, most methods rely on homophily and deteriorate in heterophilic settings.
    We address this by analyzing message passing neural networks from an information-theoretic perspective and developing a suitable analog to data processing inequality to quantify information throughout the model's layers. In contrast to non-graph domains, information about the node-level prediction target can *increase* with model depth if a node's features are semantically different from its neighbors. 
    Therefore, on heterophilic graphs, the latent embeddings of an MPNN each provide different information about the data distribution - different from homophilic settings.
    This reveals that considering all node representations simultaneously is a key design principle for epistemic uncertainty estimation on graphs beyond homophily. 
    We empirically confirm this with a simple post-hoc density estimator on the joint node embedding space that provides state-of-the-art uncertainty on heterophilic graphs. At the same time, it matches prior work on homophilic graphs without explicitly exploiting homophily through post-processing.

## Metadata
- venue: ICML
- year: 2025
- authors: Dominik Fuchsgruber, Tom Wollschläger, Johannes Bordne, Stephan Günnemann
- arxiv_id: 
- openreview_id: GDvO6viRCF
- anthology_id: 
- pdf_url: https://openreview.net/pdf/014bed92f82a4c1a939b8611dd6ecc5c15a45d48.pdf
- published: 2025
- keywords: Heterophilic Graphs, Uncertainty Estimation, Information Theory, Graph Neural Networks

---
title: "ConceptScope: Characterizing Dataset Bias via Disentangled Visual Concepts"
authors: ["Jinho Choi", "Hyesu Lim", "Steffen Schneider", "Jaegul Choo"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "lkmlNHuzY4"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/031afa843a7942deb1a05f19e02a94e349e2ca8b.pdf"
published: "2025"
categories: []
keywords: ["dataset bias analysis", "vision datasets", "sparse autoencoder"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:49+09:00"
---

# ConceptScope: Characterizing Dataset Bias via Disentangled Visual Concepts

## Abstract
Dataset bias, where data points are skewed to certain concepts, is ubiquitous in machine learning datasets. Yet, systematically identifying these biases is challenging without costly, fine-grained attribute annotations. We present ConceptScope, a scalable and automated framework for analyzing visual datasets by discovering and quantifying human-interpretable concepts using Sparse Autoencoders trained on representations from vision foundation models. ConceptScope categorizes concepts into target, context, and bias types based on their semantic relevance and statistical correlation to class labels, enabling class-level dataset characterization, bias identification, and robustness evaluation through concept-based subgrouping. We validate that ConceptScope captures a wide range of visual concepts, including objects, textures, backgrounds, facial attributes, emotions, and actions, through comparisons with annotated datasets. Furthermore, we show that concept activations produce spatial attributions that align with semantically meaningful image regions. ConceptScope reliably detects known biases (e.g., background bias in Waterbirds) and uncovers previously unannotated ones (e.g, co-occurring objects in ImageNet), offering a practical tool for dataset auditing and model diagnostics.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Jinho Choi, Hyesu Lim, Steffen Schneider, Jaegul Choo
- arxiv_id: 
- openreview_id: lkmlNHuzY4
- anthology_id: 
- pdf_url: https://openreview.net/pdf/031afa843a7942deb1a05f19e02a94e349e2ca8b.pdf
- published: 2025
- keywords: dataset bias analysis, vision datasets, sparse autoencoder

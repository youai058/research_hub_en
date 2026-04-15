---
title: "AutoSciDACT: Automated Scientific Discovery through Contrastive Embedding and Hypothesis Testing"
authors: ["Samuel Bright-Thonney", "Christina Reissel", "Gaia Grosso", "Nathaniel S. Woodward", "Katya Govorkova", "Andrzej Novak", "Sang Eon Park", "Eric A. Moreno", "Philip Harris"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "vKyiv67VWa"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/0b8812d08be89e63ea837f381a9283465beae175.pdf"
published: "2025"
categories: []
keywords: ["anomaly detection", "contrastive learning", "scientific discovery", "hypothesis testing", "automated discovery"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:33+09:00"
---

# AutoSciDACT: Automated Scientific Discovery through Contrastive Embedding and Hypothesis Testing

## Abstract
Novelty detection in large scientific datasets faces two key challenges: the noisy and high-dimensional nature of experimental data,
and the necessity of making *statistically robust* statements about any observed outliers. While there is a wealth of literature on anomaly detection via dimensionality reduction, most methods do not produce outputs compatible with quantifiable claims of scientific discovery. In this work we directly address these challenges, presenting the first step towards a unified pipeline for novelty detection adapted for the rigorous statistical demands of science. We introduce AutoSciDACT (Automated Scientific Discovery with Anomalous Contrastive Testing), a general-purpose pipeline for detecting novelty in scientific data. AutoSciDACT begins by creating expressive low-dimensional data representations using a contrastive pre-training, leveraging the abundance of high-quality simulated data in many scientific domains alongside expertise that can guide principled data augmentation strategies. These compact embeddings then enable an extremely sensitive machine learning-based two-sample test using the New Physics Learning Machine (NPLM) framework, which identifies and statistically quantifies deviations in observed data relative to a reference distribution (null hypothesis). We perform experiments across a range of astronomical, physical, biological, image, and synthetic datasets, demonstrating strong sensitivity to small injections of anomalous data across all domains.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Samuel Bright-Thonney, Christina Reissel, Gaia Grosso, Nathaniel S. Woodward, Katya Govorkova, Andrzej Novak, Sang Eon Park, Eric A. Moreno, Philip Harris
- arxiv_id: 
- openreview_id: vKyiv67VWa
- anthology_id: 
- pdf_url: https://openreview.net/pdf/0b8812d08be89e63ea837f381a9283465beae175.pdf
- published: 2025
- keywords: anomaly detection, contrastive learning, scientific discovery, hypothesis testing, automated discovery

---
title: "From Molecules to Materials: Pre-training Large Generalizable Models for Atomic Property Prediction"
authors: ["Nima Shoghi", "Adeesh Kolluru", "John R. Kitchin", "Zachary Ward Ulissi", "C. Lawrence Zitnick", "Brandon M Wood"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "PfPnugdxup"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/7ae9e4f5f396605dfda891057be51e0ec4e42fdc.pdf"
published: "2024"
categories: []
keywords: ["atomic property prediction", "pre-training", "3D atomic pre-training", "graph neural networks", "multi-task learning", "molecules", "materials"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:13+09:00"
---

# From Molecules to Materials: Pre-training Large Generalizable Models for Atomic Property Prediction

## Abstract
Foundation models have been transformational in machine learning fields such as natural language processing and computer vision. Similar success in atomic property prediction has been limited due to the challenges of training effective models across multiple chemical domains. To address this, we introduce Joint Multi-domain Pre-training (JMP), a supervised pre-training strategy that simultaneously trains on multiple datasets from different chemical domains, treating each dataset as a unique pre-training task within a multi-task framework. Our combined training dataset consists of $\sim$120M systems from OC20, OC22, ANI-1x, and Transition-1x. We evaluate performance and generalization by fine-tuning over a diverse set of downstream tasks and datasets including: QM9, rMD17, MatBench, QMOF, SPICE, and MD22. JMP demonstrates an average improvement of 59% over training from scratch and matches or sets state-of-the-art on 34 out of 40 tasks. Our work highlights the potential of pre-training strategies that utilize diverse data to advance property prediction across chemical domains, especially for low-data tasks.

## Metadata
- venue: ICLR
- year: 2024
- authors: Nima Shoghi, Adeesh Kolluru, John R. Kitchin, Zachary Ward Ulissi, C. Lawrence Zitnick, Brandon M Wood
- arxiv_id: 
- openreview_id: PfPnugdxup
- anthology_id: 
- pdf_url: https://openreview.net/pdf/7ae9e4f5f396605dfda891057be51e0ec4e42fdc.pdf
- published: 2024
- keywords: atomic property prediction, pre-training, 3D atomic pre-training, graph neural networks, multi-task learning, molecules, materials

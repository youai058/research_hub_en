---
title: "Localizing Task Information for Improved Model Merging and Compression"
authors: ["Ke Wang", "Nikolaos Dimitriadis", "Guillermo Ortiz-Jimenez", "François Fleuret", "Pascal Frossard"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "DWT9uiGjxT"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b354980180c7edaedf1349f01e8f51e51a19ddf8.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:40+09:00"
---

# Localizing Task Information for Improved Model Merging and Compression

## Abstract
Model merging and task arithmetic have emerged as promising scalable approaches to merge multiple single-task checkpoints to one multi-task model, but their applicability is reduced by significant performance loss. Previous works have linked these drops to interference in the weight space and erasure of important task-specific features. Instead, in this work we show that the information required to solve each task is still preserved after merging as different tasks mostly use non-overlapping sets of weights. We propose TALL-masks, a method to identify these task supports given a collection of task vectors and show that one can retrieve >99% of the single task accuracy by applying our masks to the multi-task vector, effectively compressing the individual checkpoints. We study the statistics of intersections among constructed masks and reveal the existence of selfish and catastrophic weights, i.e., parameters that are important exclusively to one task and irrelevant to all tasks but detrimental to multi-task fusion. For this reason, we propose Consensus Merging, an algorithm that eliminates such weights and improves the general performance of existing model merging approaches. Our experiments in vision and NLP benchmarks with up to 20 tasks, show that Consensus Merging consistently improves existing approaches. Furthermore, our proposed compression scheme reduces storage from 57Gb to 8.2Gb while retaining 99.7% of original performance.

## Metadata
- venue: ICML
- year: 2024
- authors: Ke Wang, Nikolaos Dimitriadis, Guillermo Ortiz-Jimenez, François Fleuret, Pascal Frossard
- arxiv_id: 
- openreview_id: DWT9uiGjxT
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b354980180c7edaedf1349f01e8f51e51a19ddf8.pdf
- published: 2024

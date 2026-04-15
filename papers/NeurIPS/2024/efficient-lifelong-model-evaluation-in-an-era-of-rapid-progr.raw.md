---
title: "Efficient Lifelong Model Evaluation in an Era of Rapid Progress"
authors: ["Ameya Prabhu", "Vishaal Udandarao", "Philip Torr", "Matthias Bethge", "Adel Bibi", "Samuel Albanie"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "A7wC1CTkYl"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/4c073a0e1ca042d15ebcc71c4c43019c782d60a5.pdf"
published: "2024"
categories: []
keywords: ["benchmarking", "efficient model evaluation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:56+09:00"
---

# Efficient Lifelong Model Evaluation in an Era of Rapid Progress

## Abstract
Standardized benchmarks drive progress in machine learning. However, with repeated testing, the risk of overfitting grows as algorithms over-exploit benchmark idiosyncrasies. In our work, we seek to mitigate this challenge by compiling \textit{ever-expanding} large-scale benchmarks called \textit{Lifelong Benchmarks}. As exemplars of our approach, we create \textit{Lifelong-CIFAR10} and \textit{Lifelong-ImageNet}, containing (for now) 1.69M and 1.98M test samples, respectively. While reducing overfitting, lifelong benchmarks introduce a key challenge: the high cost of evaluating a growing number of models across an ever-expanding sample set. To address this challenge, we also introduce an efficient evaluation framework: \textit{Sort \& Search (S\&S)}, which reuses previously evaluated models by leveraging dynamic programming algorithms to selectively rank and sub-select test samples, enabling cost-effective lifelong benchmarking. Extensive empirical evaluations across $\sim$31,000 models demonstrate that \textit{S\&S} achieves highly-efficient approximate accuracy measurement, reducing compute cost from 180 GPU days to 5 GPU hours ($\sim$1000x reduction) on a single A100 GPU, with low approximation error. As such, lifelong benchmarks offer a robust, practical solution to the ``benchmark exhaustion'' problem.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Ameya Prabhu, Vishaal Udandarao, Philip Torr, Matthias Bethge, Adel Bibi, Samuel Albanie
- arxiv_id: 
- openreview_id: A7wC1CTkYl
- anthology_id: 
- pdf_url: https://openreview.net/pdf/4c073a0e1ca042d15ebcc71c4c43019c782d60a5.pdf
- published: 2024
- keywords: benchmarking, efficient model evaluation

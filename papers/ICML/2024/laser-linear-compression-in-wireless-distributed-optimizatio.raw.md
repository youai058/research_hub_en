---
title: "LASER: Linear Compression in Wireless Distributed Optimization"
authors: ["Ashok Vardhan Makkuva", "Marco Bondaschi", "Thijs Vogels", "Martin Jaggi", "Hyeji Kim", "Michael Gastpar"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "sDjszMb2Ir"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/214486b51cbe39e9a4cd9c2f5f9ca6d16d9d4588.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:43+09:00"
---

# LASER: Linear Compression in Wireless Distributed Optimization

## Abstract
Data-parallel SGD is the de facto algorithm for distributed optimization, especially for large scale machine learning. Despite its merits, communication bottleneck is one of its persistent issues. Most compression schemes to alleviate this either assume noiseless communication links, or fail to achieve good performance on practical tasks. In this paper, we close this gap and introduce **LASER**: **L**ine**A**r Compre**S**sion in Wir**E**less Dist**R**ibuted Optimization. LASER capitalizes on the inherent low-rank structure of gradients and transmits them efficiently over the noisy channels. Whilst enjoying theoretical guarantees similar to those of the classical SGD, LASER shows consistent gains over baselines on a variety of practical benchmarks. In particular, it outperforms the state-of-the-art compression schemes on challenging computer vision and GPT language modeling tasks. On the latter, we obtain 50-64% improvement in perplexity over our baselines for noisy channels.

## Metadata
- venue: ICML
- year: 2024
- authors: Ashok Vardhan Makkuva, Marco Bondaschi, Thijs Vogels, Martin Jaggi, Hyeji Kim, Michael Gastpar
- arxiv_id: 
- openreview_id: sDjszMb2Ir
- anthology_id: 
- pdf_url: https://openreview.net/pdf/214486b51cbe39e9a4cd9c2f5f9ca6d16d9d4588.pdf
- published: 2024

---
title: "HM3: Hierarchical Multi-Objective Model Merging for Pretrained Models"
authors: ["Yu Zhou", "Xingyu Wu", "Jibin Wu", "Liang Feng", "KC Tan"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "JeP0lpusYw"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/4458c41d6973c01afd92fa290015347f767d7d67.pdf"
published: "2025"
categories: []
keywords: ["Large language model", "model merging", "multi-objective optimization", "architecture-level merging"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:23+09:00"
---

# HM3: Hierarchical Multi-Objective Model Merging for Pretrained Models

## Abstract
Model merging is a technique that combines multiple large pretrained models into a single model, enhancing performance and broadening task adaptability without original data or additional training. However, most existing model merging methods focus primarily on exploring the parameter space, merging models with identical architectures. Despite its potential, merging in the architecture space remains in its early stages due to the vast search space and challenges related to layer compatibility. This paper designs a hierarchical model merging framework named HM3, formulating a bilevel multi-objective model merging problem across both parameter and architecture spaces. At the parameter level, HM3 integrates existing merging methods to quickly identify optimal parameters. Based on these, an actor-critic strategy with efficient policy discretization is employed at the architecture level to explore inference paths with Markov property in the layer-granularity search space for reconstructing these optimal models. By training reusable policy and value networks, HM3 learns Pareto optimal models to provide customized solutions for various tasks. Experimental results on language and vision tasks demonstrate that HM3 outperforms methods focusing solely on the parameter or architecture space.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Yu Zhou, Xingyu Wu, Jibin Wu, Liang Feng, KC Tan
- arxiv_id: 
- openreview_id: JeP0lpusYw
- anthology_id: 
- pdf_url: https://openreview.net/pdf/4458c41d6973c01afd92fa290015347f767d7d67.pdf
- published: 2025
- keywords: Large language model, model merging, multi-objective optimization, architecture-level merging

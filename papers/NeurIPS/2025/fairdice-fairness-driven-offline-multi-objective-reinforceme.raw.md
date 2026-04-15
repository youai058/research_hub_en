---
title: "FairDICE: Fairness-Driven Offline Multi-Objective Reinforcement Learning"
authors: ["Woosung Kim", "Jinho Lee", "Jongmin Lee", "Byung-Jun Lee"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "2jQJ7aNdT1"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b62361877b7ed975af86bc908351cb1621fa0471.pdf"
published: "2025"
categories: []
keywords: ["Offline Reinforcement Learning", "Multi-objective Reinforcement Learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:46+09:00"
---

# FairDICE: Fairness-Driven Offline Multi-Objective Reinforcement Learning

## Abstract
Multi-objective reinforcement learning (MORL) aims to optimize policies in the presence of conflicting objectives, where linear scalarization is commonly used to reduce vector-valued returns into scalar signals. While effective for certain preferences, this approach cannot capture fairness-oriented goals such as Nash social welfare or max-min fairness, which require nonlinear and non-additive trade-offs. Although several online algorithms have been proposed for specific fairness objectives, a unified approach for optimizing nonlinear welfare criteria in the offline setting—where learning must proceed from a fixed dataset—remains unexplored. In this work, we present FairDICE, the first offline MORL framework that directly optimizes nonlinear welfare objective. FairDICE leverages distribution correction estimation to jointly account for welfare maximization and distributional regularization, enabling stable and sample-efficient learning without requiring explicit preference weights or exhaustive weight search. Across multiple offline benchmarks, FairDICE demonstrates strong fairness-aware performance compared to existing baselines.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Woosung Kim, Jinho Lee, Jongmin Lee, Byung-Jun Lee
- arxiv_id: 
- openreview_id: 2jQJ7aNdT1
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b62361877b7ed975af86bc908351cb1621fa0471.pdf
- published: 2025
- keywords: Offline Reinforcement Learning, Multi-objective Reinforcement Learning

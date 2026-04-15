---
title: "Towards AutoAI: Optimizing a Machine Learning System with Black-box and Differentiable Components"
authors: ["Zhiliang Chen", "Chuan-Sheng Foo", "Bryan Kian Hsiang Low"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "JVhUR8q27o"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/02e9356d41b0c047326ed912cc069bf9b62349f1.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:46+09:00"
---

# Towards AutoAI: Optimizing a Machine Learning System with Black-box and Differentiable Components

## Abstract
*Machine learning* (ML) models in the real world typically do not exist in isolation. They are usually part of a complex system (e.g., healthcare systems, self-driving cars) containing multiple ML and *black-box* components. The problem of optimizing such systems, which we refer to as *automated AI* (AutoAI), requires us to *jointly* train all ML components together and presents a significant challenge because the number of system parameters is extremely high and the system has no analytical form. To circumvent this, we introduce a novel algorithm called A-BAD-BO which uses each ML component's local loss as an auxiliary indicator for system performance. A-BAD-BO uses *Bayesian optimization* (BO) to optimize the local loss configuration of a system in a smaller dimensional space and exploits the differentiable structure of ML components to recover optimal system parameters from the optimized configuration. We show A-BAD-BO converges to optimal system parameters by showing that it is *asymptotically no regret*. We use A-BAD-BO to optimize several synthetic and real-world complex systems, including a prompt engineering pipeline for *large language models* containing millions of system parameters. Our results demonstrate that A-BAD-BO yields better system optimality than gradient-driven baselines and is more sample-efficient than pure BO algorithms.

## Metadata
- venue: ICML
- year: 2024
- authors: Zhiliang Chen, Chuan-Sheng Foo, Bryan Kian Hsiang Low
- arxiv_id: 
- openreview_id: JVhUR8q27o
- anthology_id: 
- pdf_url: https://openreview.net/pdf/02e9356d41b0c047326ed912cc069bf9b62349f1.pdf
- published: 2024

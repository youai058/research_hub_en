---
title: "AceSearcher: Bootstrapping Reasoning and Search for LLMs via Reinforced Self-Play"
authors: ["Ran Xu", "Yuchen Zhuang", "Zihan Dong", "Ruiyu Wang", "Yue Yu", "Joyce C. Ho", "Linjun Zhang", "Haoyu Wang", "Wenqi Shi", "Carl Yang"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "jSgCM0uZn3"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d73f4b0dc08ba840cfc15d8e7e9be6ad4a9b52ce.pdf"
published: "2025"
categories: []
keywords: ["large language model", "retrieval augmented generation", "self-play"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:42+09:00"
---

# AceSearcher: Bootstrapping Reasoning and Search for LLMs via Reinforced Self-Play

## Abstract
Search-augmented LLMs often struggle with complex reasoning tasks due to ineffective multi-hop retrieval and limited reasoning ability. We propose AceSearcher, a cooperative self-play framework that trains a single large language model (LLM) to alternate between two roles: a decomposer that breaks down complex queries and a solver that integrates retrieved contexts for answer generation. AceSearcher couples supervised fine-tuning on a diverse mixture of search, reasoning, and decomposition tasks with reinforcement fine-tuning optimized for final answer accuracy, eliminating the need for intermediate annotations. Extensive experiments on three reasoning-intensive tasks across 10 datasets show that AceSearcher outperforms state-of-the-art baselines, achieving an average exact match improvement of 7.6%. Remarkably, on document-level finance reasoning tasks, AceSearcher-32B matches the performance of the giant DeepSeek-V3 model using less than 5% of iits parameters. Even at smaller scales (1.5B and 8B), AceSearcher often surpasses existing search-augmented LLMs with up to 9× more parameters, highlighting its exceptional efficiency and effectiveness in tackling complex reasoning tasks.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Ran Xu, Yuchen Zhuang, Zihan Dong, Ruiyu Wang, Yue Yu, Joyce C. Ho, Linjun Zhang, Haoyu Wang, Wenqi Shi, Carl Yang
- arxiv_id: 
- openreview_id: jSgCM0uZn3
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d73f4b0dc08ba840cfc15d8e7e9be6ad4a9b52ce.pdf
- published: 2025
- keywords: large language model, retrieval augmented generation, self-play

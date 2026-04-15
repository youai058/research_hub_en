---
title: "Router-R1: Teaching LLMs Multi-Round Routing and Aggregation via Reinforcement Learning"
authors: ["Haozhen Zhang", "Tao Feng", "Jiaxuan You"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "DWf4vroKWJ"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/363710ed9012131f837da723473810ad47f9d2c9.pdf"
published: "2025"
categories: []
keywords: ["Large Language Models", "LLM Routers", "LLM Selection", "Reinforcement Learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:23+09:00"
---

# Router-R1: Teaching LLMs Multi-Round Routing and Aggregation via Reinforcement Learning

## Abstract
The rapid emergence of diverse large language models (LLMs) has spurred the development of LLM routers that assign user queries to the most suitable model. However, existing LLM routers typically perform a single-round, one-to-one mapping (\textit{i.e.}, assigning each query to a single model in isolation), which limits their capability to tackle complex tasks that demand the complementary strengths of multiple LLMs. In this paper, we present \textbf{Router-R1}, a reinforcement learning (RL)-based framework that formulates multi-LLM routing and aggregation as a sequential decision process. Router-R1 instantiates the router itself as a capable LLM, leveraging its reasoning ability to interleave "think" actions (internal deliberation) with "route" actions (dynamic model invocation), and integrates each response into its evolving context. To facilitate learning, we employ a lightweight rule-based reward comprising format rewards, final outcome rewards, and a novel cost reward for optimizing the balance between performance and cost, opening a pathway toward enhancing performance-cost trade-offs via RL. Router-R1 also conditions only on simple model descriptors such as pricing, latency, and example performance, enabling strong generalization to unseen model selection. Experiments on seven general and multi-hop QA benchmarks show that Router-R1 outperforms several strong baselines, achieving superior performance while maintaining robust generalization and cost management.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Haozhen Zhang, Tao Feng, Jiaxuan You
- arxiv_id: 
- openreview_id: DWf4vroKWJ
- anthology_id: 
- pdf_url: https://openreview.net/pdf/363710ed9012131f837da723473810ad47f9d2c9.pdf
- published: 2025
- keywords: Large Language Models, LLM Routers, LLM Selection, Reinforcement Learning

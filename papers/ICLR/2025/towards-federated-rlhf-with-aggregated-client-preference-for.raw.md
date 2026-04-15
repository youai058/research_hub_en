---
title: "Towards Federated RLHF with Aggregated Client Preference for LLMs"
authors: ["Feijie Wu", "Xiaoze Liu", "Haoyu Wang", "Xingchen Wang", "Lu Su", "Jing Gao"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "mqNKiEB6pd"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/43bfb8d07097f707f1e2264cf0784d02c7cceabb.pdf"
published: "2025"
categories: []
keywords: ["Federated learning", "RLHF", "LLM"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:15+09:00"
---

# Towards Federated RLHF with Aggregated Client Preference for LLMs

## Abstract
Reinforcement learning with human feedback (RLHF) fine-tunes a pretrained large language model (LLM) using user preference data, enabling it to generate content aligned with human preferences. However, due to privacy concerns, users may be reluctant to share sensitive preference data. To address this, we propose utilizing Federated Learning (FL) techniques, allowing large-scale preference collection from diverse real-world users without requiring them to transmit data to a central server. Our federated RLHF methods (i.e., FedBis and FedBiscuit) encode each client’s preferences into binary selectors and aggregate them to capture common preferences. In particular, FedBiscuit overcomes key challenges, such as preference heterogeneity and reward hacking, through innovative solutions like grouping clients with similar preferences to reduce heterogeneity and using multiple binary selectors to enhance LLM output quality. To evaluate the performance of the proposed methods, we establish the first federated RLHF benchmark with a heterogeneous human preference dataset. Experimental results show that by integrating the LLM with aggregated client preferences, FedBis and FedBiscuit significantly enhance the professionalism and readability of the generated content.

## Metadata
- venue: ICLR
- year: 2025
- authors: Feijie Wu, Xiaoze Liu, Haoyu Wang, Xingchen Wang, Lu Su, Jing Gao
- arxiv_id: 
- openreview_id: mqNKiEB6pd
- anthology_id: 
- pdf_url: https://openreview.net/pdf/43bfb8d07097f707f1e2264cf0784d02c7cceabb.pdf
- published: 2025
- keywords: Federated learning, RLHF, LLM

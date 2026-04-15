---
title: "Synatra: Turning Indirect Knowledge into Direct Demonstrations for Digital Agents at Scale"
authors: ["Tianyue Ou", "Frank F. Xu", "Aman Madaan", "Jiarui Liu", "Robert Lo", "Abishek Sridhar", "Sudipta Sengupta", "Dan Roth", "Graham Neubig", "Shuyan Zhou"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "KjNEzWRIqn"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e7cd1a1be77aba5525dc023f829368207511d686.pdf"
published: "2024"
categories: []
keywords: ["AI agents", "sythetic data", "web navigation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:32+09:00"
---

# Synatra: Turning Indirect Knowledge into Direct Demonstrations for Digital Agents at Scale

## Abstract
LLMs can now act as autonomous agents that interact with digital environments and complete specific objectives (e.g., arranging an online meeting). However, accuracy is still far from satisfactory, partly due to a lack of large-scale, direct demonstrations for digital tasks. Obtaining supervised data from humans is costly, and automatic data collection through exploration or reinforcement learning relies on complex environmental and content setup, resulting in datasets that lack comprehensive coverage of various scenarios. On the other hand, there is abundant knowledge that may indirectly assist task completion, such as online tutorials that were created for human consumption. In this work, we present Synatra, an approach that effectively transforms this indirect knowledge into direct supervision at scale. We define different types of indirect knowledge, and carefully study the available sources to obtain it, methods to encode the structure of direct demonstrations, and finally methods to transform indirect knowledge into direct demonstrations. We use 100k such synthetically-created demonstrations to finetune a 7B CodeLlama, and demonstrate that the resulting agent surpasses all comparably sized models on three web-based task benchmarks Mind2Web, MiniWoB++ and WebArena, as well as surpassing GPT-3.5 on WebArena and Mind2Web. In addition, while synthetic demonstrations prove to be only 3% the cost of human demonstrations (at $0.031 each), we show that the synthetic demonstrations can be more effective than an identical number of human demonstrations collected from limited domains.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Tianyue Ou, Frank F. Xu, Aman Madaan, Jiarui Liu, Robert Lo, Abishek Sridhar, Sudipta Sengupta, Dan Roth, Graham Neubig, Shuyan Zhou
- arxiv_id: 
- openreview_id: KjNEzWRIqn
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e7cd1a1be77aba5525dc023f829368207511d686.pdf
- published: 2024
- keywords: AI agents, sythetic data, web navigation

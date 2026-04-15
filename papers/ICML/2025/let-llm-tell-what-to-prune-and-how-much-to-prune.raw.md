---
title: "Let LLM Tell What to Prune and How Much to Prune"
authors: ["Mingzhe Yang", "Sihao Lin", "Changlin Li", "Xiaojun Chang"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "zFR5aWGaUs"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ec436360da168c9bfab411f3a542a84423341d9b.pdf"
published: "2025"
categories: []
keywords: ["large language models", "model compression", "network pruning", "structured pruning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:09+09:00"
---

# Let LLM Tell What to Prune and How Much to Prune

## Abstract
Large language models (LLMs) have revolutionized various AI applications. However, their billions of parameters pose significant challenges for practical deployment. Structured pruning is a hardware-friendly compression technique and receives widespread attention. Nonetheless, existing literature typically targets a single structure of LLMs. We observe that the structure units of LLMs differ in terms of inference cost and functionality. Therefore, pruning a single structure unit in isolation often results in an imbalance between performance and efficiency. In addition, previous works mainly employ a prescribed pruning ratio. Since the significance of LLM modules may vary, it is ideal to distribute the pruning load to a specific structure unit according to its role within LLMs. To address the two issues, we propose a pruning method that targets multiple LLM modules with dynamic pruning ratios. Specifically, we find the intrinsic properties of LLMs can guide us to determine the importance of each module and thus distribute the pruning load on demand, i.e., what to prune and how much to prune. This is achieved by quantifying the complex interactions within LLMs. Extensive experiments on multiple benchmarks and LLM variants demonstrate that our method effectively balances the trade-off between efficiency and performance.

## Metadata
- venue: ICML
- year: 2025
- authors: Mingzhe Yang, Sihao Lin, Changlin Li, Xiaojun Chang
- arxiv_id: 
- openreview_id: zFR5aWGaUs
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ec436360da168c9bfab411f3a542a84423341d9b.pdf
- published: 2025
- keywords: large language models, model compression, network pruning, structured pruning

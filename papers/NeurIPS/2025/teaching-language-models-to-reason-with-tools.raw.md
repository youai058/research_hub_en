---
title: "Teaching Language Models to Reason with Tools"
authors: ["Chengpeng Li", "Zhengyang Tang", "Ziniu Li", "Mingfeng Xue", "Keqin Bao", "Tian Ding", "Ruoyu Sun", "Benyou Wang", "Xiang Wang", "Junyang Lin", "Dayiheng Liu"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "kRZVz1qEqa"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/406d2cc67059647e62684368005578debbc188e9.pdf"
published: "2025"
categories: []
keywords: ["Tool-integrated Reasoning", "Large Reasoning Model", "Long Chain-of-Thought"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:33+09:00"
---

# Teaching Language Models to Reason with Tools

## Abstract
Large reasoning models (LRMs) like OpenAI-o1 have shown impressive capabilities in natural language reasoning. However, these models frequently demonstrate inefficiencies or inaccuracies when tackling complex mathematical operations. While integrating computational tools such as Code Interpreters (CIs) offers a promising solution, it introduces a critical challenge: a conflict between the model's internal, probabilistic reasoning and the external, deterministic knowledge provided by the CI, which often leads models to unproductive deliberation. To overcome this, we introduce CoRT (Code-Optimized Reasoning Training), a  post-training framework designed to teach LRMs to effectively utilize CIs. We propose **Hint-Engineering**, a new data synthesis strategy that strategically injects diverse hints at optimal points within reasoning paths. This approach generates high-quality, code-integrated reasoning data specifically tailored to optimize LRM-CI interaction. Using this method, we have synthesized 30 high-quality samples to post-train models ranging from 1.5B to 32B parameters through supervised fine-tuning. CoRT further refines the multi-round interleaving of external CI usage and internal thinking by employing rejection sampling and reinforcement learning. Our experimental evaluations demonstrate CoRT's effectiveness, yielding absolute improvements of 4\% and 8\% on DeepSeek-R1-Distill-Qwen-32B and DeepSeek-R1-Distill-Qwen-1.5B, respectively, across five challenging mathematical reasoning datasets. Moreover, CoRT significantly enhances efficiency, reducing token usage by approximately 30\% for the 32B model and 50\% for the 1.5B model compared to pure natural language reasoning baselines. The models and code are available at: [this url](https://github.com/ChengpengLi1003/CoRT).

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Chengpeng Li, Zhengyang Tang, Ziniu Li, Mingfeng Xue, Keqin Bao, Tian Ding, Ruoyu Sun, Benyou Wang, Xiang Wang, Junyang Lin, Dayiheng Liu
- arxiv_id: 
- openreview_id: kRZVz1qEqa
- anthology_id: 
- pdf_url: https://openreview.net/pdf/406d2cc67059647e62684368005578debbc188e9.pdf
- published: 2025
- keywords: Tool-integrated Reasoning, Large Reasoning Model, Long Chain-of-Thought

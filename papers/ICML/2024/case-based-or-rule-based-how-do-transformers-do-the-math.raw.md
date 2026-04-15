---
title: "Case-Based or Rule-Based: How Do Transformers Do the Math?"
authors: ["Yi Hu", "Xiaojuan Tang", "Haotong Yang", "Muhan Zhang"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "4Vqr8SRfyX"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/755611d26c3c291bd83e25b66971e74d6d96d48f.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:49+09:00"
---

# Case-Based or Rule-Based: How Do Transformers Do the Math?

## Abstract
Despite the impressive performance in a variety of complex tasks, modern large language models (LLMs) still have trouble dealing with some math problems that are simple and intuitive for humans, such as addition. While we can easily learn basic *rules* of addition and apply them to new problems of any length, LLMs struggle to do the same. Instead, they may rely on similar *cases* seen in the training corpus for help. We define these two different reasoning mechanisms as "*rule-based reasoning*" and "*case-based reasoning*". Since rule-based reasoning is essential for acquiring systematic generalization ability, we aim to explore exactly whether transformers use rule-based or case-based reasoning for math problems. Through carefully designed intervention experiments on five math tasks, we confirm that transformers are performing case-based reasoning, no matter whether scratchpad is used, which aligns with the previous observations that transformers use subgraph matching/shortcut learning to reason. To mitigate such problems, we propose a Rule-Following Fine-Tuning (RFFT) technique to teach transformers to perform rule-based reasoning. Specifically, we provide explicit rules in the input and then instruct transformers to recite and follow the rules step by step. Through RFFT, we successfully enable LLMs fine-tuned on 1-5 digit addition to generalize to up to 12-digit addition with over 95% accuracy, which is over 40% higher than scratchpad. The significant improvement demonstrates that teaching LLMs to use rules explicitly helps them learn rule-based reasoning and generalize better in length. Code is available at https://github.com/GraphPKU/Case_or_Rule.

## Metadata
- venue: ICML
- year: 2024
- authors: Yi Hu, Xiaojuan Tang, Haotong Yang, Muhan Zhang
- arxiv_id: 
- openreview_id: 4Vqr8SRfyX
- anthology_id: 
- pdf_url: https://openreview.net/pdf/755611d26c3c291bd83e25b66971e74d6d96d48f.pdf
- published: 2024

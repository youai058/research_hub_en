---
title: "NextCoder: Robust Adaptation of Code LMs to Diverse Code Edits"
authors: ["Tushar Aggarwal", "Swayam Singh", "Abhijeet Awasthi", "Aditya Kanade", "Nagarajan Natarajan"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "3B6fF1PxYD"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e4c45e8d4642143f7bff681474b7ce9634b0db2d.pdf"
published: "2025"
categories: []
keywords: ["Code-LMs", "code-editing", "code-generation", "software engineering"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:33+09:00"
---

# NextCoder: Robust Adaptation of Code LMs to Diverse Code Edits

## Abstract
Software engineering activities frequently involve edits to existing code. However, contemporary code language models (LMs) lack the ability to handle diverse types of code-edit requirements. In this work, we attempt to overcome this shortcoming through (1) a novel synthetic data generation pipeline and (2) a robust model adaptation algorithm. Starting with seed code examples and diverse editing criteria, our pipeline generates high-quality samples comprising original and modified code, along with natural language instructions in different styles and verbosity. Today's code LMs come bundled with strong abilities, such as code generation and instruction following, which should not be lost due to fine-tuning. To ensure this, we propose a novel adaptation algorithm, SeleKT, that (a) leverages a dense gradient-based step to identify the weights that are most important for code editing, and (b) does a sparse projection onto the base model to avoid overfitting. Using our approach, we obtain a new series of models NextCoder (adapted from QwenCoder-2.5) that achieves strong results on five code-editing benchmarks, outperforming comparable size models and even several larger ones. We show the generality of our approach on two model families DeepSeekCoder and QwenCoder), compare against other fine-tuning approaches, and demonstrate robustness by showing retention of code generation and general problem-solving abilities post adaptation. We opensource the models, synthetic dataset, and implementation at http://aka.ms/nextcoder.

## Metadata
- venue: ICML
- year: 2025
- authors: Tushar Aggarwal, Swayam Singh, Abhijeet Awasthi, Aditya Kanade, Nagarajan Natarajan
- arxiv_id: 
- openreview_id: 3B6fF1PxYD
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e4c45e8d4642143f7bff681474b7ce9634b0db2d.pdf
- published: 2025
- keywords: Code-LMs, code-editing, code-generation, software engineering

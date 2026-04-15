---
title: "Scaling Code-Assisted Chain-of-Thoughts and Instructions for Model Reasoning"
authors: ["Honglin Lin", "Qizhi Pei", "Zhuoshi Pan", "Yu Li", "Xin Gao", "Juntao Li", "Conghui He", "Lijun Wu"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "b7bOWd3kUL"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b5f91855f5922ea89b810ed1560821c78f774fff.pdf"
published: "2025"
categories: []
keywords: ["Data Synthesis", "Reasoning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:48+09:00"
---

# Scaling Code-Assisted Chain-of-Thoughts and Instructions for Model Reasoning

## Abstract
Reasoning capability is pivotal for Large Language Models (LLMs) to solve complex tasks, yet achieving reliable and scalable reasoning remains challenging. While Chain-of-Thought (CoT) prompting has become a mainstream approach, existing methods often suffer from uncontrolled generation, insufficient quality, and limited diversity in reasoning paths. 
Recent efforts leverage code to enhance CoT by grounding reasoning in executable steps, but such methods are typically constrained to predefined mathematical problems, hindering scalability and generalizability. 
In this work, we propose \texttt{Caco} (Code-Assisted Chain-of-ThOught), a novel framework that automates the synthesis of high-quality, verifiable, and diverse instruction-CoT reasoning data through code-driven augmentation. Unlike prior work, \texttt{Caco} first fine-tunes a code-based CoT generator on existing math and programming solutions in a unified code format, then scales the data generation to a large amount of diverse reasoning traces. Crucially, we introduce automated validation via code execution and rule-based filtering to ensure logical correctness and structural diversity, followed by reverse-engineering filtered outputs into natural language instructions and language CoTs to enrich task adaptability. This closed-loop process enables fully automated, scalable synthesis of reasoning data with guaranteed executability. 
Experiments on our created \texttt{Caco}-1.3M dataset demonstrate that \texttt{Caco}-trained models achieve strong competitive performance on mathematical reasoning benchmarks, outperforming existing strong baselines. Further analysis reveals that \texttt{Caco}’s code-anchored verification and instruction diversity contribute to superior generalization across unseen tasks. Our work establishes a paradigm for building self-sustaining, trustworthy reasoning systems without human intervention.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Honglin Lin, Qizhi Pei, Zhuoshi Pan, Yu Li, Xin Gao, Juntao Li, Conghui He, Lijun Wu
- arxiv_id: 
- openreview_id: b7bOWd3kUL
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b5f91855f5922ea89b810ed1560821c78f774fff.pdf
- published: 2025
- keywords: Data Synthesis, Reasoning

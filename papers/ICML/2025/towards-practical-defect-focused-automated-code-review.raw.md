---
title: "Towards Practical Defect-Focused Automated Code Review"
authors: ["Junyi Lu", "Lili Jiang", "Xiaojia Li", "Jianbing Fang", "Fengjun Zhang", "Li Yang", "Chun Zuo"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "mEV0nvHcK3"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c198440dd692c073594a0d054f776d664f20590b.pdf"
published: "2025"
categories: []
keywords: ["Automated Code Review", "Merge Request Analysis", "Large Language Models (LLMs)", "Defect Detection", "Evaluation Metrics for Code Review", "Code Context Extraction", "Multi-Agent LLM Collaboration"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:03+09:00"
---

# Towards Practical Defect-Focused Automated Code Review

## Abstract
The complexity of code reviews has driven efforts to automate review comments, but prior approaches oversimplify this task by treating it as snippet-level code-to-text generation and relying on text similarity metrics like BLEU for evaluation. These methods overlook repository context, real-world merge request evaluation, and defect detection, limiting their practicality. To address these issues, we explore the full automation pipeline within the online recommendation service of a company with nearly 400 million daily active users, analyzing industry-grade C++ codebases comprising hundreds of thousands of lines of code. We identify four key challenges: 1) capturing relevant context, 2) improving key bug inclusion (KBI), 3) reducing false alarm rates (FAR), and 4) integrating human workflows. To tackle these, we propose 1) code slicing algorithms for context extraction, 2) a multi-role LLM framework for KBI, 3) a filtering mechanism for FAR reduction, and 4) a novel prompt design for better human interaction. Our approach, validated on real-world merge requests from historical fault reports, achieves a 2× improvement over standard LLMs and a 10× gain over previous baselines. While the presented results focus on C++, the underlying framework design leverages language-agnostic principles (e.g., AST-based analysis), suggesting potential for broader applicability.

## Metadata
- venue: ICML
- year: 2025
- authors: Junyi Lu, Lili Jiang, Xiaojia Li, Jianbing Fang, Fengjun Zhang, Li Yang, Chun Zuo
- arxiv_id: 
- openreview_id: mEV0nvHcK3
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c198440dd692c073594a0d054f776d664f20590b.pdf
- published: 2025
- keywords: Automated Code Review, Merge Request Analysis, Large Language Models (LLMs), Defect Detection, Evaluation Metrics for Code Review, Code Context Extraction, Multi-Agent LLM Collaboration

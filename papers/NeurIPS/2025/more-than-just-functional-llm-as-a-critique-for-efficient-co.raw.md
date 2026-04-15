---
title: "More Than Just Functional: LLM-as-a-Critique for Efficient Code Generation"
authors: ["Derui Zhu", "Dingfan Chen", "jinfu chen", "Jens Grossklags", "Walter Pretschner", "Weiyi Shang"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "0Zri6HSYaK"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/078f13992647a4da32aeb346041206919cbc6ee0.pdf"
published: "2025"
categories: []
keywords: ["Code Generation", "Performance", "Software Engineering", "AI4SE"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:52+09:00"
---

# More Than Just Functional: LLM-as-a-Critique for Efficient Code Generation

## Abstract
Large language models (LLMs) have demonstrated remarkable progress in generating functional code, leading to numerous AI-based coding program tools. However, their reliance on the perplexity objective during both training and inference primarily emphasizes functionality, often at the expense of efficiency—an essential consideration for real-world coding tasks. Perhaps interestingly, we observed that well-trained LLMs inherently possess knowledge about code efficiency, but this potential remains underutilized with standard decoding approaches. To address this, we design strategic prompts to activate the model’s embedded efficiency understanding, effectively using LLMs as \textit{efficiency critiques} to guide code generation toward higher efficiency without sacrificing—and sometimes even improving—functionality, all without the need for costly real code execution. Extensive experiments on benchmark datasets (EffiBench, HumanEval+) across multiple representative code models demonstrate up to a 70.6\% reduction in average execution time and a 13.6\% decrease in maximum memory usage, highlighting the computational efficiency and practicality of our approach compared to existing alternatives.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Derui Zhu, Dingfan Chen, jinfu chen, Jens Grossklags, Walter Pretschner, Weiyi Shang
- arxiv_id: 
- openreview_id: 0Zri6HSYaK
- anthology_id: 
- pdf_url: https://openreview.net/pdf/078f13992647a4da32aeb346041206919cbc6ee0.pdf
- published: 2025
- keywords: Code Generation, Performance, Software Engineering, AI4SE

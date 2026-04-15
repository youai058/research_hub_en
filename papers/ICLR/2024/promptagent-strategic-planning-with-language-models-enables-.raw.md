---
title: "PromptAgent: Strategic Planning with Language Models Enables Expert-level Prompt Optimization"
authors: ["Xinyuan Wang", "Chenxi Li", "Zhen Wang", "Fan Bai", "Haotian Luo", "Jiayou Zhang", "Nebojsa Jojic", "Eric Xing", "Zhiting Hu"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "22pyNMuIoa"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d4dbdee0d105cd3020bffdc2f56d99c33429d49c.pdf"
published: "2024"
categories: []
keywords: ["Large Language Models", "Expert-level Prompt Optimization", "Strategic Planning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:06+09:00"
---

# PromptAgent: Strategic Planning with Language Models Enables Expert-level Prompt Optimization

## Abstract
Expert-level prompts, carefully engineered by human experts who have a deep understanding of both large language models (LLMs) and domain knowledge, are the future of prompting and pivotal to harnessing the full power of advanced LLMs. Discovering such prompts with an automated process remains a sought-after and unresolved challenge. Existing prompt optimization techniques, though automated through iterative sampling, often fall short in injecting domain knowledge and exploring the vast prompt space for complex expert-level prompts efficiently. To address this pressing need and achieve expert-level prompting, we introduce PromptAgent, which autonomously discovers prompts equivalent in quality to those handcrafted by experts. At its core, PromptAgent views prompt optimization as a strategic planning problem and employs a principled planning algorithm (rooted in Monte Carlo Tree Search) to strategically explore the vast expert-level prompt space. PromptAgent interacts with the LLM in a human-like trial-and-error manner during the planning, and injects expert-level knowledge by reflecting on model errors and generating insightful error feedback. This novel formulation allows it to iteratively evaluate intermediate prompts, refine them based on errors, simulate future rewards, and search for high-reward paths leading to expert-level prompts. We apply PromptAgent to 12 tasks spanning three practical domains: BIG-Bench Hard (BBH), domain-expert, and general NLU tasks, showing PromptAgent consistently outperforms strong prompting and prompt optimization baselines by great margins. Our qualitative analysis further emphasizes PromptAgent's capability to distill insightful errors into expert-level prompts.

## Metadata
- venue: ICLR
- year: 2024
- authors: Xinyuan Wang, Chenxi Li, Zhen Wang, Fan Bai, Haotian Luo, Jiayou Zhang, Nebojsa Jojic, Eric Xing, Zhiting Hu
- arxiv_id: 
- openreview_id: 22pyNMuIoa
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d4dbdee0d105cd3020bffdc2f56d99c33429d49c.pdf
- published: 2024
- keywords: Large Language Models, Expert-level Prompt Optimization, Strategic Planning

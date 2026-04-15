---
title: "GuardAgent: Safeguard LLM Agents via Knowledge-Enabled Reasoning"
authors: ["Zhen Xiang", "Linzhi Zheng", "Yanjie Li", "Junyuan Hong", "Qinbin Li", "Han Xie", "Jiawei Zhang", "Zidi Xiong", "Chulin Xie", "Carl Yang", "Dawn Song", "Bo Li"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "2nBcjCZrrP"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c7b75b02d57a9809d87b82ad16586b4645b560f8.pdf"
published: "2025"
categories: []
keywords: ["agent", "large language model", "guardrail", "reasoning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:36+09:00"
---

# GuardAgent: Safeguard LLM Agents via Knowledge-Enabled Reasoning

## Abstract
The rapid advancement of large language model (LLM) agents has raised new concerns regarding their safety and security. In this paper, we propose GuardAgent, the first guardrail agent to protect target agents by dynamically checking whether their actions satisfy given safety guard requests. Specifically, GuardAgent first analyzes the safety guard requests to generate a task plan, and then maps this plan into guardrail code for execution. By performing the code execution, GuardAgent can deterministically follow the safety guard request and safeguard target agents. In both steps, an LLM is utilized as the reasoning component, supplemented by in-context demonstrations retrieved from a memory module storing experiences from previous tasks. In addition, we propose two novel benchmarks: EICU-AC benchmark to assess the access control for healthcare agents and Mind2Web-SC benchmark to evaluate the safety policies for web agents. We show that GuardAgent effectively moderates the violation actions for different types of agents on these two benchmarks with over 98% and 83%
guardrail accuracies, respectively. Project page: https://guardagent.github.io/

## Metadata
- venue: ICML
- year: 2025
- authors: Zhen Xiang, Linzhi Zheng, Yanjie Li, Junyuan Hong, Qinbin Li, Han Xie, Jiawei Zhang, Zidi Xiong, Chulin Xie, Carl Yang, Dawn Song, Bo Li
- arxiv_id: 
- openreview_id: 2nBcjCZrrP
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c7b75b02d57a9809d87b82ad16586b4645b560f8.pdf
- published: 2025
- keywords: agent, large language model, guardrail, reasoning

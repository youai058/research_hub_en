---
title: "UDora: A Unified Red Teaming Framework against LLM Agents by Dynamically Hijacking Their Own Reasoning"
authors: ["Jiawei Zhang", "Shuang Yang", "Bo Li"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "pRmxQHgjb1"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/1489f884ee66981b358bb3e08dcb5c1b74ebbf4f.pdf"
published: "2025"
categories: []
keywords: ["adversarial attack; llm agent; jailbreak; reasoning and acting"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:25+09:00"
---

# UDora: A Unified Red Teaming Framework against LLM Agents by Dynamically Hijacking Their Own Reasoning

## Abstract
Large Language Model (LLM) agents equipped with external tools have become increasingly powerful for complex tasks such as web shopping, automated email replies, and financial trading. However, these advancements amplify the risks of adversarial attacks, especially when agents can access sensitive external functionalities. Nevertheless, manipulating LLM agents into performing targeted malicious actions or invoking specific tools remains challenging, as these agents extensively reason or plan before executing final actions. In this work, we present UDora, a unified red teaming framework designed for LLM agents that dynamically hijacks the agent's reasoning processes to compel malicious behavior. Specifically, UDora first generates the model’s reasoning trace for the given task, then automatically identifies optimal points within this trace to insert targeted perturbations. The resulting perturbed reasoning is then used as a surrogate response for optimization. By iteratively applying this process, the LLM agent will then be induced to undertake designated malicious actions or to invoke specific malicious tools. Our approach demonstrates superior effectiveness compared to existing methods across three LLM agent datasets. The code is available at https://github.com/AI-secure/UDora.

## Metadata
- venue: ICML
- year: 2025
- authors: Jiawei Zhang, Shuang Yang, Bo Li
- arxiv_id: 
- openreview_id: pRmxQHgjb1
- anthology_id: 
- pdf_url: https://openreview.net/pdf/1489f884ee66981b358bb3e08dcb5c1b74ebbf4f.pdf
- published: 2025
- keywords: adversarial attack; llm agent; jailbreak; reasoning and acting

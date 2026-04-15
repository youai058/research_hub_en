---
title: "Online Preference Alignment for Language Models via Count-based Exploration"
authors: ["Chenjia Bai", "Yang Zhang", "Shuang Qiu", "Qiaosheng Zhang", "Kang Xu", "Xuelong Li"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "cfKZ5VrhXt"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/8027b540bc593a3e5f70c656500980faf0c04edc.pdf"
published: "2025"
categories: []
keywords: ["Reinforcement Learning from Human Feedback", "RLHF", "Preference Alignment", "Exploration", "LLMs"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:03+09:00"
---

# Online Preference Alignment for Language Models via Count-based Exploration

## Abstract
Reinforcement Learning from Human Feedback (RLHF) has shown great potential in fine-tuning Large Language Models (LLMs) to align with human preferences. Existing methods perform preference alignment from a fixed dataset, which can be limited in data coverage and the resulting reward model is hard to generalize in out-of-distribution responses. Thus, online RLHF is more desirable to empower the LLM to explore outside the support of the initial dataset by iteratively collecting the prompt-response pairs. In this paper, we study the fundamental problem in online RLHF, i.e., how to explore for LLM. We give a theoretical motivation in linear reward assumption to show that an optimistic reward with an upper confidence bound (UCB) term leads to a provably efficient RLHF policy. Then, we reformulate our objective to direct preference optimization with an exploration term, where the UCB-term can be converted to a count-based exploration bonus. We further propose a practical algorithm, named Count-based Online Preference Optimization (COPO), which leverages a simple coin-flip counting module to estimate the pseudo-count of a prompt-response pair in previously collected data. COPO encourages LLMs to balance exploration and preference optimization in an iterative manner, which enlarges the exploration space and the entire data coverage of iterative LLM policies. We conduct online RLHF experiments on Zephyr and Llama-3 models. The results on instruction-following and standard academic benchmarks show that COPO significantly increases performance.

## Metadata
- venue: ICLR
- year: 2025
- authors: Chenjia Bai, Yang Zhang, Shuang Qiu, Qiaosheng Zhang, Kang Xu, Xuelong Li
- arxiv_id: 
- openreview_id: cfKZ5VrhXt
- anthology_id: 
- pdf_url: https://openreview.net/pdf/8027b540bc593a3e5f70c656500980faf0c04edc.pdf
- published: 2025
- keywords: Reinforcement Learning from Human Feedback, RLHF, Preference Alignment, Exploration, LLMs

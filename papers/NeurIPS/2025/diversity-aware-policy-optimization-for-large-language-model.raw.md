---
title: "Diversity-Aware Policy Optimization for Large Language Model Reasoning"
authors: ["Jian Yao", "Ran Cheng", "Xingyu Wu", "Jibin Wu", "KC Tan"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "5eZ0iykpDU"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c884fab9a8271939813690f5af1e6cebe20f7a2a.pdf"
published: "2025"
categories: []
keywords: ["LLM", "Policy Optimization", "Diversity"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:50+09:00"
---

# Diversity-Aware Policy Optimization for Large Language Model Reasoning

## Abstract
The reasoning capabilities of large language models (LLMs) have advanced rapidly, particularly following the release of DeepSeek-R1, which has inspired a surge of research into data quality and reinforcement learning (RL) algorithms. Despite the pivotal role diversity plays in RL, its influence on LLM reasoning remains largely underexplored. To bridge this gap, this work presents a systematic investigation into the impact of diversity in RL-based training for LLM reasoning, and proposes a novel diversity-aware policy optimization method. Across evaluations on 12 LLMs, we observe a strong positive correlation between the solution diversity and potential@k (a novel metric quantifying an LLM’s reasoning potential) in high-performing models. This finding motivates our method to explicitly promote diversity during RL training. Specifically,  we design a token-level diversity and reformulate it into a practical objective, then we selectively apply it to positive samples. Integrated into the R1-zero training framework, our method achieves a 3.5\% average improvement across four mathematical reasoning benchmarks, while generating more diverse and robust solutions.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Jian Yao, Ran Cheng, Xingyu Wu, Jibin Wu, KC Tan
- arxiv_id: 
- openreview_id: 5eZ0iykpDU
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c884fab9a8271939813690f5af1e6cebe20f7a2a.pdf
- published: 2025
- keywords: LLM, Policy Optimization, Diversity

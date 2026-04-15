---
title: "LLMs Can Reason Faster Only If We Let Them"
authors: ["Bilgehan Sel", "Lifu Huang", "Naren Ramakrishnan", "Ruoxi Jia", "Ming Jin"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "uTv5rOPZr4"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/5696d031029b6c039954af92740d00424af45508.pdf"
published: "2025"
categories: []
keywords: ["large language models", "decision-making", "planning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:11+09:00"
---

# LLMs Can Reason Faster Only If We Let Them

## Abstract
Large language models (LLMs) are making inroads into classical AI problems such as automated planning, yet key shortcomings continue to hamper their integration. Chain-of-Thought (CoT) struggles in complex multi-step reasoning, and Tree-of-Thoughts requires multiple queries that increase computational overhead. Recently, Algorithm-of-Thoughts (AoT) have shown promise using in-context examples, at the cost of significantly longer solutions compared to CoT.  Aimed at bridging the solution length gap between CoT and AoT, this paper introduces AoT-O3, which combines supervised finetuning on AoT-style plans with a reinforcement learning (RL) framework designed to reduce solution length. The RL component uses a reward model that favors concise, valid solutions  while maintaining planning accuracy. Empirical evaluations indicate that AoT-O3 shortens solution length by up to 80\% compared to baseline AoT while maintaining or surpassing prior performance. These findings suggest a promising pathway for more efficient, scalable LLM-based planning.

## Metadata
- venue: ICML
- year: 2025
- authors: Bilgehan Sel, Lifu Huang, Naren Ramakrishnan, Ruoxi Jia, Ming Jin
- arxiv_id: 
- openreview_id: uTv5rOPZr4
- anthology_id: 
- pdf_url: https://openreview.net/pdf/5696d031029b6c039954af92740d00424af45508.pdf
- published: 2025
- keywords: large language models, decision-making, planning

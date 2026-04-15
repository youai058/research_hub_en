---
title: "Safety-Prioritizing Curricula for Constrained Reinforcement Learning"
authors: ["Cevahir Koprulu", "Thiago D. Simão", "Nils Jansen", "ufuk topcu"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "f3QR9TEERH"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/bfc5b916d195d67ba69ecf2d2619a25b9b05a297.pdf"
published: "2025"
categories: []
keywords: ["curriculum learning", "constrained reinforcement learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:14+09:00"
---

# Safety-Prioritizing Curricula for Constrained Reinforcement Learning

## Abstract
Curriculum learning aims to accelerate reinforcement learning (RL) by generating curricula, i.e., sequences of tasks of increasing difficulty. 
Although existing curriculum generation approaches provide benefits in sample efficiency, they overlook safety-critical settings where an RL agent must adhere to safety constraints.
Thus, these approaches may generate tasks that cause RL agents to violate safety constraints during training and behave suboptimally after. 
We develop a safe curriculum generation approach (SCG) that aligns the objectives of constrained RL and curriculum learning: improving safety during training and boosting sample efficiency.
SCG generates sequences of tasks where the RL agent can be safe and performant by initially generating tasks with minimum safety violations over high-reward ones.
We empirically show that compared to the state-of-the-art curriculum learning approaches and their naively modified safe versions, SCG achieves optimal performance and the lowest amount of constraint violations during training.

## Metadata
- venue: ICLR
- year: 2025
- authors: Cevahir Koprulu, Thiago D. Simão, Nils Jansen, ufuk topcu
- arxiv_id: 
- openreview_id: f3QR9TEERH
- anthology_id: 
- pdf_url: https://openreview.net/pdf/bfc5b916d195d67ba69ecf2d2619a25b9b05a297.pdf
- published: 2025
- keywords: curriculum learning, constrained reinforcement learning

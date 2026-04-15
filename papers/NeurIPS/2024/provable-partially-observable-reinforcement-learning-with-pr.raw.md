---
title: "Provable Partially Observable Reinforcement Learning with Privileged Information"
authors: ["Yang Cai", "Xiangyu Liu", "Argyris Oikonomou", "Kaiqing Zhang"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "o3i1JEfzKw"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/03143b8a208debf6ba3bc9c75fd4b72224323628.pdf"
published: "2024"
categories: []
keywords: ["reinforcement learning", "pomdp", "partial observability", "computational", "privileged information", "expert distillation", "teacher-student learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:01+09:00"
---

# Provable Partially Observable Reinforcement Learning with Privileged Information

## Abstract
Partial observability of the underlying states generally presents significant challenges for reinforcement learning (RL). In practice, certain *privileged information* , e.g., the access to states from simulators, has been exploited in training and achieved prominent empirical successes. To better understand the benefits of privileged information, we revisit and examine several simple and practically used paradigms in this setting, with both computation and sample efficiency analyses. Specifically, we first formalize the empirical paradigm of *expert distillation* (also known as  *teacher-student* learning), demonstrating its pitfall in finding near-optimal policies. We then identify a condition of the partially observable environment, the deterministic filter condition, under which expert distillation achieves sample and computational complexities that are *both* polynomial. Furthermore, we investigate another successful empirical paradigm of *asymmetric actor-critic*, and focus on the more challenging setting of observable partially observable Markov decision processes. We develop a belief-weighted optimistic asymmetric actor-critic algorithm with polynomial sample and quasi-polynomial computational complexities, where one key component is a new provable oracle for learning belief states that preserve *filter stability* under a misspecified model, which may be of independent interest. Finally, we also investigate the provable efficiency of partially observable multi-agent RL (MARL) with privileged information. We develop algorithms with the feature of centralized-training-with-decentralized-execution, a popular framework in empirical MARL, with polynomial sample and (quasi-)polynomial computational complexity in both paradigms above. Compared with a few recent related theoretical studies, our focus is on understanding practically inspired algorithmic paradigms, without computationally intractable oracles.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Yang Cai, Xiangyu Liu, Argyris Oikonomou, Kaiqing Zhang
- arxiv_id: 
- openreview_id: o3i1JEfzKw
- anthology_id: 
- pdf_url: https://openreview.net/pdf/03143b8a208debf6ba3bc9c75fd4b72224323628.pdf
- published: 2024
- keywords: reinforcement learning, pomdp, partial observability, computational, privileged information, expert distillation, teacher-student learning

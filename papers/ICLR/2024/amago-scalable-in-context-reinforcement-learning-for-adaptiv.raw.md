---
title: "AMAGO: Scalable In-Context Reinforcement Learning for Adaptive Agents"
authors: ["Jake Grigsby", "Linxi Fan", "Yuke Zhu"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "M6XWoEdmwf"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/6ffd1eb5dc0bd2b144d5d0309763b3ed5e114e8b.pdf"
published: "2024"
categories: []
keywords: ["Meta-RL", "Generalization", "Long-Term Memory", "Transformers"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:13+09:00"
---

# AMAGO: Scalable In-Context Reinforcement Learning for Adaptive Agents

## Abstract
We introduce AMAGO, an in-context Reinforcement Learning (RL) agent that uses sequence models to tackle the challenges of generalization, long-term memory, and meta-learning. Recent works have shown that off-policy learning can make in-context RL with recurrent policies viable. Nonetheless, these approaches require extensive tuning and limit scalability by creating key bottlenecks in agents' memory capacity, planning horizon, and model size. AMAGO revisits and redesigns the off-policy in-context approach to successfully train long-sequence Transformers over entire rollouts in parallel with end-to-end RL. Our agent is scalable and applicable to a wide range of problems, and we demonstrate its strong performance empirically in meta-RL and long-term memory domains. AMAGO's focus on sparse rewards and off-policy data also allows in-context learning to extend to goal-conditioned problems with challenging exploration. When combined with a multi-goal hindsight relabeling scheme, AMAGO can solve a previously difficult category of open-world domains, where agents complete many possible instructions in procedurally generated environments.

## Metadata
- venue: ICLR
- year: 2024
- authors: Jake Grigsby, Linxi Fan, Yuke Zhu
- arxiv_id: 
- openreview_id: M6XWoEdmwf
- anthology_id: 
- pdf_url: https://openreview.net/pdf/6ffd1eb5dc0bd2b144d5d0309763b3ed5e114e8b.pdf
- published: 2024
- keywords: Meta-RL, Generalization, Long-Term Memory, Transformers

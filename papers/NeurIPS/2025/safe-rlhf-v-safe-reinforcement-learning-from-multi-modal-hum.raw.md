---
title: "Safe RLHF-V: Safe Reinforcement Learning from Multi-modal Human Feedback"
authors: ["Jiaming Ji", "Xinyu Chen", "Rui Pan", "Han Zhu", "Jiahao Li", "Donghai Hong", "Boyuan Chen", "Jiayi Zhou", "Kaile Wang", "Juntao Dai", "Chi-Min Chan", "Sirui Han", "Yike Guo", "Yaodong Yang"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "OIH3T5ZPBW"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/45d271a4ab8e4ce2a092788973240cd97b05911b.pdf"
published: "2025"
categories: []
keywords: ["AI Safety", "AI Alignment"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:30+09:00"
---

# Safe RLHF-V: Safe Reinforcement Learning from Multi-modal Human Feedback

## Abstract
Multimodal large language models (MLLMs) are essential for building general-purpose AI assistants; however, they pose increasing safety risks. How can we ensure safety alignment of MLLMs to prevent undesired behaviors? Going further, it is critical to explore how to fine-tune MLLMs to preserve capabilities while meeting safety constraints. Fundamentally, this challenge can be formulated as a min-max optimization problem. However, existing datasets have not yet disentangled single preference signals into explicit safety constraints, hindering systematic investigation in this direction. Moreover, it remains an open question whether such constraints can be effectively incorporated into the optimization process for multi-modal models. In this work, we present the first exploration of the Safe RLHF-V -- the first multimodal safety alignment framework. The framework consists of: (I) BeaverTails-V, the first open-source dataset featuring dual preference annotations for helpfulness and safety, supplemented with multi-level safety labels (minor, moderate, severe); (II) Beaver-Guard-V, a multi-level guardrail system to proactively defend against unsafe queries and adversarial attacks. Applying the guard model over five rounds of filtering and regeneration significantly enhances the precursor model’s overall safety by an average of 40.9%. (II) Based on dual preference, we initiate the first exploration of multi-modal safety alignment within a constrained optimization. Experimental results demonstrate that Safe RLHF effectively improves both model helpfulness and safety. Specifically, Safe RLHF-V enhances model safety by 34.2% and helpfulness by 34.3%.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Jiaming Ji, Xinyu Chen, Rui Pan, Han Zhu, Jiahao Li, Donghai Hong, Boyuan Chen, Jiayi Zhou, Kaile Wang, Juntao Dai, Chi-Min Chan, Sirui Han, Yike Guo, Yaodong Yang
- arxiv_id: 
- openreview_id: OIH3T5ZPBW
- anthology_id: 
- pdf_url: https://openreview.net/pdf/45d271a4ab8e4ce2a092788973240cd97b05911b.pdf
- published: 2025
- keywords: AI Safety, AI Alignment

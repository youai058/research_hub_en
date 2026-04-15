---
title: "Overcoming Long Context Limitations of State Space Models via Context Dependent Sparse Attention"
authors: ["Zhihao Zhan", "Jianan Zhao", "Zhaocheng Zhu", "Jian Tang"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "XsNi2STaj0"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9c9724da41789d862903929cae59ee38603287a1.pdf"
published: "2025"
categories: []
keywords: ["long-context modeling", "state-space models", "sparse attention", "novel architectures design"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:58+09:00"
---

# Overcoming Long Context Limitations of State Space Models via Context Dependent Sparse Attention

## Abstract
Efficient long-context modeling remains a critical challenge for natural language processing (NLP), as the time complexity of the predominant Transformer architecture scales quadratically with the sequence length. While state-space models (SSMs) offer alternative sub-quadratic solutions, they struggle to capture long-range dependencies effectively. In this work, we focus on analyzing and improving the long-context modeling capabilities of SSMs. We show that the widely used synthetic task, associative recall, which requires a model to recall a value associated with a single key without context, insufficiently represents the complexities of real-world long-context modeling. To address this limitation, we extend the associative recall to a novel synthetic task, joint recall, which requires a model to recall the value associated with a key given in a specified context. Theoretically, we prove that SSMs do not have the expressiveness to solve multi-query joint recall in sub-quadratic time complexity. To resolve this issue, we propose a solution based on integrating SSMs with Context-Dependent Sparse Attention (CDSA), which has the expressiveness to solve multi-query joint recall with sub-quadratic computation. To bridge the gap between theoretical analysis and real-world applications, we propose locality-sensitive Hashing Attention with sparse Key Selection (HAX), which instantiates the theoretical solution and is further tailored to natural language domains. Extensive experiments on both synthetic and real-world long-context benchmarks show that HAX consistently outperforms SSM baselines and SSMs integrated with context-independent sparse attention (CISA). Our code is available at: https://github.com/DeepGraphLearning/HAX.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Zhihao Zhan, Jianan Zhao, Zhaocheng Zhu, Jian Tang
- arxiv_id: 
- openreview_id: XsNi2STaj0
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9c9724da41789d862903929cae59ee38603287a1.pdf
- published: 2025
- keywords: long-context modeling, state-space models, sparse attention, novel architectures design

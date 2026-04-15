---
title: "SpareTrain: Fault-Tolerant LLM Training via Low-Cost Dual Modular Redundancy"
authors: ["Rihae Park", "Yeonjae Kim", "Seung Yul Lee", "Yeonhong Park", "Jae W. Lee"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "kDeS8jpeiZ"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a2ed15d20e38e493dfc3ddab82cb75822bdfc8df.pdf"
published: "2026"
categories: []
keywords: ["large language models", "distributed training", "silent data corruption", "fault-tolerance", "activation checkpointing", "parallelism"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:48+09:00"
---

# SpareTrain: Fault-Tolerant LLM Training via Low-Cost Dual Modular Redundancy

## Abstract
Dual Modular Redundancy (DMR) is a highly effective mechanism for detecting silent data corruption (SDC)—a critical reliability concern in large language model (LLM) training—by executing each operation twice. However, its high computation overhead has prevented practical deployment at scale. In this paper, we present SpareTrain, an LLM training system that achieves complete DMR with minimal overhead by repurposing the activation checkpointing mechanism and exploiting idle GPU time. Evaluations on up to 32 H200 GPUs show that SpareTrain improves throughput by 12–35\% over naive DMR, corresponding to only 3–14\% overhead compared to unprotected training, while maintaining full DMR error detection capabilities.

## Metadata
- venue: ICLR
- year: 2026
- authors: Rihae Park, Yeonjae Kim, Seung Yul Lee, Yeonhong Park, Jae W. Lee
- arxiv_id: 
- openreview_id: kDeS8jpeiZ
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a2ed15d20e38e493dfc3ddab82cb75822bdfc8df.pdf
- published: 2026
- keywords: large language models, distributed training, silent data corruption, fault-tolerance, activation checkpointing, parallelism

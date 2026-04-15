---
title: "Rethinking Reasoning in Document Ranking: Why Chain-of-Thought Falls Short"
authors: ["Xuan Lu", "Haohang Huang", "Rui Meng", "Yaohui Jin", "Wenjun Zeng", "Xiaoyu Shen"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "txmqENuRcc"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e7314031ebc4b2e6f24ef19f3c1aa6a0bff80aff.pdf"
published: "2026"
categories: []
keywords: ["information retrieval", "reranking", "reasoning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:47+09:00"
---

# Rethinking Reasoning in Document Ranking: Why Chain-of-Thought Falls Short

## Abstract
Document reranking is a key component in information retrieval (IR), aimed at refining initial retrieval results to improve ranking quality for downstream tasks. Recent studies—motivated by large reasoning models (LRMs)—have begun incorporating explicit chain-of-thought (CoT) reasoning into LLM-based rerankers. 
However, the effectiveness of such reasoning for ranking tasks remains underexplored.
In this work, we present the first systematic study of reasoning in reranking across both logits-based pointwise and listwise settings, under both supervised fine-tuning and reinforcement learning. Using diverse benchmarks, including reasoning-intensive datasets BRIGHT and standard IR benchmarks BEIR, we find that reasoning-augmented rerankers consistently underperform their direct counterparts that predict rankings without CoT, despite substantially higher inference costs. Our analysis reveals three core limitations: (i) in pointwise rerankers, reasoning breaks calibration and biases models toward the positive class, raising TPR but lowering TNR, which inflates false positives and degrades ranking in negative-dominant pools; (ii) in listwise rerankers, explicit reasoning improves the fit during training but leads to higher variance and fails to improve performance in both in-domain and out-of-domain evaluations, even when reinforcement learning shortens rationales; and (iii) overall, directly fine-tuned rerankers remain more stable, effective, and robust.  These findings challenge the assumption that explicit reasoning is universally beneficial for reranking. We conclude by highlighting future directions, including calibration-aware scoring for pointwise rerankers and the design of concise, targeted reasoning strategies to mitigate overfitting and overthinking in listwise rerankers.

## Metadata
- venue: ICLR
- year: 2026
- authors: Xuan Lu, Haohang Huang, Rui Meng, Yaohui Jin, Wenjun Zeng, Xiaoyu Shen
- arxiv_id: 
- openreview_id: txmqENuRcc
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e7314031ebc4b2e6f24ef19f3c1aa6a0bff80aff.pdf
- published: 2026
- keywords: information retrieval, reranking, reasoning

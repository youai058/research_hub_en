---
title: "Information-Theoretic Membership Inference for Granular Quantification of Memorization"
authors: ["Jiashu Tao", "Reza Shokri"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "4KVeb0Vv13"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f9fe47bcda021a4e7e9086ae20d5bffea654a8cf.pdf"
published: "2026"
categories: []
keywords: ["membership inference attack", "mia", "privacy", "llm privacy", "memorization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:27+09:00"
---

# Information-Theoretic Membership Inference for Granular Quantification of Memorization

## Abstract
Machine learning models are known to leak sensitive information, as they inevitably memorize (parts of) their training data. This risk is amplified for large language models (LLMs), which are trained on massive corpora and therefore create a more urgent need for privacy assessment prior to release. The standard method to quantify privacy is via membership inference attacks, where the state-of-the-art approach is the Robust Membership Inference Attack (RMIA). In this paper, we introduce \textbf{InfoRMIA}, a principled information-theoretic formulation of membership inference that consistently outperforms RMIA across benchmarks while improving computational efficiency. Moving beyond attack performance alone, we show that treating sequence-level membership inference as the gold standard obscures how memorization manifests in LLMs. To address this limitation, we propose a fine-grained memorization assessment framework based on token-level signals, with InfoRMIA serving as its algorithmic backbone. Our approach identifies which tokens within generated outputs are memorized, localizing privacy leakage from sequences to individual tokens. This framework enables more precise analysis of LLM memorization and potentially targeted mitigation strategies such as exact unlearning.

## Metadata
- venue: ICLR
- year: 2026
- authors: Jiashu Tao, Reza Shokri
- arxiv_id: 
- openreview_id: 4KVeb0Vv13
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f9fe47bcda021a4e7e9086ae20d5bffea654a8cf.pdf
- published: 2026
- keywords: membership inference attack, mia, privacy, llm privacy, memorization

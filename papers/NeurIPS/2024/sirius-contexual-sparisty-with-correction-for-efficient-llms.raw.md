---
title: "SIRIUS : Contexual Sparisty with Correction for Efficient LLMs"
authors: ["Yang Zhou", "Zhuoming Chen", "Zhaozhuo Xu", "Xi Victoria Lin", "Beidi Chen"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "5bR2l1b2eh"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/898385c8f82211966b9ec8720e075b5638d2b2a5.pdf"
published: "2024"
categories: []
keywords: ["Contextual Sparsity", "LLM inference", "Knowledge Distillation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:41+09:00"
---

# SIRIUS : Contexual Sparisty with Correction for Efficient LLMs

## Abstract
With the blossom of large language models (LLM), inference efficiency becomes increasingly important. Various approximate methods are proposed to reduce the cost at inference time. Contextual Sparsity (CS) is appealing for its training-free nature and its ability to reach a higher compression ratio seemingly without significant performance degradation. However, after a comprehensive evaluation of contextual sparsity methods on various complex generation tasks, we find that although CS succeeds in prompt-understanding tasks, it significantly degrades the model performance for reasoning, deduction, and knowledge-based tasks. Despite the gap in end-to-end accuracy, we observed that sparse models and original models often share the general problem-solving logic and require only a few token corrections to recover the original model performance. This paper introduces SIRIUS, an efficient correction mechanism, which significantly boosts CS models on reasoning tasks while maintaining its efficiency gain. SIRIUS is evaluated on 6 models with 8 difficult generation tasks in reasoning, deduction, and coding and shows consistent effectiveness and efficiency. Also, we carefully develop a system implementation for SIRIUS and show that SIRIUS delivers theoretical latency reduction with roughly a 20% reduction in latency for 8B model on-chip and a 35% reduction in latency for 70B model offloading. We open-source our implementation of Sirius at https://github.com/Infini-AI-Lab/Sirius.git.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Yang Zhou, Zhuoming Chen, Zhaozhuo Xu, Xi Victoria Lin, Beidi Chen
- arxiv_id: 
- openreview_id: 5bR2l1b2eh
- anthology_id: 
- pdf_url: https://openreview.net/pdf/898385c8f82211966b9ec8720e075b5638d2b2a5.pdf
- published: 2024
- keywords: Contextual Sparsity, LLM inference, Knowledge Distillation

---
title: "Less is More: Unlocking Specialization of Time Series Foundation Models via Structured Pruning"
authors: ["Lifan Zhao", "Yanyan Shen", "Zhaoyang Liu", "Xue Wang", "Jiaji Deng"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "jy4bBsr1Jc"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b40cac03f947be29793418e9dd7b2265ee66aab2.pdf"
published: "2025"
categories: []
keywords: ["Time series forecasting"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:56+09:00"
---

# Less is More: Unlocking Specialization of Time Series Foundation Models via Structured Pruning

## Abstract
Scaling laws motivate the development of Time Series Foundation Models (TSFMs) that pre-train vast parameters and achieve remarkable zero-shot forecasting performance. Surprisingly, even after fine-tuning, TSFMs cannot consistently outperform smaller, specialized models trained on full-shot downstream data. 
A key question is how to realize effective adaptation of TSFMs for a target forecasting task. Through empirical studies on various TSFMs, the pre-trained models often exhibit inherent sparsity and redundancy in computation, suggesting that TSFMs have learned to activate task-relevant network substructures to accommodate diverse forecasting tasks. To preserve this valuable prior knowledge, we propose a structured pruning method to regularize the subsequent fine-tuning process by focusing it on a more relevant and compact parameter space.  
Extensive experiments on seven TSFMs and six benchmarks demonstrate that fine-tuning a smaller, pruned TSFM significantly improves forecasting performance compared to fine-tuning original models. This ``prune-then-finetune'' paradigm often enables TSFMs to achieve state-of-the-art performance and surpass strong specialized baselines. 
Source code is made publicly available at \url{https://github.com/SJTU-DMTai/Prune-then-Finetune}.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Lifan Zhao, Yanyan Shen, Zhaoyang Liu, Xue Wang, Jiaji Deng
- arxiv_id: 
- openreview_id: jy4bBsr1Jc
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b40cac03f947be29793418e9dd7b2265ee66aab2.pdf
- published: 2025
- keywords: Time series forecasting

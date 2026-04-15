---
title: "TNT: Improving Chunkwise Training for Test-Time Memorization"
authors: ["Zeman Li", "Ali Behrouz", "Yuan Deng", "Peilin Zhong", "Praneeth Kacham", "Mahdi Karami", "Meisam Razaviyayn", "Vahab Mirrokni"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "rajioNWfRs"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/424813e8424a5a7c3af990a764d389ec5b389490.pdf"
published: "2026"
categories: []
keywords: ["Recurrent Neural Networks", "Sequence Modeling"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:50+09:00"
---

# TNT: Improving Chunkwise Training for Test-Time Memorization

## Abstract
Recurrent neural networks (RNNs) with deep test-time memorization modules, such as Titans and TTT, represent a promising, linearly-scaling paradigm distinct from Transformers. While these expressive models do not yet match the peak performance of state-of-the-art Transformers, their potential has been largely untapped due to prohibitively slow training and low hardware utilization.
Existing parallelization methods force a fundamental conflict governed by the chunksize hyperparameter: large chunks boost speed but degrade performance, necessitating a fixed, suboptimal compromise. To solve this challenge, we introduce TNT, a novel training paradigm that decouples training efficiency from inference performance through a two-stage process. Stage one is an efficiency-focused pre-training phase utilizing a hierarchical memory. A global module processes large, hardware-friendly chunks for long-range context, while multiple parallel local modules handle fine-grained details. Crucially, by periodically resetting local memory states, we break sequential dependencies to enable massive context parallelization. Stage two is a brief fine-tuning phase where only the local memory modules are adapted to a smaller, high-resolution chunksize, maximizing accuracy with minimal overhead. Evaluated on Titans and TTT models, TNT achieves a substantial acceleration in training speed—up to 17$\times$ faster than the most accurate baseline configuration—while simultaneously improving model accuracy. This improvement removes a critical scalability barrier, establishing a practical foundation for developing expressive RNNs and facilitating future work to close the performance gap with Transformers.

## Metadata
- venue: ICLR
- year: 2026
- authors: Zeman Li, Ali Behrouz, Yuan Deng, Peilin Zhong, Praneeth Kacham, Mahdi Karami, Meisam Razaviyayn, Vahab Mirrokni
- arxiv_id: 
- openreview_id: rajioNWfRs
- anthology_id: 
- pdf_url: https://openreview.net/pdf/424813e8424a5a7c3af990a764d389ec5b389490.pdf
- published: 2026
- keywords: Recurrent Neural Networks, Sequence Modeling

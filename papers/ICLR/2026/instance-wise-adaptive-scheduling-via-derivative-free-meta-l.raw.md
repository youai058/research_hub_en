---
title: "Instance-wise Adaptive Scheduling via Derivative-Free Meta-Learning"
authors: ["Hefang Qing", "Miao Zhang", "Yaoxin Wu", "Weinan Huang", "Jianhao Yang", "Wen Song", "Gang Wang"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "XcCqRcHzJ3"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/fe653dc6336cb712c8cc164d2dc51acae0df4756.pdf"
published: "2026"
categories: []
keywords: ["Scheduling", "Neural Combinatorial Optimization", "Meta-learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:40+09:00"
---

# Instance-wise Adaptive Scheduling via Derivative-Free Meta-Learning

## Abstract
Deep Reinforcement Learning has achieved remarkable progress in solving NP-hard scheduling problems. However, existing methods primarily focus on optimizing average performance over training instances, overlooking the core objective of solving each individual instance with high quality. While several instance-wise adaptation mechanisms have been proposed, they are test-time approaches only and cannot share knowledge across different adaptation tasks. Moreover, they largely rely on gradient-based optimization, which could be ineffective in dealing with combinatorial optimization problems. We address the above issues by proposing an instance-wise meta-learning framework. It trains a meta model to acquire a generalizable initialization that effectively guides per-instance adaptation during inference, and overcomes the limitations of gradient-based methods by leveraging a derivative-free optimization scheme that is fully GPU parallelizable. Experimental results on representative scheduling problems demonstrate that our method consistently outperforms existing learning-based scheduling methods and instance-wise adaptation mechanisms under various task sizes and distributions.

## Metadata
- venue: ICLR
- year: 2026
- authors: Hefang Qing, Miao Zhang, Yaoxin Wu, Weinan Huang, Jianhao Yang, Wen Song, Gang Wang
- arxiv_id: 
- openreview_id: XcCqRcHzJ3
- anthology_id: 
- pdf_url: https://openreview.net/pdf/fe653dc6336cb712c8cc164d2dc51acae0df4756.pdf
- published: 2026
- keywords: Scheduling, Neural Combinatorial Optimization, Meta-learning

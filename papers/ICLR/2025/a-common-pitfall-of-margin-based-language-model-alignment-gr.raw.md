---
title: "A Common Pitfall of Margin-based Language Model Alignment: Gradient Entanglement"
authors: ["Hui Yuan", "Yifan Zeng", "Yue Wu", "Huazheng Wang", "Mengdi Wang", "Liu Leqi"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "YaBiGjuDiC"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/5eed7557c3f28a8e2f5fb142bf9e58397e0080ff.pdf"
published: "2025"
categories: []
keywords: ["Alignment", "Preference Optimization", "Large Language Model"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:11+09:00"
---

# A Common Pitfall of Margin-based Language Model Alignment: Gradient Entanglement

## Abstract
Reinforcement Learning from Human Feedback (RLHF) has become the predominant approach for aligning language models (LMs) to be more helpful and less harmful. 
At its core, RLHF uses a margin-based loss for preference optimization, which specifies the ideal LM behavior only in terms of the difference between preferred and dispreferred responses. In this paper, we identify a common pitfall of margin-based methods---the under-specification of ideal LM behavior on preferred and dispreferred responses individually, which results in two unintended consequences as the margin increases:
(1) The probability of dispreferred (e.g., unsafe) responses may increase, resulting in potential safety alignment failures.
(2) The probability of preferred responses may decrease, even when those responses are ideal.
We demystify the reasons behind these problematic behaviors: margin-based losses couple the change in the preferred probability with the gradient of the dispreferred one, and vice versa, often preventing the preferred probability from increasing while the dispreferred one decreases, and thus causing a synchronized increase or decrease in both probabilities. We term this effect, inherent in margin-based objectives, gradient entanglement. 
Formally, we derive conditions for general margin-based alignment objectives under which gradient entanglement becomes concerning: the inner product between the gradient of preferred log-probability and the gradient of dispreferred log-probability is large relative to the individual gradient norms. Furthermore, we theoretically investigate why such inner products can be large when aligning language models and empirically validate our findings. Empirical implications of our framework further extend to explaining important differences in the training dynamics of various preference optimization algorithms and suggesting future directions for improvement.

## Metadata
- venue: ICLR
- year: 2025
- authors: Hui Yuan, Yifan Zeng, Yue Wu, Huazheng Wang, Mengdi Wang, Liu Leqi
- arxiv_id: 
- openreview_id: YaBiGjuDiC
- anthology_id: 
- pdf_url: https://openreview.net/pdf/5eed7557c3f28a8e2f5fb142bf9e58397e0080ff.pdf
- published: 2025
- keywords: Alignment, Preference Optimization, Large Language Model

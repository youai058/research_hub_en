---
title: "Why In-Context Learning Models are Good Few-Shot Learners?"
authors: ["Shiguang Wu", "Yaqing Wang", "Quanming Yao"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "iLUcsecZJp"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/916e0fcae345689455c6aebb0a3d941b9ceba384.pdf"
published: "2025"
categories: []
keywords: ["In-Context Learning", "Meta-Learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:56+09:00"
---

# Why In-Context Learning Models are Good Few-Shot Learners?

## Abstract
We explore in-context learning (ICL) models from a learning-to-learn perspective. Unlike studies that identify specific learning algorithms in ICL models, we compare ICL models with typical meta-learners to understand their superior performance. We theoretically prove the expressiveness of ICL models as learning algorithms and examine their learnability and generalizability. 
Our findings show that ICL with transformers 
can effectively construct data-dependent learning algorithms instead of directly follow existing ones 
(including gradient-based, metric-based, and amortization-based meta-learners). 
The construction of such learning algorithm is determined by the pre-training process, as a function fitting the training distribution, which raises generalizability as an important issue.
With above understanding, we propose strategies to transfer techniques for classical deep networks to meta-level to further improve ICL. As examples, we implement meta-level meta-learning for domain adaptability with limited data and meta-level curriculum learning for accelerated convergence during pre-training, demonstrating their empirical effectiveness.

## Metadata
- venue: ICLR
- year: 2025
- authors: Shiguang Wu, Yaqing Wang, Quanming Yao
- arxiv_id: 
- openreview_id: iLUcsecZJp
- anthology_id: 
- pdf_url: https://openreview.net/pdf/916e0fcae345689455c6aebb0a3d941b9ceba384.pdf
- published: 2025
- keywords: In-Context Learning, Meta-Learning

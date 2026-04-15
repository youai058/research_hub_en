---
title: "Gradient-Based Diversity Optimization with Differentiable Top-$k$ Objective"
authors: ["Tianyi Zhou", "Sebastian Dalleiger", "Ece Calikus", "Aristides Gionis"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "cuzWopwoZG"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a1c33da5b12e7b2c25982ffc401b940008692adf.pdf"
published: "2026"
categories: []
keywords: ["Diversity Optimization", "Gradient-based learning", "Recommendation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:20+09:00"
---

# Gradient-Based Diversity Optimization with Differentiable Top-$k$ Objective

## Abstract
Predicting relevance is a pervasive problem across digital platforms, covering social media, entertainment, and commerce. However, when optimized solely for relevance and engagement, many machine-learning models amplify data biases and produce homogeneous outputs, reinforcing filter bubbles and content uniformity. To address this issue, we introduce a pairwise top-k diversity objective with a differentiable smooth-ranking approximation, providing a model-agnostic way to incorporate diversity optimization directly into standard gradient-based learning. Building on this objective, we cast relevance and diversity as a joint optimization problem, we analyze the resulting gradient trade-offs, and propose two complementary strategies: direct optimization, which modifies the learning objective, and indirect optimization, which reweights training data. Both strategies can be applied either when training models from scratch or when fine-tuning existing relevance-optimized models. We use recommendation as a natural evaluation setting where scalability and diversity are critical, and show through extensive experiments that our methods consistently improve diversity with negligible accuracy loss. Notably, fine-tuning with our objective is especially efficient, requiring only a few gradient steps to encode diversity at scale.

## Metadata
- venue: ICLR
- year: 2026
- authors: Tianyi Zhou, Sebastian Dalleiger, Ece Calikus, Aristides Gionis
- arxiv_id: 
- openreview_id: cuzWopwoZG
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a1c33da5b12e7b2c25982ffc401b940008692adf.pdf
- published: 2026
- keywords: Diversity Optimization, Gradient-based learning, Recommendation

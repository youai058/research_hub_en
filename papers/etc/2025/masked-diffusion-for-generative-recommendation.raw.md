---
title: "Masked Diffusion for Generative Recommendation"
authors: ["Kulin Shah", "Bhuvesh Kumar", "Neil Shah", "Liam Collins"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2511.23021"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2511.23021v2"
published: "2025-11-28"
categories: ["cs.LG", "cs.IR"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:19+09:00"
---

# Masked Diffusion for Generative Recommendation

## Abstract
Generative recommendation (GR) with semantic IDs (SIDs) has emerged as a promising alternative to traditional recommendation approaches due to its performance gains, capitalization on semantic information provided through language model embeddings, and inference and storage efficiency. Existing GR with SIDs works frame the probability of a sequence of SIDs corresponding to a user's interaction history using autoregressive modeling. While this has led to impressive next item prediction performances in certain settings, these autoregressive GR with SIDs models suffer from expensive inference due to sequential token-wise decoding, potentially inefficient use of training data and bias towards learning short-context relationships among tokens. Inspired by recent breakthroughs in NLP, we propose to instead model and learn the probability of a user's sequence of SIDs using masked diffusion. Masked diffusion employs discrete masking noise to facilitate learning the sequence distribution, and models the probability of masked tokens as conditionally independent given the unmasked tokens, allowing for parallel decoding of the masked tokens. We demonstrate through thorough experiments that our proposed method consistently outperforms autoregressive modeling. This performance gap is especially pronounced in data-constrained settings and in terms of coarse-grained recall, consistent with our intuitions. Moreover, our approach allows the flexibility of predicting multiple SIDs in parallel during inference while maintaining superior performance to autoregressive modeling.

## Metadata
- venue: arXiv
- year: 2025
- authors: Kulin Shah, Bhuvesh Kumar, Neil Shah, Liam Collins
- arxiv_id: 2511.23021
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2511.23021v2
- published: 2025-11-28

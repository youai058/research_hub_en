---
title: "MDM-Prime-v2: Binary Encoding and Index Shuffling Enable Compute-optimal Scaling of Diffusion Language Models"
authors: ["Chen-Hao Chao", "Wei-Fang Sun", "Junwei Quan", "Chun-Yi Lee", "Rahul G. Krishnan"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.16077"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.16077v2"
published: "2026-03-17"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:13:58+09:00"
---

# MDM-Prime-v2: Binary Encoding and Index Shuffling Enable Compute-optimal Scaling of Diffusion Language Models

## Abstract
Masked diffusion models (MDM) exhibit superior generalization when learned using a Partial masking scheme (Prime). This approach converts tokens into sub-tokens and models the diffusion process at the sub-token level. We identify two limitations of the MDM-Prime framework. First, we lack tools to guide the hyperparameter choice of the token granularity in the subtokenizer. Second, we find that the function form of the subtokenizer significantly degrades likelihood estimation when paired with commonly used Byte-Pair-Encoding (BPE) tokenizers. To address these limitations, we study the tightness of the variational bound in MDM-Prime and develop MDM-Prime-v2, a masked diffusion language model which incorporates Binary Encoding and Index Shuffling. Our scaling analysis reveals that MDM-Prime-v2 is 21.8$\times$ more compute-efficient than autoregressive models (ARM). In compute-optimal comparisons, MDM-Prime-v2 achieves 7.77 perplexity on OpenWebText, outperforming ARM (12.99), MDM (18.94), and MDM-Prime (13.41). When extending the model size to 1.1B parameters, our model further demonstrates superior zero-shot accuracy on various commonsense reasoning tasks.

## Metadata
- venue: arXiv
- year: 2026
- authors: Chen-Hao Chao, Wei-Fang Sun, Junwei Quan, Chun-Yi Lee, Rahul G. Krishnan
- arxiv_id: 2603.16077
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.16077v2
- published: 2026-03-17

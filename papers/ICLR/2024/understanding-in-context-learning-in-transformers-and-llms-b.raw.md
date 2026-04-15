---
title: "Understanding In-Context Learning in Transformers and LLMs by Learning to Learn Discrete Functions"
authors: ["Satwik Bhattamishra", "Arkil Patel", "Phil Blunsom", "Varun Kanade"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ekeyCgeRfC"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/816f489eb70fe677c4ebc1cf159cf38b3062956b.pdf"
published: "2024"
categories: []
keywords: ["In-context learning", "Transformers", "Large language models", "Boolean functions"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:14+09:00"
---

# Understanding In-Context Learning in Transformers and LLMs by Learning to Learn Discrete Functions

## Abstract
In order to understand the in-context learning phenomenon, recent works have adopted a stylized experimental framework and demonstrated that Transformers can match the performance of gradient-based learning algorithms for various classes of real-valued functions. However, the limitations of Transformers in implementing learning algorithms, and their ability to learn other forms of algorithms are not well understood. Additionally, the degree to which these capabilities are confined to attention-based models is unclear. Furthermore, it remains to be seen whether the insights derived from these stylized settings can be extrapolated to pretrained Large Language Models (LLMs). In this work, we take a step towards answering these questions by demonstrating the following: (a) On a test-bed with a variety of Boolean function classes, we find that Transformers can nearly match the optimal learning algorithm for 'simpler' tasks, while their performance deteriorates on more 'complex' tasks. Additionally, we find that certain attention-free models perform (almost) identically to Transformers on a range of tasks. (b) When provided a *teaching sequence*, i.e. a set of examples that uniquely identifies a function in a class, we show that Transformers learn more sample-efficiently. Interestingly, our results show that Transformers can learn to implement *two distinct* algorithms to solve a *single* task, and can adaptively select the more sample-efficient algorithm depending on the sequence of in-context examples. (c) Lastly, we show that extant LLMs, e.g. LLaMA-2, GPT-4, can compete with nearest-neighbor baselines on prediction tasks that are guaranteed to not be in their training set.

## Metadata
- venue: ICLR
- year: 2024
- authors: Satwik Bhattamishra, Arkil Patel, Phil Blunsom, Varun Kanade
- arxiv_id: 
- openreview_id: ekeyCgeRfC
- anthology_id: 
- pdf_url: https://openreview.net/pdf/816f489eb70fe677c4ebc1cf159cf38b3062956b.pdf
- published: 2024
- keywords: In-context learning, Transformers, Large language models, Boolean functions

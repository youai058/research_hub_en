---
title: "Unleashing Region Understanding in Intermediate Layers for MLLM-based Referring Expression Generation"
authors: ["Yaoyuan Liang", "Zhuojun Cai", "Jian Xu", "Guanbo Huang", "Yiran Wang", "Xiao Liang", "Jiahao Liu", "Ziran Li", "Jingang Wang", "Shao-Lun Huang"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "168NLzTpw8"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/29764fb7a9e6be1a9fca7cfebb4983823894acb9.pdf"
published: "2024"
categories: []
keywords: ["Vision-Language", "Region-Level Understanding", "Multimodal Large Language Model"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:06+09:00"
---

# Unleashing Region Understanding in Intermediate Layers for MLLM-based Referring Expression Generation

## Abstract
The Multi-modal Large Language Model (MLLM) based Referring Expression Generation (REG) task has gained increasing popularity, which aims to generate an unambiguous text description that applies to exactly one object or region in the image by leveraging foundation models. We empirically found that there exists a potential trade-off between the detailedness and the correctness of the descriptions for the referring objects. On the one hand, generating sentences with more details is usually required in order to provide more precise object descriptions. On the other hand, complicated sentences could easily increase the probability of hallucinations. To address this issue, we propose a training-free framework, named ``unleash-then-eliminate'', which first elicits the latent information in the intermediate layers, and then adopts a cycle-consistency-based decoding method to alleviate the production of hallucinations. Furthermore, to reduce the computational load of cycle-consistency-based decoding, we devise a Probing-based Importance Estimation method to statistically estimate the importance weights of intermediate layers within a subset. These importance weights are then incorporated into the decoding process over the entire dataset, intervening in the next token prediction from intermediate layers.
Extensive experiments conducted on the RefCOCOg and PHD benchmarks show that our proposed framework could outperform existing methods on both semantic and hallucination-related metrics. Code will be made available in https://github.com/Glupayy/unleash-eliminate.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Yaoyuan Liang, Zhuojun Cai, Jian Xu, Guanbo Huang, Yiran Wang, Xiao Liang, Jiahao Liu, Ziran Li, Jingang Wang, Shao-Lun Huang
- arxiv_id: 
- openreview_id: 168NLzTpw8
- anthology_id: 
- pdf_url: https://openreview.net/pdf/29764fb7a9e6be1a9fca7cfebb4983823894acb9.pdf
- published: 2024
- keywords: Vision-Language, Region-Level Understanding, Multimodal Large Language Model

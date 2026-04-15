---
title: "DeltaFormer: Unlock the state space of Transformer"
authors: ["Mingyu Xu", "Tenglong Ao", "Jiaao He", "Jianqiao Lu", "Guang Shi", "Shu Zhong"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "GSE3oaiDL2"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/7f4e19832cc1713d67e131b834fbb8175f6d26d8.pdf"
published: "2025"
categories: []
keywords: ["Transformer", "Circuit Complexity", "Model Architecture"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:59+09:00"
---

# DeltaFormer: Unlock the state space of Transformer

## Abstract
In recent years, large language models with Transformer architecture as the core have made breakthrough progress in many fields. At the same time, there are also some weaknesses in the large language model that have prompted people to reflect, among which the most fundamental one is the reflection on the Transformer architecture. The Transformer architecture has high parallelism and can fully utilize the computing power of GPUs, thus replacing models such as LSTM in the past few years. However, high parallelism is not a free lunch, as it fundamentally limits the performance of models. Especially, the problems that logarithmic precision Transformer architecture can solve are strictly limited to the $TC^0$. And there are many important issues that are usually considered out of $TC^0$, such as Python code evaluation, entity tracking, chess, and other state tracking tasks. Meanwhile, some recent state space methods based on Delta Rule have been able to break through the $TC^0$ architecture, but they are limited by fixed size state spaces and perform poorly on many tasks. To this end, we have re-examined the Transformer from the perspective of a state space with kernel functions and propose an improved Transformer called DeltaFormer. We have theoretically and practically demonstrated that the proposed new architecture can break through the limitation of the inherent $TC^0$ expressivity of Transformers and verified that it is not weaker than standard Transformer in language modeling tasks. We hope our work can provide inspiration for designing more expressive models.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Mingyu Xu, Tenglong Ao, Jiaao He, Jianqiao Lu, Guang Shi, Shu Zhong
- arxiv_id: 
- openreview_id: GSE3oaiDL2
- anthology_id: 
- pdf_url: https://openreview.net/pdf/7f4e19832cc1713d67e131b834fbb8175f6d26d8.pdf
- published: 2025
- keywords: Transformer, Circuit Complexity, Model Architecture

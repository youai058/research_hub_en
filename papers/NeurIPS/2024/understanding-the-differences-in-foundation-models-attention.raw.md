---
title: "Understanding the Differences in Foundation Models: Attention, State  Space Models, and Recurrent Neural Networks"
authors: ["Jerome Sieber", "Carmen Amo Alonso", "Alexandre Didier", "Melanie Zeilinger", "Antonio Orvieto"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "iF7MnXnxRw"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/53cb725e5aa20518f58b8b6b46d806687bae9108.pdf"
published: "2024"
categories: []
keywords: ["deep learning architectures", "softmax attention", "linear attention", "state space models", "recurrent neural networks", "dynamical system models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:00+09:00"
---

# Understanding the Differences in Foundation Models: Attention, State  Space Models, and Recurrent Neural Networks

## Abstract
Softmax attention is the principle backbone of foundation models for various artificial intelligence applications, yet its quadratic complexity in sequence length can limit its inference throughput in long-context settings. To address this challenge, alternative architectures such as linear attention, State Space Models (SSMs), and Recurrent Neural Networks (RNNs) have been considered as more efficient alternatives. While connections between these approaches exist, such models are commonly developed in isolation and there is a lack of theoretical understanding of the shared principles underpinning these architectures and their subtle differences, greatly influencing performance and scalability. In this paper, we introduce the Dynamical Systems Framework (DSF), which allows a principled investigation of all these architectures in a common representation. Our framework facilitates rigorous comparisons, providing new insights on the distinctive characteristics of each model class. For instance, we compare linear attention and selective SSMs, detailing their differences and conditions under which both are equivalent. We also provide principled comparisons between softmax attention and other model classes, discussing the theoretical conditions under which softmax attention can be approximated. Additionally, we substantiate these new insights with empirical validations and mathematical arguments. This shows the DSF's potential to guide the systematic development of future more efficient and scalable foundation models.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Jerome Sieber, Carmen Amo Alonso, Alexandre Didier, Melanie Zeilinger, Antonio Orvieto
- arxiv_id: 
- openreview_id: iF7MnXnxRw
- anthology_id: 
- pdf_url: https://openreview.net/pdf/53cb725e5aa20518f58b8b6b46d806687bae9108.pdf
- published: 2024
- keywords: deep learning architectures, softmax attention, linear attention, state space models, recurrent neural networks, dynamical system models

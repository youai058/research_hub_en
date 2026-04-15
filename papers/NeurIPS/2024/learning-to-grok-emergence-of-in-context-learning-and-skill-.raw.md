---
title: "Learning to grok: Emergence of in-context learning and skill composition in modular arithmetic tasks"
authors: ["Tianyu He", "Darshil Doshi", "Aritra Das", "Andrey Gromov"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "aVh9KRZdRk"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/5737b58d308dafc16130635934df4276a7a574aa.pdf"
published: "2024"
categories: []
keywords: ["In-Context Learning", "Grokking", "Modular Arithmetic", "Interpretability"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:32+09:00"
---

# Learning to grok: Emergence of in-context learning and skill composition in modular arithmetic tasks

## Abstract
Large language models can solve tasks that were not present in the training set. This capability is believed to be due to in-context learning and skill composition. In this work, we study the emergence of in-context learning and skill composition in a collection of modular arithmetic tasks. Specifically, we consider a finite collection of linear modular functions $z = a  x + b  y \text{ mod } p$ labeled by the vector $(a, b) \in \mathbb{Z}_p^2$. We use some of these tasks for pre-training and the rest for out-of-distribution testing. We empirically show that a GPT-style transformer exhibits a transition from in-distribution to out-of-distribution generalization as the number of pre-training tasks increases. We find that the smallest model capable of out-of-distribution generalization requires two transformer blocks, while for deeper models, the out-of-distribution generalization phase is *transient*, necessitating early stopping. Finally, we perform an interpretability study of the pre-trained models, revealing highly structured representations in both attention heads and MLPs; and discuss the learned algorithms. Notably, we find an algorithmic shift in deeper models, as we go from few to many in-context examples.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Tianyu He, Darshil Doshi, Aritra Das, Andrey Gromov
- arxiv_id: 
- openreview_id: aVh9KRZdRk
- anthology_id: 
- pdf_url: https://openreview.net/pdf/5737b58d308dafc16130635934df4276a7a574aa.pdf
- published: 2024
- keywords: In-Context Learning, Grokking, Modular Arithmetic, Interpretability

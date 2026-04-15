---
title: "An Effective Deployment of Diffusion LM for Data Augmentation in Low-Resource Sentiment Classification"
authors: ["Zhuowei Chen", "Lianxi Wang", "Yuben Wu", "Xinfeng Liao", "Yujia Tian", "Junyang Zhong"]
venue: "arXiv"
year: 2024
venue_class: "etc"
arxiv_id: "2409.03203"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2409.03203v2"
published: "2024-09-05"
categories: ["cs.CL", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:20:02+09:00"
---

# An Effective Deployment of Diffusion LM for Data Augmentation in Low-Resource Sentiment Classification

## Abstract
Sentiment classification (SC) often suffers from low-resource challenges such as domain-specific contexts, imbalanced label distributions, and few-shot scenarios. The potential of the diffusion language model (LM) for textual data augmentation (DA) remains unexplored, moreover, textual DA methods struggle to balance the diversity and consistency of new samples. Most DA methods either perform logical modifications or rephrase less important tokens in the original sequence with the language model. In the context of SC, strong emotional tokens could act critically on the sentiment of the whole sequence. Therefore, contrary to rephrasing less important context, we propose DiffusionCLS to leverage a diffusion LM to capture in-domain knowledge and generate pseudo samples by reconstructing strong label-related tokens. This approach ensures a balance between consistency and diversity, avoiding the introduction of noise and augmenting crucial features of datasets. DiffusionCLS also comprises a Noise-Resistant Training objective to help the model generalize. Experiments demonstrate the effectiveness of our method in various low-resource scenarios including domain-specific and domain-general problems. Ablation studies confirm the effectiveness of our framework's modules, and visualization studies highlight optimal deployment conditions, reinforcing our conclusions.

## Metadata
- venue: arXiv
- year: 2024
- authors: Zhuowei Chen, Lianxi Wang, Yuben Wu, Xinfeng Liao, Yujia Tian, Junyang Zhong
- arxiv_id: 2409.03203
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2409.03203v2
- published: 2024-09-05

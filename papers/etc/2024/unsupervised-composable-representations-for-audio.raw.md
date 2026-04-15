---
title: "Unsupervised Composable Representations for Audio"
authors: ["Giovanni Bindi", "Philippe Esling"]
venue: "arXiv"
year: 2024
venue_class: "etc"
arxiv_id: "2408.09792"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2408.09792v1"
published: "2024-08-19"
categories: ["cs.LG", "cs.SD", "eess.AS"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:20:05+09:00"
---

# Unsupervised Composable Representations for Audio

## Abstract
Current generative models are able to generate high-quality artefacts but have been shown to struggle with compositional reasoning, which can be defined as the ability to generate complex structures from simpler elements. In this paper, we focus on the problem of compositional representation learning for music data, specifically targeting the fully-unsupervised setting. We propose a simple and extensible framework that leverages an explicit compositional inductive bias, defined by a flexible auto-encoding objective that can leverage any of the current state-of-art generative models. We demonstrate that our framework, used with diffusion models, naturally addresses the task of unsupervised audio source separation, showing that our model is able to perform high-quality separation. Our findings reveal that our proposal achieves comparable or superior performance with respect to other blind source separation methods and, furthermore, it even surpasses current state-of-art supervised baselines on signal-to-interference ratio metrics. Additionally, by learning an a-posteriori masking diffusion model in the space of composable representations, we achieve a system capable of seamlessly performing unsupervised source separation, unconditional generation, and variation generation. Finally, as our proposal works in the latent space of pre-trained neural audio codecs, it also provides a lower computational cost with respect to other neural baselines.

## Metadata
- venue: arXiv
- year: 2024
- authors: Giovanni Bindi, Philippe Esling
- arxiv_id: 2408.09792
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2408.09792v1
- published: 2024-08-19

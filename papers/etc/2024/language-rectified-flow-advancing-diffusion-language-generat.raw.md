---
title: "Language Rectified Flow: Advancing Diffusion Language Generation with Probabilistic Flows"
authors: ["Shujian Zhang", "Lemeng Wu", "Chengyue Gong", "Xingchao Liu"]
venue: "NAACL"
year: 2024
venue_class: "etc"
arxiv_id: "2403.16995"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2403.16995v1"
published: "2024-03-25"
categories: ["cs.CL", "cs.AI", "cs.LG", "stat.ML"]
keywords: []
venue_source: "arxiv-comment"
hunter_fetched: "2026-04-15T05:20:02+09:00"
---

# Language Rectified Flow: Advancing Diffusion Language Generation with Probabilistic Flows

## Abstract
Recent works have demonstrated success in controlling sentence attributes ($e.g.$, sentiment) and structure ($e.g.$, syntactic structure) based on the diffusion language model. A key component that drives theimpressive performance for generating high-quality samples from noise is iteratively denoise for thousands of steps. While beneficial, the complexity of starting from the noise and the learning steps has limited its implementation to many NLP real-world applications. This paper proposes Language Rectified Flow ({\ours}). Our method is based on the reformulation of the standard probabilistic flow models. Language rectified flow learns (neural) ordinary differential equation models to transport between the source distribution and the target distribution, hence providing a unified and effective solution to generative modeling and domain transfer. From the source distribution, our language rectified flow yields fast simulation and effectively decreases the inference time. Experiments on three challenging fine-grained control tasks and multiple high-quality text editing show that our method consistently outperforms its baselines. Extensive experiments and ablation studies demonstrate that our method can be general, effective, and beneficial for many NLP tasks.

## Metadata
- venue: NAACL
- year: 2024
- authors: Shujian Zhang, Lemeng Wu, Chengyue Gong, Xingchao Liu
- arxiv_id: 2403.16995
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2403.16995v1
- published: 2024-03-25

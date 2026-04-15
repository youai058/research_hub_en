---
title: "ViLaD: A Large Vision Language Diffusion Framework for End-to-End Autonomous Driving"
authors: ["Can Cui", "Yupeng Zhou", "Juntong Peng", "Sung-Yeon Park", "Zichong Yang", "Prashanth Sankaranarayanan", "Jiaru Zhang", "Ruqi Zhang", "Ziran Wang"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2508.12603"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2508.12603v1"
published: "2025-08-18"
categories: ["cs.CV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:29+09:00"
---

# ViLaD: A Large Vision Language Diffusion Framework for End-to-End Autonomous Driving

## Abstract
End-to-end autonomous driving systems built on Vision Language Models (VLMs) have shown significant promise, yet their reliance on autoregressive architectures introduces some limitations for real-world applications. The sequential, token-by-token generation process of these models results in high inference latency and cannot perform bidirectional reasoning, making them unsuitable for dynamic, safety-critical environments. To overcome these challenges, we introduce ViLaD, a novel Large Vision Language Diffusion (LVLD) framework for end-to-end autonomous driving that represents a paradigm shift. ViLaD leverages a masked diffusion model that enables parallel generation of entire driving decision sequences, significantly reducing computational latency. Moreover, its architecture supports bidirectional reasoning, allowing the model to consider both past and future simultaneously, and supports progressive easy-first generation to iteratively improve decision quality. We conduct comprehensive experiments on the nuScenes dataset, where ViLaD outperforms state-of-the-art autoregressive VLM baselines in both planning accuracy and inference speed, while achieving a near-zero failure rate. Furthermore, we demonstrate the framework's practical viability through a real-world deployment on an autonomous vehicle for an interactive parking task, confirming its effectiveness and soundness for practical applications.

## Metadata
- venue: arXiv
- year: 2025
- authors: Can Cui, Yupeng Zhou, Juntong Peng, Sung-Yeon Park, Zichong Yang, Prashanth Sankaranarayanan, Jiaru Zhang, Ruqi Zhang, Ziran Wang
- arxiv_id: 2508.12603
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2508.12603v1
- published: 2025-08-18

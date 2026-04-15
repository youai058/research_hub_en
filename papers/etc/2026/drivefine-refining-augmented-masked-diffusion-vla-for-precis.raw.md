---
title: "DriveFine: Refining-Augmented Masked Diffusion VLA for Precise and Robust Driving"
authors: ["Chenxu Dang", "Sining Ang", "Yongkang Li", "Haochen Tian", "Jie Wang", "Guang Li", "Hangjun Ye", "Jie Ma", "Long Chen", "Yan Wang"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.14577"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.14577v1"
published: "2026-02-16"
categories: ["cs.CV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:13+09:00"
---

# DriveFine: Refining-Augmented Masked Diffusion VLA for Precise and Robust Driving

## Abstract
Vision-Language-Action (VLA) models for autonomous driving increasingly adopt generative planners trained with imitation learning followed by reinforcement learning. Diffusion-based planners suffer from modality alignment difficulties, low training efficiency, and limited generalization. Token-based planners are plagued by cumulative causal errors and irreversible decoding. In summary, the two dominant paradigms exhibit complementary strengths and weaknesses. In this paper, we propose DriveFine, a masked diffusion VLA model that combines flexible decoding with self-correction capabilities. In particular, we design a novel plug-and-play block-MoE, which seamlessly injects a refinement expert on top of the generation expert. By enabling explicit expert selection during inference and gradient blocking during training, the two experts are fully decoupled, preserving the foundational capabilities and generic patterns of the pretrained weights, which highlights the flexibility and extensibility of the block-MoE design. Furthermore, we design a hybrid reinforcement learning strategy that encourages effective exploration of refinement expert while maintaining training stability. Extensive experiments on NAVSIM v1, v2, and Navhard benchmarks demonstrate that DriveFine exhibits strong efficacy and robustness. The code will be released at https://github.com/MSunDYY/DriveFine.

## Metadata
- venue: arXiv
- year: 2026
- authors: Chenxu Dang, Sining Ang, Yongkang Li, Haochen Tian, Jie Wang, Guang Li, Hangjun Ye, Jie Ma, Long Chen, Yan Wang
- arxiv_id: 2602.14577
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.14577v1
- published: 2026-02-16

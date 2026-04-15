---
title: "WAM-Diff: A Masked Diffusion VLA Framework with MoE and Online Reinforcement Learning for Autonomous Driving"
authors: ["Mingwang Xu", "Jiahao Cui", "Feipeng Cai", "Hanlin Shang", "Zhihao Zhu", "Shan Luan", "Yifang Xu", "Neng Zhang", "Yaoyi Li", "Jia Cai", "Siyu Zhu"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2512.11872"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2512.11872v1"
published: "2025-12-06"
categories: ["cs.RO", "cs.AI", "cs.CV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:19+09:00"
---

# WAM-Diff: A Masked Diffusion VLA Framework with MoE and Online Reinforcement Learning for Autonomous Driving

## Abstract
End-to-end autonomous driving systems based on vision-language-action (VLA) models integrate multimodal sensor inputs and language instructions to generate planning and control signals. While autoregressive large language models and continuous diffusion policies are prevalent, the potential of discrete masked diffusion for trajectory generation remains largely unexplored. This paper presents WAM-Diff, a VLA framework that employs masked diffusion to iteratively refine a discrete sequence representing future ego-trajectories. Our approach features three key innovations: a systematic adaptation of masked diffusion for autonomous driving that supports flexible, non-causal decoding orders; scalable model capacity via a sparse MoE architecture trained jointly on motion prediction and driving-oriented visual question answering (VQA); and online reinforcement learning using Group Sequence Policy Optimization (GSPO) to optimize sequence-level driving rewards. Remarkably, our model achieves 91.0 PDMS on NAVSIM-v1 and 89.7 EPDMS on NAVSIM-v2, demonstrating the effectiveness of masked diffusion for autonomous driving. The approach provides a promising alternative to autoregressive and diffusion-based policies, supporting scenario-aware decoding strategies for trajectory generation. The code for this paper will be released publicly at: https://github.com/fudan-generative-vision/WAM-Diff

## Metadata
- venue: arXiv
- year: 2025
- authors: Mingwang Xu, Jiahao Cui, Feipeng Cai, Hanlin Shang, Zhihao Zhu, Shan Luan, Yifang Xu, Neng Zhang, Yaoyi Li, Jia Cai, Siyu Zhu
- arxiv_id: 2512.11872
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2512.11872v1
- published: 2025-12-06

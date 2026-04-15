---
title: "E0: Enhancing Generalization and Fine-Grained Control in VLA Models via Tweedie Discrete Diffusion"
authors: ["Zhihao Zhan", "Jiaying Zhou", "Likui Zhang", "Qinhan Lv", "Hao Liu", "Jusheng Zhang", "Weizheng Li", "Ziliang Chen", "Tianshui Chen", "Ruifeng Zhai", "Keze Wang", "Liang Lin", "Guangrun Wang"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2511.21542"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2511.21542v2"
published: "2025-11-26"
categories: ["cs.RO", "cs.AI", "cs.CV", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:33+09:00"
---

# E0: Enhancing Generalization and Fine-Grained Control in VLA Models via Tweedie Discrete Diffusion

## Abstract
Vision-Language-Action (VLA) models offer a unified framework for robotic manipulation by integrating visual perception, language understanding, and control generation. However, existing VLA systems still struggle to generalize across diverse tasks, scenes, and camera viewpoints, and often produce coarse or unstable actions. We argue that these limitations are closely tied to the structural properties of actions in VLA settings, including the inherent multi-peaked nature of action distributions, the token-based symbolic reasoning of pretrained VLM/VLA backbones, and the effective finite resolution imposed by real-world robotic control. Motivated by these properties, we introduce E0, a tweedie discrete diffusion framework that formulates action generation as iterative denoising over quantized action tokens. By operating in a discrete action space with a principled diffusion process, E0 naturally aligns with token-based reasoning, supports fine-grained yet executable action control, and avoids the distributional mismatch of masking-based discrete diffusion. We further introduce a spherical viewpoint perturbation augmentation to enhance robustness to camera shifts without additional data. Experiments on LIBERO, VLABench, ManiSkill, and a real-world Franka arm demonstrate that E0 achieves state-of-the-art performance across 14 diverse environments, outperforming strong baselines by 10.7% on average.

## Metadata
- venue: arXiv
- year: 2025
- authors: Zhihao Zhan, Jiaying Zhou, Likui Zhang, Qinhan Lv, Hao Liu, Jusheng Zhang, Weizheng Li, Ziliang Chen, Tianshui Chen, Ruifeng Zhai, Keze Wang, Liang Lin, Guangrun Wang
- arxiv_id: 2511.21542
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2511.21542v2
- published: 2025-11-26

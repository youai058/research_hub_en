---
title: "Discrete Diffusion for Reflective Vision-Language-Action Models in Autonomous Driving"
authors: ["Pengxiang Li", "Yinan Zheng", "Yue Wang", "Huimin Wang", "Hang Zhao", "Jingjing Liu", "Xianyuan Zhan", "Kun Zhan", "Xianpeng Lang"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2509.20109"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2509.20109v1"
published: "2025-09-24"
categories: ["cs.RO", "cs.AI", "cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:14+09:00"
---

# Discrete Diffusion for Reflective Vision-Language-Action Models in Autonomous Driving

## Abstract
End-to-End (E2E) solutions have emerged as a mainstream approach for autonomous driving systems, with Vision-Language-Action (VLA) models representing a new paradigm that leverages pre-trained multimodal knowledge from Vision-Language Models (VLMs) to interpret and interact with complex real-world environments. However, these methods remain constrained by the limitations of imitation learning, which struggles to inherently encode physical rules during training. Existing approaches often rely on complex rule-based post-refinement, employ reinforcement learning that remains largely limited to simulation, or utilize diffusion guidance that requires computationally expensive gradient calculations. To address these challenges, we introduce ReflectDrive, a novel learning-based framework that integrates a reflection mechanism for safe trajectory generation via discrete diffusion. We first discretize the two-dimensional driving space to construct an action codebook, enabling the use of pre-trained Diffusion Language Models for planning tasks through fine-tuning. Central to our approach is a safety-aware reflection mechanism that performs iterative self-correction without gradient computation. Our method begins with goal-conditioned trajectory generation to model multi-modal driving behaviors. Based on this, we apply local search methods to identify unsafe tokens and determine feasible solutions, which then serve as safe anchors for inpainting-based regeneration. Evaluated on the NAVSIM benchmark, ReflectDrive demonstrates significant advantages in safety-critical trajectory generation, offering a scalable and reliable solution for autonomous driving systems.

## Metadata
- venue: arXiv
- year: 2025
- authors: Pengxiang Li, Yinan Zheng, Yue Wang, Huimin Wang, Hang Zhao, Jingjing Liu, Xianyuan Zhan, Kun Zhan, Xianpeng Lang
- arxiv_id: 2509.20109
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2509.20109v1
- published: 2025-09-24

---
title: "Discrete Diffusion Models with MLLMs for Unified Medical Multimodal Generation"
authors: ["Jiawei Mao", "Yuhan Wang", "Lifeng Chen", "Can Zhao", "Yucheng Tang", "Dong Yang", "Liangqiong Qu", "Daguang Xu", "Yuyin Zhou"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.06131"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.06131v1"
published: "2025-10-07"
categories: ["cs.CV", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:40+09:00"
---

# Discrete Diffusion Models with MLLMs for Unified Medical Multimodal Generation

## Abstract
Recent advances in generative medical models are constrained by modality-specific scenarios that hinder the integration of complementary evidence from imaging, pathology, and clinical notes. This fragmentation limits their evolution into foundation models that can learn and reason across the full spectrum of biomedical data. We propose MeDiM, the first medical discrete diffusion model that learns shared distributions across modalities without modality-specific components. MeDiM unifies multiple generative tasks: translating between images and text, and jointly producing image-report pairs across domains in response to prompts. Built on a discrete diffusion framework, MeDiM bridges vision and language representations through a shared probabilistic space. To enable unified and flexible medical generation, we employ a multimodal large language model (MLLM) as the diffusion backbone, leveraging its prior knowledge and cross-modal reasoning. Two key designs are introduced: (1) removing the causal attention mask for bidirectional context, and (2) injecting continuous timestep embeddings for diffusion awareness. Experiments demonstrate high-fidelity medical generation (FID 16.60 on MIMIC-CXR and FID 24.19 on PathGen) and accurate report generation (METEOR 0.2650 and 0.2580). Jointly generated image-report pairs further enhance downstream performance (plus6.43 percent BLEU-1, plus18.57 percent BLEU-2, plus31.58 percent BLEU-3, plus4.80 percent METEOR), showing that MeDiM supports coherent and clinically grounded multimodal outputs.

## Metadata
- venue: arXiv
- year: 2025
- authors: Jiawei Mao, Yuhan Wang, Lifeng Chen, Can Zhao, Yucheng Tang, Dong Yang, Liangqiong Qu, Daguang Xu, Yuyin Zhou
- arxiv_id: 2510.06131
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.06131v1
- published: 2025-10-07

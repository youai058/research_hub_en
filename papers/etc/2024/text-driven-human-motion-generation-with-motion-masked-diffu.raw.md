---
title: "Text-driven Human Motion Generation with Motion Masked Diffusion Model"
authors: ["Xingyu Chen"]
venue: "arXiv"
year: 2024
venue_class: "etc"
arxiv_id: "2409.19686"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2409.19686v1"
published: "2024-09-29"
categories: ["cs.CV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:20:05+09:00"
---

# Text-driven Human Motion Generation with Motion Masked Diffusion Model

## Abstract
Text-driven human motion generation is a multimodal task that synthesizes human motion sequences conditioned on natural language. It requires the model to satisfy textual descriptions under varying conditional inputs, while generating plausible and realistic human actions with high diversity. Existing diffusion model-based approaches have outstanding performance in the diversity and multimodality of generation. However, compared to autoregressive methods that train motion encoders before inference, diffusion methods lack in fitting the distribution of human motion features which leads to an unsatisfactory FID score. One insight is that the diffusion model lack the ability to learn the motion relations among spatio-temporal semantics through contextual reasoning. To solve this issue, in this paper, we proposed Motion Masked Diffusion Model \textbf{(MMDM)}, a novel human motion masked mechanism for diffusion model to explicitly enhance its ability to learn the spatio-temporal relationships from contextual joints among motion sequences. Besides, considering the complexity of human motion data with dynamic temporal characteristics and spatial structure, we designed two mask modeling strategies: \textbf{time frames mask} and \textbf{body parts mask}. During training, MMDM masks certain tokens in the motion embedding space. Then, the diffusion decoder is designed to learn the whole motion sequence from masked embedding in each sampling step, this allows the model to recover a complete sequence from incomplete representations. Experiments on HumanML3D and KIT-ML dataset demonstrate that our mask strategy is effective by balancing motion quality and text-motion consistency.

## Metadata
- venue: arXiv
- year: 2024
- authors: Xingyu Chen
- arxiv_id: 2409.19686
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2409.19686v1
- published: 2024-09-29

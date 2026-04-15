---
title: "Towards GUI Agents: Vision-Language Diffusion Models for GUI Grounding"
authors: ["Shrinidhi Kumbhar", "Haofu Liao", "Srikar Appalaraju", "Kunwar Yashraj Singh"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.26211"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.26211v1"
published: "2026-03-27"
categories: ["cs.CV", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:24+09:00"
---

# Towards GUI Agents: Vision-Language Diffusion Models for GUI Grounding

## Abstract
Autoregressive (AR) vision-language models (VLMs) have long dominated multimodal understanding, reasoning, and graphical user interface (GUI) grounding. Recently, discrete diffusion vision-language models (DVLMs) have shown strong performance in multimodal reasoning, offering bidirectional attention, parallel token generation, and iterative refinement. However, their potential for GUI grounding remains unexplored. In this work, we evaluate whether discrete DVLMs can serve as a viable alternative to AR models for GUI grounding. We adapt LLaDA-V for single-turn action and bounding-box prediction, framing the task as text generation from multimodal input. To better capture the hierarchical structure of bounding-box geometry, we propose a hybrid masking schedule that combines linear and deterministic masking, improving grounding accuracy by up to 6.1 points in Step Success Rate (SSR) over the GUI-adapted LLaDA-V trained with linear masking. Evaluations on four datasets spanning web, desktop, and mobile interfaces show that the adapted diffusion model with hybrid masking consistently outperforms the linear-masked variant and performs competitively with autoregressive counterparts despite limited pretraining. Systematic ablations reveal that increasing diffusion steps, generation length, and block length improves accuracy but also increases latency, with accuracy plateauing beyond a certain number of diffusion steps. Expanding the training data with diverse GUI domains further reduces latency by about 1.3 seconds and improves grounding accuracy by an average of 20 points across benchmarks. These results demonstrate that discrete DVLMs are a promising modeling framework for GUI grounding and represent an important step toward diffusion-based GUI agents.

## Metadata
- venue: arXiv
- year: 2026
- authors: Shrinidhi Kumbhar, Haofu Liao, Srikar Appalaraju, Kunwar Yashraj Singh
- arxiv_id: 2603.26211
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.26211v1
- published: 2026-03-27

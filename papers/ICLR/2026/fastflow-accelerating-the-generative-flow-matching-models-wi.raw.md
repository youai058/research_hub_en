---
title: "FastFlow: Accelerating The Generative Flow Matching Models with Bandit Inference"
authors: ["Divya Jyoti Bajpai", "Dhruv Bhardwaj", "Soumya Roy", "Tejas Duseja", "Harsh Agarwal", "Aashay Sandansing", "Manjesh Kumar Hanawal"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "wWkyL8D9xd"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/81dc8cd081b769755d07987fd8e7826df5745e32.pdf"
published: "2026"
categories: []
keywords: ["generative modelling", "faster inference."]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:22+09:00"
---

# FastFlow: Accelerating The Generative Flow Matching Models with Bandit Inference

## Abstract
Flow-matching models deliver state-of-the-art fidelity in image and video generation, but the inherent sequential denoising process renders them slower. Existing acceleration methods like distillation, trajectory truncation, and consistency approaches are static, require retraining, and often fail to generalize across tasks. We propose FastFlow, a plug-and-play adaptive inference framework that accelerates generation in flow matching models. FastFlow identifies denoising steps that produce only minor adjustments to the denoising path and approximates them without using the full neural network models used for velocity predictions. The approximation utilizes finite-difference velocity estimates from prior predictions to efficiently extrapolate future states, enabling faster advancements along the denoising path at zero compute cost. This enables skipping computation at intermediary steps. We model the decision of how many steps to safely skip before requiring a full model computation as a multi-armed bandit problem. The bandit learns the optimal skips to balance speed with performance. FastFlow integrates seamlessly with existing pipelines and generalizes across image generation, video generation, and editing tasks. Experiments demonstrate a speedup of over $2.6\times$ while maintaining high-quality outputs. The source code for this work can be found at https://github.com/Div290/FastFlow.

## Metadata
- venue: ICLR
- year: 2026
- authors: Divya Jyoti Bajpai, Dhruv Bhardwaj, Soumya Roy, Tejas Duseja, Harsh Agarwal, Aashay Sandansing, Manjesh Kumar Hanawal
- arxiv_id: 
- openreview_id: wWkyL8D9xd
- anthology_id: 
- pdf_url: https://openreview.net/pdf/81dc8cd081b769755d07987fd8e7826df5745e32.pdf
- published: 2026
- keywords: generative modelling, faster inference.

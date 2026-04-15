---
title: "CANDI: Hybrid Discrete-Continuous Diffusion Models"
authors: ["Patrick Pynadath", "Jiaxin Shi", "Ruqi Zhang"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.22510"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.22510v2"
published: "2025-10-26"
categories: ["cs.LG", "stat.ML"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:22+09:00"
---

# CANDI: Hybrid Discrete-Continuous Diffusion Models

## Abstract
While continuous diffusion has shown remarkable success in continuous domains such as image generation, its direct application to discrete data has underperformed compared to purely discrete formulations. This gap is counterintuitive, given that continuous diffusion learns score functions that enable joint evolution across multiple positions. To understand this gap, we introduce token identifiability as an analytical framework for understanding how Gaussian noise corrupts discrete data through two mechanisms: discrete identity corruption and continuous rank degradation. We reveal that these mechanisms scale differently with vocabulary size, creating a temporal dissonance: at noise levels where discrete corruption preserves enough structure for conditional learning, continuous denoising is trivial; at noise levels where continuous denoising is meaningful, discrete corruption destroys nearly all conditional structure. To solve this, we propose CANDI (Continuous ANd DIscrete diffusion), a hybrid framework that decouples discrete and continuous corruption, enabling simultaneous learning of both conditional structure and continuous geometry. We empirically validate the temporal dissonance phenomenon and demonstrate that CANDI successfully avoids it. This unlocks the benefits of continuous diffusion for discrete spaces: on controlled generation, CANDI enables classifier-based guidance with off-the-shelf classifiers through simple gradient addition; on text generation, CANDI outperforms masked diffusion at low NFE, demonstrating the value of learning continuous gradients for discrete spaces. We include the code on the project page available here: https://patrickpynadath1.github.io/candi-lander

## Metadata
- venue: arXiv
- year: 2025
- authors: Patrick Pynadath, Jiaxin Shi, Ruqi Zhang
- arxiv_id: 2510.22510
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.22510v2
- published: 2025-10-26

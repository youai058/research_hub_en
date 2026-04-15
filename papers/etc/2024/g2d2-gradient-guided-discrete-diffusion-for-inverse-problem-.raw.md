---
title: "G2D2: Gradient-Guided Discrete Diffusion for Inverse Problem Solving"
authors: ["Naoki Murata", "Chieh-Hsin Lai", "Yuhta Takida", "Toshimitsu Uesaka", "Bac Nguyen", "Stefano Ermon", "Yuki Mitsufuji"]
venue: "arXiv"
year: 2024
venue_class: "etc"
arxiv_id: "2410.14710"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2410.14710v2"
published: "2024-10-09"
categories: ["cs.CV", "cs.AI", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:20:09+09:00"
---

# G2D2: Gradient-Guided Discrete Diffusion for Inverse Problem Solving

## Abstract
Recent literature has effectively leveraged diffusion models trained on continuous variables as priors for solving inverse problems. Notably, discrete diffusion models with discrete latent codes have shown strong performance, particularly in modalities suited for discrete compressed representations, such as image and motion generation. However, their discrete and non-differentiable nature has limited their application to inverse problems formulated in continuous spaces. This paper presents a novel method for addressing linear inverse problems by leveraging generative models based on discrete diffusion as priors. We overcome these limitations by approximating the true posterior distribution with a variational distribution constructed from categorical distributions and continuous relaxation techniques. Furthermore, we employ a star-shaped noise process to mitigate the drawbacks of traditional discrete diffusion models with absorbing states, demonstrating that our method performs comparably to continuous diffusion techniques with a lower GPU memory consumption. Our code is available at https://github.com/sony/g2d2.

## Metadata
- venue: arXiv
- year: 2024
- authors: Naoki Murata, Chieh-Hsin Lai, Yuhta Takida, Toshimitsu Uesaka, Bac Nguyen, Stefano Ermon, Yuki Mitsufuji
- arxiv_id: 2410.14710
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2410.14710v2
- published: 2024-10-09

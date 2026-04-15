---
title: "Derivative-Free Guidance in Continuous and Discrete Diffusion Models with Soft Value-Based Decoding"
authors: ["Xiner Li", "Yulai Zhao", "Chenyu Wang", "Gabriele Scalia", "Gokcen Eraslan", "Surag Nair", "Tommaso Biancalani", "Shuiwang Ji", "Aviv Regev", "Sergey Levine", "Masatoshi Uehara"]
venue: "arXiv"
year: 2024
venue_class: "etc"
arxiv_id: "2408.08252"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2408.08252v5"
published: "2024-08-15"
categories: ["cs.LG", "cs.AI", "q-bio.GN", "stat.ML"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:20:12+09:00"
---

# Derivative-Free Guidance in Continuous and Discrete Diffusion Models with Soft Value-Based Decoding

## Abstract
Diffusion models excel at capturing the natural design spaces of images, molecules, DNA, RNA, and protein sequences. However, rather than merely generating designs that are natural, we often aim to optimize downstream reward functions while preserving the naturalness of these design spaces. Existing methods for achieving this goal often require ``differentiable'' proxy models (\textit{e.g.}, classifier guidance or DPS) or involve computationally expensive fine-tuning of diffusion models (\textit{e.g.}, classifier-free guidance, RL-based fine-tuning). In our work, we propose a new method to address these challenges. Our algorithm is an iterative sampling method that integrates soft value functions, which looks ahead to how intermediate noisy states lead to high rewards in the future, into the standard inference procedure of pre-trained diffusion models. Notably, our approach avoids fine-tuning generative models and eliminates the need to construct differentiable models. This enables us to (1) directly utilize non-differentiable features/reward feedback, commonly used in many scientific domains, and (2) apply our method to recent discrete diffusion models in a principled way. Finally, we demonstrate the effectiveness of our algorithm across several domains, including image generation, molecule generation, and DNA/RNA sequence generation. The code is available at \href{https://github.com/masa-ue/SVDD}{https://github.com/masa-ue/SVDD}.

## Metadata
- venue: arXiv
- year: 2024
- authors: Xiner Li, Yulai Zhao, Chenyu Wang, Gabriele Scalia, Gokcen Eraslan, Surag Nair, Tommaso Biancalani, Shuiwang Ji, Aviv Regev, Sergey Levine, Masatoshi Uehara
- arxiv_id: 2408.08252
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2408.08252v5
- published: 2024-08-15

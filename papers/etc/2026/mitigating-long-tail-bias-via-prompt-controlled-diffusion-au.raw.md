---
title: "Mitigating Long-Tail Bias via Prompt-Controlled Diffusion Augmentation"
authors: ["Buddhi Wijenayake", "Nichula Wasalathilake", "Roshan Godaliyadda", "Vijitha Herath", "Parakrama Ekanayake", "Vishal M. Patel"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.04749"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.04749v1"
published: "2026-02-04"
categories: ["cs.CV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:32+09:00"
---

# Mitigating Long-Tail Bias via Prompt-Controlled Diffusion Augmentation

## Abstract
Semantic segmentation of high-resolution remote-sensing imagery is critical for urban mapping and land-cover monitoring, yet training data typically exhibits severe long-tailed pixel imbalance. In the dataset LoveDA, this challenge is compounded by an explicit Urban/Rural split with distinct appearance and inconsistent class-frequency statistics across domains. We present a prompt-controlled diffusion augmentation framework that synthesizes paired label--image samples with explicit control of both domain and semantic composition. Stage~A uses a domain-aware, masked ratio-conditioned discrete diffusion model to generate layouts that satisfy user-specified class-ratio targets while respecting learned co-occurrence structure. Stage~B translates layouts into photorealistic, domain-consistent images using Stable Diffusion with ControlNet guidance. Mixing the resulting ratio and domain-controlled synthetic pairs with real data yields consistent improvements across multiple segmentation backbones, with gains concentrated on minority classes and improved Urban and Rural generalization, demonstrating controllable augmentation as a practical mechanism to mitigate long-tail bias in remote-sensing segmentation. Source codes, pretrained models, and synthetic datasets are available at \href{https://github.com/Buddhi19/SyntheticGen.git}{Github}

## Metadata
- venue: arXiv
- year: 2026
- authors: Buddhi Wijenayake, Nichula Wasalathilake, Roshan Godaliyadda, Vijitha Herath, Parakrama Ekanayake, Vishal M. Patel
- arxiv_id: 2602.04749
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.04749v1
- published: 2026-02-04

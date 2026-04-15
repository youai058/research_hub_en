---
title: "Breaking the Factorization Barrier in Diffusion Language Models"
authors: ["Ian Li", "Zilei Shao", "Benjie Wang", "Rose Yu", "Guy Van den Broeck", "Anji Liu"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.00045"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.00045v2"
published: "2026-02-09"
categories: ["cs.LG", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:05+09:00"
---

# Breaking the Factorization Barrier in Diffusion Language Models

## Abstract
Diffusion language models theoretically allow for efficient parallel generation but are practically hindered by the "factorization barrier": the assumption that simultaneously predicted tokens are independent. This limitation forces a trade-off: models must either sacrifice speed by resolving dependencies sequentially or suffer from incoherence due to factorization. We argue that this barrier arises not from limited backbone expressivity, but from a structural misspecification: models are restricted to fully factorized outputs because explicitly parameterizing a joint distribution would require the Transformer to output a prohibitively large number of parameters. We propose Coupled Discrete Diffusion (CoDD), a hybrid framework that breaks this barrier by replacing the fully-factorized output distribution with a lightweight, tractable probabilistic inference layer. This formulation yields a distribution family that is significantly more expressive than standard factorized priors, enabling the modeling of complex joint dependencies, yet remains compact enough to avoid the prohibitive parameter explosion associated with full joint modeling. Empirically, CoDD seamlessly enhances diverse diffusion language model architectures with negligible overhead, matching the reasoning performance of computationally intensive Reinforcement Learning baselines at a fraction of the training cost. Furthermore, it prevents performance collapse in few-step generation, enabling high-quality outputs at significantly reduced latencies. Code available at: https://github.com/liuanji/CoDD

## Metadata
- venue: arXiv
- year: 2026
- authors: Ian Li, Zilei Shao, Benjie Wang, Rose Yu, Guy Van den Broeck, Anji Liu
- arxiv_id: 2603.00045
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.00045v2
- published: 2026-02-09

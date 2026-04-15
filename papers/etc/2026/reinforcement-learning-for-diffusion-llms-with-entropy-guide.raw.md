---
title: "Reinforcement Learning for Diffusion LLMs with Entropy-Guided Step Selection and Stepwise Advantages"
authors: ["Vishnu Teja Kunde", "Fatemeh Doudi", "Mahdi Farahbakhsh", "Dileep Kalathil", "Krishna Narayanan", "Jean-Francois Chamberland"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.12554"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.12554v1"
published: "2026-03-13"
categories: ["cs.LG", "cs.AI", "cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:13:58+09:00"
---

# Reinforcement Learning for Diffusion LLMs with Entropy-Guided Step Selection and Stepwise Advantages

## Abstract
Reinforcement learning (RL) has been effective for post-training autoregressive (AR) language models, but extending these methods to diffusion language models (DLMs) is challenging due to intractable sequence-level likelihoods. Existing approaches therefore rely on surrogate likelihoods or heuristic approximations, which can introduce bias and obscure the sequential structure of denoising. We formulate diffusion-based sequence generation as a finite-horizon Markov decision process over the denoising trajectory and derive an exact, unbiased policy gradient that decomposes over denoising steps and is expressed in terms of intermediate advantages, without requiring explicit evaluation of the sequence likelihood. To obtain a practical and compute-efficient estimator, we (i) select denoising steps for policy updates via an entropy-guided approximation bound, and (ii) estimate intermediate advantages using a one-step denoising reward naturally provided by the diffusion model, avoiding costly multi-step rollouts. Experiments on coding and logical reasoning benchmarks demonstrate state-of-the-art results, with strong competitive performance on mathematical reasoning, outperforming existing RL post-training approaches for DLMs. Code is available at https://github.com/vishnutez/egspo-dllm-rl.

## Metadata
- venue: arXiv
- year: 2026
- authors: Vishnu Teja Kunde, Fatemeh Doudi, Mahdi Farahbakhsh, Dileep Kalathil, Krishna Narayanan, Jean-Francois Chamberland
- arxiv_id: 2603.12554
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.12554v1
- published: 2026-03-13

---
title: "DiFFPO: Training Diffusion LLMs to Reason Fast and Furious via Reinforcement Learning"
authors: ["Hanyang Zhao", "Dawen Liang", "Wenpin Tang", "David Yao", "Nathan Kallus"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.02212"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.02212v2"
published: "2025-10-02"
categories: ["cs.LG", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:10+09:00"
---

# DiFFPO: Training Diffusion LLMs to Reason Fast and Furious via Reinforcement Learning

## Abstract
We propose DiFFPO, Diffusion Fast and Furious Policy Optimization, a unified framework for training masked diffusion large language models (dLLMs) to reason not only better (furious), but also faster via reinforcement learning (RL). We first unify the existing baseline approach such as d1 by proposing to train surrogate policies via off-policy RL, whose likelihood is much more tractable as an approximation to the true dLLM policy. This naturally motivates a more accurate and informative two-stage likelihood approximation combined with importance sampling correction, which leads to generalized RL algorithms with better sample efficiency and superior task performance. Second, we propose a new direction of joint training efficient samplers/controllers of dLLMs policy. Via RL, we incentivize dLLMs' natural multi-token prediction capabilities by letting the model learn to adaptively allocate an inference threshold for each prompt. By jointly training the sampler, we yield better accuracies with lower number of function evaluations (NFEs) compared to training the model only, obtaining the best performance in improving the Pareto frontier of the inference-time compute of dLLMs. We showcase the effectiveness of our pipeline by training open source large diffusion language models over benchmark math and planning tasks.

## Metadata
- venue: arXiv
- year: 2025
- authors: Hanyang Zhao, Dawen Liang, Wenpin Tang, David Yao, Nathan Kallus
- arxiv_id: 2510.02212
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.02212v2
- published: 2025-10-02

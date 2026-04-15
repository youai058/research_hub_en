---
title: "Taming Masked Diffusion Language Models via Consistency Trajectory Reinforcement Learning with Fewer Decoding Step"
authors: ["Jingyi Yang", "Guanxu Chen", "Xuhao Hu", "Jing Shao"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2509.23924"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2509.23924v1"
published: "2025-09-28"
categories: ["cs.CL", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:14+09:00"
---

# Taming Masked Diffusion Language Models via Consistency Trajectory Reinforcement Learning with Fewer Decoding Step

## Abstract
Masked diffusion language models (MDLMs) have recently emerged as a promising alternative to autoregressive (AR) language models, offering properties such as parallel decoding, flexible generation orders, and the potential for fewer inference steps. Despite these advantages, decoding strategies and reinforcement learning (RL) algorithms tailored for MDLMs remain underexplored. A naive approach is to directly transfer techniques well-established for AR models to MDLMs. However, this raises an immediate question: Is such a naive transfer truly optimal? For example, 1) Block-wise and semi-AR decoding strategies are not employed during the training of MDLMs, so why do they outperform full diffusion-style decoding during inference? 2) Applying RL algorithms designed for AR models directly to MDLMs exhibits a training-inference inconsistency, since MDLM decoding are non-causal (parallel). This results in inconsistencies between the rollout trajectory and the optimization trajectory. To address these challenges, we propose EOS Early Rejection (EOSER) and Ascending Step-Size (ASS) decoding scheduler, which unlock the potential of MDLMs to perform full diffusion-style decoding, achieving competitive performance with fewer decoding steps. Additionally, we introduce Consistency Trajectory Group Relative Policy Optimization (CJ-GRPO) for taming MDLMs, which emphasizes the consistency between rollout trajectory and optimization trajectory, and reduces the optimization errors caused by skip-step optimization. We conduct extensive experiments on reasoning tasks, such as mathematical and planning benchmarks, using LLaDA-8B-Instruct. The results demonstrate that the proposed EOSER and ASS mechanisms, together with CJ-GRPO, hold significant promise for effectively and efficiently taming MDLMs. Code: https://github.com/yjyddq/EOSER-ASS-RL.

## Metadata
- venue: arXiv
- year: 2025
- authors: Jingyi Yang, Guanxu Chen, Xuhao Hu, Jing Shao
- arxiv_id: 2509.23924
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2509.23924v1
- published: 2025-09-28

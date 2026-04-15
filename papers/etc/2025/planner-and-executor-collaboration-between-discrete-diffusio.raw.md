---
title: "Planner and Executor: Collaboration between Discrete Diffusion And Autoregressive Models in Reasoning"
authors: ["Lina Berrayana", "Ahmed Heakl", "Muhammad Abdullah Sohail", "Thomas Hofmann", "Salman Khan", "Wei Chen"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.15244"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.15244v2"
published: "2025-10-17"
categories: ["cs.CL", "cs.AI", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:10+09:00"
---

# Planner and Executor: Collaboration between Discrete Diffusion And Autoregressive Models in Reasoning

## Abstract
Current autoregressive language models (ARMs) achieve high accuracy but require long token sequences, making them costly. Discrete diffusion language models (DDLMs) enable parallel and flexible generation within a fixed number of steps and have recently emerged for their strong performance in complex reasoning and long-term planning tasks. We present a study exploring hybrid architectures that couple DDLMs with ARMs to assess whether their collaboration can yield complementary benefits. We first examine collaboration in text space, where one model plans the reasoning process and another executes the final answer based on that plan. We then extend this setup to latent-space communication, introducing a learned projector that maps DDLM latents into the ARM's embedding space, potentially bypassing some of the text-generation limitations of diffusion models. We find that shifting DDLM --> ARM communication from text space to latent space yields significant accuracy gains, for example increasing from 27.0% to 54.0% on DART-5 and from 0.0% to 14.0% on AIME24. We also find that combining a DDLM planner with an ARM executor can provide substantial computational savings with little to no impact on accuracy. For example, the latent-space pipeline, using 64 tokens for planning and roughly 5 for execution, surpasses Qwen3.1-7B on DART-5 and AIME, despite Qwen using 44 times more tokens. Overall, our study offers new insights into reasoning with DDLMs and highlights their potential in hybrid architectures.

## Metadata
- venue: arXiv
- year: 2025
- authors: Lina Berrayana, Ahmed Heakl, Muhammad Abdullah Sohail, Thomas Hofmann, Salman Khan, Wei Chen
- arxiv_id: 2510.15244
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.15244v2
- published: 2025-10-17

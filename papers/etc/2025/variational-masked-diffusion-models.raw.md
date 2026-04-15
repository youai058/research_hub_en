---
title: "Variational Masked Diffusion Models"
authors: ["Yichi Zhang", "Alex Schwing", "Zhizhen Zhao"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.23606"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.23606v1"
published: "2025-10-27"
categories: ["cs.LG", "cs.AI", "cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:22+09:00"
---

# Variational Masked Diffusion Models

## Abstract
Masked diffusion models have recently emerged as a flexible framework for discrete generative modeling. However, a key limitation of standard masked diffusion is its inability to effectively capture dependencies among tokens that are predicted concurrently, leading to degraded generation quality when dependencies among tokens are important. To explicitly model dependencies among tokens, we propose Variational Masked Diffusion (VMD), a framework that introduces latent variables into the masked diffusion process. Through controlled experiments on synthetic datasets, we demonstrate that VMD successfully learns dependencies that conventional masked diffusion fails to capture. We further validate the effectiveness of our approach on Sudoku puzzles and text datasets, where learning of dependencies among tokens improves global consistency. Across these domains, VMD enhances both generation quality and dependency awareness, highlighting the value of integrating variational inference into masked diffusion. Our code is available at: https://riccizz.github.io/VMD.

## Metadata
- venue: arXiv
- year: 2025
- authors: Yichi Zhang, Alex Schwing, Zhizhen Zhao
- arxiv_id: 2510.23606
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.23606v1
- published: 2025-10-27

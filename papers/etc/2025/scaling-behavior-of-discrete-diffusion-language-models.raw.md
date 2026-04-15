---
title: "Scaling Behavior of Discrete Diffusion Language Models"
authors: ["Dimitri von Rütte", "Janis Fluri", "Omead Pooladzandi", "Bernhard Schölkopf", "Thomas Hofmann", "Antonio Orvieto"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2512.10858"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2512.10858v3"
published: "2025-12-11"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:03+09:00"
---

# Scaling Behavior of Discrete Diffusion Language Models

## Abstract
Modern LLM pre-training consumes vast amounts of compute and training data, making the scaling behavior, or scaling laws, of different models a key distinguishing factor. Discrete diffusion language models (DLMs) have been proposed as an alternative to autoregressive language models (ALMs). However, their scaling behavior has not yet been fully explored, with prior work suggesting that they require more data and compute to match the performance of ALMs.
  We study the scaling behavior of DLMs on different noise types by smoothly interpolating between masked and uniform diffusion while paying close attention to crucial hyperparameters such as batch size and learning rate. Our experiments reveal that the scaling behavior of DLMs strongly depends on the noise type and is considerably different from ALMs. While all noise types converge to similar loss values in compute-bound scaling, we find that uniform diffusion requires more parameters and less data for compute-efficient training compared to masked diffusion, making them a promising candidate in data-bound settings. We scale our uniform diffusion model up to 10B parameters trained for $10^{22}$ FLOPs, confirming the predicted scaling behavior and making it the largest publicly known uniform diffusion model to date.

## Metadata
- venue: arXiv
- year: 2025
- authors: Dimitri von Rütte, Janis Fluri, Omead Pooladzandi, Bernhard Schölkopf, Thomas Hofmann, Antonio Orvieto
- arxiv_id: 2512.10858
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2512.10858v3
- published: 2025-12-11

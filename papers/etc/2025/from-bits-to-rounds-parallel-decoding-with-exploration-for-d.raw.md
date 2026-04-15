---
title: "From Bits to Rounds: Parallel Decoding with Exploration for Diffusion Language Models"
authors: ["Hengyu Fu", "Baihe Huang", "Virginia Adams", "Charles Wang", "Venkat Srinivasan", "Jiantao Jiao"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2511.21103"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2511.21103v1"
published: "2025-11-26"
categories: ["cs.LG", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:03+09:00"
---

# From Bits to Rounds: Parallel Decoding with Exploration for Diffusion Language Models

## Abstract
Diffusion Language Models (DLMs) have recently emerged as a strong alternative to autoregressive language models (LMs). DLMs offer comparable accuracy with faster inference speed via parallel decoding. However, standard DLM decoding strategies relying on high-confidence tokens encounter an inherent information-theoretic bottleneck that restricts decoding progress and ultimately slows generation. We demonstrate both theoretically and empirically that prioritizing high-confidence tokens is inherently inefficient. High-probability tokens carry negligible information and strictly relying on them limits the effective progress made in each decoding round. We prove that the number of decoding rounds must grow linearly with the sample's total information (negative log-likelihood) and inversely with the per-round information budget, establishing a bits-to-rounds principle. We also propose Explore-Then-Exploit (ETE), a training-free decoding strategy that maximizes information throughput and decoding efficiency. ETE combines cross-block decoding with targeted exploration of high-uncertainty tokens to reshape the conditional distribution and trigger cascades of confident predictions. Experiments verify our theoretical bounds and demonstrate that ETE consistently reduces the required number of decoding rounds compared to confidence-only baselines without compromising generation quality.

## Metadata
- venue: arXiv
- year: 2025
- authors: Hengyu Fu, Baihe Huang, Virginia Adams, Charles Wang, Venkat Srinivasan, Jiantao Jiao
- arxiv_id: 2511.21103
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2511.21103v1
- published: 2025-11-26

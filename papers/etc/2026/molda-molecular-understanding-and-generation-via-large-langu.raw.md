---
title: "MolDA: Molecular Understanding and Generation via Large Language Diffusion Model"
authors: ["Seohyeon Shin", "HanJun Choi", "Jun-Hyung Park", "Hong Kook Kim", "Mansu Kim"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2604.04403"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2604.04403v2"
published: "2026-04-06"
categories: ["cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:09+09:00"
---

# MolDA: Molecular Understanding and Generation via Large Language Diffusion Model

## Abstract
Large Language Models (LLMs) have significantly advanced molecular discovery, but existing multimodal molecular architectures fundamentally rely on autoregressive (AR) backbones. This strict left-to-right inductive bias is sub-optimal for generating chemically valid molecules, as it struggles to account for non-local global constraints (e.g., ring closures) and often accumulates structural errors during sequential generation. To address these limitations, we propose MolDA (Molecular language model with masked Diffusion with mAsking), a novel multimodal framework that replaces the conventional AR backbone with a discrete Large Language Diffusion Model. MolDA extracts comprehensive structural representations using a hybrid graph encoder, which captures both local and global topologies, and aligns them into the language token space via a Q-Former. Furthermore, we mathematically reformulate Molecular Structure Preference Optimization specifically for the masked diffusion. Through bidirectional iterative denoising, MolDA ensures global structural coherence, chemical validity, and robust reasoning across molecule generation, captioning, and property prediction.

## Metadata
- venue: arXiv
- year: 2026
- authors: Seohyeon Shin, HanJun Choi, Jun-Hyung Park, Hong Kook Kim, Mansu Kim
- arxiv_id: 2604.04403
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2604.04403v2
- published: 2026-04-06

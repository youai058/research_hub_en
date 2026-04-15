---
title: "Discrete Stochastic Localization for Non-autoregressive Generation"
authors: ["Yunshu Wu", "Jiayi Cheng", "Partha Thakuria", "Rob Brekelmans", "Evangelos E. Papalexakis", "Greg Ver Steeg"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.16169"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.16169v1"
published: "2026-02-18"
categories: ["cs.LG", "cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:02+09:00"
---

# Discrete Stochastic Localization for Non-autoregressive Generation

## Abstract
Non-autoregressive (NAR) generation reduces decoding latency by predicting many tokens in parallel, but iterative refinement often suffers from error accumulation and distribution shift under self-generated drafts. Masked diffusion language models (MDLMs) and their remasking samplers (e.g., ReMDM) can be viewed as modern NAR iterative refinement, where generation repeatedly revises a partially observed draft. In this work we show that \emph{training alone} can substantially improve the step-efficiency of MDLM/ReMDM sampling. We propose \textsc{DSL} (Discrete Stochastic Localization), which trains a single SNR-invariant denoiser across a continuum of corruption levels, bridging intermediate draft noise and mask-style endpoint corruption within one Diffusion Transformer. On OpenWebText, \textsc{DSL} fine-tuning yields large MAUVE gains at low step budgets, surpassing the MDLM+ReMDM baseline with \(\sim\)4$\times$ fewer denoiser evaluations, and matches autoregressive quality at high budgets. Analyses show improved self-correction and uncertainty calibration, making remasking markedly more compute-efficient.

## Metadata
- venue: arXiv
- year: 2026
- authors: Yunshu Wu, Jiayi Cheng, Partha Thakuria, Rob Brekelmans, Evangelos E. Papalexakis, Greg Ver Steeg
- arxiv_id: 2602.16169
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.16169v1
- published: 2026-02-18

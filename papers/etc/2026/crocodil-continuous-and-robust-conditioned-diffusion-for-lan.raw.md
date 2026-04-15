---
title: "CRoCoDiL: Continuous and Robust Conditioned Diffusion for Language"
authors: ["Roy Uziel", "Omer Belhasin", "Itay Levi", "Akhiad Bercovich", "Ran El-Yaniv", "Ran Zilberstein", "Michael Elad"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.20210"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.20210v2"
published: "2026-03-02"
categories: ["cs.CL", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:09+09:00"
---

# CRoCoDiL: Continuous and Robust Conditioned Diffusion for Language

## Abstract
Masked Diffusion Models (MDMs) provide an efficient non-causal alternative to autoregressive generation but often struggle with token dependencies and semantic incoherence due to their reliance on discrete marginal distributions. We address these limitations by shifting the diffusion process into a continuous sentence-level semantic space. We propose CRoCoDiL (Continuous and Robust Conditioned Diffusion for Language), a unified fine-tuning approach that jointly trains an encoder-demasker architecture, grounding the MDM demasking in continuous latent representations. This leads to the formation of a novel autoencoder in which decoding is obtained by an MDM algorithm. Relying on the same framework, we introduce two unconditional text synthesis algorithms: Continuous-Then-Discrete (ConThenDisc), a hybrid-diffusion approach that first generates latent representations in continuous space and then decodes these to tokens via an MDM, and Continuous-Within-Discrete (ConWithinDisc), a multi-diffusion strategy that refines latent representations throughout the discrete sampling process. Experiments using LLaDA show that our methods achieve superior generation quality and more than 10x faster sampling speeds in an unconditional setting.

## Metadata
- venue: arXiv
- year: 2026
- authors: Roy Uziel, Omer Belhasin, Itay Levi, Akhiad Bercovich, Ran El-Yaniv, Ran Zilberstein, Michael Elad
- arxiv_id: 2603.20210
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.20210v2
- published: 2026-03-02

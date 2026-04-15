---
title: "Spectral Learning of Shared Dynamics Between Generalized-Linear Processes"
authors: ["Lucine L Oganesian", "Omid G. Sani", "Maryam Shanechi"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "DupvYqqlAG"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b3d55867c578a5270a152b2f0d3b6a4728fbfb10.pdf"
published: "2024"
categories: []
keywords: ["state space models", "subspace identification", "dynamical systems", "neural coding", "generalized-linear models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:54+09:00"
---

# Spectral Learning of Shared Dynamics Between Generalized-Linear Processes

## Abstract
Generalized-linear dynamical models (GLDMs) remain a widely-used framework within neuroscience for modeling time-series data, such as neural spiking activity or categorical decision outcomes. Whereas the standard usage of GLDMs is to model a single data source, certain applications require jointly modeling two generalized-linear time-series sources while also dissociating their shared and private dynamics. Most existing GLDM variants and their associated learning algorithms do not support this capability. Here we address this challenge by developing a multi-step analytical subspace identification algorithm for learning a GLDM that explicitly models shared vs. private dynamics within two generalized-linear time-series. In simulations, we demonstrate our algorithm's ability to dissociate and model the dynamics within two time-series sources while being agnostic to their respective observation distributions. In neural data, we consider two specific applications of our algorithm for modeling discrete population spiking activity with respect to a secondary time-series. In both synthetic and real data, GLDMs learned with our algorithm more accurately decoded one time-series from the other using lower-dimensional latent states, as compared to models identified using existing GLDM learning algorithms.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Lucine L Oganesian, Omid G. Sani, Maryam Shanechi
- arxiv_id: 
- openreview_id: DupvYqqlAG
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b3d55867c578a5270a152b2f0d3b6a4728fbfb10.pdf
- published: 2024
- keywords: state space models, subspace identification, dynamical systems, neural coding, generalized-linear models

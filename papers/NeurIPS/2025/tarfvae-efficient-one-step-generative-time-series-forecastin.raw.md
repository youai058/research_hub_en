---
title: "TARFVAE: Efficient One-Step Generative Time Series Forecasting via TARFLOW based VAE"
authors: ["Jiawen Wei", "Lan Jiang", "Pengbo Wei", "Ziwen Ye", "Teng Song", "Chen Chen", "Guangrui Ma"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "3hnqwOq7iT"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e32a3d4146a338433c4344c0c5e14a578d507130.pdf"
published: "2025"
categories: []
keywords: ["time series forecasting", "generative model", "normalizing flow", "variational autoencoder"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:46+09:00"
---

# TARFVAE: Efficient One-Step Generative Time Series Forecasting via TARFLOW based VAE

## Abstract
Time series data is ubiquitous, with forecasting applications spanning from finance to healthcare. Beyond popular deterministic methods, generative models are gaining attention due to advancements in areas like image synthesis and video generation, as well as their inherent ability to provide probabilistic predictions. However, existing generative approaches mostly involve recurrent generative operations or repeated denoising steps, making the prediction laborious, particularly for long-term forecasting. Most of them only conduct experiments for relatively short-term forecasting, with limited comparison to deterministic methods in long-term forecasting, leaving their practical advantages unclear. This paper presents TARFVAE, a novel generative framework that combines the Transformer-based autoregressive flow (TARFLOW) and variational autoencoder (VAE) for efficient one-step generative time series forecasting. Inspired by the rethinking that complex architectures for extracting time series representations might not be necessary, we add a flow module, TARFLOW, to VAE to promote spontaneous learning of latent variables that benefit predictions. TARFLOW enhances VAE's posterior estimation by breaking the Gaussian assumption, thereby enabling a more informative latent space. TARFVAE uses only the forward process of TARFLOW, avoiding autoregressive inverse operations and thus ensuring fast generation. During generation, it samples from the prior latent space and directly generates full-horizon forecasts via the VAE decoder. With simple MLP modules, TARFVAE achieves superior performance over state-of-the-art deterministic and generative models across different forecast horizons on benchmark datasets while maintaining efficient prediction speed, demonstrating its effectiveness as an efficient and powerful solution for generative time series forecasting. Our code is available at https://github.com/Gavine77/TARFVAE.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Jiawen Wei, Lan Jiang, Pengbo Wei, Ziwen Ye, Teng Song, Chen Chen, Guangrui Ma
- arxiv_id: 
- openreview_id: 3hnqwOq7iT
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e32a3d4146a338433c4344c0c5e14a578d507130.pdf
- published: 2025
- keywords: time series forecasting, generative model, normalizing flow, variational autoencoder

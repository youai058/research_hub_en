---
title: "Reverse Diffusion Monte Carlo"
authors: ["Xunpeng Huang", "Hanze Dong", "Yifan HAO", "Yian Ma", "Tong Zhang"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "kIPEyMSdFV"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/5e05dd8867eb805ba66920ee894e0234bbfd718d.pdf"
published: "2024"
categories: []
keywords: ["posterior Sampling", "multi-modal sampling", "diffusion process"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:12+09:00"
---

# Reverse Diffusion Monte Carlo

## Abstract
We propose a Monte Carlo sampler from the reverse diffusion process. Unlike the practice of diffusion models, where the intermediary updates---the score functions---are learned with a neural network, we transform the score matching problem into a mean estimation one.
By estimating the means of the regularized posterior distributions, we derive a novel Monte Carlo sampling algorithm called reverse diffusion Monte Carlo (rdMC), which is distinct from the Markov chain Monte Carlo (MCMC) methods. We determine the sample size from the error tolerance and the properties of the posterior distribution to yield an algorithm that can approximately sample the target distribution with any desired accuracy. Additionally, we demonstrate and prove under suitable conditions that sampling with rdMC can be significantly faster than that with MCMC.  For multi-modal target distributions such as those in Gaussian mixture models, rdMC greatly improves over the Langevin-style MCMC sampling methods both theoretically and in practice. The proposed rdMC method offers a new perspective and solution beyond classical MCMC algorithms for the challenging complex distributions.

## Metadata
- venue: ICLR
- year: 2024
- authors: Xunpeng Huang, Hanze Dong, Yifan HAO, Yian Ma, Tong Zhang
- arxiv_id: 
- openreview_id: kIPEyMSdFV
- anthology_id: 
- pdf_url: https://openreview.net/pdf/5e05dd8867eb805ba66920ee894e0234bbfd718d.pdf
- published: 2024
- keywords: posterior Sampling, multi-modal sampling, diffusion process

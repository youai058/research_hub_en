---
title: "Diffusion Models are Secretly Exchangeable: Parallelizing DDPMs via Auto Speculation"
authors: ["Hengyuan Hu", "Aniket Das", "Dorsa Sadigh", "Nima Anari"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "n08niE37ku"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a854b554c55b1c18405d22def69ae94a8de75115.pdf"
published: "2025"
categories: []
keywords: ["DDPM", "Stochastic Localization", "speculative decoding"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:38+09:00"
---

# Diffusion Models are Secretly Exchangeable: Parallelizing DDPMs via Auto Speculation

## Abstract
Denoising Diffusion Probabilistic Models (DDPMs) have emerged as powerful tools for generative modeling. However, their sequential computation requirements lead to significant inference-time bottlenecks. In this work, we utilize the connection between DDPMs and Stochastic Localization to prove that, under an appropriate reparametrization, the increments of DDPM satisfy an exchangeability property. This general insight enables near-black-box adaptation of various performance optimization techniques from autoregressive models to the diffusion setting. To demonstrate this, we introduce _Autospeculative Decoding_ (ASD), an extension of the widely used speculative decoding algorithm to DDPMs that does not require any auxiliary draft models. Our theoretical analysis shows that ASD achieves a $\tilde{O}(K^{\frac{1}{3}})$ parallel runtime speedup over the $K$ step sequential DDPM. We also demonstrate that a practical implementation of autospeculative decoding accelerates DDPM inference significantly in various domains.

## Metadata
- venue: ICML
- year: 2025
- authors: Hengyuan Hu, Aniket Das, Dorsa Sadigh, Nima Anari
- arxiv_id: 
- openreview_id: n08niE37ku
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a854b554c55b1c18405d22def69ae94a8de75115.pdf
- published: 2025
- keywords: DDPM, Stochastic Localization, speculative decoding

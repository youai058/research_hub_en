---
title: "LSCD: Lomb--Scargle Conditioned Diffusion for Time series Imputation"
authors: ["Elizabeth Fons", "Alejandro Sztrajman", "Yousef El-Laham", "Luciana Ferrer", "Svitlana Vyetrenko", "Manuela Veloso"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "GdYg0Ohx0k"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/12163661cd94ad6155e664a40a68f76bbc2a817c.pdf"
published: "2025"
categories: []
keywords: ["time series", "diffusion models", "frequency spectrum"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:03+09:00"
---

# LSCD: Lomb--Scargle Conditioned Diffusion for Time series Imputation

## Abstract
Time series with missing or irregularly sampled data are a persistent challenge in machine learning. Many methods operate on the frequency-domain, relying on the Fast Fourier Transform (FFT) which assumes uniform sampling, therefore requiring prior interpolation that can distort the spectra. To address this limitation, we introduce a differentiable Lomb--Scargle layer that enables a reliable computation of the power spectrum of irregularly sampled data.
We integrate this layer into a novel score-based diffusion model (LSCD) for time series imputation conditioned on the entire signal spectrum. 
Experiments on synthetic and real-world benchmarks demonstrate that our method recovers missing data more accurately than purely time-domain baselines, while simultaneously producing consistent frequency estimates. Crucially, our method can be easily integrated into learning frameworks, enabling broader adoption of spectral guidance in machine learning approaches involving incomplete or irregular data.

## Metadata
- venue: ICML
- year: 2025
- authors: Elizabeth Fons, Alejandro Sztrajman, Yousef El-Laham, Luciana Ferrer, Svitlana Vyetrenko, Manuela Veloso
- arxiv_id: 
- openreview_id: GdYg0Ohx0k
- anthology_id: 
- pdf_url: https://openreview.net/pdf/12163661cd94ad6155e664a40a68f76bbc2a817c.pdf
- published: 2025
- keywords: time series, diffusion models, frequency spectrum

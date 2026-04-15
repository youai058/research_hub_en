---
title: "Rolling Diffusion Models"
authors: ["David Ruhe", "Jonathan Heek", "Tim Salimans", "Emiel Hoogeboom"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "a9bzTv9SzO"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/3794568302cbe350f892a6ed947517db63d1839d.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:38+09:00"
---

# Rolling Diffusion Models

## Abstract
Diffusion models have recently been increasingly applied to temporal data such as video, fluid mechanics simulations, or climate data. These methods generally treat subsequent frames equally regarding the amount of noise in the diffusion process. This paper explores Rolling Diffusion: a new approach that uses a sliding window denoising process. It ensures that the diffusion process progressively corrupts through time by assigning more noise to frames that appear later in a sequence, reflecting greater uncertainty about the future as the generation process unfolds. Empirically, we show that when the temporal dynamics are complex, Rolling Diffusion is superior to standard diffusion. In particular, this result is demonstrated in a video prediction task using the Kinetics-600 video dataset and in a chaotic fluid dynamics forecasting experiment.

## Metadata
- venue: ICML
- year: 2024
- authors: David Ruhe, Jonathan Heek, Tim Salimans, Emiel Hoogeboom
- arxiv_id: 
- openreview_id: a9bzTv9SzO
- anthology_id: 
- pdf_url: https://openreview.net/pdf/3794568302cbe350f892a6ed947517db63d1839d.pdf
- published: 2024

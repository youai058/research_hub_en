---
title: "Multistep Distillation of Diffusion Models via Moment Matching"
authors: ["Tim Salimans", "Thomas Mensink", "Jonathan Heek", "Emiel Hoogeboom"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "C62d2nS3KO"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f5964a3a798db199e7614693b91434cfaca4f46c.pdf"
published: "2024"
categories: []
keywords: ["generative modeling", "diffusion", "distillation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:46+09:00"
---

# Multistep Distillation of Diffusion Models via Moment Matching

## Abstract
We present a new method for making diffusion models faster to sample. The method distills many-step diffusion models into few-step models by matching conditional expectations of the clean data given noisy data along the sampling trajectory. Our approach extends recently proposed one-step methods to the multi-step case, and provides a new perspective by interpreting these approaches in terms of moment matching. By using up to 8 sampling steps, we obtain distilled models that outperform not only their one-step versions but also their original many-step teacher models, obtaining new state-of-the-art results on the Imagenet dataset. We also show promising results on a large text-to-image model where we achieve fast generation of high resolution images directly in image space, without needing autoencoders or upsamplers.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Tim Salimans, Thomas Mensink, Jonathan Heek, Emiel Hoogeboom
- arxiv_id: 
- openreview_id: C62d2nS3KO
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f5964a3a798db199e7614693b91434cfaca4f46c.pdf
- published: 2024
- keywords: generative modeling, diffusion, distillation

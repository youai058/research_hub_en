---
title: "Discrete Feynman-Kac Correctors"
authors: ["Mohsin Hasan", "Viktor Ohanesian", "Artem Gazizov", "Yoshua Bengio", "Alán Aspuru-Guzik", "Roberto Bondesan", "Marta Skreta", "Kirill Neklyudov"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2601.10403"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2601.10403v1"
published: "2026-01-15"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:21+09:00"
---

# Discrete Feynman-Kac Correctors

## Abstract
Discrete diffusion models have recently emerged as a promising alternative to the autoregressive approach for generating discrete sequences. Sample generation via gradual denoising or demasking processes allows them to capture hierarchical non-sequential interdependencies in the data. These custom processes, however, do not assume a flexible control over the distribution of generated samples. We propose Discrete Feynman-Kac Correctors, a framework that allows for controlling the generated distribution of discrete masked diffusion models at inference time. We derive Sequential Monte Carlo (SMC) algorithms that, given a trained discrete diffusion model, control the temperature of the sampled distribution (i.e. perform annealing), sample from the product of marginals of several diffusion processes (e.g. differently conditioned processes), and sample from the product of the marginal with an external reward function, producing likely samples from the target distribution that also have high reward. Notably, our framework does not require any training of additional models or fine-tuning of the original model. We illustrate the utility of our framework in several applications including: efficient sampling from the annealed Boltzmann distribution of the Ising model, improving the performance of language models for code generation and amortized learning, as well as reward-tilted protein sequence generation.

## Metadata
- venue: arXiv
- year: 2026
- authors: Mohsin Hasan, Viktor Ohanesian, Artem Gazizov, Yoshua Bengio, Alán Aspuru-Guzik, Roberto Bondesan, Marta Skreta, Kirill Neklyudov
- arxiv_id: 2601.10403
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2601.10403v1
- published: 2026-01-15

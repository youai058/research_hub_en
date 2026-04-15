---
title: "DDMI: Domain-agnostic Latent Diffusion Models for Synthesizing High-Quality Implicit Neural Representations"
authors: ["Dogyun Park", "Sihyeon Kim", "Sojin Lee", "Hyunwoo J. Kim"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "327tbF3S65"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/716a67cdede3543daa6309c204a066e517decc41.pdf"
published: "2024"
categories: []
keywords: ["Implicit neural representation", "generative model", "domain agnostic", "diffusion model"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:56+09:00"
---

# DDMI: Domain-agnostic Latent Diffusion Models for Synthesizing High-Quality Implicit Neural Representations

## Abstract
Recent studies have introduced a new class of generative models for synthesizing implicit neural representations (INRs) that capture arbitrary continuous signals in various domains. These models opened the door for domain-agnostic generative models, but they often fail to achieve high-quality generation. We observed that the existing methods generate the weights of neural networks to parameterize INRs and evaluate the network with fixed positional embeddings (PEs). Arguably, this architecture limits the expressive power of generative models and results in low-quality INR generation. To address this limitation, we propose Domain-agnostic Latent Diffusion Model for INRs (DDMI) that generates adaptive positional embeddings instead of neural networks' weights. Specifically, we develop a Discrete-to-continuous space Variational AutoEncoder (D2C-VAE) that seamlessly connects discrete data and continuous signal functions in the shared latent space. Additionally, we introduce a novel conditioning mechanism for evaluating INRs with the hierarchically decomposed PEs to further enhance expressive power. Extensive experiments across four modalities, \eg, 2D images, 3D shapes, Neural Radiance Fields, and videos, with seven benchmark datasets, demonstrate the versatility of DDMI and its superior performance compared to the existing INR generative models. Code is available at \href{https://github.com/mlvlab/DDMI}{https://github.com/mlvlab/DDMI}.

## Metadata
- venue: ICLR
- year: 2024
- authors: Dogyun Park, Sihyeon Kim, Sojin Lee, Hyunwoo J. Kim
- arxiv_id: 
- openreview_id: 327tbF3S65
- anthology_id: 
- pdf_url: https://openreview.net/pdf/716a67cdede3543daa6309c204a066e517decc41.pdf
- published: 2024
- keywords: Implicit neural representation, generative model, domain agnostic, diffusion model

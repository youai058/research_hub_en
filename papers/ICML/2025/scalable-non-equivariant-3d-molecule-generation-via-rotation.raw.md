---
title: "Scalable Non-Equivariant 3D Molecule Generation via Rotational Alignment"
authors: ["Yuhui Ding", "Thomas Hofmann"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "l5KpQ5MmaD"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d526a2c92e7570f45137984e599cd180fcdcf5b6.pdf"
published: "2025"
categories: []
keywords: ["Non-equivariant diffusion", "3D molecule generation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:07+09:00"
---

# Scalable Non-Equivariant 3D Molecule Generation via Rotational Alignment

## Abstract
Equivariant diffusion models have achieved impressive performance in 3D molecule generation. These models incorporate Euclidean symmetries of 3D molecules by utilizing an SE(3)-equivariant denoising network. However, specialized equivariant architectures limit the scalability and efficiency of diffusion models. In this paper, we propose an approach that relaxes such equivariance constraints. Specifically, our approach learns a sample-dependent SO(3) transformation for each molecule to construct an aligned latent space. A non-equivariant diffusion model is then trained over the aligned representations. Experimental results demonstrate that our approach performs significantly better than previously reported non-equivariant models. It yields sample quality comparable to state-of-the-art equivariant diffusion models and offers improved training and sampling efficiency. Our code is available at: https://github.com/skeletondyh/RADM

## Metadata
- venue: ICML
- year: 2025
- authors: Yuhui Ding, Thomas Hofmann
- arxiv_id: 
- openreview_id: l5KpQ5MmaD
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d526a2c92e7570f45137984e599cd180fcdcf5b6.pdf
- published: 2025
- keywords: Non-equivariant diffusion, 3D molecule generation

---
title: "COSMO-INR: Complex Sinusoidal Modulation for Implicit Neural Representations"
authors: ["Pandula Thennakoon", "Avishka Ranasinghe", "Mario De Silva", "Buwaneka Epakanda", "Roshan Godaliyadda", "Mervyn Parakrama Bandara Ekanayake", "Vijitha R. Herath"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "yGJrvSU6wK"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/245005dbfe6daea3684e5e0f4469067b6f56dbae.pdf"
published: "2026"
categories: []
keywords: ["Implicit Neural Networks", "Chebyshev Polynomials", "Raised cosine filter", "Spectral bias"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:26+09:00"
---

# COSMO-INR: Complex Sinusoidal Modulation for Implicit Neural Representations

## Abstract
Implicit neural representations (INRs) have recently emerged as a powerful paradigm for modeling data, offering a continuous alternative to traditional discrete signal representations. Their ability to compactly encode complex signals has led to strong performance across a wide range of computer vision tasks. In previous studies, it has been repeatedly shown that INR performance has a strong correlation with the activation functions used in its multilayer perceptrons. Although numerous competitive activation functions for INRs have been proposed, the theoretical foundations underlying their effectiveness remain poorly understood. Moreover, key challenges persist, including spectral bias (the reduced sensitivity to high-frequency signal content), limited robustness to noise, and difficulties in jointly capturing both local and global features. In this paper, we explore the underlying mechanism of INR signal representation, leveraging harmonic analysis and Chebyshev Polynomials. Through a rigorous mathematical proof, we show that modulating activation functions using a complex sinusoidal term yields better and complete spectral support throughout the INR network. To support our theoretical framework, we present empirical results over a wide range of experiments using Chebyshev analysis. We further develop a new activation function, leveraging the new theoretical findings to highlight its feasibility in INRs. We also incorporate a regularized deep prior, extracted from the signal via a task-specific model, to adjust the activation function parameters. This integration further improves convergence speed and stability across tasks. Through a series of experiments which include image reconstruction (with an average PSNR improvement of +5.67 dB over the nearest counterpart across a diverse image dataset), denoising (with a +0.46 dB increase in PSNR), super-resolution (with a +0.64 dB improvement over the nearest State-Of-The-Art (SOTA) method for 6X super-resolution), inpainting, and 3D shape reconstruction we demonstrate the novel proposed activation over existing state of the art activation functions. The official implementation and experimental results are available at our [project page](https://cosmo-inr.github.io/).

## Metadata
- venue: ICLR
- year: 2026
- authors: Pandula Thennakoon, Avishka Ranasinghe, Mario De Silva, Buwaneka Epakanda, Roshan Godaliyadda, Mervyn Parakrama Bandara Ekanayake, Vijitha R. Herath
- arxiv_id: 
- openreview_id: yGJrvSU6wK
- anthology_id: 
- pdf_url: https://openreview.net/pdf/245005dbfe6daea3684e5e0f4469067b6f56dbae.pdf
- published: 2026
- keywords: Implicit Neural Networks, Chebyshev Polynomials, Raised cosine filter, Spectral bias

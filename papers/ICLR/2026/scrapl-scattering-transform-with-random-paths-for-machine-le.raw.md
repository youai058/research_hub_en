---
title: "SCRAPL: Scattering Transform with Random Paths for Machine Learning"
authors: ["Christopher Mitcheltree", "Vincent Lostanlen", "Emmanouil Benetos", "Mathieu Lagrange"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "RuYwbd5xYa"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/dbe1a05f9f7fe3f178dc4b7f721bb6a1365dc0f5.pdf"
published: "2026"
categories: []
keywords: ["scattering transform", "wavelets", "stochastic optimization", "ddsp", "perceptual quality assessment"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:16+09:00"
---

# SCRAPL: Scattering Transform with Random Paths for Machine Learning

## Abstract
The Euclidean distance between wavelet scattering transform coefficients (known as paths) provides informative gradients for perceptual quality assessment of deep inverse problems in computer vision, speech, and audio processing. However, these transforms are computationally expensive when employed as differentiable loss functions for stochastic gradient descent due to their numerous paths, which significantly limits their use in neural network training. Against this problem, we propose "Scattering transform with Random Paths for machine Learning" (SCRAPL): a stochastic optimization scheme for efficient evaluation of multivariable scattering transforms. We implement SCRAPL for the joint time–frequency scattering transform (JTFS) which demodulates spectrotemporal patterns at multiple scales and rates, allowing a fine characterization of intermittent auditory textures. We apply SCRAPL to differentiable digital signal processing (DDSP), specifically, unsupervised sound matching of a granular synthesizer and the Roland TR-808 drum machine. We also propose an initialization heuristic based on importance sampling, which adapts SCRAPL to the perceptual content of the dataset, improving neural network convergence and evaluation performance. We make our code and audio samples available and provide SCRAPL as a Python package.

## Metadata
- venue: ICLR
- year: 2026
- authors: Christopher Mitcheltree, Vincent Lostanlen, Emmanouil Benetos, Mathieu Lagrange
- arxiv_id: 
- openreview_id: RuYwbd5xYa
- anthology_id: 
- pdf_url: https://openreview.net/pdf/dbe1a05f9f7fe3f178dc4b7f721bb6a1365dc0f5.pdf
- published: 2026
- keywords: scattering transform, wavelets, stochastic optimization, ddsp, perceptual quality assessment

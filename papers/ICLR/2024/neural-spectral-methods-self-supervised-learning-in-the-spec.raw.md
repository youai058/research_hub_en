---
title: "Neural Spectral Methods: Self-supervised learning in the spectral domain"
authors: ["Yiheng Du", "Nithin Chalapathi", "Aditi S. Krishnapriyan"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "2DbVeuoa6a"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9aa74e5bf7d501d1a636aee71ec751a621b15eee.pdf"
published: "2024"
categories: []
keywords: ["Machine learning for PDEs", "spectral methods", "neural network differentiation", "spectral loss", "PDEs", "neural operators"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:01+09:00"
---

# Neural Spectral Methods: Self-supervised learning in the spectral domain

## Abstract
We present Neural Spectral Methods, a technique to solve parametric Partial Differential Equations (PDEs), grounded in classical spectral methods. Our method uses orthogonal bases to learn PDE solutions as mappings between spectral coefficients, instantiating a spectral-based neural operator. In contrast to current machine learning approaches which enforce PDE constraints by minimizing the numerical quadrature of the residuals in the spatiotemporal domain, we leverage Parseval's identity and introduce a new training strategy through a spectral loss. Our spectral loss enables more efficient differentiation through the neural network, and substantially reduces training complexity. At inference time, the computational cost of our method remains constant, regardless of the spatiotemporal resolution of the domain.  Our experimental results demonstrate that our method significantly outperforms previous machine learning approaches in terms of speed and accuracy by one to two orders of magnitude on multiple different problems, including reaction-diffusion, and forced and unforced Navier-Stokes equations. When compared to numerical solvers of the same accuracy, our method demonstrates a $10\times$ increase in performance speed. Our source code is publicly available at https://github.com/ASK-Berkeley/Neural-Spectral-Methods.

## Metadata
- venue: ICLR
- year: 2024
- authors: Yiheng Du, Nithin Chalapathi, Aditi S. Krishnapriyan
- arxiv_id: 
- openreview_id: 2DbVeuoa6a
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9aa74e5bf7d501d1a636aee71ec751a621b15eee.pdf
- published: 2024
- keywords: Machine learning for PDEs, spectral methods, neural network differentiation, spectral loss, PDEs, neural operators

---
title: "Error as Signal: Stiffness-Aware Diffusion Sampling via Embedded Runge-Kutta Guidance"
authors: ["Inho Kong", "Sojin Lee", "Youngjoon Hong", "Hyunwoo J. Kim"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "wKX9OL0leb"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d5ab718136e3b5eadca778b97db9cad53e677bb1.pdf"
published: "2026"
categories: []
keywords: ["Diffusion models", "Classifier-free guidance"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:36+09:00"
---

# Error as Signal: Stiffness-Aware Diffusion Sampling via Embedded Runge-Kutta Guidance

## Abstract
Classifier-Free Guidance (CFG) has established the foundation for guidance mechanisms in diffusion models, showing that well-designed guidance proxies significantly improve conditional generation and sample quality. Autoguidance (AG) has extended this idea, but it relies on an auxiliary network and leaves solver-induced errors unaddressed. In stiff regions, the ODE trajectory changes sharply, where local truncation error (LTE) becomes a critical factor that deteriorates sample quality. Our key observation is that these errors align with the dominant eigenvector, motivating us to leverage the solver-induced error as a guidance signal. We propose **E**mbedded **R**unge–**K**utta **Guid**ance (ERK-Guid), which exploits detected stiffness to reduce LTE and stabilize sampling. We theoretically and empirically analyze stiffness and eigenvector estimators with solver errors to motivate the design of ERK-Guid. Our experiments on both synthetic datasets and the popular benchmark dataset, ImageNet, demonstrate that ERK-Guid consistently outperforms state-of-the-art methods. Code is available at https://github.com/mlvlab/ERK-Guid.

## Metadata
- venue: ICLR
- year: 2026
- authors: Inho Kong, Sojin Lee, Youngjoon Hong, Hyunwoo J. Kim
- arxiv_id: 
- openreview_id: wKX9OL0leb
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d5ab718136e3b5eadca778b97db9cad53e677bb1.pdf
- published: 2026
- keywords: Diffusion models, Classifier-free guidance

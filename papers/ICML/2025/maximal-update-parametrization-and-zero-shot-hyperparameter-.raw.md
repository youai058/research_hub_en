---
title: "Maximal Update Parametrization and Zero-Shot Hyperparameter Transfer for Fourier Neural Operators"
authors: ["Shanda Li", "Shinjae Yoo", "Yiming Yang"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "fHt4Nau7FW"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/6214c7f8eacf96fe35c31942abe53f9a99fdbc9c.pdf"
published: "2025"
categories: []
keywords: ["Fourier Neural Operators", "Hyperparameter transfer"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:35+09:00"
---

# Maximal Update Parametrization and Zero-Shot Hyperparameter Transfer for Fourier Neural Operators

## Abstract
Fourier Neural Operators (FNOs) offer a principled approach for solving complex partial differential equations (PDEs). However, scaling them to handle more complex PDEs requires increasing the number of Fourier modes, which significantly expands the number of model parameters and makes hyperparameter tuning computationally impractical. To address this, we introduce $\mu$**Transfer-FNO**, a zero-shot hyperparameter transfer technique that enables optimal configurations, tuned on smaller FNOs, to be directly applied to billion-parameter FNOs _without_ additional tuning. Building on the Maximal Update Parametrization ($\mu$P) framework, we mathematically derive a parametrization scheme that facilitates the transfer of optimal hyperparameters across models with different numbers of Fourier modes in FNOs, which is validated through extensive experiments on various PDEs. Our empirical study shows that $\mu$Transfer-FNO reduces computational cost for tuning hyperparameters on large FNOs while maintaining or improving accuracy.

## Metadata
- venue: ICML
- year: 2025
- authors: Shanda Li, Shinjae Yoo, Yiming Yang
- arxiv_id: 
- openreview_id: fHt4Nau7FW
- anthology_id: 
- pdf_url: https://openreview.net/pdf/6214c7f8eacf96fe35c31942abe53f9a99fdbc9c.pdf
- published: 2025
- keywords: Fourier Neural Operators, Hyperparameter transfer

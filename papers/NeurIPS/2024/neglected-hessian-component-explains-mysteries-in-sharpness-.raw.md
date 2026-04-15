---
title: "Neglected Hessian component explains mysteries in sharpness regularization"
authors: ["Yann Dauphin", "Atish Agarwala", "Hossein Mobahi"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "m6pVpdIN0y"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c1f6ee9f0e9ec1784d61f91dc4fd53ea887eb3b7.pdf"
published: "2024"
categories: []
keywords: ["sharpness", "flatness", "regularization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:34+09:00"
---

# Neglected Hessian component explains mysteries in sharpness regularization

## Abstract
Recent work has shown that methods that regularize second order information like SAM can improve generalization in deep learning. Seemingly similar methods like weight noise and gradient penalties often fail to provide such benefits. We investigate this inconsistency and reveal its connection to the the structure of the Hessian of the loss. Specifically, its decomposition into the positive semi-definite Gauss-Newton matrix and an indefinite matrix, which we call the Nonlinear Modeling Error (NME) matrix. Previous studies have largely overlooked the significance of the NME in their analysis for various reasons. However, we provide empirical and theoretical evidence that the NME is important to the performance of gradient penalties and explains their sensitivity to activation functions. We also provide evidence that the difference in regularization performance between gradient penalties and weight noise can be explained by the NME. Our findings emphasize the necessity of considering the NME in both experimental design and theoretical analysis for sharpness regularization.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Yann Dauphin, Atish Agarwala, Hossein Mobahi
- arxiv_id: 
- openreview_id: m6pVpdIN0y
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c1f6ee9f0e9ec1784d61f91dc4fd53ea887eb3b7.pdf
- published: 2024
- keywords: sharpness, flatness, regularization

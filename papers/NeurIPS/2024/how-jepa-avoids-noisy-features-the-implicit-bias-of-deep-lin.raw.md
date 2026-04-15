---
title: "How JEPA Avoids Noisy Features: The Implicit Bias of Deep Linear Self Distillation Networks"
authors: ["Etai Littwin", "Omid Saremi", "Madhu Advani", "Vimal Thilak", "Preetum Nakkiran", "Chen Huang", "Joshua M. Susskind"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ez7w0Ss4g9"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/57102015900c78b2349245b28beca0370b087879.pdf"
published: "2024"
categories: []
keywords: ["SSL", "JEPA"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:45+09:00"
---

# How JEPA Avoids Noisy Features: The Implicit Bias of Deep Linear Self Distillation Networks

## Abstract
Two competing paradigms exist for self-supervised learning of data representations. 
    Joint Embedding Predictive Architectures (JEPAs) is a class of architectures in which semantically similar inputs are encoded into representations that are predictive of each other. A recent successful approach that falls under the JEPA framework is self-distillation, where an online encoder is trained to predict the output of the target encoder, sometimes with a lightweight predictor network. This is contrasted with the Masked Auto Encoder (MAE) paradigm, where an encoder and decoder are trained to reconstruct missing parts of the input in ambient space rather than its latent representation. A common motivation for using the JEPA approach over MAE is that the JEPA objective prioritizes abstract features over fine-grained pixel information (which can be unpredictable and uninformative).
    In this work, we seek to understand the mechanism behind this empirical observation by analyzing deep linear models. We uncover a surprising mechanism: in a simplified linear setting where both approaches learn similar representations, JEPAs are biased to learn high influence features, or features characterized by having high regression coefficients. Our results point to a distinct implicit bias of predicting in latent space that may shed light on its success in practice.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Etai Littwin, Omid Saremi, Madhu Advani, Vimal Thilak, Preetum Nakkiran, Chen Huang, Joshua M. Susskind
- arxiv_id: 
- openreview_id: ez7w0Ss4g9
- anthology_id: 
- pdf_url: https://openreview.net/pdf/57102015900c78b2349245b28beca0370b087879.pdf
- published: 2024
- keywords: SSL, JEPA

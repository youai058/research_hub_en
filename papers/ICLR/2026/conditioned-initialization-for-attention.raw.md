---
title: "Conditioned Initialization for Attention"
authors: ["Hemanth Saratchandran", "Simon Lucey"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "cKNOCYPo2W"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/224af19cb1db77002488bc02b630761039463494.pdf"
published: "2026"
categories: []
keywords: ["spectral conditioning transformers", "spectral properties of attention"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:18+09:00"
---

# Conditioned Initialization for Attention

## Abstract
Transformers are a dominant architecture in modern machine learning, powering applications across vision, language, and beyond. At the core of their success lies the attention layer, where the query, key, and value matrices determine how token dependencies are captured. While considerable work has focused on scaling and optimizing Transformers, comparatively little attention has been paid to how the weights of the queries, keys and values are initialized. Common practice relies on random initialization or alternatives such as mimetic initialization, which imitates weight patterns from converged models, and weight selection, which transfers weights from a teacher model. In this paper, we argue that initialization can introduce an optimization bias that fundamentally shapes training dynamics. We propose **conditioned initialization**, a principled scheme that initializes attention weights to improve the spectral properties of the attention layer. Theoretically, we show that conditioned initialization can potentially reduce the condition number of the attention Jacobian, leading to more stable optimization. Empirically, it accelerates convergence and improves generalization across diverse applications, highlighting conditioning as a critical yet underexplored area for advancing Transformer performance. Importantly, conditioned initialization is simple to apply and integrates seamlessly into a wide range of Transformer architectures.

## Metadata
- venue: ICLR
- year: 2026
- authors: Hemanth Saratchandran, Simon Lucey
- arxiv_id: 
- openreview_id: cKNOCYPo2W
- anthology_id: 
- pdf_url: https://openreview.net/pdf/224af19cb1db77002488bc02b630761039463494.pdf
- published: 2026
- keywords: spectral conditioning transformers, spectral properties of attention

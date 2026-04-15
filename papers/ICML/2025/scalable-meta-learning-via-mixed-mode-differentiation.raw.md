---
title: "Scalable Meta-Learning via Mixed-Mode Differentiation"
authors: ["Iurii Kemaev", "Dan A. Calian", "Luisa M Zintgraf", "Gregory Farquhar", "Hado van Hasselt"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "NWKjVzkDzg"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c7233539f750a18c225d2019524bb8fd2c3903ee.pdf"
published: "2025"
categories: []
keywords: ["meta-learning", "bilevel optimization", "second-order optimization", "automatic differentiation", "autodiff", "mixed-mode differentiation", "gradient-based methods", "scalable algorithms"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:06+09:00"
---

# Scalable Meta-Learning via Mixed-Mode Differentiation

## Abstract
Gradient-based bilevel optimisation is a powerful technique with applications in hyperparameter optimisation, task adaptation, algorithm discovery, meta-learning more broadly, and beyond. It often requires differentiating through the gradient-based optimisation process itself, leading to "gradient-of-a-gradient" calculations with computationally expensive second-order and mixed derivatives. While modern automatic differentiation libraries provide a convenient way to write programs for calculating these derivatives, they oftentimes cannot fully exploit the specific structure of these problems out-of-the-box, leading to suboptimal performance. In this paper, we analyse such cases and propose Mixed-Flow Meta-Gradients, or MixFlow-MG -- a practical algorithm that uses mixed-mode differentiation to construct more efficient and scalable computational graphs yielding over 10x memory and up to 25\% wall-clock time improvements over standard implementations in modern meta-learning setups.

## Metadata
- venue: ICML
- year: 2025
- authors: Iurii Kemaev, Dan A. Calian, Luisa M Zintgraf, Gregory Farquhar, Hado van Hasselt
- arxiv_id: 
- openreview_id: NWKjVzkDzg
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c7233539f750a18c225d2019524bb8fd2c3903ee.pdf
- published: 2025
- keywords: meta-learning, bilevel optimization, second-order optimization, automatic differentiation, autodiff, mixed-mode differentiation, gradient-based methods, scalable algorithms

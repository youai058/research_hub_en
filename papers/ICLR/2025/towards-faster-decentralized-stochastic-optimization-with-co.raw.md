---
title: "Towards Faster Decentralized Stochastic Optimization with Communication Compression"
authors: ["Rustem Islamov", "Yuan Gao", "Sebastian U Stich"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "CMMpcs9prj"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/db91a1f9b5191d22f46819f74495e8037584f11a.pdf"
published: "2025"
categories: []
keywords: ["Optimization", "Decentralized Learning", "Federated Learning", "Communication Compression"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:57+09:00"
---

# Towards Faster Decentralized Stochastic Optimization with Communication Compression

## Abstract
Communication efficiency has garnered significant attention as it is considered the main bottleneck for large-scale decentralized Machine Learning applications in distributed and federated settings. In this regime, clients are restricted to transmitting small amounts of compressed information to their neighbors over a communication graph. Numerous endeavors have been made to address this challenging problem by developing algorithms with compressed communication for decentralized non-convex optimization problems. Despite considerable efforts, current theoretical understandings of the problem are still very limited, and existing algorithms all suffer from various limitations. In particular, these algorithms typically rely on strong, and often infeasible assumptions such as bounded data heterogeneity or require large batch access while failing to achieve linear speedup with the number of clients. In this paper, we introduce MoTEF, a novel approach that integrates communication compression with $\textbf{Mo}$mentum $\textbf{T}$racking and $\textbf{E}$rror $\textbf{F}$eedback. MoTEF is the first algorithm to achieve an asymptotic rate matching that of distributed SGD under arbitrary data heterogeneity, hence resolving a long-standing theoretical obstacle in decentralized optimization with compressed communication. We provide numerical experiments to validate our theoretical findings and confirm the practical superiority of MoTEF.

## Metadata
- venue: ICLR
- year: 2025
- authors: Rustem Islamov, Yuan Gao, Sebastian U Stich
- arxiv_id: 
- openreview_id: CMMpcs9prj
- anthology_id: 
- pdf_url: https://openreview.net/pdf/db91a1f9b5191d22f46819f74495e8037584f11a.pdf
- published: 2025
- keywords: Optimization, Decentralized Learning, Federated Learning, Communication Compression

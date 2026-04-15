---
title: "Escaping saddle points without Lipschitz smoothness: the power of nonlinear preconditioning"
authors: ["Alexander Bodard", "Panagiotis Patrinos"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "7qrhHzZpTA"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d73a4f2b49a9cca19b750c8c17c0411132d8beca.pdf"
published: "2025"
categories: []
keywords: ["Nonconvex optimization", "generalized smoothness", "saddle point avoidance"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:37+09:00"
---

# Escaping saddle points without Lipschitz smoothness: the power of nonlinear preconditioning

## Abstract
We study generalized smoothness in nonconvex optimization, focusing on $(L_0, L_1)$-smoothness and anisotropic smoothness. The former was empirically derived from practical neural network training examples, while the latter arises naturally in the analysis of nonlinearly preconditioned gradient methods. We introduce a new sufficient condition that encompasses both notions, reveals their close connection, and holds in key applications such as phase retrieval and matrix factorization. Leveraging tools from dynamical systems theory, we then show that nonlinear preconditioning—including gradient clipping—preserves the saddle point avoidance property of classical gradient descent. Crucially, the assumptions required for this analysis are actually satisfied in these applications, unlike in classical results that rely on restrictive Lipschitz smoothness conditions. We further analyze a perturbed variant that efficiently attains second-order stationarity with only logarithmic dependence on dimension, matching similar guarantees of classical gradient methods.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Alexander Bodard, Panagiotis Patrinos
- arxiv_id: 
- openreview_id: 7qrhHzZpTA
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d73a4f2b49a9cca19b750c8c17c0411132d8beca.pdf
- published: 2025
- keywords: Nonconvex optimization, generalized smoothness, saddle point avoidance

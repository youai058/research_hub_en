---
title: "Positive Concave Deep Equilibrium Models"
authors: ["Mateusz Gabor", "Tomasz Piotrowski", "Renato L. G. Cavalcante"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "e0SKaKEEdr"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/868b96fe23e7facf6f339c52243838b7c1f13549.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:45+09:00"
---

# Positive Concave Deep Equilibrium Models

## Abstract
Deep equilibrium (DEQ) models are widely recognized as a memory efficient alternative to standard neural networks, achieving state-of-the-art performance in language modeling and computer vision tasks. These models solve a fixed point equation instead of explicitly computing the output, which sets them apart from standard neural networks. However, existing DEQ models often lack formal guarantees of the existence and uniqueness of the fixed point, and the convergence of the numerical scheme used for computing the fixed point is not formally established. As a result, DEQ models are potentially unstable in practice. To address these drawbacks, we introduce a novel class of DEQ models called positive concave deep equilibrium (pcDEQ) models. Our approach, which is based on nonlinear Perron-Frobenius theory, enforces nonnegative weights and activation functions that are concave on the positive orthant. By imposing these constraints, we can easily ensure the existence and uniqueness of the fixed point without relying on additional complex assumptions commonly found in the DEQ literature, such as those based on monotone operator theory in convex analysis. Furthermore, the fixed point can be computed with the standard fixed point algorithm, and we provide theoretical guarantees of its geometric convergence, which, in particular, simplifies the training process. Experiments demonstrate the competitiveness of our pcDEQ models against other implicit models.

## Metadata
- venue: ICML
- year: 2024
- authors: Mateusz Gabor, Tomasz Piotrowski, Renato L. G. Cavalcante
- arxiv_id: 
- openreview_id: e0SKaKEEdr
- anthology_id: 
- pdf_url: https://openreview.net/pdf/868b96fe23e7facf6f339c52243838b7c1f13549.pdf
- published: 2024

---
title: "On the Convergence of Two-Layer Kolmogorov-Arnold Networks with First-Layer Training"
authors: ["Seyed Mohammad Eshtehardian", "Mohammad Hossein Yassaee", "Babak Khalaj"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "buuwRBYfrP"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/4e9c88ec37373e293e9498bb54a4e98bf2d8aa37.pdf"
published: "2026"
categories: []
keywords: ["Kolmogorov-Arnold Networks (KANs)", "Overparameterization", "Neural Tangent Kernel (NTK)", "Gradient Descent"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:46+09:00"
---

# On the Convergence of Two-Layer Kolmogorov-Arnold Networks with First-Layer Training

## Abstract
Kolmogorov-Arnold Networks (KANs) have emerged as a promising alternative to traditional neural networks, offering enhanced interpretability based on the Kolmogorov-Arnold representation theorem. While their empirical success is growing, a theoretical understanding of their training dynamics remains nascent. This paper investigates the optimization of a two-layer KAN in the overparameterized regime, focusing on a simplified yet insightful setting where only the first-layer coefficients are trained via gradient descent.

Our main result establishes that, provided the network is sufficiently wide, this training method is guaranteed to converge to a global minimum and achieve zero training error. Furthermore, we derive a novel, fine-grained convergence rate that explicitly connects the optimization speed to the structure of the data labels through the eigenspectrum of the KAN Tangent Kernel (KAN-TK). Our analysis reveals a key advantage of this architecture: guaranteed convergence is achieved with a hidden layer width of $m=\mathcal{O}(n^2)$, a significant polynomial improvement over the $m=\mathcal{O}(n^6)$ requirement for classic two-layer neural networks using ReLU activation functions and analyzed within the same Tangent Kernel framework. We validate our theoretical findings with numerical experiments that corroborate our predictions on convergence speed and the impact of label structure.

## Metadata
- venue: ICLR
- year: 2026
- authors: Seyed Mohammad Eshtehardian, Mohammad Hossein Yassaee, Babak Khalaj
- arxiv_id: 
- openreview_id: buuwRBYfrP
- anthology_id: 
- pdf_url: https://openreview.net/pdf/4e9c88ec37373e293e9498bb54a4e98bf2d8aa37.pdf
- published: 2026
- keywords: Kolmogorov-Arnold Networks (KANs), Overparameterization, Neural Tangent Kernel (NTK), Gradient Descent

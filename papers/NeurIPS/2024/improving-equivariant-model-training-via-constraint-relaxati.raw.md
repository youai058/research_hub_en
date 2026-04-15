---
title: "Improving Equivariant Model Training via Constraint Relaxation"
authors: ["Stefanos Pertigkiozoglou", "Evangelos Chatzipantazis", "Shubhendu Trivedi", "Kostas Daniilidis"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "tWkL7k1u5v"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/bc08cca49893134348537df9e6335e1e32619ffc.pdf"
published: "2024"
categories: []
keywords: ["Equivariant Neural Networks", "Symmetries", "Approximate Equivariance", "Optimization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:58+09:00"
---

# Improving Equivariant Model Training via Constraint Relaxation

## Abstract
Equivariant neural networks have been widely used in a variety of applications due to their ability to generalize well in tasks where the underlying data symmetries are known. Despite their successes, such networks can be difficult to optimize and require careful hyperparameter tuning to train successfully. In this work, we propose a novel framework for improving the optimization of such models by relaxing the hard equivariance constraint during training: We relax the equivariance constraint of the network's intermediate layers by introducing an additional non-equivariant term that we progressively constrain until we arrive at an equivariant solution. By controlling the magnitude of the activation of the additional relaxation term, we allow the model to optimize over a larger hypothesis space containing approximate equivariant networks and converge back to an equivariant solution at the end of training. We provide experimental results on different state-of-the-art network architectures, demonstrating how this training framework can result in equivariant models with improved generalization performance. Our code is available at https://github.com/StefanosPert/Equivariant_Optimization_CR

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Stefanos Pertigkiozoglou, Evangelos Chatzipantazis, Shubhendu Trivedi, Kostas Daniilidis
- arxiv_id: 
- openreview_id: tWkL7k1u5v
- anthology_id: 
- pdf_url: https://openreview.net/pdf/bc08cca49893134348537df9e6335e1e32619ffc.pdf
- published: 2024
- keywords: Equivariant Neural Networks, Symmetries, Approximate Equivariance, Optimization

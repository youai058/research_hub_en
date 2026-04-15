---
title: "A geometric framework for momentum-based optimizers for low-rank training"
authors: ["Steffen Schotthöfer", "Timon Klein", "Jonas Kusch"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "cCefuzQrjK"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/3123a99ffb27c5786fc5d6f3339c21a660306131.pdf"
published: "2025"
categories: []
keywords: ["Low-Rank", "Compression", "Finetuning", "Optimization", "Manifold"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:27+09:00"
---

# A geometric framework for momentum-based optimizers for low-rank training

## Abstract
Low-rank pre-training and fine-tuning have recently emerged as promising techniques for reducing the computational and storage costs of large neural networks. Training low-rank parameterizations typically relies on conventional optimizers such as heavy ball momentum methods or Adam. In this work, we identify and analyze potential difficulties that these training methods encounter when used to train low-rank parameterizations of weights. In particular, we show that classical momentum methods can struggle to converge to a local optimum due to the geometry of the underlying optimization landscape. To address this, we introduce novel training strategies derived from dynamical low-rank approximation, which explicitly account for the underlying geometric structure. Our approach leverages and combines tools from dynamical low-rank approximation and momentum-based optimization to design optimizers that respect the intrinsic geometry of the parameter space. We validate our methods through numerical experiments, demonstrating faster convergence, and stronger validation metrics at given parameter budgets.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Steffen Schotthöfer, Timon Klein, Jonas Kusch
- arxiv_id: 
- openreview_id: cCefuzQrjK
- anthology_id: 
- pdf_url: https://openreview.net/pdf/3123a99ffb27c5786fc5d6f3339c21a660306131.pdf
- published: 2025
- keywords: Low-Rank, Compression, Finetuning, Optimization, Manifold

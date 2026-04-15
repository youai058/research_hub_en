---
title: "Neural Stochastic Differential Equations for Uncertainty-Aware Offline RL"
authors: ["Cevahir Koprulu", "Franck Djeumou", "ufuk topcu"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "hxUMQ4fic3"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/de6c3aad1e7850cf0e5fbffbd30537f5d7642ae9.pdf"
published: "2025"
categories: []
keywords: ["neural stochastic differential equations", "offline reinforcement learning", "physics-informed machine learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:14+09:00"
---

# Neural Stochastic Differential Equations for Uncertainty-Aware Offline RL

## Abstract
Offline model-based reinforcement learning (RL) offers a principled approach to using a learned dynamics model as a simulator to optimize a control policy. 
Despite the near-optimal performance of existing approaches on benchmarks with high-quality datasets, most struggle on datasets with low state-action space coverage or suboptimal demonstrations.
We develop a novel offline model-based RL approach that particularly shines in low-quality data regimes while maintaining competitive performance on high-quality datasets.
Neural Stochastic Differential Equations for Uncertainty-aware, Offline RL (NUNO) learns a dynamics model as neural stochastic differential equations (SDE), 
where its drift term can leverage prior physics knowledge as inductive bias.
In parallel, its diffusion term provides distance-aware estimates of model uncertainty by matching the dynamics' underlying stochasticity near the training data regime while providing high but bounded estimates beyond it.
To address the so-called model exploitation problem in offline model-based RL, NUNO builds on existing studies by penalizing and adaptively truncating neural SDE's rollouts according to uncertainty estimates.
Our empirical results in D4RL and NeoRL MuJoCo benchmarks evidence that NUNO outperforms state-of-the-art methods in low-quality datasets by up to 93% while matching or surpassing their performance by up to 55% in some high-quality counterparts.

## Metadata
- venue: ICLR
- year: 2025
- authors: Cevahir Koprulu, Franck Djeumou, ufuk topcu
- arxiv_id: 
- openreview_id: hxUMQ4fic3
- anthology_id: 
- pdf_url: https://openreview.net/pdf/de6c3aad1e7850cf0e5fbffbd30537f5d7642ae9.pdf
- published: 2025
- keywords: neural stochastic differential equations, offline reinforcement learning, physics-informed machine learning

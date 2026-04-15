---
title: "An Efficient Framework for Crediting Data Contributors of Diffusion Models"
authors: ["MingYu Lu", "Chris Lin", "Chanwoo Kim", "Su-In Lee"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "9EqQC2ct4H"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e88699b21a1482af6236a4910d74ceee95115e97.pdf"
published: "2025"
categories: []
keywords: ["data attribution", "diffusion models", "Shapley values"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:58+09:00"
---

# An Efficient Framework for Crediting Data Contributors of Diffusion Models

## Abstract
As diffusion models are deployed in real-world settings and their performance driven by training data, appraising the contribution of data contributors is crucial to creating incentives for sharing quality data and to implementing policies for data compensation. Depending on the use case, model performance corresponds to various global properties of the distribution learned by a diffusion model (e.g., overall aesthetic quality). Hence, here we address the problem of attributing global properties of diffusion models to data contributors. The Shapley value provides a principled approach to valuation by uniquely satisfying game-theoretic axioms of fairness. However, estimating Shapley values for diffusion models is computationally impractical because it requires retraining and rerunning inference on many subsets of data contributors. We introduce a method to efficiently retrain and rerun inference for Shapley value estimation, by leveraging model pruning and fine-tuning. We evaluate the utility of our method with three use cases: (i) image quality for a DDPM trained on a CIFAR dataset, (ii) demographic diversity for an LDM trained on CelebA-HQ, and (iii) aesthetic quality for a Stable Diffusion model LoRA-finetuned on Post-Impressionist artworks. Our results empirically demonstrate that our framework can identify important data contributors across global properties, outperforming existing attribution methods for diffusion models.

## Metadata
- venue: ICLR
- year: 2025
- authors: MingYu Lu, Chris Lin, Chanwoo Kim, Su-In Lee
- arxiv_id: 
- openreview_id: 9EqQC2ct4H
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e88699b21a1482af6236a4910d74ceee95115e97.pdf
- published: 2025
- keywords: data attribution, diffusion models, Shapley values

---
title: "Elastic ViTs from Pretrained Models without Retraining"
authors: ["Walter Simoncini", "Michael Dorkenwald", "Tijmen Blankevoort", "Cees G. M. Snoek", "Yuki M Asano"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "OU6FXkSIe0"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/52f0b6417df1a42ed2ffc0615675b98ceb157da8.pdf"
published: "2025"
categories: []
keywords: ["Elastic Inference", "Elastic ViTs", "Pruning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:51+09:00"
---

# Elastic ViTs from Pretrained Models without Retraining

## Abstract
Vision foundation models achieve remarkable performance but are only available in a limited set of pre-determined sizes, forcing sub-optimal deployment choices under real-world constraints. We introduce SnapViT: single-shot network approximation for pruned Vision Transformers, a new post-pretraining structured pruning method that enables elastic inference across a continuum of compute budgets. Our approach efficiently combines gradient information with cross-network structure correlations, approximated via an evolutionary algorithm, does not require labeled data, generalizes to models without a classification head, and is retraining-free. Experiments on DINO, SigLIPv2, DeIT, and AugReg models demonstrate superior performance over state-of-the-art methods across various sparsities, requiring less than five minutes on a single A100 GPU to generate elastic models that can be adjusted to any computational budget. Our key contributions include an efficient pruning strategy for pretrained Vision Transformers, a novel evolutionary approximation of Hessian off-diagonal structures, and a self-supervised importance scoring mechanism that maintains strong performance without requiring retraining or labels. Code and pruned models are available at: https://elastic.ashita.nl/

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Walter Simoncini, Michael Dorkenwald, Tijmen Blankevoort, Cees G. M. Snoek, Yuki M Asano
- arxiv_id: 
- openreview_id: OU6FXkSIe0
- anthology_id: 
- pdf_url: https://openreview.net/pdf/52f0b6417df1a42ed2ffc0615675b98ceb157da8.pdf
- published: 2025
- keywords: Elastic Inference, Elastic ViTs, Pruning

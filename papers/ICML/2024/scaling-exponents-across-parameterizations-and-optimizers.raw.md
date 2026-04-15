---
title: "Scaling Exponents Across Parameterizations and Optimizers"
authors: ["Katie E Everett", "Lechao Xiao", "Mitchell Wortsman", "Alexander A Alemi", "Roman Novak", "Peter J Liu", "Izzeddin Gur", "Jascha Sohl-Dickstein", "Leslie Pack Kaelbling", "Jaehoon Lee", "Jeffrey Pennington"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "0ksNeD1SJT"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/579c102a8c067102c85e27612c36d7a356ea9b0b.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:39+09:00"
---

# Scaling Exponents Across Parameterizations and Optimizers

## Abstract
Robust and effective scaling of models from small to large width typically requires the precise adjustment of many algorithmic and architectural details, such as parameterization and optimizer choices. In this work, we propose a new perspective on parameterization by investigating a key assumption in prior work about the alignment between parameters and data and derive new theoretical results under weaker assumptions and a broader set of optimizers. Our extensive empirical investigation includes *tens of thousands* of models trained with *all combinations of* three optimizers, four parameterizations, several alignment assumptions, more than a dozen learning rates, and fourteen model sizes up to 27B parameters. We find that the best learning rate scaling prescription would often have been excluded by the assumptions in prior work. Our results show that all parameterizations, not just maximal update parameterization (muP), can achieve hyperparameter transfer; moreover, our novel per-layer learning rate prescription for standard parameterization outperforms muP. Finally, we demonstrate that an overlooked aspect of parameterization, the epsilon parameter in Adam, must be scaled correctly to avoid gradient underflow and propose *Adam-atan2*, a new numerically stable, scale-invariant version of Adam that eliminates the epsilon hyperparameter entirely.

## Metadata
- venue: ICML
- year: 2024
- authors: Katie E Everett, Lechao Xiao, Mitchell Wortsman, Alexander A Alemi, Roman Novak, Peter J Liu, Izzeddin Gur, Jascha Sohl-Dickstein, Leslie Pack Kaelbling, Jaehoon Lee, Jeffrey Pennington
- arxiv_id: 
- openreview_id: 0ksNeD1SJT
- anthology_id: 
- pdf_url: https://openreview.net/pdf/579c102a8c067102c85e27612c36d7a356ea9b0b.pdf
- published: 2024

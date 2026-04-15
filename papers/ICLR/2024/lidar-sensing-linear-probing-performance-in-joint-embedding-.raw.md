---
title: "LiDAR: Sensing Linear Probing Performance in Joint Embedding SSL Architectures"
authors: ["Vimal Thilak", "Chen Huang", "Omid Saremi", "Laurent Dinh", "Hanlin Goh", "Preetum Nakkiran", "Joshua M. Susskind", "Etai Littwin"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "f3g5XpL9Kb"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/fee7013fbdfbbccda18d5123b30300919a05a18f.pdf"
published: "2024"
categories: []
keywords: ["Self Supervised Learning", "Joint Embedding Architectures"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:20+09:00"
---

# LiDAR: Sensing Linear Probing Performance in Joint Embedding SSL Architectures

## Abstract
Joint embedding (JE) architectures have emerged as a promising avenue for ac-
quiring transferable data representations. A key obstacle to using JE methods,
however, is the inherent challenge of evaluating learned representations without
access to a downstream task, and an annotated dataset. Without efficient and re-
liable evaluation, it is difficult to iterate on architectural and training choices for
JE methods. In this paper, we introduce LiDAR (Linear Discriminant Analysis
Rank), a metric designed to measure the quality of representations within JE archi-
tectures. Our metric addresses several shortcomings of recent approaches based
on feature covariance rank by discriminating between informative and uninforma-
tive features. In essence, LiDAR quantifies the rank of the Linear Discriminant
Analysis (LDA) matrix associated with the surrogate SSL task—a measure that
intuitively captures the information content as it pertains to solving the SSL task.
We empirically demonstrate that LiDAR significantly surpasses naive rank based
approaches in its predictive power of optimal hyperparameters. Our proposed cri-
terion presents a more robust and intuitive means of assessing the quality of rep-
resentations within JE architectures, which we hope facilitates broader adoption
of these powerful techniques in various domains.

## Metadata
- venue: ICLR
- year: 2024
- authors: Vimal Thilak, Chen Huang, Omid Saremi, Laurent Dinh, Hanlin Goh, Preetum Nakkiran, Joshua M. Susskind, Etai Littwin
- arxiv_id: 
- openreview_id: f3g5XpL9Kb
- anthology_id: 
- pdf_url: https://openreview.net/pdf/fee7013fbdfbbccda18d5123b30300919a05a18f.pdf
- published: 2024
- keywords: Self Supervised Learning, Joint Embedding Architectures

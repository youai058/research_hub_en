---
title: "Generative Conditional Distributions by Neural (Entropic) Optimal Transport"
authors: ["Bao Nguyen", "Binh Nguyen", "Hieu Trung Nguyen", "Viet Anh Nguyen"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "FoRqdsN4IA"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b058be8068e1d7ace6b3138fc57cbb8a2849b77a.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:21+09:00"
---

# Generative Conditional Distributions by Neural (Entropic) Optimal Transport

## Abstract
Learning conditional distributions is challenging because the desired outcome is not a single distribution but multiple distributions that correspond to multiple instances of the covariates. We introduce a novel neural entropic optimal transport method designed to effectively learn generative models of conditional distributions, particularly in scenarios characterized by limited sample sizes. Our method relies on the minimax training of two neural networks: a generative network parametrizing the inverse cumulative distribution functions of the conditional distributions and another network parametrizing the conditional Kantorovich potential. To prevent overfitting, we regularize the objective function by penalizing the Lipschitz constant of the network output. Our experiments on real-world datasets show the effectiveness of our algorithm compared to state-of-the-art conditional distribution learning techniques. Our implementation can be found at https://github.com/nguyenngocbaocmt02/GENTLE.

## Metadata
- venue: ICML
- year: 2024
- authors: Bao Nguyen, Binh Nguyen, Hieu Trung Nguyen, Viet Anh Nguyen
- arxiv_id: 
- openreview_id: FoRqdsN4IA
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b058be8068e1d7ace6b3138fc57cbb8a2849b77a.pdf
- published: 2024

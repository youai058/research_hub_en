---
title: "From Search to Sampling: Generative Models for Robust Algorithmic Recourse"
authors: ["Prateek Garg", "Lokesh Nagalapatti", "Sunita Sarawagi"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "NtwFghsJne"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/fcce4ead07ac9d558bf045dbc62907d1308dd399.pdf"
published: "2025"
categories: []
keywords: ["Algorithmic recourse", "explainability", "generative modelling"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:42+09:00"
---

# From Search to Sampling: Generative Models for Robust Algorithmic Recourse

## Abstract
Algorithmic Recourse provides recommendations to individuals who are adversely impacted by automated model decisions, on how to alter their profiles to achieve a favorable outcome. Effective recourse methods must balance three conflicting goals: proximity to the original profile to minimize cost, plausibility for realistic recourse, and validity to ensure the desired outcome. We show that existing methods train for these objectives separately and then search for recourse through a joint optimization over the recourse goals during inference, leading to poor recourse recommendations. We introduce GenRe, a generative recourse model designed to train the three recourse objectives jointly. Training such generative models is non-trivial due to lack of direct recourse supervision. We propose efficient ways to synthesize such supervision and further show that GenRe's training leads to a consistent estimator. Unlike most prior methods, that employ non-robust gradient descent based search during inference, GenRe simply performs a forward sampling over the generative model to produce minimum cost recourse, leading to superior performance across multiple metrics. We also demonstrate GenRe provides the best trade-off between cost, plausibility and validity, compared to state-of-art baselines. Our code is available at: https://github.com/prateekgargX/genre

## Metadata
- venue: ICLR
- year: 2025
- authors: Prateek Garg, Lokesh Nagalapatti, Sunita Sarawagi
- arxiv_id: 
- openreview_id: NtwFghsJne
- anthology_id: 
- pdf_url: https://openreview.net/pdf/fcce4ead07ac9d558bf045dbc62907d1308dd399.pdf
- published: 2025
- keywords: Algorithmic recourse, explainability, generative modelling

---
title: "Personalized Federated Learning via Feature Distribution Adaptation"
authors: ["Connor Mclaughlin", "Lili Su"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Wl2optQcng"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/1a9f33b0581034773546376be681dd6dfdbef3ba.pdf"
published: "2024"
categories: []
keywords: ["Federated Learning", "Data Heterogeneity", "Personalization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:53+09:00"
---

# Personalized Federated Learning via Feature Distribution Adaptation

## Abstract
Federated learning (FL) is a distributed learning framework that leverages commonalities between distributed client datasets to train a global model. Under heterogeneous clients, however, FL can fail to produce stable training results. Personalized federated learning (PFL) seeks to address this by learning individual models tailored to each client. One approach is to decompose model training into shared representation learning and personalized classifier training. Nonetheless, previous works struggle to navigate the bias-variance trade-off in classifier learning, relying solely on limited local datasets or introducing costly techniques to improve generalization.
In this work, we frame representation learning as a generative modeling task, where representations are trained with a classifier based on the global feature distribution. We then propose an algorithm, pFedFDA, that efficiently generates personalized models by adapting global generative classifiers to their local feature distributions. Through extensive computer vision benchmarks, we demonstrate that our method can adjust to complex distribution shifts with significant improvements over current state-of-the-art in data-scarce settings.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Connor Mclaughlin, Lili Su
- arxiv_id: 
- openreview_id: Wl2optQcng
- anthology_id: 
- pdf_url: https://openreview.net/pdf/1a9f33b0581034773546376be681dd6dfdbef3ba.pdf
- published: 2024
- keywords: Federated Learning, Data Heterogeneity, Personalization

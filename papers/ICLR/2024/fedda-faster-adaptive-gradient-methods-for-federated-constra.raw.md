---
title: "FedDA: Faster Adaptive Gradient Methods for Federated Constrained Optimization"
authors: ["Junyi Li", "Feihu Huang", "Heng Huang"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "kjn99xFUF3"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/db0f03c6b9016274933d2407dddcaef05789c2f2.pdf"
published: "2024"
categories: []
keywords: ["Federated Learning", "Adaptive Gradient Methods"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:03+09:00"
---

# FedDA: Faster Adaptive Gradient Methods for Federated Constrained Optimization

## Abstract
Federated learning (FL) is an emerging learning paradigm where a set of distributed clients learns a task under the coordination of a server. The FedAvg algorithm is one of the most widely used methods in FL. In FedAvg, the learning rate is a constant rather than changing adaptively. Adaptive gradient methods have demonstrated superior performance over the constant learning rate schedules in non-distributed settings, and they have recently been adapted to FL. However, the majority of these methods are designed for unconstrained settings. Meanwhile, many crucial FL applications, like disease diagnosis and biomarker identification, often rely on constrained formulations such as Lasso and group Lasso. It remains an open question as to whether adaptive gradient methods can be effectively applied to FL problems with constrains. In this work, we introduce \textbf{FedDA}, a novel adaptive gradient framework for FL. This framework utilizes a restarted dual averaging technique and is compatible with a range of gradient estimation methods and adaptive learning rate schedules.  Specifically, an instantiation of our framework FedDA-MVR achieves sample complexity $\tilde{O}(K^{-1}\epsilon^{-1.5})$ and communication complexity $\tilde{O}(K^{-0.25}\epsilon^{-1.25})$ for finding a stationary point $\epsilon$ in the constrained setting with $K$ be the number of clients. We conduct experiments over both constrained and unconstrained tasks to confirm the effectiveness of our approach.

## Metadata
- venue: ICLR
- year: 2024
- authors: Junyi Li, Feihu Huang, Heng Huang
- arxiv_id: 
- openreview_id: kjn99xFUF3
- anthology_id: 
- pdf_url: https://openreview.net/pdf/db0f03c6b9016274933d2407dddcaef05789c2f2.pdf
- published: 2024
- keywords: Federated Learning, Adaptive Gradient Methods

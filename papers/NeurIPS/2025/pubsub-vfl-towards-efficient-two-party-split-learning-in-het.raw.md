---
title: "PubSub-VFL: Towards Efficient Two-Party Split Learning in Heterogeneous Environments via Publisher/Subscriber Architecture"
authors: ["Yi Liu", "Yang Liu", "Leqian Zheng", "Jue Hong", "Junjie Shi", "Qingyou Yang", "Ye Wu", "Cong Wang"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "B5mEYUJi85"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/6efddd81fa9fa2d7d7a74e0d4954faf308e7745e.pdf"
published: "2025"
categories: []
keywords: ["Vertical Federated Learning", "Publisher/Subscriber Architecture", "Computational Resource Utilization", "Asynchronous Mechanism"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:29+09:00"
---

# PubSub-VFL: Towards Efficient Two-Party Split Learning in Heterogeneous Environments via Publisher/Subscriber Architecture

## Abstract
With the rapid advancement of the digital economy, data collaboration between organizations has become a well-established business model, driving the growth of various industries. However, privacy concerns make direct data sharing impractical. To address this,  Two-Party Split Learning (a.k.a. Vertical Federated Learning (VFL)) has emerged as a promising solution for secure collaborative learning. Despite its advantages, this architecture still suffers from low computational resource utilization and training efficiency. Specifically, its synchronous dependency design increases training latency, while resource and data heterogeneity among participants further hinder efficient computation. To overcome these challenges, we propose \texttt{PubSub-VFL}, a novel VFL paradigm with a Publisher/Subscriber architecture optimized for two-party collaborative learning with high computational efficiency. \texttt{PubSub-VFL} leverages the decoupling capabilities of the Pub/Sub architecture and the data parallelism of the parameter server architecture to design a hierarchical asynchronous mechanism, reducing training latency and improving system efficiency. Additionally, to mitigate the training imbalance caused by resource and data heterogeneity, we formalize an optimization problem based on participants’ system profiles, enabling the selection of optimal hyperparameters while preserving privacy. We conduct a theoretical analysis to demonstrate that \texttt{PubSub-VFL} achieves stable convergence and is compatible with security protocols such as differential privacy. Extensive case studies on five benchmark datasets further validate its effectiveness, showing that \texttt{PubSub-VFL} compared to state-of-the-art baselines not only accelerates training by $2 \sim 7\times$ without compromising accuracy but also achieves computational resource utilization by up to 91.07\%.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Yi Liu, Yang Liu, Leqian Zheng, Jue Hong, Junjie Shi, Qingyou Yang, Ye Wu, Cong Wang
- arxiv_id: 
- openreview_id: B5mEYUJi85
- anthology_id: 
- pdf_url: https://openreview.net/pdf/6efddd81fa9fa2d7d7a74e0d4954faf308e7745e.pdf
- published: 2025
- keywords: Vertical Federated Learning, Publisher/Subscriber Architecture, Computational Resource Utilization, Asynchronous Mechanism

---
title: "Voronoi-grid-based Pareto Front Learning and Its Application to Collaborative Federated Learning"
authors: ["Mengmeng Chen", "Xiaohu Wu", "QIQI LIU", "Tiantian He", "Yew-Soon Ong", "Yaochu Jin", "Qicheng Lao", "Han Yu"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "hrBfufwMzg"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/293e6140e75a0cc75f8cdb375a7e52bc8b370874.pdf"
published: "2025"
categories: []
keywords: ["Hypernetwork", "Multi-objective optimization", "Hypervolume", "Collaborative federated learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:10+09:00"
---

# Voronoi-grid-based Pareto Front Learning and Its Application to Collaborative Federated Learning

## Abstract
Multi-objective optimization (MOO) exists extensively in machine learning, and aims to find a set of Pareto-optimal solutions, called the Pareto front, e.g., it is fundamental for multiple avenues of research in federated learning (FL). Pareto-Front Learning (PFL) is a powerful method implemented using Hypernetworks (PHNs) to approximate the Pareto front. This method enables the acquisition of a mapping function from a given preference vector to the solutions on the Pareto front. However, most existing PFL approaches still face two challenges: (a) sampling rays in high-dimensional spaces; (b) failing to cover the entire Pareto Front which has a convex shape. Here, we introduce a novel PFL framework, called as PHN-HVVS, which decomposes the design space into Voronoi grids and deploys a genetic algorithm (GA) for Voronoi grid partitioning within high-dimensional space. We put forward a new loss function, which effectively contributes to more extensive coverage of the resultant Pareto front and maximizes the HV Indicator. Experimental results on multiple MOO machine learning tasks demonstrate that PHN-HVVS outperforms the baselines significantly in generating Pareto front. Also, we illustrate that PHN-HVVS advances the methodologies of several recent problems in the FL field. The code is available at
https://github.com/buptcmm/phnhvvs.

## Metadata
- venue: ICML
- year: 2025
- authors: Mengmeng Chen, Xiaohu Wu, QIQI LIU, Tiantian He, Yew-Soon Ong, Yaochu Jin, Qicheng Lao, Han Yu
- arxiv_id: 
- openreview_id: hrBfufwMzg
- anthology_id: 
- pdf_url: https://openreview.net/pdf/293e6140e75a0cc75f8cdb375a7e52bc8b370874.pdf
- published: 2025
- keywords: Hypernetwork, Multi-objective optimization, Hypervolume, Collaborative federated learning

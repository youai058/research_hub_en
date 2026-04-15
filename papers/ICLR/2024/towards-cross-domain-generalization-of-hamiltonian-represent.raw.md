---
title: "Towards Cross Domain Generalization of Hamiltonian Representation via Meta Learning"
authors: ["Yeongwoo Song", "Hawoong Jeong"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "AZGIwqCyYY"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b18ec7715410bb144074f86aecfa3acfa91b52d9.pdf"
published: "2024"
categories: []
keywords: ["hamiltonian dynamics", "cross domain generalization", "learning physics", "meta learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:48+09:00"
---

# Towards Cross Domain Generalization of Hamiltonian Representation via Meta Learning

## Abstract
Recent advances in deep learning for physics have focused on discovering shared representations of target systems by incorporating physics priors or inductive biases into neural networks. While effective, these methods are limited to the system domain, where the type of system remains consistent and thus cannot ensure the adaptation to new, or unseen physical systems governed by different laws. For instance, a neural network trained on a mass-spring system cannot guarantee accurate predictions for the behavior of a two-body system or any other system with different physical laws.
In this work, we take a significant leap forward by targeting cross domain generalization within the field of Hamiltonian dynamics. 
We model our system with a graph neural network (GNN) and employ a meta learning algorithm to enable the model to gain experience over a distribution of systems and make it adapt to new physics. Our approach aims to learn a unified Hamiltonian representation that is generalizable across multiple system domains, thereby overcoming the limitations of system-specific models. 
We demonstrate that the meta-trained model captures the generalized Hamiltonian representation that is consistent across different physical domains.
Overall, through the use of meta learning, we offer a framework that achieves cross domain generalization, providing a step towards a unified model for understanding a wide array of dynamical systems via deep learning.

## Metadata
- venue: ICLR
- year: 2024
- authors: Yeongwoo Song, Hawoong Jeong
- arxiv_id: 
- openreview_id: AZGIwqCyYY
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b18ec7715410bb144074f86aecfa3acfa91b52d9.pdf
- published: 2024
- keywords: hamiltonian dynamics, cross domain generalization, learning physics, meta learning

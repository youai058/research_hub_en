---
title: "PDHG-Unrolled Learning-to-Optimize Method for Large-Scale Linear Programming"
authors: ["Bingheng Li", "Linxin Yang", "Yupeng Chen", "Senmiao Wang", "Haitao Mao", "Qian Chen", "Yao Ma", "Akang Wang", "Tian Ding", "Jiliang Tang", "Ruoyu Sun"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "2cXzNDe614"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9629df6a80e9b3fa1c739336d6392b97a0aac2f8.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:33+09:00"
---

# PDHG-Unrolled Learning-to-Optimize Method for Large-Scale Linear Programming

## Abstract
Solving large-scale linear programming (LP) problems is an important task in various areas such as communication networks, power systems, finance and logistics. Recently, two distinct approaches have emerged to expedite LP solving: (i) First-order methods (FOMs); (ii) Learning to optimize (L2O). In this work, we propose an FOM-unrolled neural network (NN) called PDHG-Net, and propose a two-stage L2O method to solve large-scale LP problems. The new architecture PDHG-Net is designed by unrolling the recently emerged PDHG method into a neural network, combined with channel-expansion techniques borrowed from graph neural networks. We prove that the proposed PDHG-Net can recover PDHG algorithm, thus can approximate optimal solutions of LP instances with a polynomial number of neurons. We propose a two-stage inference approach: first use PDHG-Net to generate an approximate solution, and then apply PDHG algorithm to further improve the solution. Experiments show that our approach can significantly accelerate LP solving, achieving up to a 3$\times$ speedup compared to FOMs for large-scale LP problems.

## Metadata
- venue: ICML
- year: 2024
- authors: Bingheng Li, Linxin Yang, Yupeng Chen, Senmiao Wang, Haitao Mao, Qian Chen, Yao Ma, Akang Wang, Tian Ding, Jiliang Tang, Ruoyu Sun
- arxiv_id: 
- openreview_id: 2cXzNDe614
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9629df6a80e9b3fa1c739336d6392b97a0aac2f8.pdf
- published: 2024

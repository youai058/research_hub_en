---
title: "On the Scalability and Memory Efficiency of Semidefinite Programs  for Lipschitz Constant Estimation of Neural Networks"
authors: ["Zi Wang", "Bin Hu", "Aaron J Havens", "Alexandre Araujo", "Yang Zheng", "Yudong Chen", "Somesh Jha"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "dwzLn78jq7"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/333a8145de80d282eac48f6722bab292ed03b563.pdf"
published: "2024"
categories: []
keywords: ["Semidefinite programming", "Lipschitz constant", "Deep learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:09+09:00"
---

# On the Scalability and Memory Efficiency of Semidefinite Programs  for Lipschitz Constant Estimation of Neural Networks

## Abstract
Lipschitz constant estimation plays an important role in understanding generalization, robustness, and fairness in deep learning. Unlike naive bounds based on the network weight norm product, semidefinite programs (SDPs) have shown great promise in providing less conservative Lipschitz bounds with polynomial-time complexity guarantees. However, due to the memory consumption and running speed, standard SDP algorithms cannot scale to modern neural network architectures. In this paper, we transform the SDPs for Lipschitz constant estimation into an eigenvalue optimization problem, which aligns with the modern large-scale optimization paradigms based on first-order methods. This is amenable to autodiff frameworks such as PyTorch and TensorFlow, requiring significantly less memory than standard SDP algorithms. The transformation also allows us to leverage various existing numerical techniques for eigenvalue optimization, opening the way for further memory improvement and computational speedup. The essential technique of our eigenvalue-problem transformation is to introduce redundant quadratic constraints and then utilize both Lagrangian and Shor's SDP relaxations under a certain trace constraint.  Notably, our numerical study successfully scales the SDP-based Lipschitz constant estimation to address large neural networks on ImageNet. Our numerical examples on CIFAR10 and ImageNet demonstrate that our technique is more scalable than existing approaches. Our code is available at https://github.com/z1w/LipDiff.

## Metadata
- venue: ICLR
- year: 2024
- authors: Zi Wang, Bin Hu, Aaron J Havens, Alexandre Araujo, Yang Zheng, Yudong Chen, Somesh Jha
- arxiv_id: 
- openreview_id: dwzLn78jq7
- anthology_id: 
- pdf_url: https://openreview.net/pdf/333a8145de80d282eac48f6722bab292ed03b563.pdf
- published: 2024
- keywords: Semidefinite programming, Lipschitz constant, Deep learning

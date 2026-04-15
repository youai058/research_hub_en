---
title: "GotenNet: Rethinking Efficient 3D Equivariant Graph Neural Networks"
authors: ["Sarp Aykent", "Tian Xia"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "5wxCQDtbMo"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a1396f1d1e7975177c314f3bddd7e718fc87796e.pdf"
published: "2025"
categories: []
keywords: ["graph neural networks", "computational physics", "3D graphs"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:58+09:00"
---

# GotenNet: Rethinking Efficient 3D Equivariant Graph Neural Networks

## Abstract
Understanding complex three-dimensional (3D) structures of graphs is essential for accurately modeling various properties, yet many existing approaches struggle with fully capturing the intricate spatial relationships and symmetries inherent in such systems, especially in large-scale, dynamic molecular datasets. These methods often must balance trade-offs between expressiveness and computational efficiency, limiting their scalability. To address this gap, we propose a novel Geometric Tensor Network (GotenNet) that effectively models the geometric intricacies of 3D graphs while ensuring strict equivariance under the Euclidean group E(3). Our approach directly tackles the expressiveness-efficiency trade-off by leveraging effective geometric tensor representations without relying on irreducible representations or Clebsch-Gordan transforms, thereby reducing computational overhead. We introduce a unified structural embedding, incorporating geometry-aware tensor attention and hierarchical tensor refinement that iteratively updates edge representations through inner product operations on high-degree steerable features, allowing for flexible and efficient representations for various tasks. We evaluated models on QM9, rMD17, MD22, and Molecule3D datasets, where the proposed model consistently outperforms state-of-the-art methods in both scalar and high-degree property predictions, demonstrating exceptional robustness across diverse datasets, and establishes GotenNet as a versatile and scalable framework for 3D equivariant Graph Neural Networks.

## Metadata
- venue: ICLR
- year: 2025
- authors: Sarp Aykent, Tian Xia
- arxiv_id: 
- openreview_id: 5wxCQDtbMo
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a1396f1d1e7975177c314f3bddd7e718fc87796e.pdf
- published: 2025
- keywords: graph neural networks, computational physics, 3D graphs

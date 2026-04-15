---
title: "HiRemate: Hierarchical Approach for Efficient Re-materialization of Neural Networks"
authors: ["Julia Gusak", "Xunyi Zhao", "Théotime Le Hellard", "Zhe LI", "Lionel Eyraud-Dubois", "Olivier Beaumont"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "rnx11J4hsg"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ba3fdf7e28d1a05cb61ef49564fac32d254255f2.pdf"
published: "2025"
categories: []
keywords: ["Rematerialization", "Checkpointing", "Memory-Efficient Training", "Neural Networks", "PyTorch", "Integer Linear Programming", "Training"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:03+09:00"
---

# HiRemate: Hierarchical Approach for Efficient Re-materialization of Neural Networks

## Abstract
Training deep neural networks (DNNs) on memory-limited GPUs is challenging,  as storing intermediate activations often exceeds available memory. Re-materialization, a technique that preserves exact computations, addresses this by selectively recomputing activations instead of storing them. However, existing methods either fail to scale, lack generality, or introduce excessive execution overhead. We introduce ${\mbox{HiRemate}}$ a ${\textit hierarchical}$ re-materialization framework that recursively partitions  large computation graphs, applies optimized solvers at multiple levels, and merges solutions into a global efficient training schedule. This enables scalability to significantly larger graphs than prior ILP-based methods while keeping runtime overhead low. Designed for single-GPU models and activation re-materialization, HiRemate extends  the feasibility of training networks with thousands of graph nodes, surpassing  prior methods in both efficiency and scalability. Experiments on various types of networks yield up to 50-70%  memory reduction with only 10-15% overhead, closely matching optimal solutions while significantly reducing solver time. Seamlessly integrating with PyTorch Autograd, HiRemate requires almost no  code change to use,  enabling broad adoption in memory-constrained deep learning.

## Metadata
- venue: ICML
- year: 2025
- authors: Julia Gusak, Xunyi Zhao, Théotime Le Hellard, Zhe LI, Lionel Eyraud-Dubois, Olivier Beaumont
- arxiv_id: 
- openreview_id: rnx11J4hsg
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ba3fdf7e28d1a05cb61ef49564fac32d254255f2.pdf
- published: 2025
- keywords: Rematerialization, Checkpointing, Memory-Efficient Training, Neural Networks, PyTorch, Integer Linear Programming, Training

---
title: "Solver-Free Decision-Focused Learning for Linear Optimization Problems"
authors: ["Senne Berden", "Ali İrfan Mahmutoğulları", "Dimos Tsouros", "Tias Guns"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "xMcKyUGTt1"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/861234a45c586918a05e4a83eaa548f4588a0d2c.pdf"
published: "2025"
categories: []
keywords: ["Decision-Focused Learning", "Predict-then-Optimize", "Contextual Optimization", "Linear Programming"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:57+09:00"
---

# Solver-Free Decision-Focused Learning for Linear Optimization Problems

## Abstract
Mathematical optimization is a fundamental tool for decision-making in a wide range of applications. However, in many real-world scenarios, the parameters of the optimization problem are not known a priori and must be predicted from contextual features. This gives rise to predict-then-optimize problems, where a machine learning model predicts problem parameters that are then used to make decisions via optimization. A growing body of work on decision-focused learning (DFL) addresses this setting by training models specifically to produce predictions that maximize downstream decision quality, rather than accuracy. While effective, DFL is computationally expensive, because it requires solving the optimization problem with the predicted parameters at each loss evaluation. In this work, we address this computational bottleneck for linear optimization problems, a common class of problems in both DFL literature and real-world applications. We propose a solver-free training method that exploits the geometric structure of linear optimization to enable efficient training with minimal degradation in solution quality. Our method is based on the insight that a solution is optimal if and only if it achieves an objective value that is at least as good as that of its adjacent vertices on the feasible polytope. Building on this, our method compares the estimated quality of the ground-truth optimal solution with that of its precomputed adjacent vertices, and uses this as loss function. Experiments demonstrate that our method significantly reduces computational cost while maintaining high decision quality.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Senne Berden, Ali İrfan Mahmutoğulları, Dimos Tsouros, Tias Guns
- arxiv_id: 
- openreview_id: xMcKyUGTt1
- anthology_id: 
- pdf_url: https://openreview.net/pdf/861234a45c586918a05e4a83eaa548f4588a0d2c.pdf
- published: 2025
- keywords: Decision-Focused Learning, Predict-then-Optimize, Contextual Optimization, Linear Programming

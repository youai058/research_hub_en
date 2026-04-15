---
title: "Learning Initial Basis Selection for Linear Programming via Duality-Inspired Tripartite Graph Representation and Comprehensive Supervision"
authors: ["Anqi Lu", "Junchi Yan"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "WtD8EIzkmm"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/1bf68a1d5ba6ad60821dc484f401e5d2cbaa03d6.pdf"
published: "2025"
categories: []
keywords: ["supervised learning", "graph neural network", "linear programming", "simplex method", "initial basis"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:26+09:00"
---

# Learning Initial Basis Selection for Linear Programming via Duality-Inspired Tripartite Graph Representation and Comprehensive Supervision

## Abstract
For the fundamental linear programming (LP) problems, the simplex method remains popular, which usually requires an appropriate initial basis as a warm start to accelerate the solving process. Predicting an initial basis close to an optimal one can often accelerate the solver, but a closer initial basis does not always result in greater acceleration. To achieve better acceleration, we propose a GNN model based on a tripartite graph representation inspired by LP duality. This approach enables more effective feature extraction for general LP problems and enhances the expressiveness of GNNs. Additionally, we introduce novel loss functions targeting basic variable selection and basis feasibility, along with data preprocessing schemes, to further improve learning capability. In addition to achieving high prediction accuracy, we enhance the quality of the initial basis for practical use. Experimental results show that our approach greatly surpasses the state-of-the-art method in predicting initial basis with greater accuracy and in reducing the number of iterations and solving time of the LP solver.

## Metadata
- venue: ICML
- year: 2025
- authors: Anqi Lu, Junchi Yan
- arxiv_id: 
- openreview_id: WtD8EIzkmm
- anthology_id: 
- pdf_url: https://openreview.net/pdf/1bf68a1d5ba6ad60821dc484f401e5d2cbaa03d6.pdf
- published: 2025
- keywords: supervised learning, graph neural network, linear programming, simplex method, initial basis

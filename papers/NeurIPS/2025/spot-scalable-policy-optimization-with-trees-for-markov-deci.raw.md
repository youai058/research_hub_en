---
title: "SPOT: Scalable Policy Optimization with Trees for Markov Decision Processes"
authors: ["Xuyuan Xiong", "Pedro Chumpitaz-Flores", "Kaixun Hua", "Cheng Hua"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "OR5WyyTESh"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/cc3f46c5114ba237ef39ab22ad248f54cf718a37.pdf"
published: "2025"
categories: []
keywords: ["Decision Tree", "Markov Decision Processes"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:26+09:00"
---

# SPOT: Scalable Policy Optimization with Trees for Markov Decision Processes

## Abstract
Interpretable reinforcement learning policies are essential for high-stakes decision-making, yet optimizing decision tree policies in Markov Decision Processes (MDPs) remains challenging. We propose SPOT, a novel method for computing decision tree policies, which formulates the optimization problem as a mixed-integer linear program (MILP). To enhance efficiency, we employ a reduced-space branch-and-bound approach that decouples the MDP dynamics from tree-structure constraints, enabling efficient parallel search. This significantly improves runtime and scalability compared to previous methods. Our approach ensures that each iteration yields the optimal decision tree. Experimental results on standard benchmarks demonstrate that SPOT achieves substantial speedup and scales to larger MDPs with a significantly higher number of states. The resulting decision tree policies are interpretable and compact, maintaining transparency without compromising performance. These results demonstrate that our approach simultaneously achieves interpretability and scalability, delivering high-quality policies an order of magnitude faster than existing approaches.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Xuyuan Xiong, Pedro Chumpitaz-Flores, Kaixun Hua, Cheng Hua
- arxiv_id: 
- openreview_id: OR5WyyTESh
- anthology_id: 
- pdf_url: https://openreview.net/pdf/cc3f46c5114ba237ef39ab22ad248f54cf718a37.pdf
- published: 2025
- keywords: Decision Tree, Markov Decision Processes

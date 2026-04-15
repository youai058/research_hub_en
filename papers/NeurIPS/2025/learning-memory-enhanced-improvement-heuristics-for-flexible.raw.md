---
title: "Learning Memory-Enhanced Improvement Heuristics for Flexible Job Shop Scheduling"
authors: ["Jiaqi Wang", "Zhiguang Cao", "Peng Zhao", "Rui Cao", "Yubin Xiao", "Yuan Jiang", "You Zhou"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "sdlLycSeZl"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c1281713ced0a0c3c3513aa630523fa4a9d60946.pdf"
published: "2025"
categories: []
keywords: ["Flexible Job-Shop Scheduling Problem", "Graph Neural Network", "Reinforcement Learning", "Combinatorial Optimization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:50+09:00"
---

# Learning Memory-Enhanced Improvement Heuristics for Flexible Job Shop Scheduling

## Abstract
The rise of smart manufacturing under Industry 4.0 introduces mass customization and dynamic production, demanding more advanced and flexible scheduling techniques. The flexible job-shop scheduling problem (FJSP) has attracted significant attention due to its complex constraints and strong alignment with real-world production scenarios. Current deep reinforcement learning (DRL)-based approaches to FJSP predominantly employ constructive methods. While effective, they often fall short of reaching (near-)optimal solutions. In contrast, improvement-based methods iteratively explore the neighborhood of initial solutions and are more effective in approaching optimality. However, the flexible machine allocation in FJSP poses significant challenges to the application of this framework, including accurate state representation, effective policy learning, and efficient search strategies. To address these challenges, this paper proposes a $\textbf{M}$emory-enhanced $\textbf{I}$mprovement $\textbf{S}$earch framework with he$\textbf{t}$erogeneous gr$\textbf{a}$ph $\textbf{r}$epresentation—$\textit{MIStar}$. It employs a novel heterogeneous disjunctive graph that explicitly models the operation sequences on machines to accurately represent scheduling solutions. Moreover, a memory-enhanced heterogeneous graph neural network (MHGNN) is designed for feature extraction, leveraging historical trajectories to enhance the decision-making capability of the policy network. Finally, a parallel greedy search strategy is adopted to explore the solution space, enabling superior solutions with fewer iterations. Extensive experiments on synthetic data and public benchmarks demonstrate that $\textit{MIStar}$ significantly outperforms both traditional handcrafted improvement heuristics and state-of-the-art DRL-based constructive methods.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Jiaqi Wang, Zhiguang Cao, Peng Zhao, Rui Cao, Yubin Xiao, Yuan Jiang, You Zhou
- arxiv_id: 
- openreview_id: sdlLycSeZl
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c1281713ced0a0c3c3513aa630523fa4a9d60946.pdf
- published: 2025
- keywords: Flexible Job-Shop Scheduling Problem, Graph Neural Network, Reinforcement Learning, Combinatorial Optimization

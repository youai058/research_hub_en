---
title: "CaDA: Cross-Problem Routing Solver with Constraint-Aware Dual-Attention"
authors: ["Han Li", "Fei Liu", "Zhi Zheng", "Yu Zhang", "Zhenkun Wang"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "CS4RyQuTig"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c313519baeef3489a1f66159f8314120407bd813.pdf"
published: "2025"
categories: []
keywords: ["Vehicle Routing Problem", "Multi-Task Learning", "Task-Specific Prompt", "Dual Attention Mechanism", "Cross-Problem Learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:14+09:00"
---

# CaDA: Cross-Problem Routing Solver with Constraint-Aware Dual-Attention

## Abstract
Vehicle routing problems (VRPs) are significant combinatorial optimization problems (COPs) holding substantial practical importance. Recently, neural combinatorial optimization (NCO), which involves training deep learning models on extensive data to learn vehicle routing heuristics, has emerged as a promising approach due to its efficiency and the reduced need for manual algorithm design. However, applying NCO across diverse real-world scenarios with various constraints necessitates cross-problem capabilities. Current cross-problem NCO methods for VRPs typically employ a constraint-unaware model, limiting their cross-problem performance. Furthermore, they rely solely on global connectivity, which fails to focus on key nodes and leads to inefficient representation learning. This paper introduces a \underline{C}onstraint-\underline{A}ware \underline{D}ual-\underline{A}ttention Model (CaDA), designed to address these limitations. CaDA incorporates a constraint prompt that efficiently represents different problem variants. Additionally, it features a dual-attention mechanism with a global branch for capturing broader graph-wide information and a sparse branch that selectively focuses on the key node connections. We comprehensively evaluate our model on 16 different VRPs and compare its performance against existing cross-problem VRP solvers. CaDA achieves state-of-the-art results across all tested VRPs. Our ablation study confirms that each component contributes to its cross-problem learning performance. The source code for CaDA is publicly available at \url{https://github.com/CIAM-Group/CaDA}.

## Metadata
- venue: ICML
- year: 2025
- authors: Han Li, Fei Liu, Zhi Zheng, Yu Zhang, Zhenkun Wang
- arxiv_id: 
- openreview_id: CS4RyQuTig
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c313519baeef3489a1f66159f8314120407bd813.pdf
- published: 2025
- keywords: Vehicle Routing Problem, Multi-Task Learning, Task-Specific Prompt, Dual Attention Mechanism, Cross-Problem Learning

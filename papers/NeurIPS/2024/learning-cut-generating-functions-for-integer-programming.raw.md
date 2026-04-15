---
title: "Learning Cut Generating Functions for Integer Programming"
authors: ["Hongyu Cheng", "Amitabh Basu"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "8mZc259r8X"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/08f049aa35c3814ad4503bad3dfdb5bc899c7504.pdf"
published: "2024"
categories: []
keywords: ["Integer programming", "branch-and-cut", "cut generating functions", "cutting planes", "branch-and-bound", "sample complexity", "learning theory"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:02+09:00"
---

# Learning Cut Generating Functions for Integer Programming

## Abstract
The branch-and-cut algorithm is the method of choice to solve large scale integer programming problems in practice. A key ingredient of branch-and-cut is the use of *cutting planes* which are derived constraints that reduce the search space for an optimal solution. Selecting effective cutting planes to produce small branch-and-cut trees is a critical challenge in the branch-and-cut algorithm. Recent advances have employed a data-driven approach to select good cutting planes from a parameterized family, aimed at reducing the branch-and-bound tree size (in expectation) for a given distribution of integer programming instances. We extend this idea to the selection of the best cut generating function (CGF), which is a tool in the integer programming literature for generating a wide variety of cutting planes that generalize the well-known Gomory Mixed-Integer (GMI) cutting planes. We provide rigorous sample complexity bounds for the selection of an effective CGF from certain parameterized families that provably performs well for any specified distribution on the problem instances. Our empirical results show that the selected CGF can outperform the GMI cuts for certain distributions. Additionally, we explore the sample complexity of using neural networks for instance-dependent CGF selection.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Hongyu Cheng, Amitabh Basu
- arxiv_id: 
- openreview_id: 8mZc259r8X
- anthology_id: 
- pdf_url: https://openreview.net/pdf/08f049aa35c3814ad4503bad3dfdb5bc899c7504.pdf
- published: 2024
- keywords: Integer programming, branch-and-cut, cut generating functions, cutting planes, branch-and-bound, sample complexity, learning theory

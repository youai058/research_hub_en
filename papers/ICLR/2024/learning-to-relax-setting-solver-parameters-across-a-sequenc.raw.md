---
title: "Learning to Relax: Setting Solver Parameters Across a Sequence of Linear System Instances"
authors: ["Mikhail Khodak", "Edmond Chow", "Maria Florina Balcan", "Ameet Talwalkar"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "5t57omGVMw"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/352f7e2fbdc33555b4c784ea0abafc770f9f6836.pdf"
published: "2024"
categories: []
keywords: ["scientific computing", "data-driven algorithm design", "online learning", "multi-armed bandits", "contextual bandits", "numerical analysis", "learning-augmented algorithms", "algorithms with predictions"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:04+09:00"
---

# Learning to Relax: Setting Solver Parameters Across a Sequence of Linear System Instances

## Abstract
Solving a linear system ${\bf Ax}={\bf b}$ is a fundamental scientific computing primitive for which numerous solvers and preconditioners have been developed. 
	These come with parameters whose optimal values depend on the system being solved and are often impossible or too expensive to identify;
	thus in practice sub-optimal heuristics are used.
	We consider the common setting in which many related linear systems need to be solved, e.g. during a single numerical simulation.
	In this scenario, can we sequentially choose parameters that attain a near-optimal overall number of iterations, without extra matrix computations?
	We answer in the affirmative for Successive Over-Relaxation (SOR), a standard solver whose parameter $\omega$ has a strong impact on its runtime.
	For this method, we prove that a bandit online learning algorithm—using only the number of iterations as feedback—can select parameters for a sequence of instances such that the overall cost approaches that of the best fixed $\omega$ as the sequence length increases.
	Furthermore, when given additional structural information, we show that a _contextual_ bandit method asymptotically achieves the performance of the _instance-optimal_ policy, which selects the best $\omega$ for each instance.
	Our work provides the first learning-theoretic treatment of high-precision linear system solvers and the first end-to-end guarantees for data-driven scientific computing, demonstrating theoretically the potential to speed up numerical methods using well-understood learning algorithms.

## Metadata
- venue: ICLR
- year: 2024
- authors: Mikhail Khodak, Edmond Chow, Maria Florina Balcan, Ameet Talwalkar
- arxiv_id: 
- openreview_id: 5t57omGVMw
- anthology_id: 
- pdf_url: https://openreview.net/pdf/352f7e2fbdc33555b4c784ea0abafc770f9f6836.pdf
- published: 2024
- keywords: scientific computing, data-driven algorithm design, online learning, multi-armed bandits, contextual bandits, numerical analysis, learning-augmented algorithms, algorithms with predictions

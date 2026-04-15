---
title: "Semi-Random Matrix Completion via Flow-Based Adaptive Reweighting"
authors: ["Jonathan Kelner", "Jerry Li", "Allen Liu", "Aaron Sidford", "Kevin Tian"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "XZp1uP0hh2"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f37ead2ac2d353db44749fa8bfbc69aa88ba15c6.pdf"
published: "2024"
categories: []
keywords: ["matrix completion", "semi-random model", "flow solver", "short-flat decomposition", "adaptive reweighting"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:31+09:00"
---

# Semi-Random Matrix Completion via Flow-Based Adaptive Reweighting

## Abstract
We consider the well-studied problem of completing a rank-$r$, $\mu$-incoherent matrix $\mathbf{M} \in \mathbb{R}^{d \times d}$ from incomplete observations. We focus on this problem in the semi-random setting where each entry is independently revealed with probability at least $p = \frac{\textup{poly}(r, \mu, \log d)}{d}$. 
Whereas multiple nearly-linear time algorithms have been established in the more specialized fully-random setting where each entry is revealed with probablity exactly $p$, the only known nearly-linear time algorithm in the semi-random setting is due to [CG18], whose sample complexity has a polynomial dependence on the inverse accuracy and condition number and thus cannot achieve high-accuracy recovery. 
Our main result is the first high-accuracy nearly-linear time algorithm for solving semi-random matrix completion, and an extension to the noisy observation setting.
Our result builds upon the recent short-flat decomposition framework of [KLLST23a, KLLST23b] and leverages fast algorithms for flow problems on graphs to solve adaptive reweighting subproblems efficiently.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Jonathan Kelner, Jerry Li, Allen Liu, Aaron Sidford, Kevin Tian
- arxiv_id: 
- openreview_id: XZp1uP0hh2
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f37ead2ac2d353db44749fa8bfbc69aa88ba15c6.pdf
- published: 2024
- keywords: matrix completion, semi-random model, flow solver, short-flat decomposition, adaptive reweighting

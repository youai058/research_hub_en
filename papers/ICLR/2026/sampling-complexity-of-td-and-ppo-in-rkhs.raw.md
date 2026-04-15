---
title: "Sampling Complexity of TD and PPO in RKHS"
authors: ["LU ZOU", "Wendi Ren", "WEIZHONG ZHANG", "Liang Ding", "Shuang Li"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "5gUMhTUDi0"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/7b45a51bf5f40d1afee4a426a90775992d712c61.pdf"
published: "2026"
categories: []
keywords: ["Kernel method", "Kernel gradient descent", "PPO", "Temporal difference"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:44+09:00"
---

# Sampling Complexity of TD and PPO in RKHS

## Abstract
We revisit Proximal Policy Optimization (PPO) from a function-space perspective. 
Our analysis decouples policy evaluation and improvement in a reproducing kernel Hilbert space (RKHS): 
(i)  A kernelized temporal-difference (TD) critic performs efficient RKHS-gradient updates using only one-step state–action transition samples.
(ii) a KL-regularized, natural-gradient policy step exponentiates the evaluated action-value, recovering a PPO/TRPO-style proximal update in continuous state-action spaces. 
We provide non-asymptotic, instance-adaptive guarantees whose rates depend on RKHS entropy, unifying tabular, linear, Sobolev, Gaussian, and Neural Tangent Kernel (NTK) regimes, and we derive a sampling rule for the proximal update that ensures the optimal $k^{-1/2}$  convergence rate for stochastic optimization.
Empirically, the theory-aligned schedule improves stability and sample efficiency on common control tasks (e.g., CartPole, Acrobot, and HalfCheetah), while our TD-based critic attains favorable throughput versus a GAE baseline. 
Altogether, our results place PPO on a firmer theoretical footing beyond finite-dimensional assumptions and clarify when RKHS-proximal updates with kernel-TD critics yield global policy improvement with practical efficiency.

## Metadata
- venue: ICLR
- year: 2026
- authors: LU ZOU, Wendi Ren, WEIZHONG ZHANG, Liang Ding, Shuang Li
- arxiv_id: 
- openreview_id: 5gUMhTUDi0
- anthology_id: 
- pdf_url: https://openreview.net/pdf/7b45a51bf5f40d1afee4a426a90775992d712c61.pdf
- published: 2026
- keywords: Kernel method, Kernel gradient descent, PPO, Temporal difference

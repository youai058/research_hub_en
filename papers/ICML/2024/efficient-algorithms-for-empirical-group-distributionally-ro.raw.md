---
title: "Efficient Algorithms for Empirical Group Distributionally Robust Optimization and Beyond"
authors: ["Dingzhi Yu", "Yunuo Cai", "Wei Jiang", "Lijun Zhang"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "pOJbk4Nzmi"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f287b77bba02edd7f0307d9353e94fb1a90cc75c.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:11+09:00"
---

# Efficient Algorithms for Empirical Group Distributionally Robust Optimization and Beyond

## Abstract
In this paper, we investigate the empirical counterpart of Group Distributionally Robust Optimization (GDRO), which aims to minimize the maximal empirical risk across $m$ distinct groups. We formulate empirical GDRO as a *two-level* finite-sum convex-concave minimax optimization problem and develop an algorithm called ALEG to benefit from its special structure. ALEG is a double-looped stochastic primal-dual algorithm that incorporates variance reduction techniques into a modified mirror prox routine. To exploit the two-level finite-sum structure, we propose a simple group sampling strategy to construct the stochastic gradient with a smaller Lipschitz constant and then perform variance reduction for all groups. Theoretical analysis shows that ALEG achieves $\varepsilon$-accuracy within a computation complexity of $\mathcal{O}\left(\frac{m\sqrt{\bar{n}\ln{m}}}{\varepsilon}\right)$, where $\bar n$ is the average number of samples among $m$ groups. Notably, our approach outperforms the state-of-the-art method by a factor of $\sqrt{m}$. Based on ALEG, we further develop a two-stage optimization algorithm called ALEM to deal with the empirical Minimax Excess Risk Optimization (MERO) problem. The computation complexity of ALEM nearly matches that of ALEG, surpassing the rates of existing methods.

## Metadata
- venue: ICML
- year: 2024
- authors: Dingzhi Yu, Yunuo Cai, Wei Jiang, Lijun Zhang
- arxiv_id: 
- openreview_id: pOJbk4Nzmi
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f287b77bba02edd7f0307d9353e94fb1a90cc75c.pdf
- published: 2024

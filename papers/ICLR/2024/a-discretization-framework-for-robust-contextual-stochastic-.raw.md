---
title: "A Discretization Framework for Robust Contextual Stochastic Optimization"
authors: ["Rares C Cristian", "Georgia Perakis"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ueTdErd5Ib"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2097641b7d16f85a6d284604d4e690fc32f2e79e.pdf"
published: "2024"
categories: []
keywords: ["Robust Optimization", "Stochastic Optimization", "End-to-End learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:26+09:00"
---

# A Discretization Framework for Robust Contextual Stochastic Optimization

## Abstract
We study contextual stochastic optimization problems. Optimization problems have uncertain parameters stemming from unknown, context-dependent, distributions. Due to the inherent uncertainty in these problems, one is often interested not only in minimizing expected cost, but also to be robust and protect against worst case scenarios. We propose a novel method that combines the learning stage with knowledge of the downstream optimization task. The method prescribes decisions which aim to maximize the likelihood that the cost is below a (user-controlled) threshold. The key idea is (1) to discretize the feasible region into subsets so that the uncertain objective function can be well approximated deterministically within each subset, and (2) devise a secondary optimization problem to prescribe decisions by integrating the individual approximations determined in step (1). We provide theoretical guarantees bounding the underlying regret of decisions proposed by our method. In addition, experimental results demonstrate that our approach is competitive in terms of average regret and yields more robust solutions than other methods proposed in the literature, including up to 20 times lower worst-case cost on a real-world electricity generation problem.

## Metadata
- venue: ICLR
- year: 2024
- authors: Rares C Cristian, Georgia Perakis
- arxiv_id: 
- openreview_id: ueTdErd5Ib
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2097641b7d16f85a6d284604d4e690fc32f2e79e.pdf
- published: 2024
- keywords: Robust Optimization, Stochastic Optimization, End-to-End learning

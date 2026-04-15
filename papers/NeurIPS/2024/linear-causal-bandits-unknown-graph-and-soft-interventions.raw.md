---
title: "Linear Causal Bandits: Unknown Graph and Soft Interventions"
authors: ["Zirui Yan", "Ali Tajer"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "PAu0W5YAKC"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e2c7942455420e359af0afa223783e8645830b0d.pdf"
published: "2024"
categories: []
keywords: ["causal bandit", "unknown graph", "soft interventions"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:04+09:00"
---

# Linear Causal Bandits: Unknown Graph and Soft Interventions

## Abstract
Designing causal bandit algorithms depends on two central categories of assumptions: (i) the extent of information about the underlying causal graphs and (ii) the extent of information about interventional statistical models. There have been extensive recent advances in dispensing with assumptions on either category. These include assuming known graphs but unknown interventional distributions, and the converse setting of assuming unknown graphs but access to restrictive hard/$\operatorname{do}$ interventions, which removes the stochasticity and ancestral dependencies. Nevertheless, the problem in its general form, i.e., _unknown_ graph and _unknown_ stochastic intervention models, remains open. This paper addresses this problem and establishes that in a graph with $N$ nodes, maximum in-degree $d$ and maximum causal path length $L$, after $T$ interaction rounds the regret upper bound scales as $\tilde{\mathcal{O}}((cd)^{L-\frac{1}{2}}\sqrt{T} + d + RN)$ where $c>1$ is a constant and  $R$ is a measure of intervention power. A universal minimax lower bound is also established, which scales as $\Omega(d^{L-\frac{3}{2}}\sqrt{T})$. Importantly, the graph size $N$ has a diminishing effect on the regret as $T$ grows. These bounds have matching behavior in $T$, exponential dependence on $L$, and polynomial dependence on $d$ (with the gap $d\ $). On the algorithmic aspect, the paper presents a novel way of designing a computationally efficient CB algorithm, addressing a challenge that the existing CB algorithms using soft interventions face.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Zirui Yan, Ali Tajer
- arxiv_id: 
- openreview_id: PAu0W5YAKC
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e2c7942455420e359af0afa223783e8645830b0d.pdf
- published: 2024
- keywords: causal bandit, unknown graph, soft interventions

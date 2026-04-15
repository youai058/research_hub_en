---
title: "Causal Mixture Models: Characterization and Discovery"
authors: ["Sarah Mameche", "Janis Kalofolias", "Jilles Vreeken"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "aI3d897dgV"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ccff832195f36966f6e37445c6efaa5f900570e8.pdf"
published: "2025"
categories: []
keywords: ["causal discovery", "mixture modelling"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:32+09:00"
---

# Causal Mixture Models: Characterization and Discovery

## Abstract
Real-world datasets are often a combination of unobserved subpopulations that follow distinct causal generating processes. In an observational study, for example, participants may fall into unknown groups that either (a) respond effectively to a drug, or (b) show no response due to drug resistance. Not accounting for such heterogeneity then risks biased estimates of  drug effectiveness.  
 In this work, we formulate this setting through a causal mixture model,
 in which the data-generating process of each variable depends on latent group membership (a or b). Specifically, we model each variable as a   mixture of structural causal equation models, where latent categorical (mixing) variables index assignment to subpopulations. Unlike prior work, the approach allows  for multiple independent mixing variables, each affecting distinct sets of observed variables. To infer both the graph, mixing variables, and assignments jointly, we integrate mixture modeling into score-based causal discovery; show theoretically that the resulting scoring criterion is consistent; and demonstrate  empirically that the resulting causal discovery approach discovers the causal model in synthetic and real-world evaluations.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Sarah Mameche, Janis Kalofolias, Jilles Vreeken
- arxiv_id: 
- openreview_id: aI3d897dgV
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ccff832195f36966f6e37445c6efaa5f900570e8.pdf
- published: 2025
- keywords: causal discovery, mixture modelling

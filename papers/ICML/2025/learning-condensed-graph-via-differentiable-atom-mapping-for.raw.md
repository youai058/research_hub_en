---
title: "Learning Condensed Graph via Differentiable Atom Mapping for Reaction Yield Prediction"
authors: ["Ankit Ghosh", "Gargee Kashyap", "Sarthak Mittal", "Nupur Jain", "Raghavan B Sunoj", "Abir De"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "sqjQ6p56GR"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/8ed2edcb4d1c67b609b9a3092caeb9244f289c25.pdf"
published: "2025"
categories: []
keywords: ["Yield Prediction", "GNN", "Atom Mapping"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:31+09:00"
---

# Learning Condensed Graph via Differentiable Atom Mapping for Reaction Yield Prediction

## Abstract
Yield of chemical reactions generally depends on the activation barrier, i.e., the energy difference between the reactant and the transition state. Computing the transition state from the reactant and product graphs requires prior knowledge of the correct node alignment (i.e., atom mapping), which is not available in yield prediction datasets.  In this work, we propose YieldNet, a neural yield prediction model, which tackles these challenges.  Here, we first  approximate the atom mapping between the reactants and products using a differentiable node alignment network. We then use this approximate atom mapping to obtain a noisy realization of the condensed graph of reaction (CGR),  which is a supergraph encompassing both the reactants and products. This CGR  serves as a surrogate for the transition state graph structure. The CGR embeddings of different steps in a multi-step reaction are then passed into a transformer-guided reaction path encoder.
Our experiments  show that YieldNet can predict the yield more accurately than the baselines. Furthermore, the model is trained only under the distant supervision of yield values, without requiring fine-grained supervision of atom mapping.

## Metadata
- venue: ICML
- year: 2025
- authors: Ankit Ghosh, Gargee Kashyap, Sarthak Mittal, Nupur Jain, Raghavan B Sunoj, Abir De
- arxiv_id: 
- openreview_id: sqjQ6p56GR
- anthology_id: 
- pdf_url: https://openreview.net/pdf/8ed2edcb4d1c67b609b9a3092caeb9244f289c25.pdf
- published: 2025
- keywords: Yield Prediction, GNN, Atom Mapping

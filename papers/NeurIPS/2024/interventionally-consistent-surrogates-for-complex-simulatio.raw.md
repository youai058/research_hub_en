---
title: "Interventionally Consistent Surrogates for Complex Simulation Models"
authors: ["Joel Dyer", "Nicholas George Bishop", "Yorgos Felekis", "Fabio Massimo Zennaro", "Ani Calinescu", "Theodoros Damoulas", "Michael J. Wooldridge"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "UtTjgMDTFO"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/cdbaac6298725b814263edd7f961c715387b47c9.pdf"
published: "2024"
categories: []
keywords: ["agent-based model", "causal abstraction", "complex simulator", "surrogate model"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:01+09:00"
---

# Interventionally Consistent Surrogates for Complex Simulation Models

## Abstract
Large-scale simulation models of complex socio-technical systems provide decision-makers with high-fidelity testbeds in which policy interventions can be evaluated and _what-if_ scenarios explored. Unfortunately, the high computational cost of such models inhibits their widespread use in policy-making settings. Surrogate models can address these computational limitations, but to do so they must behave consistently with the simulator under interventions of interest. In this paper, we build upon recent developments in causal abstractions to develop a framework for learning interventionally consistent surrogate models for large-scale, complex simulation models. We provide theoretical results showing that our proposed approach induces surrogates to behave consistently with high probability with respect to the simulator across interventions of interest, facilitating rapid experimentation with policy interventions in complex systems. We further demonstrate with empirical studies that conventionally trained surrogates can misjudge the effect of interventions and misguide decision-makers towards suboptimal interventions, while surrogates trained for _interventional_ consistency with our method closely mimic the behaviour of the original simulator under interventions of interest.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Joel Dyer, Nicholas George Bishop, Yorgos Felekis, Fabio Massimo Zennaro, Ani Calinescu, Theodoros Damoulas, Michael J. Wooldridge
- arxiv_id: 
- openreview_id: UtTjgMDTFO
- anthology_id: 
- pdf_url: https://openreview.net/pdf/cdbaac6298725b814263edd7f961c715387b47c9.pdf
- published: 2024
- keywords: agent-based model, causal abstraction, complex simulator, surrogate model

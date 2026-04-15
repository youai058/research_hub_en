---
title: "Principled Gradient-Based MCMC for Conditional Sampling of Text"
authors: ["Li Du", "Afra Amini", "Lucas Torroba Hennigen", "Xinyan Velocity Yu", "Holden Lee", "Jason Eisner", "Ryan Cotterell"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "AwLLSlJAeJ"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/3aabd40646c02f252beccb39b594e5187e925562.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:18+09:00"
---

# Principled Gradient-Based MCMC for Conditional Sampling of Text

## Abstract
We consider the problem of sampling text from an energy-based model. This arises, for example, when sampling text from a neural language model subject to soft constraints. Although the target distribution is discrete, the internal computations of the energy function (given by the language model) are differentiable, so one would like to exploit gradient information within a method such as MCMC. Alas, all previous attempts to generalize gradient-based MCMC to text sampling fail to sample correctly from the target distribution. We propose a solution, along with variants, and study its theoretical properties. Through experiments on various forms of text generation, we demonstrate that our unbiased samplers are able to generate more fluent text while better adhering to the control objectives. The same methods could be used to sample from discrete energy-based models unrelated to text.

## Metadata
- venue: ICML
- year: 2024
- authors: Li Du, Afra Amini, Lucas Torroba Hennigen, Xinyan Velocity Yu, Holden Lee, Jason Eisner, Ryan Cotterell
- arxiv_id: 
- openreview_id: AwLLSlJAeJ
- anthology_id: 
- pdf_url: https://openreview.net/pdf/3aabd40646c02f252beccb39b594e5187e925562.pdf
- published: 2024

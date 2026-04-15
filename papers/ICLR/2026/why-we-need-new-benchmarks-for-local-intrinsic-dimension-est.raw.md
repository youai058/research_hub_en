---
title: "Why We Need New Benchmarks for Local Intrinsic Dimension Estimation"
authors: ["Piotr Tempczyk", "Dominik Filipiak", "Łukasz Garncarek", "Ksawery Smoczyński", "Adam Kurpisz"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ZEf03Uunvk"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/88bbda820d2f79b397171d3dca3bb65cc8637253.pdf"
published: "2026"
categories: []
keywords: ["Local intrinsic dimension estimation", "LIDL", "FLIPD", "Diffusion Models", "Benhamark", "Normalizing Flows", "ESS", "Normal Bundle", "NB", "LID"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:19+09:00"
---

# Why We Need New Benchmarks for Local Intrinsic Dimension Estimation

## Abstract
Neural Local Intrinsic Dimension (LID) estimators are typically bound to domain-specific architectures whose inductive biases can yield inconsistent estimates for the same underlying manifold. Existing evaluations either use overly simple synthetic data (with known LID) or real datasets (with unknown LID), obscuring true performance. We introduce a principled benchmarking framework that (i) maps the same manifold into multiple domain representations while preserving its structure, enabling like-for-like cross-architecture tests; (ii) designs harder variants of popular datasets that target key manifold properties; and (iii) applies controlled transformations with known LID shifts to stress-test methods even when absolute LID is unknown. Across this suite, including non-trivial synthetic datasets, we show that accuracy on simple manifolds does not transfer across domains and that state-of-the-art methods fail under targeted stressors, revealing clear failure modes and areas for improvement. Data and code are available: https://github.com/DominikFilipiak/LID-Benchmarks.

## Metadata
- venue: ICLR
- year: 2026
- authors: Piotr Tempczyk, Dominik Filipiak, Łukasz Garncarek, Ksawery Smoczyński, Adam Kurpisz
- arxiv_id: 
- openreview_id: ZEf03Uunvk
- anthology_id: 
- pdf_url: https://openreview.net/pdf/88bbda820d2f79b397171d3dca3bb65cc8637253.pdf
- published: 2026
- keywords: Local intrinsic dimension estimation, LIDL, FLIPD, Diffusion Models, Benhamark, Normalizing Flows, ESS, Normal Bundle, NB, LID

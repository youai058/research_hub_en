---
title: "Kernel conditional tests from learning-theoretic bounds"
authors: ["Pierre-François Massiani", "Christian Fiedler", "Lukas Haverbeck", "Friedrich Solowjow", "Sebastian Trimpe"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "hJKDwf32Xu"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/6ae0f3a1db8c4fe681990872efc325f93981205b.pdf"
published: "2025"
categories: []
keywords: ["kernel methods", "hypothesis testing", "statistical learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:26+09:00"
---

# Kernel conditional tests from learning-theoretic bounds

## Abstract
We propose a framework for hypothesis testing on conditional probability distributions, which we then use to construct *statistical tests of functionals of conditional distributions*.
These tests identify the inputs where the functionals differ with high probability, and include tests of conditional moments or two-sample tests.
Our key idea is to transform confidence bounds of a learning method into a test of conditional expectations.
We instantiate this principle for kernel ridge regression (KRR) with subgaussian noise.
An intermediate data embedding then enables more general tests — including *conditional two-sample tests* — via kernel mean embeddings of distributions.
To have guarantees in this setting, we generalize existing pointwise-in-time or time-uniform confidence bounds for KRR to previously-inaccessible yet essential cases such as infinite-dimensional outputs with non-trace-class kernels.
These bounds also circumvent the need for independent data, allowing for instance online sampling.
To make our tests readily applicable in practice, we introduce bootstrapping schemes leveraging the parametric form of testing thresholds identified in theory to avoid tuning inaccessible parameters.
We illustrate the tests on examples, including one in process monitoring and comparison of dynamical systems.
Overall, our results establish a comprehensive foundation for conditional testing on functionals, from theoretical guarantees to an algorithmic implementation, and advance the state of the art on confidence bounds for vector-valued least squares estimation.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Pierre-François Massiani, Christian Fiedler, Lukas Haverbeck, Friedrich Solowjow, Sebastian Trimpe
- arxiv_id: 
- openreview_id: hJKDwf32Xu
- anthology_id: 
- pdf_url: https://openreview.net/pdf/6ae0f3a1db8c4fe681990872efc325f93981205b.pdf
- published: 2025
- keywords: kernel methods, hypothesis testing, statistical learning

---
title: "Random Controlled Differential Equations"
authors: ["Francesco Piatti", "Thomas Cass", "William F. Turner"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "kHqt0ZSbKT"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a08f8f90a5ce76215ac189115e5bd5274f7d5d35.pdf"
published: "2026"
categories: []
keywords: ["random features", "time-series", "path signatures", "CDEs", "RDEs", "reservoir computing", "kernels"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:22+09:00"
---

# Random Controlled Differential Equations

## Abstract
We introduce a training-efficient framework for time-series learning that combines random features with controlled differential equations (CDEs). In this approach, large randomly parameterized CDEs act as continuous-time reservoirs, mapping input paths to rich representations. Only a linear readout layer is trained, resulting in fast, scalable models with strong inductive bias. Building on this foundation, we propose two variants: (i) Random Fourier CDEs (RF-CDEs): these lift the input signal using random Fourier features prior to the dynamics, providing a kernel-free approximation of RBF-enhanced sequence models; (ii) Random Rough DEs (R-RDEs): these operate directly on rough-path inputs via a log-ODE discretisation, using log-signatures to capture higher-order temporal interactions while remaining stable and efficient. We prove that in the infinite-width limit, these models induce the RBF-lifted signature kernel and the rough signature kernel, respectively, offering a unified perspective on random-feature reservoirs, continuous-time deep architectures, and path-signature theory.

We evaluate both models across a range of time-series benchmarks, demonstrating competitive or superior performance. These methods provide a practical alternative to explicit signature computations, retaining their inductive bias while benefiting from the efficiency of random features. Code is publicly available at: https://github.com/FrancescoPiatti/RandomSigJax.

## Metadata
- venue: ICLR
- year: 2026
- authors: Francesco Piatti, Thomas Cass, William F. Turner
- arxiv_id: 
- openreview_id: kHqt0ZSbKT
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a08f8f90a5ce76215ac189115e5bd5274f7d5d35.pdf
- published: 2026
- keywords: random features, time-series, path signatures, CDEs, RDEs, reservoir computing, kernels

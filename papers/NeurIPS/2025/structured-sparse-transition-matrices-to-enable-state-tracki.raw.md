---
title: "Structured Sparse Transition Matrices to Enable State Tracking in State-Space Models"
authors: ["Aleksandar Terzic", "Nicolas Menet", "Michael Hersche", "Thomas Hofmann", "Abbas Rahimi"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "RDbuSCWhad"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/0e83e1ab7e0aace90a87b9ec410932a6355e3af2.pdf"
published: "2025"
categories: []
keywords: ["State-Space Models", "Expressiveness", "Efficiency", "Matrix Parametrisation", "State-Tracking", "Finite-State Automata"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:24+09:00"
---

# Structured Sparse Transition Matrices to Enable State Tracking in State-Space Models

## Abstract
Modern state-space models (SSMs) often utilize structured transition matrices
which enable efficient computation but pose restrictions on the model’s expressivity,
as measured in terms of the ability to emulate finite-state automata (FSA). While
unstructured transition matrices are optimal in terms of expressivity, they come
at a prohibitively high compute and memory cost, even for moderate state sizes.
We propose a structured sparse parametrization of transition matrices in SSMs
that enables FSA state tracking with provably optimal state size and depth, while
keeping the computational cost of the recurrence comparable to that of diagonal
SSMs. Our method, \emph{PD-SSM}, parametrizes the transition matrix as the product
of a column one-hot matrix ($P$) and a complex-valued diagonal matrix ($D$). As
a result, the computational cost of parallel scans scales linearly with the state
size. Theoretically, the model is BIBO-stable and can emulate any $N$-state FSA
with one layer of dimension $N$ and a linear readout of size $N ×N$, significantly
improving on all current structured SSM guarantees. Experimentally, the model
significantly outperforms a wide collection of modern SSM variants on various FSA
state tracking tasks. On multivariate time-series classification, it outperforms neural
controlled differential equations, a paradigm explicitly built for time-series analysis.
Finally, we integrate PD-SSM into a hybrid Transformer-SSM architecture and
demonstrate that the model can effectively track the states of a complex FSA in
which transitions are encoded into sets of variable-length English sentences. The
code is available at https://github.com/IBM/expressive-sparse-state-space-model.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Aleksandar Terzic, Nicolas Menet, Michael Hersche, Thomas Hofmann, Abbas Rahimi
- arxiv_id: 
- openreview_id: RDbuSCWhad
- anthology_id: 
- pdf_url: https://openreview.net/pdf/0e83e1ab7e0aace90a87b9ec410932a6355e3af2.pdf
- published: 2025
- keywords: State-Space Models, Expressiveness, Efficiency, Matrix Parametrisation, State-Tracking, Finite-State Automata

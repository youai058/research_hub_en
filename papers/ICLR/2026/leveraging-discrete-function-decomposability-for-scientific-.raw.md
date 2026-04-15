---
title: "Leveraging Discrete Function Decomposability for Scientific Design"
authors: ["James C Bowden", "Sergey Levine", "Jennifer Listgarten"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "lndDn7i8W6"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a9f1ded08b65ca8b872f351633bcebbc3f7de719.pdf"
published: "2026"
categories: []
keywords: ["scientific", "protein", "design", "generative model", "decomposability"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:46+09:00"
---

# Leveraging Discrete Function Decomposability for Scientific Design

## Abstract
In the era of AI-driven science and engineering, we often want to design discrete
objects (e.g., circuits, proteins, materials) in silico according to user-specified
properties (e.g., that a protein binds its target). Given a property predictive model,
in silico design typically involves training a generative model over the design
space (e.g., over the set of all length-L proteins) to concentrate on designs with the
desired properties. Distributional optimization, formalized as an estimation of distribution algorithm or as reinforcement learning policy optimization, maximizes
an objective function in expectation over samples. Optimizing a distribution over
discrete-valued designs is in general challenging due to the combinatorial nature
of the design space. However, many property predictors in scientific applications
are decomposable in the sense that they can be factorized over design variables in a
way that will prove useful. For example, the active site amino acids in a catalytic
protein may need to only loosely interact with the rest of the protein for maximal catalytic activity. Current distributional optimization algorithms are unable to
make use of such structure, which could dramatically improve the optimization.
Herein, we propose and demonstrate use of a new distributional optimization algorithm, Decomposition-Aware Distributional Optimization (DADO),
that can leverage any decomposability defined by a junction tree on the design
variables. At its core, DADO employs a factorized “search distribution”—a
learned generative model—for efficient navigation of the search space, and invokes graph message passing to coordinate optimization across all variables.

## Metadata
- venue: ICLR
- year: 2026
- authors: James C Bowden, Sergey Levine, Jennifer Listgarten
- arxiv_id: 
- openreview_id: lndDn7i8W6
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a9f1ded08b65ca8b872f351633bcebbc3f7de719.pdf
- published: 2026
- keywords: scientific, protein, design, generative model, decomposability

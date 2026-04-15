---
title: "NeuroBack: Improving CDCL SAT Solving using Graph Neural Networks"
authors: ["Wenxi Wang", "Yang Hu", "Mohit Tiwari", "Sarfraz Khurshid", "Kenneth McMillan", "Risto Miikkulainen"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "samyfu6G93"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/68668727b395677105cd2bfd38dc554dc5b67212.pdf"
published: "2024"
categories: []
keywords: ["Propositional satisfiability", "Graph Neural Networks", "CDCL SAT Solving", "Backbone", "Phase Prediction"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:24+09:00"
---

# NeuroBack: Improving CDCL SAT Solving using Graph Neural Networks

## Abstract
Propositional satisfiability (SAT) is an NP-complete problem that impacts many
research fields, such as planning, verification, and security. Mainstream modern
SAT solvers are based on the Conflict-Driven Clause Learning (CDCL) algorithm.
Recent work aimed to enhance CDCL SAT solvers using Graph Neural Networks
(GNNs). However, so far this approach either has not made solving more effective,
or required substantial GPU resources for frequent online model inferences. Aiming
to make GNN improvements practical, this paper proposes an approach called
NeuroBack, which builds on two insights: (1) predicting phases (i.e., values) of
variables appearing in the majority (or even all) of the satisfying assignments are
essential for CDCL SAT solving, and (2) it is sufficient to query the neural model
only once for the predictions before the SAT solving starts. Once trained, the
offline model inference allows NeuroBack to execute exclusively on the CPU,
removing its reliance on GPU resources. To train NeuroBack, a new dataset called
DataBack containing 120,286 data samples is created. Finally, NeuroBack is implemented
as an enhancement to a state-of-the-art SAT solver called Kissat. As a result,
it allowed Kissat to solve 5.2% more problems on the recent SAT competition
problem set, SATCOMP-2022. NeuroBack therefore shows how machine learning
can be harnessed to improve SAT solving in an effective and practical manner.

## Metadata
- venue: ICLR
- year: 2024
- authors: Wenxi Wang, Yang Hu, Mohit Tiwari, Sarfraz Khurshid, Kenneth McMillan, Risto Miikkulainen
- arxiv_id: 
- openreview_id: samyfu6G93
- anthology_id: 
- pdf_url: https://openreview.net/pdf/68668727b395677105cd2bfd38dc554dc5b67212.pdf
- published: 2024
- keywords: Propositional satisfiability, Graph Neural Networks, CDCL SAT Solving, Backbone, Phase Prediction

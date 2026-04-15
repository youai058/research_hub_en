---
title: "The surprising efficiency of temporal difference learning for rare event prediction"
authors: ["Xiaoou Cheng", "Jonathan Weare"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "QEUntqKvmm"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/0d56bb358e3727dbb74159bbeb7f4e5745b00f1f.pdf"
published: "2024"
categories: []
keywords: ["temporal difference learning", "reinforcement learning", "rare events", "policy evaluation", "prediction", "perturbation bounds"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:59+09:00"
---

# The surprising efficiency of temporal difference learning for rare event prediction

## Abstract
We quantify the efficiency of temporal difference (TD) learning over the direct, or Monte Carlo (MC), estimator for policy evaluation in reinforcement learning, with an emphasis on estimation of quantities related to rare events. Policy evaluation is complicated in the rare event setting by the long timescale of the event and by the need for \emph{relative accuracy} in estimates of very small values.  Specifically, we focus on least-squares TD (LSTD) prediction for finite state Markov chains, and show that LSTD can achieve relative accuracy far more efficiently than MC.  We prove a central limit theorem for the LSTD estimator and upper bound the 
  \emph{relative asymptotic variance}
  by simple quantities characterizing the connectivity of states relative to the transition probabilities between them. Using this bound, we show that, even when both the timescale of the rare event and the relative accuracy of the MC estimator are exponentially large in the number of states, LSTD maintains a fixed level of relative accuracy with  a total number of observed transitions of the Markov chain that is only \emph{polynomially} large in the number of states.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Xiaoou Cheng, Jonathan Weare
- arxiv_id: 
- openreview_id: QEUntqKvmm
- anthology_id: 
- pdf_url: https://openreview.net/pdf/0d56bb358e3727dbb74159bbeb7f4e5745b00f1f.pdf
- published: 2024
- keywords: temporal difference learning, reinforcement learning, rare events, policy evaluation, prediction, perturbation bounds

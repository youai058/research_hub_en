---
title: "Mixed Dynamics In Linear Networks: Unifying the Lazy and Active Regimes"
authors: ["Zhenfeng Tu", "Santiago Aranguri", "Arthur Jacot"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "9zQl27mqWE"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/704a6c9c809023554c632572ed54615fa25ac4e4.pdf"
published: "2024"
categories: []
keywords: ["Linear Networks", "Lazy Regime", "Active Regime", "Training Dynamics", "Phase Diagram"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:57+09:00"
---

# Mixed Dynamics In Linear Networks: Unifying the Lazy and Active Regimes

## Abstract
The training dynamics of linear networks are well studied in two distinct
setups: the lazy regime and balanced/active regime, depending on the
initialization and width of the network. We provide a surprisingly
simple unifying formula for the evolution of the learned matrix that
contains as special cases both lazy and balanced regimes but also
a mixed regime in between the two. In the mixed regime, a part of
the network is lazy while the other is balanced. More precisely the
network is lazy along singular values that are below a certain threshold
and balanced along those that are above the same threshold. At initialization,
all singular values are lazy, allowing for the network to align itself
with the task, so that later in time, when some of the singular value
cross the threshold and become active they will converge rapidly (convergence
in the balanced regime is notoriously difficult in the absence of
alignment). The mixed regime is the `best of both worlds': it converges
from any random initialization (in contrast to balanced dynamics which
require special initialization), and has a low rank bias (absent in
the lazy dynamics). This allows us to prove an almost complete phase
diagram of training behavior as a function of the variance at initialization
and the width, for a MSE training task.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Zhenfeng Tu, Santiago Aranguri, Arthur Jacot
- arxiv_id: 
- openreview_id: 9zQl27mqWE
- anthology_id: 
- pdf_url: https://openreview.net/pdf/704a6c9c809023554c632572ed54615fa25ac4e4.pdf
- published: 2024
- keywords: Linear Networks, Lazy Regime, Active Regime, Training Dynamics, Phase Diagram

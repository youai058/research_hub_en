---
title: "Minor First, Major Last: A Depth-Induced Implicit Bias of Sharpness-Aware Minimization"
authors: ["Chaewon Moon", "Dongkuk Si", "Chulhee Yun"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ErnnE2UNI2"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/dbf704dd71f3742b3f3be051228665a721985818.pdf"
published: "2026"
categories: []
keywords: ["sharpness-aware minimization", "implicit bias", "gradient flow"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:27+09:00"
---

# Minor First, Major Last: A Depth-Induced Implicit Bias of Sharpness-Aware Minimization

## Abstract
We study the implicit bias of sharpness-aware minimization (SAM) when training $L$-layer linear diagonal networks on linearly separable binary classification. For linear models ($L=1$), both $\ell_\infty$- and $\ell_2$-SAM recover the $\ell_2$ max-margin classifier, matching gradient descent (GD). However, for depth $L = 2$, the behavior changes drastically—even on a single-example dataset where we can analyze the dynamics. For $\ell_\infty$-SAM, the limit direction depends critically on initialization and can converge to $0$ or to any standard basis vector; this is in stark contrast to GD, whose limit aligns with the basis vector of the dominant coordinate in the data. For $\ell_2$-SAM, we uncover a phenomenon we call *sequential feature amplification*, in which the predictor initially relies on minor coordinates and gradually shifts to larger ones as training proceeds or initialization increases. Our theoretical analysis attributes this phenomenon to $\ell_2$-SAM’s gradient normalization factor applied in its perturbation, which amplifies minor coordinates early and allows major ones to dominate later, giving a concrete example where infinite-time implicit-bias analyses are insufficient. Synthetic and real-data experiments corroborate our findings.

## Metadata
- venue: ICLR
- year: 2026
- authors: Chaewon Moon, Dongkuk Si, Chulhee Yun
- arxiv_id: 
- openreview_id: ErnnE2UNI2
- anthology_id: 
- pdf_url: https://openreview.net/pdf/dbf704dd71f3742b3f3be051228665a721985818.pdf
- published: 2026
- keywords: sharpness-aware minimization, implicit bias, gradient flow

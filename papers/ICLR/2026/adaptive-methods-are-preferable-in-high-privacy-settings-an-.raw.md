---
title: "Adaptive Methods Are Preferable in High Privacy Settings: An SDE Perspective"
authors: ["Enea Monzio Compagnoni", "Alessandro Stanghellini", "Rustem Islamov", "Aurelien Lucchi", "Anastasia Koloskova"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "hSpA4DAoMk"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/8f16d4e60e3785ab5d582bfd185b1b9a95ffbc71.pdf"
published: "2026"
categories: []
keywords: ["Stochastic Differential Equations", "Differential Privacy"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:24+09:00"
---

# Adaptive Methods Are Preferable in High Privacy Settings: An SDE Perspective

## Abstract
Differential Privacy (DP) is becoming central to large-scale training as privacy regulations tighten. We revisit how DP noise interacts with _adaptivity_ in optimization through the lens of _stochastic differential equations_, providing the first SDE-based analysis of private optimizers. Focusing on *DP-SGD* and *DP-SignSGD* under per-example clipping, we show a sharp contrast under fixed hyperparameters: *DP-SGD* converges at a Privacy-Utility Trade-Off of $\mathcal{O}(1/\varepsilon^2)$ with speed independent of $\varepsilon$, while *DP-SignSGD* converges at a speed *linear* in $\varepsilon$ with a $\mathcal{O}(1/\varepsilon)$ trade-off, dominating in high-privacy or large batch noise regimes. By contrast, under optimal learning rates, both methods achieve comparable theoretical asymptotic performance; however, the optimal learning rate of *DP-SGD* scales linearly with $\varepsilon$, while that of *DP-SignSGD* is essentially $\varepsilon$-independent. This makes adaptive methods far more practical, as their hyperparameters transfer across privacy levels with little or no re-tuning. Empirical results confirm our theory across training and test metrics, and empirically extend from *DP-SignSGD* to *DP-Adam*.

## Metadata
- venue: ICLR
- year: 2026
- authors: Enea Monzio Compagnoni, Alessandro Stanghellini, Rustem Islamov, Aurelien Lucchi, Anastasia Koloskova
- arxiv_id: 
- openreview_id: hSpA4DAoMk
- anthology_id: 
- pdf_url: https://openreview.net/pdf/8f16d4e60e3785ab5d582bfd185b1b9a95ffbc71.pdf
- published: 2026
- keywords: Stochastic Differential Equations, Differential Privacy

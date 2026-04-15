---
title: "Detection of unknown unknowns in autonomous systems"
authors: ["Ayan Banerjee", "Sandeep Gupta"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "GrsofC2FqF"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/dd813d685b41d914ce5c0f116f206714af99836b.pdf"
published: "2026"
categories: []
keywords: ["unknown unknowns", "autonomous systems", "conformal bounds"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:25+09:00"
---

# Detection of unknown unknowns in autonomous systems

## Abstract
Unknown unknowns (U2s) are deployment-time scenarios absent from development/testing. Unlike conventional anomalies, U2s are not out-of-distribution (OOD); they stem from changes in underlying system dynamics without a distribution shift from normal data. Thus, existing multi-variate time series anomaly detection (MTAD) methods—which rely on distribution-shift cues—are ill-suited for U2 detection. Specifically: (i) we show most anomaly datasets exhibit distribution shift between normal and anomalous data and therefore are not representative of U2s; (ii) we introduce eight U2 benchmarks where training data contain OOD anomalies but no U2s, while test sets contain both OOD anomalies and U2s; (iii) we demonstrate that state-of-the-art (SOTA) MTAD results often depend on impractical enhancements: point adjustment (PA) (uses ground truth to flip false negatives to true positives, inflating precision) and threshold learning with data leakage (TL) (tuning thresholds on test data and labels); (iv) with PA+TL, even untrained deterministic methods can match or surpass MTAD baselines; (v) without PA/TL, existing MTAD methods degrade sharply on U2 benchmarks. Finally, we present sparse model identification–enhanced anomaly detection (SPIE-AD), a model-recovery-and-conformance, zero-shot MTAD approach that outperforms baselines on all eight U2 benchmarks and on six additional real-world MTAD datasets—without PA or TL. Code and data available in https://github.com/ImpactLabASU/U2Recognition.

## Metadata
- venue: ICLR
- year: 2026
- authors: Ayan Banerjee, Sandeep Gupta
- arxiv_id: 
- openreview_id: GrsofC2FqF
- anthology_id: 
- pdf_url: https://openreview.net/pdf/dd813d685b41d914ce5c0f116f206714af99836b.pdf
- published: 2026
- keywords: unknown unknowns, autonomous systems, conformal bounds

---
title: "Time Series Representations with Hard-Coded Invariances"
authors: ["Thibaut Germain", "Chrysoula Kosma", "Laurent Oudre"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "SaKPKyjDp6"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/59898546845d19b0c9d865bcae0fb49388f668da.pdf"
published: "2025"
categories: []
keywords: ["Time Series", "Invariances", "Neural Networks", "Convolutions"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:10+09:00"
---

# Time Series Representations with Hard-Coded Invariances

## Abstract
Automatically extracting robust representations from large and complex time series data is becoming imperative for several real-world applications. Unfortunately, the potential of common neural network architectures in capturing invariant properties of time series remains relatively underexplored. For instance, convolutional layers often fail to capture underlying patterns in time series inputs that encompass strong deformations, such as trends. Indeed, invariances to some deformations may be critical for solving complex time series tasks, such as classification, while guaranteeing good generalization performance.
To address these challenges, we mathematically formulate and technically design efficient and hard-coded *invariant convolutions* for specific group actions applicable to the case of time series.
We construct these convolutions by considering specific sets of deformations commonly observed in time series, including *scaling*, *offset shift*, and *trend*.
We further combine the proposed invariant convolutions with standard convolutions in single embedding layers, and we showcase the layer capacity to capture complex invariant time series properties in several scenarios.

## Metadata
- venue: ICML
- year: 2025
- authors: Thibaut Germain, Chrysoula Kosma, Laurent Oudre
- arxiv_id: 
- openreview_id: SaKPKyjDp6
- anthology_id: 
- pdf_url: https://openreview.net/pdf/59898546845d19b0c9d865bcae0fb49388f668da.pdf
- published: 2025
- keywords: Time Series, Invariances, Neural Networks, Convolutions

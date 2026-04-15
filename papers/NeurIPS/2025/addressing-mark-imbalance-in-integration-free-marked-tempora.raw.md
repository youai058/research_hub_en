---
title: "Addressing Mark Imbalance in Integration-free Marked Temporal Point Processes"
authors: ["Sishun Liu", "KE DENG", "Yongli Ren", "Yan Wang", "Xiuzhen Zhang"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "lUtNvMiW3C"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c78e691c878be96fc2d5f19bc35e7ebdc4b61099.pdf"
published: "2025"
categories: []
keywords: ["Marked Temporal Point Process", "Data Imbalance"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:52+09:00"
---

# Addressing Mark Imbalance in Integration-free Marked Temporal Point Processes

## Abstract
Marked Temporal Point Process (MTPP) has been well studied to model the event distribution in marked event streams, which can be used to predict the mark and arrival time of the next event. However, existing studies overlook that the distribution of event marks is highly imbalanced in many real-world applications, with some marks being frequent but others rare. The imbalance poses a significant challenge to the performance of the next event prediction, especially for events of rare marks. To address this issue, we propose a thresholding method, which learns thresholds to tune the mark probability normalized by the mark's prior probability to optimize mark prediction, rather than predicting the mark directly based on the mark probability as in existing studies. In conjunction with this method, we predict the mark first and then the time.  In particular, we develop a novel neural Marked Temporal Point Process (MTPP) model to support effective time sampling and estimation of mark probability without computationally expensive numerical improper integration. Extensive experiments on real-world datasets demonstrate the superior performance of our solution against various baselines for the next event mark and time prediction. The code is available at https://github.com/undes1red/IFNMTPP.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Sishun Liu, KE DENG, Yongli Ren, Yan Wang, Xiuzhen Zhang
- arxiv_id: 
- openreview_id: lUtNvMiW3C
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c78e691c878be96fc2d5f19bc35e7ebdc4b61099.pdf
- published: 2025
- keywords: Marked Temporal Point Process, Data Imbalance

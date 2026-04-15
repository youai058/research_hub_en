---
title: "Epistemic Uncertainty Quantification To Improve Decisions From Black-Box Models"
authors: ["Sébastien Melo", "Gaël Varoquaux", "Marine Le Morvan"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "JfiwaTxhI8"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9bc12196f1c2c872bd17bcbcd56c1de17eb8c345.pdf"
published: "2026"
categories: []
keywords: ["Epistemic uncertainty", "Excess risk", "Uncertainty quantification", "Aleatoric", "LLM", "Deferral", "Calibration"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:34+09:00"
---

# Epistemic Uncertainty Quantification To Improve Decisions From Black-Box Models

## Abstract
Distinguishing epistemic uncertainty (model ignorance) from aleatoric uncertainty (task randomness) is critical for reliable AI systems, yet standard confidence evaluation metrics capture different and incomplete aspects of uncertainty. While AUC and accuracy measure predictive signal, proper scoring rules assess overall uncertainty, and calibration metrics isolate part of the epistemic uncertainty but ignore within-bin heterogeneity of errors, known as grouping loss. We bridge this evaluation gap by introducing asymptotically consistent and sample-efficient estimators of the grouping loss and excess decision risk, providing a fine-grained assessment of epistemic uncertainty that complements existing calibration metrics. Applied to LLM question-answering with inherent aleatoric noise, our estimators reveal substantial grouping loss which decreases with model scale and instruction tuning. Their local nature enables automatic identification of subgroups with systematic over- or under-confidence, supporting interpretable confidence audits. Finally, we leverage these estimates to design LLM cascades that defer high excess decision risk predictions to stronger models, achieving higher accuracy at lower cost than competing approaches.

## Metadata
- venue: ICLR
- year: 2026
- authors: Sébastien Melo, Gaël Varoquaux, Marine Le Morvan
- arxiv_id: 
- openreview_id: JfiwaTxhI8
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9bc12196f1c2c872bd17bcbcd56c1de17eb8c345.pdf
- published: 2026
- keywords: Epistemic uncertainty, Excess risk, Uncertainty quantification, Aleatoric, LLM, Deferral, Calibration

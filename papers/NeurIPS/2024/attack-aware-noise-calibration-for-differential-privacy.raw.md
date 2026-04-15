---
title: "Attack-Aware Noise Calibration for Differential Privacy"
authors: ["Bogdan Kulynych", "Juan Felipe Gomez", "Georgios Kaissis", "Flavio Calmon", "Carmela Troncoso"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "hOcsUrOY0D"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2ff39869c612a7bbef84ddca4b9e48a96163a680.pdf"
published: "2024"
categories: []
keywords: ["differential privacy", "DP-SGD"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:41+09:00"
---

# Attack-Aware Noise Calibration for Differential Privacy

## Abstract
Differential privacy (DP) is a widely used approach for mitigating privacy risks when training machine learning models on sensitive data. DP mechanisms add noise during training to limit the risk of information leakage. The scale of the added noise is critical, as it determines the trade-off between privacy and utility. The standard practice is to select the noise scale to satisfy a given privacy budget ε. This privacy budget is in turn interpreted in terms of operational attack risks, such as accuracy, sensitivity, and specificity of inference attacks aimed to recover
information about the training data records. We show that first calibrating the noise scale to a privacy budget ε, and then translating ε to attack risk leads to overly conservative risk assessments and unnecessarily low utility. Instead, we propose methods to directly calibrate the noise scale to a desired attack risk level, bypassing the step of choosing ε. For a given notion of attack risk, our approach significantly
decreases noise scale, leading to increased utility at the same level of privacy. We empirically demonstrate that calibrating noise to attack sensitivity/specificity, rather than ε, when training privacy-preserving ML models substantially improves model accuracy for the same risk level. Our work provides a principled and practical way to improve the utility of privacy-preserving ML without compromising on privacy.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Bogdan Kulynych, Juan Felipe Gomez, Georgios Kaissis, Flavio Calmon, Carmela Troncoso
- arxiv_id: 
- openreview_id: hOcsUrOY0D
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2ff39869c612a7bbef84ddca4b9e48a96163a680.pdf
- published: 2024
- keywords: differential privacy, DP-SGD

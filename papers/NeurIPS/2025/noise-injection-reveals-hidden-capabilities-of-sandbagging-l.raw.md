---
title: "Noise Injection Reveals Hidden Capabilities of Sandbagging Language Models"
authors: ["Cameron Tice", "Philipp Alexander Kreer", "Nathan Helm-Burger", "Prithviraj Singh Shahani", "Fedor Ryzhenkov", "Fabien Roger", "Clement Neo", "Jacob Haimes", "Felix Hofstätter", "Teun van der Weij"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "uUWb5eawL9"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/270d56d8f07a02f9a239ad5968c7f14775a15f28.pdf"
published: "2025"
categories: []
keywords: ["Large Language Models", "Sandbagging", "Noise Injection", "Deception Detection"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:58+09:00"
---

# Noise Injection Reveals Hidden Capabilities of Sandbagging Language Models

## Abstract
Capability evaluations play a crucial role in assessing and regulating frontier AI systems. The effectiveness of these evaluations faces a significant challenge: strategic underperformance, or ``sandbagging'', where models deliberately underperform during evaluation. 
Sandbagging can manifest either through explicit developer intervention or through unintended model behavior, presenting a fundamental obstacle to accurate capability assessment. We introduce a novel sandbagging detection method based on injecting noise of varying magnitudes into model weights. While non-sandbagging models show predictable performance degradation with increasing noise, we demonstrate that sandbagging models exhibit anomalous performance improvements, likely due to disruption of underperformance mechanisms while core capabilities remain partially intact. Through experiments across various model architectures, sizes, and sandbagging techniques, we establish this distinctive response pattern as a reliable, model-agnostic signal for detecting sandbagging behavior. Importantly, we find noise-injection is capable of eliciting the full performance of Mistral Large 120B in a setting where the model underperforms without being instructed to do so. Our findings provide a practical tool for AI evaluation and oversight, addressing a challenge in ensuring accurate capability assessment of frontier AI systems.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Cameron Tice, Philipp Alexander Kreer, Nathan Helm-Burger, Prithviraj Singh Shahani, Fedor Ryzhenkov, Fabien Roger, Clement Neo, Jacob Haimes, Felix Hofstätter, Teun van der Weij
- arxiv_id: 
- openreview_id: uUWb5eawL9
- anthology_id: 
- pdf_url: https://openreview.net/pdf/270d56d8f07a02f9a239ad5968c7f14775a15f28.pdf
- published: 2025
- keywords: Large Language Models, Sandbagging, Noise Injection, Deception Detection

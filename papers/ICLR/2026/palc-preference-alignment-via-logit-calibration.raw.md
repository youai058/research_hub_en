---
title: "PALC: Preference Alignment via Logit Calibration"
authors: ["SANGHYUN LEE", "Hoh Peter In"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "0cmuYj3WeG"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/8506eb5974fdf10333050a3fc631349b99106876.pdf"
published: "2026"
categories: []
keywords: ["AI alignment", "Representation Editing"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:48+09:00"
---

# PALC: Preference Alignment via Logit Calibration

## Abstract
Aligning Large Language Models with human preferences typically requires computationally intensive training or complex reward architectures. We introduce PALC (Preference Alignment via Logit Calibration), a parameter-efficient framework that achieves test-time alignment through a novel intervention strategy: direct calibration in vocabulary space. Unlike existing methods that manipulate entangled hidden representations or rely on external reward models, PALC operates at the logit layer where each dimension corresponds to a distinct token, providing interpretable and efficient control. Our approach employs a bottleneck architecture that learns to compress the base model's hidden states and generate position-dependent calibration vectors, requiring only a fraction of the base model's parameters. Through this design, PALC sidesteps the superposition problem inherent in representation engineering while eliminating the computational overhead of guided decoding methods. A single scaling factor enables runtime adjustment of alignment strength without retraining, allowing practitioners to balance between preserving model capabilities and enforcing preferences. Experiments demonstrate that PALC outperforms most test-time alignment methods while maintaining near-baseline inference speed. Our ablations reveal that human preferences concentrate on surprisingly low-dimensional manifolds, validating our architectural choices. By establishing vocabulary-space intervention as an effective alignment paradigm, PALC makes preference alignment accessible for resource-constrained deployments where traditional methods are infeasible, opening new avenues for scalable and adaptive AI alignment.

## Metadata
- venue: ICLR
- year: 2026
- authors: SANGHYUN LEE, Hoh Peter In
- arxiv_id: 
- openreview_id: 0cmuYj3WeG
- anthology_id: 
- pdf_url: https://openreview.net/pdf/8506eb5974fdf10333050a3fc631349b99106876.pdf
- published: 2026
- keywords: AI alignment, Representation Editing

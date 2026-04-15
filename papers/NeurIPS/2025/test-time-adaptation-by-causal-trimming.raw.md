---
title: "Test-Time Adaptation by Causal Trimming"
authors: ["Yingnan Liu", "Rui Qiao", "Mong-Li Lee", "Wynne Hsu"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "zFGdHL9pcD"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/bd21a97bfe2d6a07915addfa7b8df32661f0fca1.pdf"
published: "2025"
categories: []
keywords: ["test-time adaptation; distribution shift; causality; representation;"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:54+09:00"
---

# Test-Time Adaptation by Causal Trimming

## Abstract
Test-time adaptation aims to improve model robustness under distribution shifts by adapting models with access to unlabeled target samples. A primary cause of performance degradation under such shifts is the model’s reliance on features that lack a direct causal relationship with the prediction target. We introduce Test-time Adaptation by Causal Trimming (TACT), a method that identifies and removes non-causal components from representations for test distributions. TACT applies data augmentations that preserve causal features while varying non-causal ones. By analyzing the changes in the representations using Principal Component Analysis, TACT identifies the highest variance directions associated with non-causal features. It trims the representations by removing their projections on the identified directions, and uses the trimmed representations for the predictions. During adaptation, TACT continuously tracks and refines these directions to get a better estimate of non-causal features. We theoretically analyze the effectiveness of this approach and empirically validate TACT on real-world out-of-distribution benchmarks. TACT consistently outperforms state-of-the-art methods by a significant margin.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Yingnan Liu, Rui Qiao, Mong-Li Lee, Wynne Hsu
- arxiv_id: 
- openreview_id: zFGdHL9pcD
- anthology_id: 
- pdf_url: https://openreview.net/pdf/bd21a97bfe2d6a07915addfa7b8df32661f0fca1.pdf
- published: 2025
- keywords: test-time adaptation; distribution shift; causality; representation;

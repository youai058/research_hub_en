---
title: "Test-time Adaptation against Multi-modal Reliability Bias"
authors: ["Mouxing Yang", "Yunfan Li", "Changqing Zhang", "Peng Hu", "Xi Peng"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "TPZRq4FALB"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b4995bcc3ee4d649705147591c205b904f4a9d13.pdf"
published: "2024"
categories: []
keywords: ["Test-time adaption", "Imbalanced multi-modal learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:49+09:00"
---

# Test-time Adaptation against Multi-modal Reliability Bias

## Abstract
Test-time adaptation (TTA) has emerged as a new paradigm for reconciling distribution shifts across domains without accessing source data. However, existing TTA methods mainly concentrate on uni-modal tasks, overlooking the complexity of multi-modal scenarios.
In this paper, we delve into the multi-modal test-time adaptation and reveal a new challenge named reliability bias. Different from the definition of traditional distribution shifts, reliability bias refers to the information discrepancies across different modalities derived from intra-modal distribution shifts. To solve the challenge, we propose a novel method, dubbed REliable fusion and robust ADaptation (READ). On the one hand, unlike the existing TTA paradigm that mainly repurposes the normalization layers, READ employs a new paradigm that modulates the attention between modalities in a self-adaptive way, supporting reliable fusion against reliability bias. On the other hand, READ adopts a novel objective function for robust multi-modal adaptation, where the contributions of confident predictions could be amplified and the negative impacts of noisy predictions could be mitigated. Moreover, we introduce two new benchmarks to facilitate comprehensive evaluations of multi-modal TTA under reliability bias. Extensive experiments on the benchmarks verify the effectiveness of our method against multi-modal reliability bias. The code and benchmarks are available at https://github.com/XLearning-SCU/2024-ICLR-READ.

## Metadata
- venue: ICLR
- year: 2024
- authors: Mouxing Yang, Yunfan Li, Changqing Zhang, Peng Hu, Xi Peng
- arxiv_id: 
- openreview_id: TPZRq4FALB
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b4995bcc3ee4d649705147591c205b904f4a9d13.pdf
- published: 2024
- keywords: Test-time adaption, Imbalanced multi-modal learning

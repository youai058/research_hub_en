---
title: "Purifying Quantization-conditioned Backdoors via Layer-wise Activation Correction with Distribution Approximation"
authors: ["Boheng Li", "Yishuo Cai", "Jisong Cai", "Yiming Li", "Han Qiu", "Run Wang", "Tianwei Zhang"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "CEfr3h68KU"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/914e8b54bd87e1d3696604182af3212a858260a8.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:45+09:00"
---

# Purifying Quantization-conditioned Backdoors via Layer-wise Activation Correction with Distribution Approximation

## Abstract
Model quantization is a compression technique that converts a full-precision model to a more compact low-precision version for better storage. Despite the great success of quantization, recent studies revealed the feasibility of malicious exploiting model quantization via implanting quantization-conditioned backdoors (QCBs). These special backdoors remain dormant in full-precision models but are exposed upon quantization. Unfortunately, existing defenses have limited effects on mitigating QCBs. In this paper, we conduct an in-depth analysis of QCBs. We reveal an intriguing characteristic of QCBs, where activation of backdoor-related neurons on even benign samples enjoy a distribution drift after quantization, although this drift is more significant on poisoned samples. Motivated by this finding, we propose to purify the backdoor-exposed quantized model by aligning its layer-wise activation with its full-precision version. To further exploit the more pronounced activation drifts on poisoned samples, we design an additional module to layer-wisely approximate poisoned activation distribution based on batch normalization statistics of the full-precision model. Extensive experiments are conducted, verifying the effectiveness of our defense. Our code is publicly available.

## Metadata
- venue: ICML
- year: 2024
- authors: Boheng Li, Yishuo Cai, Jisong Cai, Yiming Li, Han Qiu, Run Wang, Tianwei Zhang
- arxiv_id: 
- openreview_id: CEfr3h68KU
- anthology_id: 
- pdf_url: https://openreview.net/pdf/914e8b54bd87e1d3696604182af3212a858260a8.pdf
- published: 2024

---
title: "ErrorTrace: A Black-Box Traceability Mechanism Based on Model Family Error Space"
authors: ["Chuanchao Zang", "Xiangtao Meng", "Wenyu Chen", "Tianshuo Cong", "Zha Yaxing", "Dong Qi", "Zheng Li", "Shanqing Guo"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "3P3PL7aCXM"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d7ee6b9c50f47b267806e2463cc1c6fc31a5ac46.pdf"
published: "2025"
categories: []
keywords: ["LLM Intellectual Property Protection", "LLM", "LLM Safety", "Error Space"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:58+09:00"
---

# ErrorTrace: A Black-Box Traceability Mechanism Based on Model Family Error Space

## Abstract
The open-source release of large language models (LLMs) enables malicious users to create unauthorized derivative models at low cost, posing significant threats to intellectual property (IP) and market stability. Existing IP protection methods either require access to model parameters or are vulnerable to fine-tuning attacks. To fill this gap, we propose ErrorTrace, a robust and black-box traceability mechanism for protecting LLM IP. Specifically, ErrorTrace leverages the unique error patterns of model families by mapping and analyzing their distinct error spaces, enabling robust and efficient IP protection without relying on internal parameters or specific query responses. 
Experimental results show that ErrorTrace achieves a traceability accuracy of 0.8518 for 27 base models when the suspect model is not included in ErrorTrace's training set, outperforming the baseline by 0.2593. Additionally,ErrorTrace successfully tracks 34 fine-tuned, pruned and merged models across various scenarios, demonstrating its broad applicability and robustness. In addition, ErrorTrace shows a certain level of resilience when subjected to adversarial attacks. Our code is available at: https://github.com/csdatazcc/ErrorTrace.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Chuanchao Zang, Xiangtao Meng, Wenyu Chen, Tianshuo Cong, Zha Yaxing, Dong Qi, Zheng Li, Shanqing Guo
- arxiv_id: 
- openreview_id: 3P3PL7aCXM
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d7ee6b9c50f47b267806e2463cc1c6fc31a5ac46.pdf
- published: 2025
- keywords: LLM Intellectual Property Protection, LLM, LLM Safety, Error Space

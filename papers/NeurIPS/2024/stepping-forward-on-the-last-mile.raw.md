---
title: "Stepping Forward on the Last Mile"
authors: ["Chen Feng", "Shaojie Zhuo", "Xiaopeng Zhang", "Ramchalam Kinattinkara Ramakrishnan", "Zhaocong Yuan", "Andrew Zou Li"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "yCh1z6Dcto"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/6c685c934218042e4f6892abccb9b4a82a86be97.pdf"
published: "2024"
categories: []
keywords: ["On-device model adaptation", "Fixed-point forward gradient learning", "Low memory", "Edge devices"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:31+09:00"
---

# Stepping Forward on the Last Mile

## Abstract
Continuously adapting pre-trained models to local data on resource constrained edge devices is the \emph{last mile} for model deployment. However, as models increase in size and depth, backpropagation requires a large amount of memory, which becomes prohibitive for edge devices. In addition, most existing low power neural processing engines (e.g., NPUs, DSPs, MCUs, etc.) are designed as fixed-point inference accelerators, without training capabilities. Forward gradients, solely based on directional derivatives computed from two forward calls, have been recently used for model training, with substantial savings in computation and memory. However, the performance of quantized training with fixed-point forward gradients remains unclear. In this paper, we investigate the feasibility of on-device training using fixed-point forward gradients, by conducting comprehensive experiments across a variety of deep learning benchmark tasks in both vision and audio domains. We propose a series of algorithm enhancements that further reduce the memory footprint, and the accuracy gap compared to backpropagation. An empirical study on how training with forward gradients navigates in the loss landscape is further explored. Our results demonstrate that on the last mile of model customization on edge devices, training with fixed-point forward gradients is a feasible and practical approach.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Chen Feng, Shaojie Zhuo, Xiaopeng Zhang, Ramchalam Kinattinkara Ramakrishnan, Zhaocong Yuan, Andrew Zou Li
- arxiv_id: 
- openreview_id: yCh1z6Dcto
- anthology_id: 
- pdf_url: https://openreview.net/pdf/6c685c934218042e4f6892abccb9b4a82a86be97.pdf
- published: 2024
- keywords: On-device model adaptation, Fixed-point forward gradient learning, Low memory, Edge devices

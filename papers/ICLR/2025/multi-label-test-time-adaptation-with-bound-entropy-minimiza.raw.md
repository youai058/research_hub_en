---
title: "Multi-Label Test-Time Adaptation with Bound Entropy Minimization"
authors: ["Xiangyu Wu", "Feng Yu", "Yang Yang", "Qing-Guo Chen", "Jianfeng Lu"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "75PhjtbBdr"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2bff6d5745da5c1b694abcf3275a5de715dcd964.pdf"
published: "2025"
categories: []
keywords: ["Vision-Language Models", "Zero-Shot Multi-Label Generalization", "Test-Time Adaptation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:40+09:00"
---

# Multi-Label Test-Time Adaptation with Bound Entropy Minimization

## Abstract
Mainstream test-time adaptation (TTA) techniques endeavor to mitigate distribution shifts via entropy minimization for multi-class classification, inherently increasing the probability of the most confident class. However, when encountering multi-label instances, the primary challenge stems from the varying number of labels per image, and prioritizing only the highest probability class inevitably undermines the adaptation of other positive labels. To address this issue, we investigate TTA within multi-label scenario (ML--TTA), developing Bound Entropy Minimization (BEM) objective to simultaneously increase the confidence of multiple top predicted labels. Specifically, to determine the number of labels for each augmented view, we retrieve a paired caption with yielded textual labels for that view. These labels are allocated to both the view and caption, called weak label set and strong label set with the same size k. Following this, the proposed BEM considers the highest top-k predicted labels from view and caption as a single entity, respectively, learning both view and caption prompts concurrently. By binding top-k predicted labels, BEM overcomes the limitation of vanilla entropy minimization, which exclusively optimizes the most confident class. Across the MSCOCO, VOC, and NUSWIDE multi-label datasets, our ML--TTA framework equipped with BEM exhibits superior performance compared to the latest SOTA methods, across various model architectures, prompt initialization, and varying label scenarios. The code is available at https://github.com/Jinx630/ML-TTA.

## Metadata
- venue: ICLR
- year: 2025
- authors: Xiangyu Wu, Feng Yu, Yang Yang, Qing-Guo Chen, Jianfeng Lu
- arxiv_id: 
- openreview_id: 75PhjtbBdr
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2bff6d5745da5c1b694abcf3275a5de715dcd964.pdf
- published: 2025
- keywords: Vision-Language Models, Zero-Shot Multi-Label Generalization, Test-Time Adaptation

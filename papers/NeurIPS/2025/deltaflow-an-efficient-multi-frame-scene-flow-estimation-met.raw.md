---
title: "DeltaFlow: An Efficient Multi-frame Scene Flow Estimation Method"
authors: ["Qingwen Zhang", "Xiaomeng Zhu", "Yushan Zhang", "Yixi Cai", "Olov Andersson", "Patric Jensfelt"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "T9qNDtvAJX"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/058d68c6055660f7a33942f5d8e662e65a5d68ac.pdf"
published: "2025"
categories: []
keywords: ["Scene flow estimation", "Point clouds", "Efficient and scalable vision"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:43+09:00"
---

# DeltaFlow: An Efficient Multi-frame Scene Flow Estimation Method

## Abstract
Previous dominant methods for scene flow estimation focus mainly on input from two consecutive frames, neglecting valuable information in the temporal domain. While recent trends shift towards multi-frame reasoning, they suffer from rapidly escalating computational costs as the number of frames grows. To leverage temporal information more efficiently, we propose DeltaFlow ($\Delta$Flow), a lightweight 3D framework that captures motion cues via a $\Delta$ scheme, extracting temporal features with minimal computational cost, regardless of the number of frames. Additionally, scene flow estimation faces challenges such as imbalanced object class distributions and motion inconsistency. To tackle these issues, we introduce a Category-Balanced Loss to enhance learning across underrepresented classes and an Instance Consistency Loss to enforce coherent object motion, improving flow accuracy. Extensive evaluations on the Argoverse 2, Waymo and nuScenes datasets show that $\Delta$Flow achieves state-of-the-art performance with up to 22\% lower error and $2\times$ faster inference compared to the next-best multi-frame supervised method, while also demonstrating a strong cross-domain generalization ability. The code is open-sourced at https://github.com/Kin-Zhang/DeltaFlow along with trained model weights.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Qingwen Zhang, Xiaomeng Zhu, Yushan Zhang, Yixi Cai, Olov Andersson, Patric Jensfelt
- arxiv_id: 
- openreview_id: T9qNDtvAJX
- anthology_id: 
- pdf_url: https://openreview.net/pdf/058d68c6055660f7a33942f5d8e662e65a5d68ac.pdf
- published: 2025
- keywords: Scene flow estimation, Point clouds, Efficient and scalable vision

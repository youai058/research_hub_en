---
title: "Lightweight Spatio-Temporal Modeling via Temporally Shifted Distillation for Real-Time Accident Anticipation"
authors: ["Patrik Patera", "Yie-Tarng Chen", "Wen-Hsien Fang"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "8zzfTSVds2"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/60b6ec5612eed21036f4a85abbf3f76816a5df3c.pdf"
published: "2026"
categories: []
keywords: ["lightweight spatio-temporal modeling", "model distillation", "accident anticipation", "edge deployment"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:47+09:00"
---

# Lightweight Spatio-Temporal Modeling via Temporally Shifted Distillation for Real-Time Accident Anticipation

## Abstract
Anticipating traffic accidents in real time is critical for intelligent transportation systems, yet remains challenging under edge-device constraints. We propose a lightweight spatio-temporal framework that introduces a temporally shifted distillation strategy, enabling a student model to acquire predictive temporal dynamics from a frozen image-based teacher without requiring a video pre-trained teacher. The student combines a RepMixer spatial encoding with a RWKV-inspired recurrent module for efficient long-range temporal reasoning. To enhance robustness under partial observability, we design a masking memory strategy that leverages memory retention to reconstruct missing visual tokens, effectively simulating occlusions and future events. In addition, multi-modal vision-language supervision enriches semantic grounding. Our framework achieves state-of-the-art performance on multiple real-world dashcam benchmarks while sustaining real-time inference on resource-limited platforms such as the NVIDIA Jetson Orin Nano. Remarkably, it is 3-7$\times$ smaller than leading approaches yet delivers superior accuracy and earlier anticipation, underscoring its practicality for deployment in intelligent vehicles.

## Metadata
- venue: ICLR
- year: 2026
- authors: Patrik Patera, Yie-Tarng Chen, Wen-Hsien Fang
- arxiv_id: 
- openreview_id: 8zzfTSVds2
- anthology_id: 
- pdf_url: https://openreview.net/pdf/60b6ec5612eed21036f4a85abbf3f76816a5df3c.pdf
- published: 2026
- keywords: lightweight spatio-temporal modeling, model distillation, accident anticipation, edge deployment

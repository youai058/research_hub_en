---
title: "AnomalyCLIP: Object-agnostic Prompt Learning for Zero-shot Anomaly Detection"
authors: ["Qihang Zhou", "Guansong Pang", "Yu Tian", "Shibo He", "Jiming Chen"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "buC4E91xZE"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c8c456c139a7b7f9cbf659ae062d7e3f9cba1aff.pdf"
published: "2024"
categories: []
keywords: ["Anomaly detection", "Zero-shot anomaly detection", "CLIP", "Industrial defect inspection"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:52+09:00"
---

# AnomalyCLIP: Object-agnostic Prompt Learning for Zero-shot Anomaly Detection

## Abstract
Zero-shot anomaly detection (ZSAD) requires detection models trained using auxiliary
data to detect anomalies without any training sample in a target dataset. It
is a crucial task when training data is not accessible due to various concerns, e.g.,
data privacy, yet it is challenging since the models need to generalize to anomalies
across different domains where the appearance of foreground objects, abnormal
regions, and background features, such as defects/tumors on different products/
organs, can vary significantly. Recently large pre-trained vision-language
models (VLMs), such as CLIP, have demonstrated strong zero-shot recognition
ability in various vision tasks, including anomaly detection. However, their ZSAD
performance is weak since the VLMs focus more on modeling the class semantics
of the foreground objects rather than the abnormality/normality in the images. In
this paper we introduce a novel approach, namely AnomalyCLIP, to adapt CLIP
for accurate ZSAD across different domains. The key insight of AnomalyCLIP
is to learn object-agnostic text prompts that capture generic normality and abnormality
in an image regardless of its foreground objects. This allows our model to
focus on the abnormal image regions rather than the object semantics, enabling
generalized normality and abnormality recognition on diverse types of objects.
Large-scale experiments on 17 real-world anomaly detection datasets show that
AnomalyCLIP achieves superior zero-shot performance of detecting and segmenting
anomalies in datasets of highly diverse class semantics from various defect
inspection and medical imaging domains. Code will be made available at https://github.com/zqhang/AnomalyCLIP.

## Metadata
- venue: ICLR
- year: 2024
- authors: Qihang Zhou, Guansong Pang, Yu Tian, Shibo He, Jiming Chen
- arxiv_id: 
- openreview_id: buC4E91xZE
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c8c456c139a7b7f9cbf659ae062d7e3f9cba1aff.pdf
- published: 2024
- keywords: Anomaly detection, Zero-shot anomaly detection, CLIP, Industrial defect inspection

---
title: "REVE: A Foundation Model for EEG - Adapting to Any Setup with Large-Scale Pretraining on 25,000 Subjects"
authors: ["Yassine El Ouahidi", "Jonathan Lys", "Philipp Thölke", "Nicolas Farrugia", "Bastien Pasdeloup", "Vincent Gripon", "Karim Jerbi", "Giulia Lioi"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ZeFMtRBy4Z"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/0b9fb85ecc9a62002866ac3fb9367e22d13fa0db.pdf"
published: "2025"
categories: []
keywords: ["Foundation Model", "EEG", "SSL", "BCI"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:20+09:00"
---

# REVE: A Foundation Model for EEG - Adapting to Any Setup with Large-Scale Pretraining on 25,000 Subjects

## Abstract
Foundation models have transformed AI by reducing reliance on task-specific data through large-scale pretraining. While successful in language and vision, their adoption in EEG has lagged due to the heterogeneity of public datasets, which are collected under varying protocols, devices, and electrode configurations. Existing EEG foundation models struggle to generalize across these variations, often restricting pretraining to a single setup, resulting in suboptimal performance, in particular under linear probing.
We present REVE (Representation for EEG with Versatile Embeddings), a pretrained model explicitly designed to generalize across diverse EEG signals. REVE introduces a novel 4D positional encoding scheme that enables it to process signals of arbitrary length and electrode arrangement. Using a masked autoencoding objective, we pretrain REVE on over 60,000 hours of EEG data from 92 datasets spanning 25,000 subjects, representing the largest EEG pretraining effort to date.
REVE achieves state-of-the-art results on 10 downstream EEG tasks, including motor imagery classification, seizure detection, sleep staging, cognitive load estimation, and emotion recognition. With little to no fine-tuning, it demonstrates strong generalization, and nuanced spatio-temporal modeling. We release code, pretrained weights, and tutorials to support standardized EEG research and accelerate progress in clinical neuroscience.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Yassine El Ouahidi, Jonathan Lys, Philipp Thölke, Nicolas Farrugia, Bastien Pasdeloup, Vincent Gripon, Karim Jerbi, Giulia Lioi
- arxiv_id: 
- openreview_id: ZeFMtRBy4Z
- anthology_id: 
- pdf_url: https://openreview.net/pdf/0b9fb85ecc9a62002866ac3fb9367e22d13fa0db.pdf
- published: 2025
- keywords: Foundation Model, EEG, SSL, BCI

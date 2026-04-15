---
title: "Improving Target Sound Extraction via Disentangled Codec Representations with Privileged Knowledge Distillation"
authors: ["Dail Kim", "Joon-Hyuk Chang"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "rew03VaNUJ"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/728fcc79c0e6398a8d6115c89e30c5d818096b74.pdf"
published: "2025"
categories: []
keywords: ["Target Sound Extraction", "Privileged Knowledge distillation", "Disentangled Representation Learning", "Neural Audio Codec", "Feature-level Knowledge Distillation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:28+09:00"
---

# Improving Target Sound Extraction via Disentangled Codec Representations with Privileged Knowledge Distillation

## Abstract
Target sound extraction aims to isolate target sound sources from an input mixture using a target clue to identify the sounds of interest. To address the challenge posed by the wide variety of sounds, recent work has introduced privileged knowledge distillation (PKD), which utilizes privileged information (PI) about the target sound, available only during training. While PKD has shown promise, existing approaches often suffer from overfitting of the teacher model for the overly rich PI and ineffective knowledge transfer to the student model. In this paper, we propose Disentangled Codec Knowledge Distillation (DCKD) to mitigate these issues by regulating the amount and the flow of target sound information within the teacher model. We begin by extracting a compressed representation of the target sound using a neural audio codec to regulate the amount of PI. Disentangled representation learning is then applied to remove class information and extract fine-grained temporal information as PI. Subsequently, an n-hot vector as the class information and the class-independent PI are used to condition the early and later layers of the teacher model, respectively, forming a regulated coarse-to-fine target information flow. The resulting representation is transferred to the student model through feature-level knowledge distillation. Experimental results show that DCKD consistently improves existing methods across model architectures under the multi-target selection condition.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Dail Kim, Joon-Hyuk Chang
- arxiv_id: 
- openreview_id: rew03VaNUJ
- anthology_id: 
- pdf_url: https://openreview.net/pdf/728fcc79c0e6398a8d6115c89e30c5d818096b74.pdf
- published: 2025
- keywords: Target Sound Extraction, Privileged Knowledge distillation, Disentangled Representation Learning, Neural Audio Codec, Feature-level Knowledge Distillation

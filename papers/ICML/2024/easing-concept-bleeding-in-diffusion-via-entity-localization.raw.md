---
title: "Easing Concept Bleeding in Diffusion via Entity Localization and Anchoring"
authors: ["Jiewei Zhang", "Song Guo", "Peiran Dong", "Jie ZHANG", "Ziming Liu", "Yue Yu", "Xiao-Ming Wu"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "MsnJl6JkZS"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/7153eba338ccd0fbf79bd80e735ccb22ac714ffb.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:43+09:00"
---

# Easing Concept Bleeding in Diffusion via Entity Localization and Anchoring

## Abstract
Recent diffusion models have manifested extraordinary capabilities in generating high-quality, diverse, and innovative images guided by textual prompts. Nevertheless, these state-of-the-art models may encounter the challenge of concept bleeding when generating images with multiple entities or attributes in the prompt, leading to the unanticipated merging or overlapping of distinct objects in the synthesized result. The current work exploits auxiliary networks to produce mask-constrained regions for entities, necessitating the training of an object detection network. In this paper, we investigate the bleeding reason and find that the cross-attention map associated with a specific entity or attribute tends to extend beyond its intended focus, encompassing the background or other unrelated objects and thereby acting as the primary source of concept bleeding. Motivated by this, we propose Entity Localization and Anchoring (ELA) to drive the entity to concentrate on the expected region accurately during inference, eliminating the necessity for training. Specifically, we initially identify the region corresponding to each entity and subsequently employ a tailored loss function to anchor entities within their designated positioning areas. Extensive experiments demonstrate its superior capability in precisely generating multiple objects as specified in the textual prompts.

## Metadata
- venue: ICML
- year: 2024
- authors: Jiewei Zhang, Song Guo, Peiran Dong, Jie ZHANG, Ziming Liu, Yue Yu, Xiao-Ming Wu
- arxiv_id: 
- openreview_id: MsnJl6JkZS
- anthology_id: 
- pdf_url: https://openreview.net/pdf/7153eba338ccd0fbf79bd80e735ccb22ac714ffb.pdf
- published: 2024

---
title: "What Matters to You? Towards Visual Representation Alignment for Robot Learning"
authors: ["Thomas Tian", "Chenfeng Xu", "Masayoshi Tomizuka", "Jitendra Malik", "Andrea Bajcsy"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "CTlUHIKF71"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b089a2d0ee33f551f8ee252854a9a7630830fe59.pdf"
published: "2024"
categories: []
keywords: ["Robot learning", "Preference learning", "Visual reward learning", "Representation alignment"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:03+09:00"
---

# What Matters to You? Towards Visual Representation Alignment for Robot Learning

## Abstract
When operating in service of people, robots need to optimize rewards aligned with end-user preferences. Since robots will rely on raw perceptual inputs, their rewards will inevitably use visual representations. Recently there has been excitement in using representations from pre-trained visual models, but key to making these work in robotics is fine-tuning, which is typically done via proxy tasks like dynamics prediction or enforcing temporal cycle-consistency. However, all these proxy tasks bypass the human’s input on what matters to them, exacerbating spurious correlations and ultimately leading to behaviors that are misaligned with user preferences. In this work, we propose that robots should leverage human feedback to align their visual representations with the end-user and disentangle what matters for the task. We propose Representation-Aligned Preference-based Learning (RAPL), a method for solving the visual representation alignment problem and visual reward learning problem through the lens of preference-based learning and optimal transport. Across experiments in X MAGICAL and in robotic manipulation, we find that RAPL’s reward consistently generates preferred robot behaviors with high sample efficiency, and shows strong zero-shot generalization when the visual representation is learned from a different embodiment than the robot’s.

## Metadata
- venue: ICLR
- year: 2024
- authors: Thomas Tian, Chenfeng Xu, Masayoshi Tomizuka, Jitendra Malik, Andrea Bajcsy
- arxiv_id: 
- openreview_id: CTlUHIKF71
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b089a2d0ee33f551f8ee252854a9a7630830fe59.pdf
- published: 2024
- keywords: Robot learning, Preference learning, Visual reward learning, Representation alignment

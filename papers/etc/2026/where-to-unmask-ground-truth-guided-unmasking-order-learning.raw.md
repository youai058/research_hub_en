---
title: "Where-to-Unmask: Ground-Truth-Guided Unmasking Order Learning for Masked Diffusion Language Models"
authors: ["Hikaru Asano", "Tadashi Kozuno", "Kuniaki Saito", "Yukino Baba"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.09501"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.09501v1"
published: "2026-02-10"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:05+09:00"
---

# Where-to-Unmask: Ground-Truth-Guided Unmasking Order Learning for Masked Diffusion Language Models

## Abstract
Masked Diffusion Language Models (MDLMs) generate text by iteratively filling masked tokens, requiring two coupled decisions at each step: which positions to unmask (where-to-unmask) and which tokens to place (what-to-unmask). While standard MDLM training directly optimizes token prediction (what-to-unmask), inference-time unmasking orders (where-to-unmask) are typically determined by heuristic confidence measures or trained through reinforcement learning with costly on-policy rollouts. To address this, we introduce Gt-Margin, a position-wise score derived from ground-truth tokens, defined as the probability margin between the correct token and its strongest alternative. Gt-Margin yields an oracle unmasking order that prioritizes easier positions first under each partially masked state. We demonstrate that leveraging this oracle unmasking order significantly enhances final generation quality, particularly on logical reasoning benchmarks. Building on this insight, we train a supervised unmasking planner via learning-to-rank to imitate the oracle ordering from masked contexts. The resulting planner integrates into standard MDLM sampling to select where-to-unmask, improving reasoning accuracy without modifying the token prediction model.

## Metadata
- venue: arXiv
- year: 2026
- authors: Hikaru Asano, Tadashi Kozuno, Kuniaki Saito, Yukino Baba
- arxiv_id: 2602.09501
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.09501v1
- published: 2026-02-10

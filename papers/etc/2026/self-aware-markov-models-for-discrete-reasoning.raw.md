---
title: "Self-Aware Markov Models for Discrete Reasoning"
authors: ["Gregor Kornhardt", "Jannis Chemseddine", "Christian Wald", "Gabriele Steidl"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.16661"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.16661v2"
published: "2026-03-17"
categories: ["cs.LG", "stat.ML"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:24+09:00"
---

# Self-Aware Markov Models for Discrete Reasoning

## Abstract
Standard masked discrete diffusion models face limitations in reasoning tasks due to their inability to correct their own mistakes on the masking path. Since they rely on a fixed number of denoising steps, they are unable to adjust their computation to the complexity of a given problem. To address these limitations, we introduce a method based on learning a Markov transition kernel that is trained on its own outputs. This design enables tokens to be remasked, allowing the model to correct its previous mistakes. Furthermore, we do not need a fixed time schedule but use a trained stopping criterion. This allows for adaptation of the number of function evaluations to the difficulty of the reasoning problem. Our adaptation adds two lightweight prediction heads, enabling reuse and fine-tuning of existing pretrained models. On the Sudoku-Extreme dataset we clearly outperform other flow based methods with a validity of 95%. For the Countdown-4 we only need in average of 10 steps to solve almost 96% of them correctly, while many problems can be solved already in 2 steps.

## Metadata
- venue: arXiv
- year: 2026
- authors: Gregor Kornhardt, Jannis Chemseddine, Christian Wald, Gabriele Steidl
- arxiv_id: 2603.16661
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.16661v2
- published: 2026-03-17

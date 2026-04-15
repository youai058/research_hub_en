---
title: "Inductive biases of multi-task learning and finetuning: multiple regimes of feature reuse"
authors: ["Samuel Lippl", "Jack Lindsey"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "UwvjJZWjPT"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ee7924e5fbd2c59861128894655788624dabe426.pdf"
published: "2024"
categories: []
keywords: ["multi-task learning", "implicit regularization", "finetuning", "pretraining", "implicit bias"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:36+09:00"
---

# Inductive biases of multi-task learning and finetuning: multiple regimes of feature reuse

## Abstract
Neural networks are often trained on multiple tasks, either simultaneously (multi-task learning, MTL) or sequentially (pretraining and subsequent finetuning, PT+FT). In particular, it is common practice to pretrain neural networks on a large auxiliary task before finetuning on a downstream task with fewer samples. Despite the prevalence of this approach, the inductive biases that arise from learning multiple tasks are poorly characterized. In this work, we address this gap. We describe novel implicit regularization penalties associated with MTL and PT+FT in diagonal linear networks and single-hidden-layer ReLU networks. These penalties indicate that MTL and PT+FT induce the network to reuse features in different ways. 1) Both MTL and PT+FT exhibit biases towards feature reuse between tasks, and towards sparsity in the set of learned features. We show a "conservation law" that implies a direct tradeoff between these two biases. 2) PT+FT exhibits a novel "nested feature selection" regime, not described by either the "lazy" or "rich" regimes identified in prior work, which biases it to *rely on a sparse subset* of the features learned during pretraining. This regime is much narrower for MTL. 3) PT+FT (but not MTL) in ReLU networks benefits from features that are correlated between the auxiliary and main task. We confirm these findings empirically with teacher-student models, and introduce a technique -- weight rescaling following pretraining -- that can elicit the nested feature selection regime. Finally, we validate our theory in deep neural networks trained on image classification. We find that weight rescaling improves performance when it causes models to display signatures of nested feature selection. Our results suggest that nested feature selection may be an important inductive bias for finetuning neural networks.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Samuel Lippl, Jack Lindsey
- arxiv_id: 
- openreview_id: UwvjJZWjPT
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ee7924e5fbd2c59861128894655788624dabe426.pdf
- published: 2024
- keywords: multi-task learning, implicit regularization, finetuning, pretraining, implicit bias

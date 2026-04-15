---
title: "On the Inductive Bias of Stacking Towards Improving Reasoning"
authors: ["Nikunj Saunshi", "Stefani Karp", "Shankar Krishnan", "Sobhan Miryoosefi", "Sashank J. Reddi", "Sanjiv Kumar"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "3ZAfFoAcUI"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/30d478429b58478c4650f019a85f0ef30d3e5b85.pdf"
published: "2024"
categories: []
keywords: ["stacking", "language model", "reasoning", "inductive bias", "efficient training"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:36+09:00"
---

# On the Inductive Bias of Stacking Towards Improving Reasoning

## Abstract
Given the increasing scale of model sizes, efficient training strategies like gradual stacking have garnered interest. Stacking enables efficient training by gradually growing the depth of a model in stages and using layers from a smaller model in an earlier stage to initialize the next stage. Although efficient for training, the model biases induced by such growing approaches are largely unexplored. In this work, we examine this fundamental aspect of gradual stacking, going beyond its efficiency benefits. We propose a variant of gradual stacking called MIDAS that can speed up language model training by up to 40\%. Furthermore we discover an intriguing phenomenon: MIDAS is not only training-efficient but surprisingly also has an inductive bias towards improving downstream tasks, especially tasks that require reasoning abilities like reading comprehension and math problems, despite having similar or slightly worse perplexity compared to baseline training. To further analyze this inductive bias, we construct {\em reasoning primitives} – simple synthetic tasks that are building blocks for reasoning – and find that a model pretrained with stacking is significantly better than standard pretraining on these primitives, with and without fine-tuning. This provides stronger and more robust evidence for this inductive bias towards reasoning. These findings of training efficiency and inductive bias towards reasoning are verified at 1B, 2B and 8B parameter language models. Finally, we conjecture the underlying reason for this inductive bias by exploring the connection of stacking to looped models and provide strong supporting empirical analysis.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Nikunj Saunshi, Stefani Karp, Shankar Krishnan, Sobhan Miryoosefi, Sashank J. Reddi, Sanjiv Kumar
- arxiv_id: 
- openreview_id: 3ZAfFoAcUI
- anthology_id: 
- pdf_url: https://openreview.net/pdf/30d478429b58478c4650f019a85f0ef30d3e5b85.pdf
- published: 2024
- keywords: stacking, language model, reasoning, inductive bias, efficient training

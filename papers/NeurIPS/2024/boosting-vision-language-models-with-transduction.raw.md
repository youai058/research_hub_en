---
title: "Boosting Vision-Language Models with Transduction"
authors: ["Maxime Zanella", "Benoît Gérin", "Ismail Ben Ayed"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "go4zzXBWVs"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/165a3547dab21e1476a8a33906c72652f74ed988.pdf"
published: "2024"
categories: []
keywords: ["Vision-Language", "zero-shot", "transduction", "unsupervised learning", "few-shot"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:04+09:00"
---

# Boosting Vision-Language Models with Transduction

## Abstract
Transduction is a powerful paradigm that leverages the structure of unlabeled data to boost predictive accuracy. We present TransCLIP, a novel and computationally efficient transductive approach designed for Vision-Language Models (VLMs). TransCLIP is applicable as a plug-and-play module on top of popular inductive zero- and few-shot models, consistently improving their performances. Our new objective function can be viewed as a regularized maximum-likelihood estimation, constrained by a KL divergence penalty that integrates the text-encoder knowledge and guides the transductive learning process. We further derive an iterative Block Majorize-Minimize (BMM) procedure for optimizing our objective, with guaranteed convergence and decoupled sample-assignment updates, yielding computationally efficient transduction for large-scale datasets. We report comprehensive evaluations, comparisons, and ablation studies that demonstrate: (i) Transduction can greatly enhance the generalization capabilities of inductive pretrained zero- and few-shot VLMs; (ii) TransCLIP substantially outperforms standard transductive few-shot learning methods relying solely on vision features, notably due to the KL-based language constraint.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Maxime Zanella, Benoît Gérin, Ismail Ben Ayed
- arxiv_id: 
- openreview_id: go4zzXBWVs
- anthology_id: 
- pdf_url: https://openreview.net/pdf/165a3547dab21e1476a8a33906c72652f74ed988.pdf
- published: 2024
- keywords: Vision-Language, zero-shot, transduction, unsupervised learning, few-shot

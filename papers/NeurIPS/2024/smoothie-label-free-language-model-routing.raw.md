---
title: "Smoothie: Label Free Language Model Routing"
authors: ["Neel Guha", "Mayee F Chen", "Trevor Chow", "Ishan S. Khare", "Christopher Re"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "pPSWHsgqRp"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/5c0e172eaa2e9b1dfee0fa41fd6b06f1eb52c2b7.pdf"
published: "2024"
categories: []
keywords: ["large language models", "weak supervision", "graphical models", "routing"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:37+09:00"
---

# Smoothie: Label Free Language Model Routing

## Abstract
Large language models (LLMs) are increasingly used in applications where LLM inputs may span many different tasks. Recent work has found that the choice of LLM is consequential, and different LLMs may be good for different input samples. Prior approaches have thus explored how engineers might select an LLM to use for each sample (i.e. _routing_). While existing routing methods mostly require training auxiliary models on human-annotated data, our work explores whether it is possible to perform _unsupervised_ routing. We propose Smoothie, a weak supervision-inspired routing approach that requires no labeled data. Given a set of outputs from different LLMs, Smoothie constructs a latent variable graphical model over embedding representations of observable LLM outputs and unknown “true” outputs. Using this graphical model, we estimate sample-dependent quality scores for each LLM, and route each sample to the LLM with the highest corresponding score. We find that Smoothie's LLM quality-scores correlate with ground-truth model quality (correctly identifying the optimal model on 9/14 tasks), and that Smoothie outperforms baselines for routing by up to 10 points accuracy.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Neel Guha, Mayee F Chen, Trevor Chow, Ishan S. Khare, Christopher Re
- arxiv_id: 
- openreview_id: pPSWHsgqRp
- anthology_id: 
- pdf_url: https://openreview.net/pdf/5c0e172eaa2e9b1dfee0fa41fd6b06f1eb52c2b7.pdf
- published: 2024
- keywords: large language models, weak supervision, graphical models, routing

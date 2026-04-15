---
title: "TRACE Back from the Future: A Probabilistic Reasoning Approach to Controllable Language Generation"
authors: ["Gwen Yidou Weng", "Benjie Wang", "Guy Van den Broeck"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "LhkSfpfRXW"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9de1d354ce6ff3b20b5590851982e61ae19189fb.pdf"
published: "2025"
categories: []
keywords: ["Controlled Generation", "Probabilistic Reasoning", "Tractable Inference", "Hidden Markov Models (HMM)", "Detoxification"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:23+09:00"
---

# TRACE Back from the Future: A Probabilistic Reasoning Approach to Controllable Language Generation

## Abstract
As large language models (LMs) advance, there is an increasing need to control their outputs to align with human values (e.g., detoxification) or desired attributes (e.g., personalization, topic). However, autoregressive models focus on next-token predictions and struggle with global properties that require looking ahead. Existing solutions either post-train LMs for each new attribute—expensive and inflexible—or approximate the Expected Attribute Probability (EAP) of future sequences by sampling or training, which is slow and unreliable for rare attributes. We introduce **TRACE** (Tractable Probabilistic Reasoning for Adaptable Controllable gEneration), a novel framework that efficiently computes EAP and adapts to new attributes through tractable *probabilistic* reasoning and lightweight *control*. TRACE distills a Hidden Markov Model (HMM) from an LM and pairs it with a small classifier to estimate attribute probabilities, enabling exact EAP computation over the HMM’s predicted futures. This EAP is then used to reweigh the LM’s next-token probabilities for globally compliant continuations. Empirically, TRACE achieves state-of-the-art detoxification results with only 20% decoding overhead, yields 76 low-resource personalized LMs within seconds, and seamlessly extends to composite attributes.

## Metadata
- venue: ICML
- year: 2025
- authors: Gwen Yidou Weng, Benjie Wang, Guy Van den Broeck
- arxiv_id: 
- openreview_id: LhkSfpfRXW
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9de1d354ce6ff3b20b5590851982e61ae19189fb.pdf
- published: 2025
- keywords: Controlled Generation, Probabilistic Reasoning, Tractable Inference, Hidden Markov Models (HMM), Detoxification

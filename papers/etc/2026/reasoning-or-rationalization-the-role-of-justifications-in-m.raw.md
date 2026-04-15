---
title: "Reasoning or Rationalization? The Role of Justifications in Masked Diffusion Models for Fact Verification"
authors: ["Jacob Devasier"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.01190"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.01190v1"
published: "2026-03-01"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:02+09:00"
---

# Reasoning or Rationalization? The Role of Justifications in Masked Diffusion Models for Fact Verification

## Abstract
Unlike autoregressive models, which generate tokens sequentially and benefit from reasoning-before-answering strategies such as Chain-of-Thought, Masked Diffusion Language Models (MDLMs) refine all sequence positions simultaneously, raising questions about how these models handle tasks requiring justified verdicts. In this work, we investigate the dynamics of MDLM reasoning on fact verification, examining whether justifications serve as genuine reasoning or post-hoc rationalization. We observe that MDLMs typically converge on a verdict early in the diffusion process, treating it as a global anchor that is resolved before the justification is complete. Crucially, enforcing a reasoning-first constraint via delayed verdict unmasking actively degrades performance, dropping accuracy from 86.2% to 71.9% as accumulating justification tokens introduce inconsistencies that override initially correct predictions. Interventional experiments reveal that the model rationalizes incorrect forced verdicts in 56% of cases, and that verdicts are strongly causally dependent on justification quality (57.3% accuracy with corrupted justifications vs. 97.1% with ground-truth). This causal dependence explains the degradation under forced deliberation: as the model generates noisy justification tokens, it conditions on them, gradually overriding its initially correct assessment. Our findings suggest that for fact verification with MDLMs, extended deliberation can be counterproductive, risking the dilution of accurate early predictions with noise introduced during justification generation.

## Metadata
- venue: arXiv
- year: 2026
- authors: Jacob Devasier
- arxiv_id: 2603.01190
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.01190v1
- published: 2026-03-01

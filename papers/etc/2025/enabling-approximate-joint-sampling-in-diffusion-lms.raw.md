---
title: "Enabling Approximate Joint Sampling in Diffusion LMs"
authors: ["Parikshit Bansal", "Sujay Sanghavi"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2509.22738"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2509.22738v2"
published: "2025-09-25"
categories: ["cs.CL", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:14+09:00"
---

# Enabling Approximate Joint Sampling in Diffusion LMs

## Abstract
In autoregressive language models, each token is sampled by conditioning on all the past tokens; the overall string has thus been sampled from the correct underlying joint distribution represented by the model. In contrast, masked diffusion language models generate text by unmasking tokens out of order and potentially in parallel. Generating an overall string sampled from the correct underlying joint distribution would (again) require exactly one token unmasking in every full-model forward pass. The more tokens unmasked in parallel, the further away the string is from the true joint; this can be seen in the resulting drop in accuracy (but, increase in speed). In this paper we devise a way to {\em approximately} sample multiple tokens from the joint distribution in a single full-model forward pass; we do so by developing a new lightweight single-layer ``sampler" on top of an existing large diffusion LM. One forward pass of the full model can now be followed by multiple forward passes of only this sampler layer, to yield multiple unmasked tokens. Our sampler is trained to mimic exact joint sampling from the (frozen) full model. We show the effectiveness of our approximate joint sampling for both pretrained-only (Dream-7B-Base, Llada-7B-Base) and instruction-tuned (Dream-7B-Instruct, Dream-7B-Coder) models on language modeling and math \& coding tasks. When four tokens are unmasked for each full-model denoising step, our sampling algorithm achieves a MAUVE score of 0.87 (vs marginal baseline of 0.31) with respect to the true joint distribution.

## Metadata
- venue: arXiv
- year: 2025
- authors: Parikshit Bansal, Sujay Sanghavi
- arxiv_id: 2509.22738
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2509.22738v2
- published: 2025-09-25

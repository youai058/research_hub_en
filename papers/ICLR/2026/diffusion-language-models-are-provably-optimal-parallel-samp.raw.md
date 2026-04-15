---
title: "Diffusion Language Models are Provably Optimal Parallel Samplers"
authors: ["Haozhe Jiang", "Nika Haghtalab", "Lijie Chen"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: "2512.25014"
openreview_id: "5bkAbueJwM"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ec3e7006903668cdd22b384ca76eccf5169f00f0.pdf"
published: "2026"
categories: []
keywords: ["Theory", "Diffusion Language Model", "Large Language Model"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:49+09:00"
---

# Diffusion Language Models are Provably Optimal Parallel Samplers

## Abstract
Diffusion language models (DLMs) have emerged as a promising alternative to autoregressive models for faster inference via parallel token generation. We provide a rigorous foundation for this advantage by formalizing a model of parallel sampling and showing that DLMs augmented with polynomial-length chain-of-thought (CoT) can simulate any parallel sampling algorithm using an optimal number of sequential steps. 
Consequently, whenever a target distribution 
can be generated using a small number of sequential steps, a DLM can be used to generate the distribution using the same number of optimal sequential steps.
However, without the ability to modify previously revealed tokens, DLMs with CoT can still incur large intermediate footprints. We prove that enabling remasking (converting unmasked tokens to masks or revision (converting unmasked tokens to other unmasked tokens) together with CoT further allows DLMs to simulate any parallel sampling algorithm with optimal space complexity.
We further justify the advantage of revision by establishing a strict expressivity gap: DLMs with revision or remasking are strictly more powerful than those without.
Our results not only provide a theoretical justification for the promise of DLMs as the most efficient sampler, but also 
advocate for why revisions should be enabled in DLMs.

## Metadata
- venue: ICLR
- year: 2026
- authors: Haozhe Jiang, Nika Haghtalab, Lijie Chen
- arxiv_id: 
- openreview_id: 5bkAbueJwM
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ec3e7006903668cdd22b384ca76eccf5169f00f0.pdf
- published: 2026
- keywords: Theory, Diffusion Language Model, Large Language Model

---
title: "Continuous Diffusion Models Can Obey Formal Syntax"
authors: ["Jinwoo Kim", "Taylor Berg-Kirkpatrick", "Loris D'Antoni"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.12468"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.12468v1"
published: "2026-02-12"
categories: ["cs.LG", "cs.FL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:02+09:00"
---

# Continuous Diffusion Models Can Obey Formal Syntax

## Abstract
Diffusion language models offer a promising alternative to autoregressive models due to their global, non-causal generation process, but their continuous latent dynamics make discrete constraints -- e.g., the output should be a JSON file that matches a given schema -- difficult to impose. We introduce a training-free guidance method for steering continuous diffusion language models to satisfy formal syntactic constraints expressed using regular expressions. Our approach constructs an analytic score estimating the probability that a latent state decodes to a valid string accepted by a given regular expression, and uses its gradient to guide sampling, without training auxiliary classifiers. The denoising process targets the base model conditioned on syntactic validity.
  We implement our method in Diffinity on top of the PLAID diffusion model and evaluate it on 180 regular-expression constraints over JSON and natural-language benchmarks. Diffinity achieves 68-96\% constraint satisfaction while incurring only a small perplexity cost relative to unconstrained sampling, outperforming autoregressive constrained decoding in both constraint satisfaction and output quality.

## Metadata
- venue: arXiv
- year: 2026
- authors: Jinwoo Kim, Taylor Berg-Kirkpatrick, Loris D'Antoni
- arxiv_id: 2602.12468
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.12468v1
- published: 2026-02-12

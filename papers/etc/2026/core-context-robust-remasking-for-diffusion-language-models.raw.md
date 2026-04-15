---
title: "CORE: Context-Robust Remasking for Diffusion Language Models"
authors: ["Kevin Zhai", "Sabbir Mollah", "Zhenyi Wang", "Mubarak Shah"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.04096"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.04096v3"
published: "2026-02-04"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:17+09:00"
---

# CORE: Context-Robust Remasking for Diffusion Language Models

## Abstract
Standard decoding in Masked Diffusion Models (MDMs) is hindered by context rigidity: tokens are retained based on transient high confidence, often ignoring that early predictions lack full context. This creates cascade effects where initial inconsistencies misguide the remaining generation. Existing revision strategies attempt to mitigate this by relying on static confidence scores, but these signals are inherently myopic; inconsistent tokens can appear confident to the model itself. We propose Context-Robust Remasking (CORE), a training-free framework for inference-time revision. Rather than trusting static token probabilities, CORE identifies context-brittle tokens by probing their sensitivity to targeted masked-context perturbations. We formalize revision as a robust optimization objective over context shifts and efficiently approximate this objective to prioritize unstable tokens for revision. On LLaDA-8B-Base, CORE delivers consistent improvements across reasoning and code benchmarks, outperforming compute-matched baselines and improving MBPP by up to 9.2 percentage points.

## Metadata
- venue: arXiv
- year: 2026
- authors: Kevin Zhai, Sabbir Mollah, Zhenyi Wang, Mubarak Shah
- arxiv_id: 2602.04096
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.04096v3
- published: 2026-02-04

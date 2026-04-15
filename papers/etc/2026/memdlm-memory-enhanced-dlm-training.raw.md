---
title: "MemDLM: Memory-Enhanced DLM Training"
authors: ["Zehua Pei", "Hui-Ling Zhen", "Weizhe Lin", "Sinno Jialin Pan", "Yunhe Wang", "Mingxuan Yuan", "Bei Yu"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.22241"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.22241v2"
published: "2026-03-23"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:13:58+09:00"
---

# MemDLM: Memory-Enhanced DLM Training

## Abstract
Diffusion Language Models (DLMs) offer attractive advantages over Auto-Regressive (AR) models, such as full-attention parallel decoding and flexible generation. However, standard DLM training uses a static, single-step masked prediction objective that never exposes the model to the progressive denoising dynamics of inference, and forces all contextual information to be maintained purely through token-space attention, which becomes increasingly diluted as context length grows. We propose MemDLM (Memory-Enhanced DLM), which introduces a second memory channel by embedding a simulated denoising trajectory into training via Bi-level Optimization. An inner loop updates a set of fast weights, forming a Parametric Memory that captures the local trajectory experience, while an outer loop updates the base model conditioned on this memory. By offloading part of the memorization burden from token-space attention to parameter space, MemDLM yields faster convergence, stronger long-context representations, and lower training loss, even when the fast weights are discarded at inference time. Re-enabling the inner loop at inference provides an additional prompt-specific adaptation effect, where the Parametric Memory acts as an emergent in-weight retrieval mechanism on challenging Needle-in-a-Haystack tasks. Code: https://github.com/JarvisPei/MemDLM.

## Metadata
- venue: arXiv
- year: 2026
- authors: Zehua Pei, Hui-Ling Zhen, Weizhe Lin, Sinno Jialin Pan, Yunhe Wang, Mingxuan Yuan, Bei Yu
- arxiv_id: 2603.22241
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.22241v2
- published: 2026-03-23

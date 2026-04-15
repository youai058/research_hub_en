---
title: "A Tale of Two Temperatures: Simple, Efficient, and Diverse Sampling from Diffusion Language Models"
authors: ["Theo X. Olausson", "Metod Jazbec", "Xi Wang", "Armando Solar-Lezama", "Christian A. Naesseth", "Stephan Mandt", "Eric Nalisnick"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2604.09921"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2604.09921v1"
published: "2026-04-10"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:13:54+09:00"
---

# A Tale of Two Temperatures: Simple, Efficient, and Diverse Sampling from Diffusion Language Models

## Abstract
Much work has been done on designing fast and accurate sampling for diffusion language models (dLLMs). However, these efforts have largely focused on the tradeoff between speed and quality of individual samples; how to additionally ensure diversity across samples remains less well understood. In this work, we show that diversity can be increased by using softened, tempered versions of familiar confidence-based remasking heuristics, retaining their computational benefits and offering simple implementations. We motivate this approach by introducing an idealized formal model of fork tokens and studying the impact of remasking on the expected entropy at the forks. Empirically, the proposed tempered heuristics close the exploration gap (pass@k) between existing confidence-based and autoregressive sampling, hence outperforming both when controlling for cost (pass@NFE). We further study how the increase in diversity translates to downstream post-training and test-time compute scaling. Overall, our findings demonstrate that simple, efficient, and diverse sampling from dLLMs is possible.

## Metadata
- venue: arXiv
- year: 2026
- authors: Theo X. Olausson, Metod Jazbec, Xi Wang, Armando Solar-Lezama, Christian A. Naesseth, Stephan Mandt, Eric Nalisnick
- arxiv_id: 2604.09921
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2604.09921v1
- published: 2026-04-10

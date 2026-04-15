---
title: "Reproducing and Dissecting Denoising Language Models for Speech Recognition"
authors: ["Dorian Koch", "Albert Zeyer", "Nick Rossenbach", "Ralf Schlüter", "Hermann Ney"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2512.13576"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2512.13576v1"
published: "2025-12-15"
categories: ["cs.NE"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:03+09:00"
---

# Reproducing and Dissecting Denoising Language Models for Speech Recognition

## Abstract
Denoising language models (DLMs) have been proposed as a powerful alternative to traditional language models (LMs) for automatic speech recognition (ASR), motivated by their ability to use bidirectional context and adapt to a specific ASR model's error patterns. However, the complexity of the DLM training pipeline has hindered wider investigation. This paper presents the first independent, large-scale empirical study of DLMs. We build and release a complete, reproducible pipeline to systematically investigate the impact of key design choices. We evaluate dozens of configurations across multiple axes, including various data augmentation techniques (e.g., SpecAugment, dropout, mixup), different text-to-speech systems, and multiple decoding strategies. Our comparative analysis in a common subword vocabulary setting demonstrates that DLMs outperform traditional LMs, but only after a distinct compute tipping point. While LMs are more efficient at lower budgets, DLMs scale better with longer training, mirroring behaviors observed in diffusion language models. However, we observe smaller improvements than those reported in prior character-based work, which indicates that the DLM's performance is conditional on factors such as the vocabulary. Our analysis reveals that a key factor for improving performance is to condition the DLM on richer information from the ASR's hypothesis space, rather than just a single best guess. To this end, we introduce DLM-sum, a novel method for decoding from multiple ASR hypotheses, which consistently outperforms the previously proposed DSR decoding method. We believe our findings and public pipeline provide a crucial foundation for the community to better understand, improve, and build upon this promising class of models. The code is publicly available at https://github.com/rwth-i6/2025-denoising-lm/.

## Metadata
- venue: arXiv
- year: 2025
- authors: Dorian Koch, Albert Zeyer, Nick Rossenbach, Ralf Schlüter, Hermann Ney
- arxiv_id: 2512.13576
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2512.13576v1
- published: 2025-12-15

---
title: "Learning Unmasking Policies for Diffusion Language Models"
authors: ["Metod Jazbec", "Theo X. Olausson", "Louis Béthune", "Pierre Ablin", "Michael Kirchhof", "João Monteiro", "Victor Turrisi", "Jason Ramapuram", "Marco Cuturi"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2512.09106"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2512.09106v3"
published: "2025-12-09"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:19+09:00"
---

# Learning Unmasking Policies for Diffusion Language Models

## Abstract
Diffusion (Large) Language Models (dLLMs) now match the downstream performance of their autoregressive counterparts on many tasks, while holding the promise of being more efficient during inference. One critical design aspect of dLLMs is the sampling procedure that selects which tokens to unmask at each diffusion step. Indeed, recent work has found that heuristic strategies such as confidence thresholding improve both sample quality and token throughput compared to random unmasking. However, such heuristics have downsides: they require manual tuning, and we observe that their performance degrades with larger block sizes. In this work, we instead propose to train sampling procedures using reinforcement learning. Specifically, we formalize masked diffusion sampling as a Markov decision process in which the dLLM serves as the environment, and propose a lightweight policy based on a single-layer transformer that maps dLLM token confidences to unmasking decisions. Our experiments show that these trained policies match the performance of state-of-the-art heuristics when combined with semi-autoregressive (block) generation, while outperforming them in the full-diffusion setting.

## Metadata
- venue: arXiv
- year: 2025
- authors: Metod Jazbec, Theo X. Olausson, Louis Béthune, Pierre Ablin, Michael Kirchhof, João Monteiro, Victor Turrisi, Jason Ramapuram, Marco Cuturi
- arxiv_id: 2512.09106
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2512.09106v3
- published: 2025-12-09

---
title: "Masks Can Be Distracting: On Context Comprehension in Diffusion Language Models"
authors: ["Julianna Piskorz", "Cristina Pinneri", "Alvaro Correia", "Motasem Alfarra", "Risheek Garrepalli", "Christos Louizos"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2511.21338"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2511.21338v1"
published: "2025-11-26"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:03+09:00"
---

# Masks Can Be Distracting: On Context Comprehension in Diffusion Language Models

## Abstract
Masked Diffusion Language Models (MDLMs) have recently emerged as a promising alternative to Autoregressive Language Models (ARLMs), leveraging a denoising objective that, in principle, should enable more uniform context utilisation. In this work, we examine the context comprehension abilities of MDLMs and uncover two key limitations. First, despite their more global training objective and bidirectional attention mechanism, similarly to ARLMS, MDLMs exhibit a strong locality bias: performance is highly sensitive to the position of relevant information within the input, favouring local over distant context. Second, we show that appending a large number of mask tokens--required for generation--can significantly degrade context comprehension. Through systematic ablations, we find that these masks act as distractors, reducing the model's ability to process relevant information. To address this, we introduce a mask-agnostic loss function that encourages predictions to remain invariant to the number of appended masks. Fine-tuning with this objective substantially mitigates the distracting effect of masks, improving robustness of MDLMs. Overall, our findings reveal critical limitations of the current MDLM training paradigm and provide actionable insights for building diffusion-based language models with stronger context comprehension.

## Metadata
- venue: arXiv
- year: 2025
- authors: Julianna Piskorz, Cristina Pinneri, Alvaro Correia, Motasem Alfarra, Risheek Garrepalli, Christos Louizos
- arxiv_id: 2511.21338
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2511.21338v1
- published: 2025-11-26

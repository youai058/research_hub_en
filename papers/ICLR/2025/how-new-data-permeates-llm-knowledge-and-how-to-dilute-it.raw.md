---
title: "How new data permeates LLM knowledge and how to dilute it"
authors: ["Chen Sun", "Renat Aksitov", "Andrey Zhmoginov", "Nolan Andrew Miller", "Max Vladymyrov", "Ulrich Rueckert", "Been Kim", "Mark Sandler"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "NGKQoaqLpo"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/6ae382f493c61d71d3eac223066862546ff54232.pdf"
published: "2025"
categories: []
keywords: ["fine-tuning", "hallucinations", "knowledge injection", "memory", "LLMs"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:47+09:00"
---

# How new data permeates LLM knowledge and how to dilute it

## Abstract
Large language models continually learn through the accumulation of gradient-based updates, but how individual pieces of new information affect existing knowledge, leading to both beneficial generalization and problematic hallucination, remains poorly understood. We demonstrate that when learning new information, LLMs exhibit a "priming" effect: learning a new fact can cause the model to inappropriately apply that knowledge in unrelated contexts.
To systematically study this phenomenon, we introduce "Outlandish," a carefully curated dataset of 1320 diverse text samples designed to probe how new knowledge permeates through an LLM's existing knowledge base. Using this dataset, we show that the degree of priming after learning new information can be predicted by measuring the token probability of key words before training. This relationship holds robustly across different model architectures (PALM-2, Gemma, Llama), sizes, and training stages.
Finally, we develop two novel techniques to modulate how new knowledge affects existing model behavior: (1) a ``stepping-stone'' text augmentation strategy and (2) an ``ignore-k'' update pruning method. These approaches reduce undesirable priming effects by 50-95% while preserving the model's ability to learn new information. Our findings provide both empirical insights into how LLMs learn and practical tools for improving the specificity of knowledge insertion in language models. Further materials: https://sunchipsster1.github.io/projects/outlandish/

## Metadata
- venue: ICLR
- year: 2025
- authors: Chen Sun, Renat Aksitov, Andrey Zhmoginov, Nolan Andrew Miller, Max Vladymyrov, Ulrich Rueckert, Been Kim, Mark Sandler
- arxiv_id: 
- openreview_id: NGKQoaqLpo
- anthology_id: 
- pdf_url: https://openreview.net/pdf/6ae382f493c61d71d3eac223066862546ff54232.pdf
- published: 2025
- keywords: fine-tuning, hallucinations, knowledge injection, memory, LLMs

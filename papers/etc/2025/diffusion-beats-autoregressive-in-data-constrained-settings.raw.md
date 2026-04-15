---
title: "Diffusion Beats Autoregressive in Data-Constrained Settings"
authors: ["Mihir Prabhudesai", "Mengning Wu", "Amir Zadeh", "Katerina Fragkiadaki", "Deepak Pathak"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2507.15857"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2507.15857v7"
published: "2025-07-21"
categories: ["cs.LG", "cs.AI", "cs.CV", "cs.RO"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:29+09:00"
---

# Diffusion Beats Autoregressive in Data-Constrained Settings

## Abstract
Autoregressive (AR) models have long dominated the landscape of large language models, driving progress across a wide range of tasks. Recently, diffusion-based language models have emerged as a promising alternative, though their advantages over AR models remain underexplored. In this paper, we systematically study masked diffusion models in data-constrained settings where training involves repeated passes over limited data and find that they significantly outperform AR models when compute is abundant but data is scarce. Diffusion models make better use of repeated data, achieving lower validation loss and superior downstream performance. We find new scaling laws for diffusion models and derive a closed-form expression for the critical compute threshold at which diffusion begins to outperform AR. Finally, we explain why diffusion models excel in this regime: their randomized masking objective implicitly trains over a rich distribution of token orderings, acting as an implicit data augmentation that AR's fixed left-to-right factorization lacks. Our results suggest that when data, not compute, is the bottleneck, diffusion models offer a compelling alternative to the standard AR paradigm. Our code is available at: https://diffusion-scaling.github.io.

## Metadata
- venue: arXiv
- year: 2025
- authors: Mihir Prabhudesai, Mengning Wu, Amir Zadeh, Katerina Fragkiadaki, Deepak Pathak
- arxiv_id: 2507.15857
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2507.15857v7
- published: 2025-07-21

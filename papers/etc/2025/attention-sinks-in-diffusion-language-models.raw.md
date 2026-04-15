---
title: "Attention Sinks in Diffusion Language Models"
authors: ["Maximo Eduardo Rulli", "Simone Petruzzi", "Edoardo Michielon", "Fabrizio Silvestri", "Simone Scardapane", "Alessio Devoto"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.15731"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.15731v2"
published: "2025-10-17"
categories: ["cs.CL", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:10+09:00"
---

# Attention Sinks in Diffusion Language Models

## Abstract
Masked Diffusion Language Models (DLMs) have recently emerged as a promising alternative to traditional Autoregressive Models (ARMs). DLMs employ transformer encoders with bidirectional attention, enabling parallel token generation while maintaining competitive performance. Although their efficiency and effectiveness have been extensively studied, the internal mechanisms that govern DLMs remain largely unexplored. In this work, we conduct an empirical analysis of DLM attention patterns, focusing on the attention sinking phenomenon, an effect previously observed in various transformer-based architectures. Our findings reveal that DLMs also exhibit attention sinks, but with distinct characteristics. First, unlike in ARMs, the sink positions in DLMs tend to shift throughout the generation process, displaying a dynamic behaviour. Second, while ARMs are highly sensitive to the removal of attention sinks, DLMs remain robust: masking sinks leads to only a minor degradation in performance. These results provide new insights into the inner workings of diffusion-based language models and highlight fundamental differences in how they allocate and utilize attention compared to autoregressive models.

## Metadata
- venue: arXiv
- year: 2025
- authors: Maximo Eduardo Rulli, Simone Petruzzi, Edoardo Michielon, Fabrizio Silvestri, Simone Scardapane, Alessio Devoto
- arxiv_id: 2510.15731
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.15731v2
- published: 2025-10-17

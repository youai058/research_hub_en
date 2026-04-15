---
title: "ZUNA: Flexible EEG Superresolution with Position-Aware Diffusion Autoencoders"
authors: ["Christopher Warner", "Jonas Mago", "JR Huml", "Mohamed Osman", "Beren Millidge"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.18478"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.18478v1"
published: "2026-02-09"
categories: ["eess.SP", "cs.AI", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:17+09:00"
---

# ZUNA: Flexible EEG Superresolution with Position-Aware Diffusion Autoencoders

## Abstract
We present \texttt{ZUNA}, a 380M-parameter masked diffusion autoencoder trained to perform masked channel infilling and superresolution for arbitrary electrode numbers and positions in EEG signals. The \texttt{ZUNA} architecture tokenizes multichannel EEG into short temporal windows and injects spatiotemporal structure via a 4D rotary positional encoding over (x,y,z,t), enabling inference on arbitrary channel subsets and positions. We train ZUNA on an aggregated and harmonized corpus spanning 208 public datasets containing approximately 2 million channel-hours using a combined reconstruction and heavy channel-dropout objective. We show that \texttt{ZUNA} substantially improves over ubiquitous spherical-spline interpolation methods, with the gap widening at higher dropout rates. Crucially, compared to other deep learning methods in this space, \texttt{ZUNA}'s performance \emph{generalizes} across datasets and channel positions allowing it to be applied directly to novel datasets and problems. Despite its generative capabilities, \texttt{ZUNA} remains computationally practical for deployment. We release Apache-2.0 weights and an MNE-compatible preprocessing/inference stack to encourage reproducible comparisons and downstream use in EEG analysis pipelines.

## Metadata
- venue: arXiv
- year: 2026
- authors: Christopher Warner, Jonas Mago, JR Huml, Mohamed Osman, Beren Millidge
- arxiv_id: 2602.18478
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.18478v1
- published: 2026-02-09

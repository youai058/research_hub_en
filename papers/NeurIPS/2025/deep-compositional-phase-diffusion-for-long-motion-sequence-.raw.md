---
title: "Deep Compositional Phase Diffusion for Long Motion Sequence Generation"
authors: ["Ho Yin Au", "Jie Chen", "Junkun Jiang", "Jingyu Xiang"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "jzPQRbGkAq"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/1130d293ca50514da0c4fc6832964cee8756084b.pdf"
published: "2025"
categories: []
keywords: ["Motion Generation", "Phase Autoencoder", "Long Term Motion Sequence Generation", "Motion Inbetweening"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:48+09:00"
---

# Deep Compositional Phase Diffusion for Long Motion Sequence Generation

## Abstract
Recent research on motion generation has shown significant progress in generating semantically aligned motion with singular semantics. However, when employing these models to create composite sequences containing multiple semantically generated motion clips, they often struggle to preserve the continuity of motion dynamics at the transition boundaries between clips, resulting in awkward transitions and abrupt artifacts. To address these challenges, we present Compositional Phase Diffusion, which leverages the Semantic Phase Diffusion Module (SPDM) and Transitional Phase Diffusion Module (TPDM) to progressively incorporate semantic guidance and phase details from adjacent motion clips into the diffusion process. Specifically, SPDM and TPDM operate within the latent motion frequency domain established by the pre-trained Action-Centric Motion Phase Autoencoder (ACT-PAE). This allows them to learn semantically important and transition-aware phase information from variable-length motion clips during training. Experimental results demonstrate the competitive performance of our proposed framework in generating compositional motion sequences that align semantically with the input conditions, while preserving phase transitional continuity between preceding and succeeding motion clips. Additionally, motion inbetweening task is made possible by keeping the phase parameter of the input motion sequences fixed throughout the diffusion process, showcasing the potential for extending the proposed framework to accommodate various application scenarios. Codes are available at
https://github.com/asdryau/TransPhase.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Ho Yin Au, Jie Chen, Junkun Jiang, Jingyu Xiang
- arxiv_id: 
- openreview_id: jzPQRbGkAq
- anthology_id: 
- pdf_url: https://openreview.net/pdf/1130d293ca50514da0c4fc6832964cee8756084b.pdf
- published: 2025
- keywords: Motion Generation, Phase Autoencoder, Long Term Motion Sequence Generation, Motion Inbetweening

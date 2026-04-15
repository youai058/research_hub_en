---
title: "CoDAR: Continuous Diffusion Language Models are More Powerful Than You Think"
authors: ["Junzhe Shen", "Jieru Zhao", "Ziwei He", "Zhouhan Lin"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.02547"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.02547v1"
published: "2026-03-03"
categories: ["cs.CL", "cs.AI", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:13:58+09:00"
---

# CoDAR: Continuous Diffusion Language Models are More Powerful Than You Think

## Abstract
We study why continuous diffusion language models (DLMs) have lagged behind discrete diffusion approaches despite their appealing continuous generative dynamics. Under a controlled token--recovery study, we identify token rounding, the final projection from denoised embeddings to tokens, as a primary bottleneck. Building on these insights, we propose CoDAR (Continuous Diffusion with Contextual AutoRegressive Decoder), a two--stage framework that keeps diffusion entirely continuous in an embedding space while learning a strong, context--conditional discretizer: an autoregressive Transformer decoder that cross--attends to the denoised embedding sequence and performs contextualized rounding to tokens. Experiments on LM1B and OpenWebText demonstrate that CoDAR substantially improves generation quality over latent diffusion and becomes competitive with strong discrete DLMs, while exposing a simple decoder--temperature knob to navigate the fluency--diversity trade off.

## Metadata
- venue: arXiv
- year: 2026
- authors: Junzhe Shen, Jieru Zhao, Ziwei He, Zhouhan Lin
- arxiv_id: 2603.02547
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.02547v1
- published: 2026-03-03

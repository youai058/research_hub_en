---
title: "Any-Order Flexible Length Masked Diffusion"
authors: ["Jaeyeon Kim", "Lee Cheuk-Kit", "Carles Domingo-Enrich", "Yilun Du", "Sham Kakade", "Timothy Ngotiaoco", "Sitan Chen", "Michael Albergo"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2509.01025"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2509.01025v2"
published: "2025-08-31"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:29+09:00"
---

# Any-Order Flexible Length Masked Diffusion

## Abstract
Masked diffusion models (MDMs) have recently emerged as a promising alternative to autoregressive models over discrete domains. MDMs generate sequences in an any-order, parallel fashion, enabling fast inference and strong performance on non-causal tasks. However, a crucial limitation is that they do not support token insertions and are thus limited to fixed-length generations. To this end, we introduce Flexible Masked Diffusion Models (FlexMDMs), a discrete diffusion paradigm that simultaneously can model sequences of flexible length while provably retaining MDMs' flexibility of any-order inference. Grounded in an extension of the stochastic interpolant framework, FlexMDMs generate sequences by inserting mask tokens and unmasking them. Empirically, we show that FlexMDMs match MDMs in perplexity while modeling length statistics with much higher fidelity. On a synthetic maze planning task, they achieve $\approx 60 \%$ higher success rate than MDM baselines. Finally, we show pretrained MDMs can easily be retrofitted into FlexMDMs: on 16 H100s, it takes only three days to fine-tune LLaDA-8B into a FlexMDM, achieving superior performance on math (GSM8K, $58\% \to 67\%$) and code infilling performance ($52\% \to 65\%$).

## Metadata
- venue: arXiv
- year: 2025
- authors: Jaeyeon Kim, Lee Cheuk-Kit, Carles Domingo-Enrich, Yilun Du, Sham Kakade, Timothy Ngotiaoco, Sitan Chen, Michael Albergo
- arxiv_id: 2509.01025
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2509.01025v2
- published: 2025-08-31

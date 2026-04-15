---
title: "Compute-Optimal LLMs Provably Generalize Better with Scale"
authors: ["Marc Anton Finzi", "Sanyam Kapoor", "Diego Granziol", "Anming Gu", "Christopher De Sa", "J Zico Kolter", "Andrew Gordon Wilson"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "MF7ljU8xcf"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e35f09f288013a64bdf237be6a81cf0891307411.pdf"
published: "2025"
categories: []
keywords: ["generalization bounds", "language models", "scaling laws"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:13+09:00"
---

# Compute-Optimal LLMs Provably Generalize Better with Scale

## Abstract
Why do larger language models generalize better? To explore this question, we develop generalization bounds on the pretraining objective of large language models (LLMs) in the compute-optimal regime, as described by the Chinchilla scaling laws. We introduce a novel, fully empirical Freedman-type martingale concentration inequality that tightens existing bounds by accounting for the variance of the loss function. The generalization bound can be broken into three contributions: the number of parameters per token, the loss variance, and the quantization error at a fixed bitrate. As language models are scaled up, the number of parameters per data point stays constant; however, both the loss variance and the quantization error decrease, implying that larger models should have \emph{smaller} generalization gaps. We examine why larger models tend to be more quantizable from an information theoretic perspective, showing that the rate at which they can integrate new information grows slower than their capacity on the compute optimal frontier. From these findings we produce a scaling law for the generalization gap, showing that our bounds decrease in a predictable way.

## Metadata
- venue: ICLR
- year: 2025
- authors: Marc Anton Finzi, Sanyam Kapoor, Diego Granziol, Anming Gu, Christopher De Sa, J Zico Kolter, Andrew Gordon Wilson
- arxiv_id: 
- openreview_id: MF7ljU8xcf
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e35f09f288013a64bdf237be6a81cf0891307411.pdf
- published: 2025
- keywords: generalization bounds, language models, scaling laws

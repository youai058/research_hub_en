---
title: "Mechanism Shift During Post-training from Autoregressive to Masked Diffusion Language Models"
authors: ["Injin Kong", "Hyoungjoon Lee", "Yohan Jo"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2601.14758"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2601.14758v3"
published: "2026-01-21"
categories: ["cs.LG", "cs.AI", "cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:21+09:00"
---

# Mechanism Shift During Post-training from Autoregressive to Masked Diffusion Language Models

## Abstract
Post-training pretrained autoregressive models (ARMs) into masked diffusion models (MDMs) has emerged as a cost-effective way to overcome the limitations of sequential generation. Yet the internal algorithmic changes induced by this shift remain poorly understood, leaving it unclear whether post-trained MDMs acquire genuine bidirectional reasoning or merely repackage autoregressive heuristics. We address this question through a comparative circuit analysis of ARMs and their MDM counterparts. Our analysis reveals a systematic "mechanism shift" that depends on the structural nature of the task. MDMs largely preserve autoregressive circuitry for tasks driven by local causal dependencies, but for global planning tasks they abandon initialized pathways and exhibit distinct rewiring with increased early-layer processing. At the semantic level, we observe a transition from sharp, localized specialization in ARMs to distributed integration in MDMs. These findings show that diffusion post-training does not simply adjust model parameters, but reorganizes internal computation to support non-sequential global planning.

## Metadata
- venue: arXiv
- year: 2026
- authors: Injin Kong, Hyoungjoon Lee, Yohan Jo
- arxiv_id: 2601.14758
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2601.14758v3
- published: 2026-01-21

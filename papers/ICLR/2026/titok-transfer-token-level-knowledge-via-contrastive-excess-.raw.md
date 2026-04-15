---
title: "TiTok: Transfer Token-level Knowledge via Contrastive Excess to Transplant LoRA"
authors: ["ChanJoo Jung", "Jaehyung Kim"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "0B5K9pIdSK"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e92a4c12cf2cb233ac7b387defdb05dc20b33758.pdf"
published: "2026"
categories: []
keywords: ["Large Language Models", "Knowledge Transfer", "PEFT"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:26+09:00"
---

# TiTok: Transfer Token-level Knowledge via Contrastive Excess to Transplant LoRA

## Abstract
Large Language Models (LLMs) are widely applied in real world scenarios, yet fine-tuning them comes with significant computational and storage costs. Parameter-Efficient Fine-Tuning (PEFT) methods such as LoRA mitigate these costs; however, the adapted parameters are dependent on the base model and cannot be transferred across different backbones. One way to address this issue is through knowledge distillation, but its effectiveness inherently depends on training data. Recent work such as TransLoRA avoids this by generating synthetic data; nevertheless, this adds complexity since it requires training an additional discriminator model. In this paper, we propose TiTok, a new framework that enables effective LoRA Transplantation through Token-level knowledge transfer. Specifically, TiTok captures task-relevant information through a token-wise contrastive excess between a source model with and without LoRA. This excess highlights informative tokens and enables selective filtering of synthetic data, all without additional models or overhead. Through experiments on three benchmarks across multiple transfer settings, we demonstrate that TiTok is consistently effective, achieving average performance gains of +4–10% compared to baselines overall.

## Metadata
- venue: ICLR
- year: 2026
- authors: ChanJoo Jung, Jaehyung Kim
- arxiv_id: 
- openreview_id: 0B5K9pIdSK
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e92a4c12cf2cb233ac7b387defdb05dc20b33758.pdf
- published: 2026
- keywords: Large Language Models, Knowledge Transfer, PEFT

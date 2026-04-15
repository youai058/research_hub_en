---
title: "DualTSR: Unified Dual-Diffusion Transformer for Scene Text Image Super-Resolution"
authors: ["Axi Niu", "Kang Zhang", "Qingsen Yan", "Hao Jin", "Jinqiu Sun", "Yanning Zhang"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.14207"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.14207v1"
published: "2026-03-15"
categories: ["cs.CV", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:28+09:00"
---

# DualTSR: Unified Dual-Diffusion Transformer for Scene Text Image Super-Resolution

## Abstract
Scene Text Image Super-Resolution (STISR) aims to restore high-resolution details in low-resolution text images, which is crucial for both human readability and machine recognition. Existing methods, however, often depend on external Optical Character Recognition (OCR) models for textual priors or rely on complex multi-component architectures that are difficult to train and reproduce. In this paper, we introduce DualTSR, a unified end-to-end framework that addresses both issues. DualTSR employs a single multimodal transformer backbone trained with a dual diffusion objective. It simultaneously models the continuous distribution of high-resolution images via Conditional Flow Matching and the discrete distribution of textual content via discrete diffusion. This shared design enables visual and textual information to interact at every layer, allowing the model to infer text priors internally instead of relying on an external OCR module. Compared with prior multi-branch diffusion systems, DualTSR offers a simpler end-to-end formulation with fewer hand-crafted components. Experiments on synthetic Chinese benchmarks and a curated real-world evaluation protocol show that DualTSR achieves strong perceptual quality and text fidelity.

## Metadata
- venue: arXiv
- year: 2026
- authors: Axi Niu, Kang Zhang, Qingsen Yan, Hao Jin, Jinqiu Sun, Yanning Zhang
- arxiv_id: 2603.14207
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.14207v1
- published: 2026-03-15

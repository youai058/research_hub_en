---
title: "Condition Errors Refinement in Autoregressive Image Generation with Diffusion Loss"
authors: ["Yucheng Zhou", "Hao Li", "Jianbing Shen"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "IqXlvYA7En"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/55070ba9a31d859073e5eec6449fef4fe57391ad.pdf"
published: "2026"
categories: []
keywords: ["Language Models", "Autoregressive Language Models", "Autoregressive Image Generation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:35+09:00"
---

# Condition Errors Refinement in Autoregressive Image Generation with Diffusion Loss

## Abstract
Recent studies have explored autoregressive models for image generation, with promising results, and have combined diffusion models with autoregressive frameworks to optimize image generation via diffusion losses. In this study, we present a theoretical analysis of diffusion and autoregressive models with diffusion loss, highlighting the latter's advantages. We present a theoretical comparison of conditional diffusion and autoregressive diffusion with diffusion loss, demonstrating that patch denoising optimization in autoregressive models effectively mitigates condition errors and leads to a stable condition distribution. Our analysis also reveals that autoregressive condition generation refines the condition, causing the condition error influence to decay exponentially. In addition, we introduce a novel condition refinement approach based on Optimal Transport (OT) theory to address ``condition inconsistency''. We theoretically demonstrate that formulating condition refinement as a Wasserstein Gradient Flow ensures convergence toward the ideal condition distribution, effectively mitigating condition inconsistency. Experiments demonstrate the superiority of our method over diffusion and autoregressive models with diffusion loss methods.

## Metadata
- venue: ICLR
- year: 2026
- authors: Yucheng Zhou, Hao Li, Jianbing Shen
- arxiv_id: 
- openreview_id: IqXlvYA7En
- anthology_id: 
- pdf_url: https://openreview.net/pdf/55070ba9a31d859073e5eec6449fef4fe57391ad.pdf
- published: 2026
- keywords: Language Models, Autoregressive Language Models, Autoregressive Image Generation

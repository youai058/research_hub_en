---
title: "SAFEx: Analyzing Vulnerabilities of MoE-Based LLMs via Stable Safety-critical Expert Identification"
authors: ["ZhengLin Lai", "Mengyao Liao", "Bingzhe Wu", "Dong Xu", "Zebin Zhao", "Zhihang Yuan", "Chao Fan", "Jianqiang Li"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "VwsXmcMyg5"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/fedcd79e0b8d0417167c9aa43e3096fe21438d2d.pdf"
published: "2025"
categories: []
keywords: ["Trustworthy AI"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:27+09:00"
---

# SAFEx: Analyzing Vulnerabilities of MoE-Based LLMs via Stable Safety-critical Expert Identification

## Abstract
Large language models with Mixture-of-Experts (MoE) architectures achieve efficiency and scalability, yet their routing mechanisms introduce safety alignment challenges insufficiently addressed by techniques developed for dense models. In this work, the MoE-specific safety risk of positional vulnerability—that safety-aligned behaviors rely on specific expert modules—is formalized and systematically analyzed. An analytical framework, SAFEx, is presented to robustly identify, characterize, and validate safety-critical experts via a stability-based expert selection procedure, and to decompose them into two functional groups: the Harmful Content Detection Group (HCDG), which specializes in identifying and recognizing harmful content within user inputs, and the Harmful Response Control Group (HRCG), which specializes in controlling and enforcing model behaviors to generate appropriate safety responses. Expert-level interventions are conducted to probe causality and to test mitigation. Targeted masking of SAFEx-selected experts reveals that safety behavior is highly concentrated. On Qwen3-30B-A3B, configured with 48 MoE-FFN layers and 128 experts per layer under top-8 routing (48×128=6,144 experts in total), disabling 12 selected experts reduces the refusal rate by 22%. In addition, lightweight adaptation is performed using LoRA under three configurations—the HRCG, the union of HCDG and HRCG, and all experts—and the resulting updates are composed through negative weight merging targeted at the HRCG, leading to improved refusal under adversarial prompts without full-model retraining. These results establish positional vulnerability as a distinct MoE-specific safety challenge and provide a practical, compute-efficient pathway for expert-level safety interventions within routed architectures.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: ZhengLin Lai, Mengyao Liao, Bingzhe Wu, Dong Xu, Zebin Zhao, Zhihang Yuan, Chao Fan, Jianqiang Li
- arxiv_id: 
- openreview_id: VwsXmcMyg5
- anthology_id: 
- pdf_url: https://openreview.net/pdf/fedcd79e0b8d0417167c9aa43e3096fe21438d2d.pdf
- published: 2025
- keywords: Trustworthy AI

---
title: "HippoTune: A Hippocampal Associative Loop–Inspired Fine-Tuning Method for Continual Learning"
authors: ["chenyanxi", "Xiuxing Li", "Han Yuyang", "Zhuo Wang", "Qing Li", "Ziyu Li", "Xiang Li", "Chen Wei", "Xia Wu"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "MtDiLnnYgm"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/37c6dea361a35fe6de4f2d583dac6a7d752a0b6e.pdf"
published: "2026"
categories: []
keywords: ["Associative Memory", "Key–Value Memory", "Parameter-Efficient Fine-Tuning", "Continual Learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:43+09:00"
---

# HippoTune: A Hippocampal Associative Loop–Inspired Fine-Tuning Method for Continual Learning

## Abstract
Studies have shown that catastrophic forgetting primarily stems from the difficulty of reactivating old memories; although parameter-efficient fine-tuning can mitigate forgetting while keeping most model parameters frozen, it still falls short in fully reawakening knowledge of prior tasks. In contrast, humans can efficiently retrieve and flexibly integrate existing experiences when learning new tasks, thereby maintaining stable performance on earlier ones. During cognition, the hippocampal EC–DG–CA3–CA1 circuit engages in multiple rounds of associative recall, and its pattern-separation and memory-completion mechanisms excel at activating historical information. Inspired by this mechanism, we propose HippoTune, a latent-space iterative retrieval strategy that embeds a query–retrieve–feedback loop within each Transformer layer. Starting from the hidden state as an initial query, the model performs a few rounds of soft key–value retrieval, projects the retrieved signals back into the query, and updates it iteratively until convergence or a preset iteration limit. Theoretically, we show this process implements a Krylov-style polynomial approximation, equivalent to a differentiable second-order preconditioner, thereby deepening retrieval in a principled way. Empirically, HippoTune outperforms classical buffer-free PEFT-CL methods by 5–8\% in accuracy across three vision benchmarks, while reducing training FLOPs by 50\%, effectively mitigating forgetting under tight compute constraints. 
Code is available at: https://github.com/yan4xi1/HippoTune.

## Metadata
- venue: ICLR
- year: 2026
- authors: chenyanxi, Xiuxing Li, Han Yuyang, Zhuo Wang, Qing Li, Ziyu Li, Xiang Li, Chen Wei, Xia Wu
- arxiv_id: 
- openreview_id: MtDiLnnYgm
- anthology_id: 
- pdf_url: https://openreview.net/pdf/37c6dea361a35fe6de4f2d583dac6a7d752a0b6e.pdf
- published: 2026
- keywords: Associative Memory, Key–Value Memory, Parameter-Efficient Fine-Tuning, Continual Learning

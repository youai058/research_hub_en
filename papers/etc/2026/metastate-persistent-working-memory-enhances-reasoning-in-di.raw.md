---
title: "MetaState: Persistent Working Memory Enhances Reasoning in Discrete Diffusion Language Models"
authors: ["Kejing Xia", "Mingzhe Li", "Lixuan Wei", "Zhenbang Du", "Xiangchi Yuan", "Dachuan Shi", "Qirui Jin", "Wenke Lee"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.01331"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.01331v2"
published: "2026-03-02"
categories: ["cs.CL", "cs.AI", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:02+09:00"
---

# MetaState: Persistent Working Memory Enhances Reasoning in Discrete Diffusion Language Models

## Abstract
Discrete diffusion language models (dLLMs) generate text by iteratively denoising a masked sequence. However, standard dLLMs condition each denoising step solely on the current hard-masked sequence, while intermediate continuous representations are discarded after sampling and remasking. We term this bottleneck the \textbf{Information Island} issue: continuous information remains isolated within individual denoising steps and fails to propagate across the trajectory. This bottleneck is especially harmful for reasoning, which requires intermediate reasoning state to be preserved and updated across many denoising steps. To address this limitation, we introduce \textbf{MetaState}, a lightweight recurrent augmentation that equips a frozen dLLM backbone with persistent, fixed-size working memory. MetaState comprises three modules with a shared time conditioner: a cross-attention \textbf{Mixer} that reads backbone activations into memory slots, a GRU-style \textbf{Updater} that integrates information across steps, and a cross-attention \textbf{Injector} that writes the updated memory back into the backbone. We train these modules with a dedicated $K$-step unrolling pipeline to learn multi-step dynamics. MetaState adds only ${\sim}0.6\%$ trainable parameters while keeping the backbone frozen, and consistently improves reasoning performance over frozen baselines on mathematical reasoning and code generation benchmarks, with an average gain of $4.5\%$ across all evaluations.

## Metadata
- venue: arXiv
- year: 2026
- authors: Kejing Xia, Mingzhe Li, Lixuan Wei, Zhenbang Du, Xiangchi Yuan, Dachuan Shi, Qirui Jin, Wenke Lee
- arxiv_id: 2603.01331
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.01331v2
- published: 2026-03-02

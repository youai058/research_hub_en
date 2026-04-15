---
title: "Diffusion Language Models Know the Answer Before Decoding"
authors: ["Pengxiang Li", "Yefan Zhou", "Dilxat Muhtar", "Lu Yin", "Shilin Yan", "Li Shen", "Soroush Vosoughi", "Shiwei Liu"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2508.19982"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2508.19982v5"
published: "2025-08-27"
categories: ["cs.CL", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:14+09:00"
---

# Diffusion Language Models Know the Answer Before Decoding

## Abstract
Diffusion language models (DLMs) have recently emerged as an alternative to autoregressive approaches, offering parallel sequence generation and flexible token orders. However, their inference remains slower than that of autoregressive models, primarily due to the cost of bidirectional attention and the large number of refinement steps required for high quality outputs. In this work, we highlight and leverage an overlooked property of DLMs early answer convergence: in many cases, the correct answer can be internally identified by half steps before the final decoding step, both under semi-autoregressive and random remasking schedules. For example, on GSM8K and MMLU, up to 97% and 99% of instances, respectively, can be decoded correctly using only half of the refinement steps. Building on this observation, we introduce Prophet, a training-free fast decoding paradigm that enables early commit decoding. Specifically, Prophet dynamically decides whether to continue refinement or to go "all-in" (i.e., decode all remaining tokens in one step), using the confidence gap between the top-2 prediction candidates as the criterion. It integrates seamlessly into existing DLM implementations, incurs negligible overhead, and requires no additional training. Empirical evaluations of LLaDA-8B and Dream-7B across multiple tasks show that Prophet reduces the number of decoding steps by up to 3.4x while preserving high generation quality. These results recast DLM decoding as a problem of when to stop sampling, and demonstrate that early decode convergence provides a simple yet powerful mechanism for accelerating DLM inference, complementary to existing speedup techniques. Our code is publicly available at https://github.com/pixeli99/Prophet.

## Metadata
- venue: arXiv
- year: 2025
- authors: Pengxiang Li, Yefan Zhou, Dilxat Muhtar, Lu Yin, Shilin Yan, Li Shen, Soroush Vosoughi, Shiwei Liu
- arxiv_id: 2508.19982
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2508.19982v5
- published: 2025-08-27

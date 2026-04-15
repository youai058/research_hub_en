---
title: "Corrective Diffusion Language Models"
authors: ["Shuibai Zhang", "Fred Zhangzhi Peng", "Yiheng Zhang", "Jin Pan", "Grigorios G. Chrysos"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2512.15596"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2512.15596v2"
published: "2025-12-17"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:03+09:00"
---

# Corrective Diffusion Language Models

## Abstract
While Diffusion Language Models (DLMs) are theoretically well-suited for iterative refinement due to their non-causal structure, they often fail to reliably revise incorrect tokens in practice. The key challenge lies in the model's inability to distinguish between correct and erroneous tokens in a visible sequence. Standard masked diffusion language model (MDLM) training is restricted to the objective of unmasking, undermining the effectiveness of refinement guided by confidence. Based on this observation, we study corrective behavior in DLMs, defined as the ability to assign lower confidence to incorrect tokens and iteratively refine them while preserving correct content. We show that this capability is not induced by conventional masked diffusion objectives and propose a post-training principle oriented by correction that explicitly supervises visible incorrect tokens, enabling discriminative confidence and targeted refinement. To evaluate corrective behavior, we introduce the Code Revision Benchmark, a controllable and executable benchmark for assessing error localization and in-place correction. Experiments on code revision tasks and parallel decoding scenarios demonstrate that models trained with our approach substantially outperform standard MDLMs, with gains that are most pronounced when parallel decoding introduces substantial uncertainty and iterative refinement becomes essential. Our code is publicly available at https://github.com/zhangshuibai/CDLM.

## Metadata
- venue: arXiv
- year: 2025
- authors: Shuibai Zhang, Fred Zhangzhi Peng, Yiheng Zhang, Jin Pan, Grigorios G. Chrysos
- arxiv_id: 2512.15596
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2512.15596v2
- published: 2025-12-17

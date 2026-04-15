---
title: "From Next-Token to Next-Block: A Principled Adaptation Path for Diffusion LLMs"
authors: ["Yuchuan Tian", "Yuchen Liang", "Shuo Zhang", "Yingte Shu", "Guangwen Yang", "Wei He", "Sibo Fang", "Tianyu Guo", "Kai Han", "Chao Xu", "Hanting Chen", "Xinghao Chen", "Yunhe Wang"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2512.06776"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2512.06776v2"
published: "2025-12-07"
categories: ["cs.CL", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:03+09:00"
---

# From Next-Token to Next-Block: A Principled Adaptation Path for Diffusion LLMs

## Abstract
Diffusion Language Models (DLMs) enable fast generation, yet training large DLMs from scratch is costly. As a practical shortcut, adapting off-the-shelf Auto-Regressive (AR) model weights into a DLM could quickly equip the DLM with strong long-context generation capabilies. Prior "adaptation" attempts either modify logits or randomly grow attention masks to Full-Sequence diffusion, or simply transplant AR weights into a Block-Diffusion recipe, leaving two key questions unaddressed: where is the final destination of adaptation, and how to adapt better? For manifold benefits, we reframe the whole AR-to-DLM adaptation under the Block-Diffusion paradigm, transitioning from block size 1 to the final Block-Diffusion state. Concretely, the principled pathway of adaptation is designed as follows: we keep a context-causal path where causal attention is kept in the prefix, an efficient parallel adaptation procedure where an AR guidance is maintained, and gradual increment of the generation block size for a smoother transition. Built on these components, the adaptation is proved competitive on various models at different scales. With better adaptation, we propose NBDiff-7B that could inherit the long-context modeling and reasoning capabilities, and achieve state-of-the-art performance among the 7B-class DLMs. Codes: https://github.com/YuchuanTian/NBDiff.

## Metadata
- venue: arXiv
- year: 2025
- authors: Yuchuan Tian, Yuchen Liang, Shuo Zhang, Yingte Shu, Guangwen Yang, Wei He, Sibo Fang, Tianyu Guo, Kai Han, Chao Xu, Hanting Chen, Xinghao Chen, Yunhe Wang
- arxiv_id: 2512.06776
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2512.06776v2
- published: 2025-12-07

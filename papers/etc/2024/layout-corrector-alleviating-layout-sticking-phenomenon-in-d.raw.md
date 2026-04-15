---
title: "Layout-Corrector: Alleviating Layout Sticking Phenomenon in Discrete Diffusion Model"
authors: ["Shoma Iwai", "Atsuki Osanai", "Shunsuke Kitada", "Shinichiro Omachi"]
venue: "arXiv"
year: 2024
venue_class: "etc"
arxiv_id: "2409.16689"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2409.16689v1"
published: "2024-09-25"
categories: ["cs.CV", "cs.AI", "cs.GR", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:20:12+09:00"
---

# Layout-Corrector: Alleviating Layout Sticking Phenomenon in Discrete Diffusion Model

## Abstract
Layout generation is a task to synthesize a harmonious layout with elements characterized by attributes such as category, position, and size. Human designers experiment with the placement and modification of elements to create aesthetic layouts, however, we observed that current discrete diffusion models (DDMs) struggle to correct inharmonious layouts after they have been generated. In this paper, we first provide novel insights into layout sticking phenomenon in DDMs and then propose a simple yet effective layout-assessment module Layout-Corrector, which works in conjunction with existing DDMs to address the layout sticking problem. We present a learning-based module capable of identifying inharmonious elements within layouts, considering overall layout harmony characterized by complex composition. During the generation process, Layout-Corrector evaluates the correctness of each token in the generated layout, reinitializing those with low scores to the ungenerated state. The DDM then uses the high-scored tokens as clues to regenerate the harmonized tokens. Layout-Corrector, tested on common benchmarks, consistently boosts layout-generation performance when in conjunction with various state-of-the-art DDMs. Furthermore, our extensive analysis demonstrates that the Layout-Corrector (1) successfully identifies erroneous tokens, (2) facilitates control over the fidelity-diversity trade-off, and (3) significantly mitigates the performance drop associated with fast sampling.

## Metadata
- venue: arXiv
- year: 2024
- authors: Shoma Iwai, Atsuki Osanai, Shunsuke Kitada, Shinichiro Omachi
- arxiv_id: 2409.16689
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2409.16689v1
- published: 2024-09-25

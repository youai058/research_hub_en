---
title: "On the Role of Discreteness in Diffusion LLMs"
authors: ["Ziqi Jin", "Bin Wang", "Xiang Lin", "Lidong Bing", "Aixin Sun"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2512.22630"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2512.22630v1"
published: "2025-12-27"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:03+09:00"
---

# On the Role of Discreteness in Diffusion LLMs

## Abstract
Diffusion models offer appealing properties for language generation, such as parallel decoding and iterative refinement, but the discrete and highly structured nature of text challenges the direct application of diffusion principles. In this paper, we revisit diffusion language modeling from the view of diffusion process and language modeling, and outline five properties that separate diffusion mechanics from language-specific requirements. We first categorize existing approaches into continuous diffusion in embedding space and discrete diffusion over tokens. We then show that each satisfies only part of the five essential properties and therefore reflects a structural trade-off. Through analyses of recent large diffusion language models, we identify two central issues: (i) uniform corruption does not respect how information is distributed across positions, and (ii) token-wise marginal training cannot capture multi-token dependencies during parallel decoding. These observations motivate diffusion processes that align more closely with the structure of text, and encourage future work toward more coherent diffusion language models.

## Metadata
- venue: arXiv
- year: 2025
- authors: Ziqi Jin, Bin Wang, Xiang Lin, Lidong Bing, Aixin Sun
- arxiv_id: 2512.22630
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2512.22630v1
- published: 2025-12-27

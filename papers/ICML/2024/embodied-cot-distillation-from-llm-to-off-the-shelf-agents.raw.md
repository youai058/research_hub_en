---
title: "Embodied CoT Distillation From LLM To Off-the-shelf Agents"
authors: ["Wonje Choi", "Woo Kyung Kim", "Minjong Yoo", "Honguk Woo"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "M4Htd52HMH"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/4d395cf5c651f46c1b5123f8a7fceaf0400fd638.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:41+09:00"
---

# Embodied CoT Distillation From LLM To Off-the-shelf Agents

## Abstract
We address the challenge of utilizing large language models (LLMs) for complex embodied tasks, in the environment where decision-making systems operate timely on capacity-limited, off-the-shelf devices. We present DeDer, a framework for decomposing and distilling the embodied reasoning capabilities from LLMs to efficient, small language model (sLM)-based policies. In DeDer, the decision-making process of LLM-based strategies is restructured into a hierarchy with a reasoning-policy and planning-policy. The reasoning-policy is distilled from the data that is generated through the embodied in-context learning and self-verification of an LLM, so it can produce effective rationales. The planning-policy, guided by the rationales, can render optimized plans efficiently. In turn, DeDer allows for adopting sLMs for both policies, deployed on off-the-shelf devices. Furthermore, to enhance the quality of intermediate rationales, specific to embodied tasks, we devise the embodied knowledge graph, and to generate multiple rationales timely through a single inference, we also use the contrastively prompted attention model. Our experiments with the ALFRED benchmark demonstrate that DeDer surpasses leading language planning and distillation approaches, indicating the applicability and efficiency of sLM-based embodied policies derived through DeDer.

## Metadata
- venue: ICML
- year: 2024
- authors: Wonje Choi, Woo Kyung Kim, Minjong Yoo, Honguk Woo
- arxiv_id: 
- openreview_id: M4Htd52HMH
- anthology_id: 
- pdf_url: https://openreview.net/pdf/4d395cf5c651f46c1b5123f8a7fceaf0400fd638.pdf
- published: 2024

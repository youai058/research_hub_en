---
title: "Micro-Macro Retrieval: Reducing Long-Form Hallucination in Large Language Models"
authors: ["Yujie Feng", "Jian Li", "Zhihan Zhou", "Pengfei Xu", "Yujia Zhang", "xiaoyu li", "Xiaohui Zhou", "Alan Zhao", "Xi Chen", "Xiao-Ming Wu"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ABdgMoJhlO"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/bed820835ca925881e22659711d1ef46b97596bd.pdf"
published: "2026"
categories: []
keywords: ["Hallucination", "Long-form Hallucination", "Large Language Models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:29+09:00"
---

# Micro-Macro Retrieval: Reducing Long-Form Hallucination in Large Language Models

## Abstract
Large Language Models (LLMs) achieve impressive performance across many tasks but remain prone to hallucination, especially in long-form generation where redundant retrieved contexts and lengthy reasoning chains amplify factual errors. Recent studies highlight a critical phenomenon: the closer key information appears to the model outputs, the higher the factual accuracy. However, existing retrieval-augmented language models (RALMs) lack effective mechanisms to ensure this proximity — external evidence is injected into reasoning via multi-turn retrieval, but this cannot ensure key information stays close to the outputs. We propose Micro–Macro Retrieval ($M^2R$), a novel retrieve-while-generate framework to fill this gap. At the macro level, $M^2R$ retrieves coarse-grained evidence from external sources; at the micro level, it extracts essential results from a key information repository built during reasoning and reuses them while generating answers. This design directly addresses the key-information–to-output proximity bottleneck, effectively reducing hallucination in long-form tasks. $M^2R$ is trained with a curriculum learning–based reinforcement learning strategy using customized rule-based rewards, enabling stable acquisition of retrieval and grounding skills.  Extensive experiments across different benchmarks demonstrate the effectiveness of $M^2R$, especially in lengthy-context settings.

## Metadata
- venue: ICLR
- year: 2026
- authors: Yujie Feng, Jian Li, Zhihan Zhou, Pengfei Xu, Yujia Zhang, xiaoyu li, Xiaohui Zhou, Alan Zhao, Xi Chen, Xiao-Ming Wu
- arxiv_id: 
- openreview_id: ABdgMoJhlO
- anthology_id: 
- pdf_url: https://openreview.net/pdf/bed820835ca925881e22659711d1ef46b97596bd.pdf
- published: 2026
- keywords: Hallucination, Long-form Hallucination, Large Language Models

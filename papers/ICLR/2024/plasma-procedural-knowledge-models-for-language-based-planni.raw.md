---
title: "PlaSma: Procedural Knowledge Models for Language-based Planning and Re-Planning"
authors: ["Faeze Brahman", "Chandra Bhagavatula", "Valentina Pyatkin", "Jena D. Hwang", "Xiang Lorraine Li", "Hirona Jacqueline Arai", "Soumya Sanyal", "Keisuke Sakaguchi", "Xiang Ren", "Yejin Choi"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "dFcXJgnrGB"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b88eaa0cc84120348881ebfc5dd4fe00210337df.pdf"
published: "2024"
categories: []
keywords: ["language-based planning", "procedural/script knowledge", "distillation", "large language models", "decoding-time algorithm"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:13+09:00"
---

# PlaSma: Procedural Knowledge Models for Language-based Planning and Re-Planning

## Abstract
Procedural planning, which entails decomposing a high-level goal into a sequence of temporally ordered steps, is an important yet intricate task for machines. It involves integrating common-sense knowledge to reason about complex and often contextualized situations, e.g. ``scheduling a doctor's appointment without a phone''. While current approaches show encouraging results using large language models (LLMs), they are hindered by drawbacks such as costly API calls and reproducibility issues. In this paper, we advocate planning using smaller language models. We present PlaSma, a novel two-pronged approach to endow small language models with procedural knowledge and (constrained) language-based planning capabilities. More concretely, we develop *symbolic procedural knowledge distillation* to enhance the commonsense knowledge in small language models and an *inference-time algorithm* to facilitate more structured and accurate reasoning. In addition, we introduce a new related task, *Replanning*, that requires a revision of a plan to cope with a constrained situation. In both the planning and replanning settings, we show that orders-of-magnitude smaller models (770M-11B parameters) can compete and often surpass their larger teacher models' capabilities. Finally, we showcase successful application of PlaSma in an embodied environment, VirtualHome.

## Metadata
- venue: ICLR
- year: 2024
- authors: Faeze Brahman, Chandra Bhagavatula, Valentina Pyatkin, Jena D. Hwang, Xiang Lorraine Li, Hirona Jacqueline Arai, Soumya Sanyal, Keisuke Sakaguchi, Xiang Ren, Yejin Choi
- arxiv_id: 
- openreview_id: dFcXJgnrGB
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b88eaa0cc84120348881ebfc5dd4fe00210337df.pdf
- published: 2024
- keywords: language-based planning, procedural/script knowledge, distillation, large language models, decoding-time algorithm

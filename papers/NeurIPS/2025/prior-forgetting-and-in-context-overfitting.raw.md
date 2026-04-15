---
title: "Prior Forgetting and In-Context Overfitting"
authors: ["Sungyoon Lee"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "p37Kd7EQhy"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/6716c3a29f99dd908caabe8683887a219481855e.pdf"
published: "2025"
categories: []
keywords: ["in-context learning", "transformer", "task recognition", "task learning", "pretraining", "prior forgetting", "in-context overfitting"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:51+09:00"
---

# Prior Forgetting and In-Context Overfitting

## Abstract
In-context learning (ICL) is one of the key capabilities contributing to the great success of LLMs. At test time, ICL is known to operate in the two modes: task recognition and task learning. In this paper, we investigate the emergence and dynamics of the two modes of ICL during pretraining. To provide an analytical understanding of the learning dynamics of the ICL abilities, we investigate the in-context random linear regression problem with a simple linear-attention-based transformer, and define and disentangle the strengths of the task recognition and task learning abilities stored in the transformer model’s parameters. We show that, during the pretraining phase, the model first learns the task learning and the task recognition abilities together in the beginning, but it (a) gradually forgets the task recognition ability to recall the priorly learned tasks and (b) relies more on the given context in the later phase, which we call (a) \textit{prior forgetting} and (b) \textit{in-context overfitting}, respectively.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Sungyoon Lee
- arxiv_id: 
- openreview_id: p37Kd7EQhy
- anthology_id: 
- pdf_url: https://openreview.net/pdf/6716c3a29f99dd908caabe8683887a219481855e.pdf
- published: 2025
- keywords: in-context learning, transformer, task recognition, task learning, pretraining, prior forgetting, in-context overfitting
